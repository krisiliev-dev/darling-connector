# -*- coding: utf-8 -*-
"""Deterministic Bulgarian spellcheck for agent output (no LLM involved).

Uses phunspell (pure-Python Hunspell) with LibreOffice's bg_BG dictionary.
Catches the garbled words models produce ("преенен", "чени", "Применение",
transliterated brands like "Лъки") that reviewers keep missing.

Only Cyrillic tokens are checked — Latin brands, units (ml/cm/W) and numbers
pass through untouched. Domain words the dictionary lacks go into
bg_whitelist.txt (one per line) as false positives are found.
"""
import re
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).parent
WHITELIST_PATH = HERE / "bg_whitelist.txt"

_CYR_WORD = re.compile(r"[а-яА-Я]{3,}")


@lru_cache(maxsize=1)
def _speller():
    import phunspell
    return phunspell.Phunspell("bg_BG")


@lru_cache(maxsize=1)
def _whitelist():
    if WHITELIST_PATH.exists():
        return {w.strip().lower() for w in
                WHITELIST_PATH.read_text(encoding="utf-8").splitlines() if w.strip()}
    return set()


def unknown_words(text, limit=10, known_text=""):
    """Return up to `limit` unknown Cyrillic words from `text`.

    Words that also appear in `known_text` (e.g. the product's ground truth)
    are exempt — the agents copy vocabulary from there, and the bg dictionary
    lacks a lot of ordinary commerce words the till data uses daily.
    """
    if not text:
        return []
    plain = re.sub(r"<[^>]+>", " ", str(text))
    known = {w.lower() for w in _CYR_WORD.findall(str(known_text))} if known_text else set()
    sp = _speller()
    wl = _whitelist()
    bad, seen = [], set()
    for word in _CYR_WORD.findall(plain):
        low = word.lower()
        if low in seen or low in wl or low in known:
            continue
        # Stem-prefix match: entry "подаръчн" covers подаръчният/подаръчна/…
        # (the bg dictionary lacks whole word families, not just single forms).
        # The whitelist is curated, so even short stems ("моп" -> мопът/мопа)
        # may act as prefixes.
        if any(len(w) >= 3 and low.startswith(w) for w in wl):
            seen.add(low)
            continue
        seen.add(low)
        try:
            ok = sp.lookup(word) or sp.lookup(low) or sp.lookup(word.capitalize())
        except Exception:
            ok = True  # dictionary hiccup must not block the pipeline
        if not ok:
            bad.append(word)
            if len(bad) >= limit:
                break
    return bad


if __name__ == "__main__":
    import io, sys
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    samples = [
        ("bad", "Тази тава е преенен за миене и има 7 компартмента за чени и кички."),
        ("bad", "Сервиз за кафе Лъки с приложение за ежедневна употреба, цвет бял."),
        ("good", "Металната поставка за домакинска хартия осигурява стабилно съхранение "
                 "и лесен достъп до ролката в кухнята. Подходяща за ежедневна употреба."),
        ("good", "Комплект гарафа и шест чаши за уиски от стъкло, елегантен подарък."),
    ]
    for tag, s in samples:
        print(tag, "->", unknown_words(s))
