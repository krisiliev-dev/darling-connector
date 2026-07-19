# -*- coding: utf-8 -*-
"""ПОМОЩ / onboarding page for the human reviewer (owner request 2026-07-17).
Everything a new reviewer needs: what the system is, how a product is composed and
stored, how it will look in the Shopify store, the review workflow, and every page."""
from schema_pages import _SHELL


def help_page():
    body = """
<style>
 .toc{background:var(--vanilla);border:1px solid var(--honey);border-radius:10px;padding:.8rem 1.2rem;font-size:.9rem;}
 .toc a{color:var(--cherry);display:inline-block;margin:.15rem .8rem .15rem 0;}
 .card{background:#fff;border:1px solid var(--line);border-radius:10px;padding:1rem 1.3rem;margin:1rem 0;}
 .ex{background:var(--cream);border-left:3px solid var(--honey);padding:.5rem .8rem;margin:.5rem 0;font-size:.88rem;}
 .ok{color:var(--ok);font-weight:700;} .no{color:#a12020;font-weight:700;}
 kbd{background:#eee;border:1px solid #ccc;border-radius:4px;padding:0 .35rem;font-size:.85em;}
 td,th{font-size:.85rem;}
 .flag{background:#fff4e0;border-left:3px solid #d99b2b;padding:.5rem .8rem;margin:.4rem 0;font-size:.88rem;}
 .diagram{margin:1rem 0;overflow-x:auto;}
 .rowmock{display:flex;gap:.5rem;align-items:stretch;flex-wrap:nowrap;overflow-x:auto;padding:.4rem 0;}
 .mcard{min-width:9.5rem;max-width:10.5rem;background:#fff;border:1px solid var(--line);border-radius:8px;padding:.45rem .55rem;font-size:.68rem;line-height:1.35;}
 .mcard h5{margin:0 0 .25rem;font-size:.7rem;color:var(--cherry);}
 .mcard.cur{border:2px solid var(--cherry);}
 .mcard .lbl{display:block;margin-top:.35rem;padding-top:.25rem;border-top:1px dashed var(--honey);color:#8a7d68;font-size:.64rem;}
 .marrow{align-self:center;color:var(--cherry);font-size:1.1rem;flex:0 0 auto;}
 .mrem{color:#a12020;text-decoration:line-through;} .madd{color:var(--ok);font-weight:600;}
 .mbtn{display:inline-block;background:var(--cherry);color:#fff;border-radius:5px;padding:.05rem .3rem;font-size:.62rem;margin-right:.15rem;}
 .mbtn.g{background:#fff;color:var(--cherry);border:1px solid var(--cherry);}
 .namechips{display:flex;gap:.3rem;flex-wrap:wrap;align-items:center;margin:.5rem 0;}
 .nchip{border-radius:9px;padding:.2rem .55rem;font-size:.78rem;border:1px solid;}
 .nc1{background:#eef2fb;border-color:#b8c6e8;color:#2c4a8a;} .nc2{background:#eef8ee;border-color:#b5d9b5;color:#1d6b2a;}
 .nc3{background:#fdf1e2;border-color:#e8cfa0;color:#8a5a12;} .nc4{background:#fbeaea;border-color:#e3b8b8;color:#8c1d2f;font-weight:700;}
 .nc5{background:#f3ecfa;border-color:#d0bce6;color:#5b3a8a;}
 .namestr{font-size:.95rem;background:#fff;border:1px solid var(--line);border-radius:8px;padding:.5rem .8rem;margin:.4rem 0;}
 .shopmock{display:grid;grid-template-columns:8.5rem 1fr;gap:.6rem;background:#fff;border:1px solid var(--line);border-radius:10px;padding:.8rem;font-size:.72rem;max-width:38rem;}
 .shopmock .lab{color:var(--cherry);font-size:.62rem;font-weight:700;}
 .sfilters{background:var(--vanilla);border:1px solid var(--honey);border-radius:6px;padding:.45rem;}
 .simg{background:var(--cream);border:1px dashed var(--honey);border-radius:6px;height:5.2rem;display:flex;align-items:center;justify-content:center;color:#8a7d68;}
 .gsnip{max-width:38rem;background:#fff;border:1px solid var(--line);border-radius:10px;padding:.6rem .8rem;font-size:.75rem;margin:.5rem 0;}
 .gsnip .gt{color:#1a0dab;font-size:.9rem;} .gsnip .gu{color:#0a7a33;font-size:.68rem;}
 .timeline{display:flex;align-items:flex-start;gap:0;overflow-x:auto;margin:.8rem 0;}
 .tstep{min-width:7.2rem;text-align:center;font-size:.68rem;position:relative;padding-top:1.1rem;}
 .tstep::before{content:'';position:absolute;top:.35rem;left:50%;transform:translateX(-50%);width:.75rem;height:.75rem;border-radius:50%;background:var(--honey);border:2px solid var(--cherry);}
 .tstep::after{content:'';position:absolute;top:.66rem;left:calc(50% + .5rem);width:calc(100% - 1rem);height:2px;background:var(--honey);}
 .tstep:last-child::after{display:none;}
 .tstep.hum::before{background:var(--ok);}
 .dbrec{background:#22262e;color:#d8dce6;border-radius:10px;padding:.8rem 1rem;font-family:Consolas,monospace;font-size:.76rem;line-height:1.7;max-width:44rem;}
 .dbrec .k{color:#7fa7d8;} .dbrec .arr{color:#8a7d68;font-family:Georgia,serif;font-style:italic;font-size:.72rem;}
 .f-name{color:#ff9d9d;} .f-price{color:#8fd89b;} .f-attr{color:#9db8ef;} .f-desc{color:#e8c98a;} .f-rel{color:#cbaef0;} .f-meta{color:#9aa3b2;}
 .vstack{position:relative;max-width:44rem;margin:.6rem 0 0;}
 .vstack .v{background:#fff;border:1px solid var(--line);border-radius:8px;padding:.3rem .7rem;font-size:.72rem;margin-top:-.15rem;}
 .vstack .v.old{opacity:.55;transform:translateX(.5rem);}
 .vstack .v.older{opacity:.35;transform:translateX(1rem);}
 .dawn{max-width:44rem;background:#fff;border:1px solid #d0d0d0;border-radius:12px;padding:1rem 1.2rem;font-family:Arial,Helvetica,sans-serif;color:#121212;}
 .dawn .cols{display:grid;grid-template-columns:1.1fr 1fr;gap:1.1rem;}
 .dawn .pimg{background:#f6f6f6;border-radius:8px;min-height:11rem;display:flex;align-items:center;justify-content:center;color:#999;font-size:.75rem;position:relative;}
 .dawn .vendor{font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:#666;}
 .dawn .ptitle{font-size:1.25rem;font-weight:400;margin:.15rem 0 .4rem;line-height:1.25;}
 .dawn .pprice{font-size:1rem;letter-spacing:.06em;margin:.2rem 0;}
 .dawn .tax{font-size:.62rem;color:#666;}
 .dawn .qty{display:inline-flex;border:1px solid #121212;margin:.5rem 0;font-size:.8rem;}
 .dawn .qty span{padding:.25rem .7rem;}
 .dawn .btn-o{display:block;text-align:center;border:1px solid #121212;padding:.45rem;font-size:.8rem;margin:.3rem 0;}
 .dawn .btn-s{display:block;text-align:center;background:#121212;color:#fff;padding:.5rem;font-size:.8rem;margin:.3rem 0;}
 .dawn .sect{border-top:1px solid #e5e5e5;margin-top:.9rem;padding-top:.7rem;font-size:.78rem;}
 .dawn .sect h6{margin:0 0 .3rem;font-size:.8rem;font-weight:700;}
 .dawn table{width:100%;border-collapse:collapse;}
 .dawn td{border:1px solid #eee;padding:.25rem .5rem;font-size:.74rem;}
 .dawn .relrow{display:flex;gap:.5rem;}
 .dawn .relrow div{flex:1;background:#f6f6f6;border-radius:6px;height:3.4rem;display:flex;align-items:center;justify-content:center;font-size:.65rem;color:#999;}
 .tag{position:absolute;font-size:.58rem;font-weight:700;padding:.05rem .35rem;border-radius:4px;color:#fff;}
 .taglbl{display:inline-block;font-size:.6rem;font-weight:700;padding:.06rem .4rem;border-radius:4px;color:#fff;margin-left:.3rem;vertical-align:middle;font-family:Georgia,serif;}
 .tg-name{background:#c04747;} .tg-price{background:#1d6b2a;} .tg-attr{background:#2c4a8a;} .tg-desc{background:#8a5a12;} .tg-rel{background:#5b3a8a;} .tg-img{background:#666;}

 /* --- Darling storefront replica (colors/fonts sampled from the live theme) --- */
 .dar{max-width:46rem;background:#fff6e9;border:1px solid #e8d9b8;border-radius:12px;font-family:Inter,Arial,sans-serif;color:#3a1d20;overflow:hidden;}
 .dar-head{background:#fdecd2;display:flex;align-items:center;gap:.8rem;padding:.5rem .9rem;font-size:.66rem;}
 .dar-logo{font-family:'Playfair Display',Georgia,serif;font-size:1.15rem;color:#3a1d20;}
 .dar-nav{color:#9c6f2f;}
 .dar-search{flex:1;background:#fff;border-radius:99px;padding:.32rem .8rem;color:#9a9a9a;}
 .dar-cols{display:grid;grid-template-columns:1.05fr 1fr;gap:1rem;padding:1rem;}
 .dar-img{background:#fff;border-radius:8px;display:flex;align-items:center;justify-content:center;min-height:11rem;}
 .dar-mat{background:linear-gradient(135deg,#c09a63,#a97f4b);border-radius:6px;width:85%;height:8.5rem;display:flex;align-items:center;justify-content:center;font-family:'Comic Sans MS',cursive;font-weight:700;font-size:1.5rem;color:#1c1611;letter-spacing:.06em;transform:rotate(-1deg);}
 .dar-title{font-family:'Playfair Display',Georgia,serif;font-size:1.18rem;line-height:1.3;}
 .dar-price{font-family:'Playfair Display',Georgia,serif;font-size:1rem;margin:.45rem 0;}
 .dar-price .lv{color:#9c6f2f;}
 .dar-hr{border:none;border-top:1px solid #e0b95c;margin:.5rem 0 .7rem;}
 .dar-buyrow{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap;}
 .dar-qty{border:1.5px solid #e8cfa0;border-radius:99px;padding:.35rem .8rem;font-size:.8rem;color:#c58a2a;background:#fff6e9;}
 .dar-btn{background:#dda220;color:#2d1b06;border-radius:99px;padding:.45rem 1.1rem;font-size:.78rem;font-weight:600;}
 .dar-info{background:#fffdf8;border:1px solid #efe3cd;border-radius:10px;padding:.6rem .8rem;font-size:.72rem;margin:.7rem 0 0;}
 .dar-red{color:#c0392b;}
 .dar-sub{color:#7a6a58;font-size:.66rem;margin:.3rem 0 .2rem;}
 .dar-row{border-top:1px solid #efe3cd;margin-top:.4rem;padding-top:.4rem;font-weight:700;font-size:.72rem;}
 .dar-desc{font-size:.76rem;margin-top:.7rem;line-height:1.5;}
 .dar-attrs{margin:0 1rem .8rem;font-size:.74rem;}
 .dar-attrs table{background:#fff;border-radius:8px;overflow:hidden;width:100%;border-collapse:collapse;margin-top:.3rem;}
 .dar-attrs td{border:1px solid #f2e7d2;padding:.28rem .6rem;}
 .dar-relh{font-family:'Playfair Display',Georgia,serif;color:#b98a2e;font-size:1.05rem;margin:.2rem 1rem .4rem;}
 .dar-rel{display:flex;gap:.6rem;padding:0 1rem .9rem;}
 .dar-rel div{flex:1;background:#fff;border:1px solid #f2e7d2;border-radius:10px;padding:.4rem;font-size:.62rem;text-align:center;color:#7a6a58;}
 .dar-rel .ph{background:#faf1e2;border-radius:6px;height:3rem;margin-bottom:.25rem;}
 .dar-reviews{border-top:1px solid #efe3cd;padding:.6rem 1rem .8rem;font-size:.72rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap;}
 .dar-revbtn{background:#d8374a;color:#fff;border-radius:6px;padding:.3rem .8rem;font-size:.68rem;}
 /* --- animated connector arrows --- */
 #linkoverlay{position:absolute;top:0;left:0;pointer-events:none;z-index:5;}
 .lnk{fill:none;stroke-width:2.6;opacity:0;}
 .lnk.drawing{opacity:.95;}
 .lnk.flowing{opacity:.95;stroke-dasharray:7 5;animation:helpdash 1.1s linear infinite;}
 @keyframes helpdash{to{stroke-dashoffset:-24;}}
 .srcfield{cursor:pointer;border-bottom:1px dotted currentColor;}
 .tgt-hl{outline:3px solid #c04747;outline-offset:3px;border-radius:4px;}
 .fg-flow{fill:none;stroke-dasharray:6 5;animation:helpdash 1.1s linear infinite;stroke-width:2;}

 .livestats{display:flex;gap:1.4rem;flex-wrap:wrap;background:var(--vanilla);border:1px solid var(--honey);border-radius:10px;padding:.5rem 1rem;margin:.6rem 0;font-size:.8rem;}
 .livestats b{font-size:1.05rem;color:var(--cherry);}
 .toc a.on{font-weight:700;text-decoration:underline;}
 .glow{background:#fff3b0;border-radius:4px;box-shadow:0 0 0 3px #fff3b0;transition:all .2s;}
 .nchip{cursor:pointer;}
 .tstep{opacity:0;transform:translateY(10px);transition:opacity .5s,transform .5s;}
 .tstep.vis{opacity:1;transform:none;}
 details.flag{cursor:pointer;}
 details.flag summary{font-weight:600;list-style:none;}
 details.flag summary::before{content:'▸ ';color:#d99b2b;}
 details.flag[open] summary::before{content:'▾ ';}
 .fix{display:grid;grid-template-columns:1fr 1fr;gap:.5rem;margin-top:.45rem;font-size:.8rem;}
 .fix .w{background:#fbeaea;border:1px solid #e3b8b8;border-radius:7px;padding:.35rem .55rem;}
 .fix .r{background:#eef8ee;border:1px solid #b5d9b5;border-radius:7px;padding:.35rem .55rem;}
 .fix .w::before{content:'✗ грешно';display:block;font-size:.62rem;font-weight:700;color:#a12020;}
 .fix .r::before{content:'✓ вярно';display:block;font-size:.62rem;font-weight:700;color:#186034;}

 .catbox{max-width:46rem;background:#fdf6e7;border:2px solid #c9a24a;border-radius:14px;padding:.7rem .9rem;transition:box-shadow .4s;}
 .catbox h4{margin:0 0 .5rem;font-size:.95rem;color:#8a5a12;}
 .catbox h4 .fadeval{font-weight:700;color:var(--cherry);}
 .prodbox{background:#fff;border:1.5px solid var(--line);border-radius:11px;padding:.6rem .8rem;}
 .prodbox>h5{margin:0 0 .5rem;font-size:.8rem;color:#2a2118;}
 .prodgrid{display:grid;grid-template-columns:1fr auto 1.2fr;gap:.6rem;align-items:start;}
 .fieldbox{border:1.5px solid;border-radius:9px;padding:.4rem .6rem;font-size:.74rem;margin-bottom:.45rem;transition:box-shadow .4s;}
 .fieldbox b{display:block;font-size:.68rem;letter-spacing:.03em;margin-bottom:.15rem;}
 .fb-attr{background:#eef2fb;border-color:#b8c6e8;color:#2c4a8a;min-height:6.2rem;}
 .fb-brand{background:#eef2fb;border-color:#b8c6e8;color:#2c4a8a;}
 .fb-name{background:#fbeaea;border-color:#c04747;color:#8c1d2f;min-height:3.4rem;}
 .fb-desc{background:#fdf1e2;border-color:#e8cfa0;color:#8a5a12;}
 .fb-meta{background:#f0f2f5;border-color:#c6ccd6;color:#4a5464;}
 .fb-rel{background:#f3ecfa;border-color:#d0bce6;color:#5b3a8a;}
 .fb-price{background:#eef8ee;border-color:#b5d9b5;color:#1d6b2a;}
 .fadeval{transition:opacity .3s;}
 .fadeval.out{opacity:0;}
 .tick{box-shadow:0 0 0 4px rgba(201,162,74,.4);}
 .gluearr{align-self:start;margin-top:.2rem;}
</style>

<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&display=swap" rel="stylesheet">
<div class="toc"><b>Съдържание:</b>
 <a href="#what">Какво е това</a> <a href="#sacred">Неприкосновените данни</a>
 <a href="#fields">Как е устроен продуктът</a> <a href="#shop">Как изглежда в магазина</a>
 <a href="#review">Как се преглежда (работният процес)</a> <a href="#edit">Редактиране</a>
 <a href="#names">Имената</a> <a href="#pages">Всички страници</a>
 <a href="#storage">Как се съхранява</a> <a href="#flags">Червени флагове</a>
</div>

<h2 id="what">1. Какво е това и каква е твоята роля</h2>
<div class="card">
<p>Подготвяме онлайн магазин (Shopify) с <b>14 159 продукта</b> за дома. Изходните данни са
от касовата система (Microinvest) + свалени данни от страниците на доставчиците. AI агенти
са обогатили всеки продукт: написали са описание, попълнили са атрибути, проверили са марката
в интернет и са сверили текста със снимката.</p>
<p><b>Ти си последната дума.</b> НИЩО не тръгва към магазина без човешко одобрение — само
продуктите, които ТИ одобриш, се изнасят. Автоматичният AI-рецензент само <i>предлага</i>
(син чип „Рецензентът предлага: готов за сайта“) — предложението му няма сила, докато ти
не натиснеш <b>✓ Одобри</b>.</p>
<div class="livestats" id="livestats">
 <span><b id="st-enr">…</b><br>обработени</span>
 <span><b id="st-appr">…</b><br>одобрени от теб</span>
 <span><b id="st-sugg">…</b><br>чакат твоя преглед с предложение</span>
 <span class="muted" style="align-self:center">← на живо, обновява се при всяко отваряне</span>
</div>
<p>Твоите редакции са неприкосновени: никой агент никога не презаписва това, което си
променил. Системата дори се <b>учи от редакциите ти</b> — ако системно махаш определен тип
думи, тя извежда правило и започва да пише така за следващите продукти (виж „Уроци“).</p>
</div>


<div class="diagram">
<svg viewBox="0 0 960 190" xmlns="http://www.w3.org/2000/svg" style="max-width:960px;width:100%">
 <defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#8c1d2f"/></marker></defs>
 <rect x="8" y="14" width="150" height="52" rx="9" fill="#fdf9f0" stroke="#e8d9b8"/>
 <text x="83" y="36" text-anchor="middle" font-size="13" font-weight="bold" fill="#2a2118">Каса Microinvest</text>
 <text x="83" y="54" text-anchor="middle" font-size="10.5" fill="#8a7d68">код · цена · количество</text>
 <rect x="8" y="118" width="150" height="52" rx="9" fill="#fdf9f0" stroke="#e8d9b8"/>
 <text x="83" y="140" text-anchor="middle" font-size="13" font-weight="bold" fill="#2a2118">Сайт на доставчика</text>
 <text x="83" y="158" text-anchor="middle" font-size="10.5" fill="#8a7d68">описания · снимки · размери</text>
 <line class="fg-flow" x1="158" y1="40" x2="230" y2="78" stroke="#8c1d2f" marker-end="url(#ar)"/>
 <line class="fg-flow" x1="158" y1="144" x2="230" y2="106" stroke="#8c1d2f" marker-end="url(#ar)"/>
 <rect x="236" y="62" width="160" height="62" rx="9" fill="#fff" stroke="#8c1d2f" stroke-width="1.5"/>
 <text x="316" y="84" text-anchor="middle" font-size="13" font-weight="bold" fill="#8c1d2f">AI агент обогатява</text>
 <text x="316" y="101" text-anchor="middle" font-size="10" fill="#8a7d68">чете снимката · търси в уеб</text>
 <text x="316" y="114" text-anchor="middle" font-size="10" fill="#8a7d68">проверява марката · пише текст</text>
 <line class="fg-flow" x1="396" y1="93" x2="446" y2="93" stroke="#8c1d2f" marker-end="url(#ar)"/>
 <rect x="452" y="62" width="150" height="62" rx="9" fill="#fff" stroke="#e8d9b8"/>
 <text x="527" y="84" text-anchor="middle" font-size="13" font-weight="bold" fill="#2a2118">AI рецензент</text>
 <text x="527" y="101" text-anchor="middle" font-size="10" fill="#8a7d68">проверява всичко и само</text>
 <text x="527" y="114" text-anchor="middle" font-size="10" fill="#25508f">ПРЕДЛАГА 🔎</text>
 <line class="fg-flow" x1="602" y1="93" x2="652" y2="93" stroke="#8c1d2f" marker-end="url(#ar)"/>
 <rect x="658" y="54" width="150" height="78" rx="9" fill="#dcefdd" stroke="#186034" stroke-width="2"><animate attributeName="stroke-width" values="2;4;2" dur="2.2s" repeatCount="indefinite"/></rect>
 <text x="733" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#186034">ЧОВЕК — ТИ</text>
 <text x="733" y="99" text-anchor="middle" font-size="10.5" fill="#186034">преглеждаш · редактираш</text>
 <text x="733" y="116" text-anchor="middle" font-size="11" font-weight="bold" fill="#186034">✓ Одобряваш</text>
 <line class="fg-flow" x1="808" y1="93" x2="858" y2="93" stroke="#186034" marker-end="url(#ar)"/>
 <rect x="864" y="66" width="88" height="54" rx="9" fill="#fdf9f0" stroke="#e8d9b8"/>
 <text x="908" y="89" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#2a2118">Shopify</text>
 <text x="908" y="106" text-anchor="middle" font-size="10.5" fill="#8a7d68">магазинът</text>
 <text x="733" y="150" text-anchor="middle" font-size="10.5" fill="#186034" font-weight="bold">← нищо не минава без теб</text>
</svg>
</div>

<h2 id="sacred">2. Неприкосновените данни (не се редактират)</h2>
<div class="card" id="sacred-card">
<p>Четири полета идват директно от касата и <b>никой</b> — нито AI, нито ние — не ги променя:</p>
<p><span id="sacred-line" style="display:inline-block"><b>Код · Цена · Количество · Мярка</b></span></p>
<p>Цената на сайта е ТОЧНО касовата „Продажна цена“ — същото число, показано в евро
(напр. 12,50 €). Ако видиш грешна цена, тя се оправя в касата, не тук.</p>
</div>

<h2 id="fields">3. Как е устроен един продукт (полетата)</h2>
<div class="card">
<table>
<tr><th>Поле</th><th>Какво е</th><th>За какво внимавай</th></tr>
<tr><td><b>Наименование</b></td><td>Името на продукта, СГЛОБЕНО по конвенция от атрибутите
(виж т. 6)</td><td>Следва ли шаблона; вярно ли описва продукта</td></tr>
<tr><td><b>Бранд</b></td><td>Истинската марка на производителя</td><td>Да НЕ е доставчик
(Levena, Mira-N, Egera…), материал („Инокс“), складов префикс или име на колекция</td></tr>
<tr><td><b>Атрибути</b></td><td>„Ключ: стойност; ключ: стойност“ — Тип, Материал, Цвят,
Размер, Форма… по списъка на категорията</td><td>Те стават ФИЛТРИТЕ в магазина и от тях се
сглобява името — грешен атрибут = грешно име + грешен филтър</td></tr>
<tr><td><b>Описание</b></td><td>HTML текст за продуктовата страница</td><td>Чист български
(без русизми), БЕЗ измислици — всяко твърдение да идва от източника или снимката</td></tr>
<tr><td><b>Мета наименование</b></td><td>SEO заглавие (какво вижда Google), до 60 знака</td>
<td>Броячът на картата показва дължината и ✓</td></tr>
<tr><td><b>Мета описание</b></td><td>SEO описание, до 160 знака</td><td>Да не е отрязано
насред дума</td></tr>
<tr><td><b>Свързани</b></td><td>Кодове на ВАРИАНТИ на същия продукт (друг цвят/размер на
същия модел)</td><td>Само истински варианти — не просто „подобни“ продукти</td></tr>
<tr><td><b>Категория</b></td><td>Категорията в магазина (по Shopify таксономията)</td>
<td>Определя кой списък с атрибути важи</td></tr>
</table>
<p style="margin-top:.8rem"><b>Как изглежда записът в базата</b> — един продукт е един запис
с тези полета (цветът на всяко поле съвпада с етикета му върху страницата в т. 4 ↓):</p>
<div class="dbrec">{<br>
&nbsp;<span class="k">"Код"</span>: "070233", <span class="k">"Цена"</span>: <span class="f-price srcfield" id="db-price">"6,90 € / 13,50 лв."</span>, <span class="k">"Мярка"</span>: "бр." <span class="arr">← от касата, недосегаеми</span><br>
&nbsp;<span class="k">"Категория"</span>: <span class="f-meta srcfield" id="db-cat">"Изтривалки"</span> <span class="arr">← определя кои атрибути се попълват</span><br>
&nbsp;<span class="k">"Бранд"</span>: <span class="f-name" id="db-brand">"—"</span><br>
&nbsp;<span class="k">"Атрибути"</span>: <span class="f-attr srcfield" id="db-attr">"Тип: Изтривалка; Материал: Кокосово влакно; Размер: 40×60 см; Цвят: Бежов"</span><br>
&nbsp;<span class="k">"Наименование"</span>: <span class="f-name srcfield" id="db-name">"Входна изтривалка WELCOME 40x60 см – Бежова / Кокос"</span><br>
&nbsp;<span class="k">"Описание"</span>: <span class="f-desc srcfield" id="db-desc">"&lt;p&gt;Класическа входна изтривалка от естествен кокос…&lt;/p&gt;"</span><br>
&nbsp;<span class="k">"Мета наименование"</span>: <span class="f-meta srcfield" id="db-meta">"Входна изтривалка WELCOME 40×60 см | Дарлинг"</span><br>
&nbsp;<span class="k">"Мета описание"</span>: <span class="f-meta srcfield" id="db-meta2">"Кокосова изтривалка WELCOME за входна врата…"</span><br>
&nbsp;<span class="k">"Свързани"</span>: <span class="f-rel srcfield" id="db-rel">"070234, 070235"</span><br>
}</div>
<p class="muted" style="margin:.5rem 0 0">Това е само СЪХРАНЕНИЕТО — как полетата се
захранват едно друго и къде отиват на сайта показва диаграмата по-долу ↓.</p>

<p style="margin-top:1rem"><b>Как полетата живеят едно в друго и се захранват</b> —
всеки продукт е ВЪТРЕ в категория; категорията определя кои атрибути се попълват, а
атрибутите + брандът сглобяват името. Гледай как категорията се сменя на всеки 2 секунди
и атрибутите + името се сменят В РИТЪМ с нея:</p>
<div class="catbox" id="g-cat">
 <h4>Категория: „<span class="fadeval" id="rot-cat">Изтривалки</span>“
  <span class="muted" style="font-size:.7rem;font-weight:400"> — определя списъка с атрибути ↓</span></h4>
 <div class="prodbox">
  <h5>Продукт <span class="muted">(070233)</span></h5>
  <div class="prodgrid">
   <div>
    <div class="fieldbox fb-attr" id="g-attr"><b>АТРИБУТИ</b><span class="fadeval" id="rot-attr">Тип: Изтривалка<br>Материал: Кокос<br>Размер: 40×60 см<br>Цвят: Бежов</span></div>
    <div class="fieldbox fb-brand" id="g-brand"><b>БРАНД</b><span class="fadeval" id="rot-brand">—</span></div>
   </div>
   <svg class="gluearr" width="46" height="175" viewBox="0 0 46 175">
    <defs><marker id="ga2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#8c1d2f"/></marker></defs>
    <path class="fg-flow" d="M4,55 C 24,55 26,40 40,32" stroke="#2c4a8a" marker-end="url(#ga2)"/>
    <path class="fg-flow" d="M4,150 C 30,150 30,55 40,38" stroke="#2c4a8a" marker-end="url(#ga2)"/>
    <text x="21" y="95" text-anchor="middle" font-size="8.5" fill="#8a7d68" font-style="italic">сглобяват</text>
    <text x="21" y="105" text-anchor="middle" font-size="8.5" fill="#8a7d68" font-style="italic">името</text>
   </svg>
   <div>
    <div class="fieldbox fb-name" id="g-name"><b>НАИМЕНОВАНИЕ</b><span class="fadeval" id="rot-name">Входна изтривалка WELCOME 40x60 см – Бежова / Кокос</span></div>
    <div class="fieldbox fb-desc" id="g-desc"><b>ОПИСАНИЕ</b>Класическа входна изтривалка от естествен кокос…</div>
    <div class="fieldbox fb-meta" id="g-meta"><b>МЕТА (SEO)</b>Входна изтривалка WELCOME 40×60 см | Дарлинг</div>
    <div class="fieldbox fb-rel" id="g-rel"><b>СВЪРЗАНИ</b>070234, 070235</div>
    <div class="fieldbox fb-price" id="g-price"><b>ЦЕНА · КОД · МЯРКА</b>6,90 € — от касата, недосегаеми</div>
   </div>
  </div>
 </div>
</div>
<p class="muted" style="max-width:46rem">Пунктираните стрелки тръгват от тези кутии надолу към
страницата на магазина (т. 4) и към Google — <b>задръж мишката върху кутия</b>, за да светне
нейната стрелка и мястото ѝ.</p>
<div class="vstack">
 <div class="v older">версия 1 — суров запис от касата (14.07)</div>
 <div class="v old">версия 2 — AI обогатяване (14.07) · версия 3 — име по конвенцията (17.07)</div>
 <div class="v"><b>версия 4 — твоята редакция + одобрение (текуща)</b> — старите остават завинаги</div>
</div>
</div>

<h2 id="shop">4. Как ще изглежда продуктът в магазина</h2>
<div class="card">

<div class="diagram">
<div class="gsnip" id="t-google"><span class="lab" style="color:var(--cherry);font-size:.62rem;font-weight:700">ТАКА ИЗГЛЕЖДА В GOOGLE (мета полетата)</span><br>
 <span class="gt">Входна изтривалка WELCOME 40×60 см | Дарлинг</span><br>
 <span class="gu">darling7.com › изтривалки</span><br>
 Кокосова изтривалка WELCOME за входна врата — здрава, попиваща, 40×60 см…</div>
<div class="dar" id="t-shop">
 <div class="dar-head"><span class="dar-logo">Darling</span>
  <span class="dar-nav">Продукти&ensp;За нас&ensp;Помощ&ensp;Контакти</span>
  <span class="dar-search">🔍&ensp;Какво търсиш, darling?</span><span>👤&ensp;🛍</span></div>
 <div class="dar-cols">
  <div class="dar-img" id="t-img"><div class="dar-mat">WELCOME</div></div>
  <div>
   <div class="dar-title" id="t-title">Входна изтривалка WELCOME 40x60 см – Бежова / Кокос</div>
   <div class="dar-price" id="t-price">€6,90 <span class="lv">/ 13,50 лв.</span></div>
   <hr class="dar-hr">
   <div class="dar-buyrow"><span class="dar-qty">−&ensp;1&ensp;+</span>
    <span class="dar-btn">🛍 Добавяне към количката</span></div>
   <div class="dar-info">✦ <b class="dar-red">Наложен платеж</b> — плати при получаване.<br>
    Отвори и виж, преди да платиш, darling.
    <div class="dar-sub">Еконт и Спиди · до адрес или до офис · Поръчай до 15:00 и изпращаме
    още същия работен ден.</div>
    <div class="dar-row">Доставка</div><div class="dar-row">Връщане и замяна</div></div>
   <div class="dar-desc" id="t-desc">Класическа входна изтривалка от естествен кокос с надпис
    WELCOME — здрава, попиваща и устойчива на изтриване. Подходяща за входни врати и антрета.</div>
  </div>
 </div>
 <div class="dar-attrs" id="t-attr"><b>Характеристики</b>
  <table><tr><td>Тип</td><td>Изтривалка</td></tr><tr><td>Материал</td><td>Кокосово влакно</td></tr>
  <tr><td>Размер</td><td>40×60 см</td></tr><tr><td>Цвят</td><td>Бежов</td></tr></table>
  <span style="font-size:.62rem;color:#7a6a58">същите стойности стават и филтрите в категорията</span></div>
 <div class="dar-relh">Може да ти хареса и това</div>
 <div class="dar-rel" id="t-rel">
  <div><div class="ph"></div>070234 · Сива / Кокос</div>
  <div><div class="ph"></div>070235 · Кафява / Кокос</div>
  <div><div class="ph"></div>Табуретка стълба</div></div>
 <div class="dar-reviews"><b>Отзиви от клиенти</b> Бъдете първият, който ще напише отзив
  <span class="dar-revbtn">Напишете отзив</span></div>
</div>
<p class="muted" style="max-width:46rem">Точно така изглежда страницата в магазина (по темата
на darling — кремав фон, златни бутони, серифни заглавия). Описанието и характеристиките се
показват под бутона за купуване; „Може да ти хареса и това“ идва от полето Свързани.</p>

<p>• <b>Наименование</b> → заглавието на продуктовата страница и в списъците/резултатите.<br>
• <b>Мета полетата</b> → какво показва Google в резултатите от търсене.<br>
• <b>Атрибутите</b> → филтрите отстрани („Материал: Керамика“, „Цвят: Син“…) — клиентът
филтрира по тях; празен атрибут = продуктът ИЗПАДА от този филтър.<br>
• <b>Описанието</b> → текстът на страницата на продукта.<br>
• <b>Снимките</b> → автоматично изрязани от фона и уголемени (виж ги на картата — бял фон
в прегледа = прозрачен в магазина).<br>
• <b>Свързани</b> → блок „Други варианти“ на страницата на продукта.<br>
• <b>Цената</b> → касовата цена в евро.</p>
</div>

<h2 id="review">5. Работният процес на преглед</h2>
<div class="card">
<p>Работиш на главната страница (<a href="/">Преглед по етапи</a>). Всеки продукт е РЕД ОТ
КАРТИ — историята му отляво надясно:</p>
<p><b>Microinvest източник</b> (суровата каса) → <b>Данни от доставчика</b> (свалени от
страницата му, с линк и снимки) → <b>обработващите стъпки</b> (какво е променила всяка —
<span class="no" style="text-decoration:line-through">махнатото в червено</span> /
<span class="ok">добавеното в зелено</span>) → <b>ТЕКУЩО СЪСТОЯНИЕ</b> (голямата карта с
бутоните) → евентуално <b>предложение от рецензента</b>.</p>

<div class="diagram"><div class="rowmock">
 <div class="mcard"><h5>📒 Каса</h5>BR-ALKAN Капак акрил (17703)<br>Код 0136270 · 24,90 лв
  <span class="lbl">суровият запис — само за справка</span></div>
 <div class="marrow">→</div>
 <div class="mcard"><h5>🌐 Доставчик</h5>Акрилен капак, 27×33, прозрачен + 3 снимки · линк ↗
  <span class="lbl">какво е свалено от сайта му</span></div>
 <div class="marrow">→</div>
 <div class="mcard"><h5>⚙ AI стъпка</h5><span class="mrem">Капак акрил (17703)</span><br>
  <span class="madd">Акрилен капак 27×33 см</span><br>Цвят: <span class="mrem">Черен</span> <span class="madd">Прозрачен</span>
  <span class="lbl">какво е променила — червено/зелено</span></div>
 <div class="marrow">→</div>
 <div class="mcard cur" id="mk-cur"><h5>★ ТЕКУЩО СЪСТОЯНИЕ</h5>Alkan Züccaciye Акрилен капак 27×33 см<br>24,90 лв → 12,73 €<br>
  <span class="mbtn">✓ Одобри</span><span class="mbtn g">✎ Редактирай</span>
  <span class="lbl">тук работиш ти</span></div>
 <div class="marrow">→</div>
 <div class="mcard"><h5>🔎 Рецензент</h5>„Готов за сайта“ или предложени корекции с 1 клик
  <span class="lbl">само предложение — ти решаваш</span></div>
</div></div>

<p><b>За всеки продукт провери</b> (30–60 сек при добър продукт):</p>
<p>1. Снимката съответства ли на текста? (форма, материал, цвят, брой)<br>
2. Името по конвенцията ли е и вярно ли е?<br>
3. Брандът истинска марка ли е?<br>
4. Атрибутите пълни и верни ли са?<br>
5. Описанието честно ли е? Всяко конкретно твърдение (материал, размер, съвместимост)
трябва да се вижда на снимката или да е в източника.<br>
6. Свързаните наистина варианти ли са?</p>
<p><b>Ако всичко е наред → ✓ Одобри.</b> Продуктът се заключва и влиза в „Одобрени“ —
готов за магазина. <b>Ако нещо не е наред → ✎ Редактирай</b>, поправи и после Одобри —
твоята версия става окончателна.</p>
<p><b>Ред на работа:</b> започни с филтъра „За преглед“ (рисковите), после „С предложение“
(там рецензентът е свършил половината работа — проверяваш предложението му), накрая
останалите. Продуктите-варианти се показват един след друг (⛓ „свързан с горния“) — така
оправяш цялото семейство наведнъж.</p>
<p>Филтрите горе: <b>Всички</b> · <b>За преглед</b> · <b>С предложение</b> ·
<b>Одобрени</b> · <b>Необработени</b> (тези още чакат AI обработка — тях не ги гледаш).</p>
</div>

<h2 id="edit">6. Редактиране</h2>
<div class="card">
<p>Бутонът <b>✎ Редактирай</b> на текущата карта отваря всички полета:</p>
<p>• Текстовите полета се редактират направо.<br>
• <b>Свързани продукти</b>: чипове с × за махане; пишеш код или име в кутията и избираш от
падащия списък (със снимка) за добавяне.<br>
• <b>„↻ Състави името от атрибутите“</b> — сглобява име по конвенцията от текущите
атрибути. Ползвай го така: първо оправи атрибутите, после натисни бутона, после пипни
името на ръка ако трябва.<br>
• Накрая <b>✓ Одобри</b> — редакциите се записват като нова версия и продуктът се одобрява.</p>
<p>Ако сгрешиш — всяка версия се пази; собственикът може да върне всичко. Не можеш да
счупиш нищо необратимо.</p>
</div>

<h2 id="names">7. Имената — как се сглобяват</h2>
<div class="card">
<p>Имената НЕ се измислят на ръка — РЕНДВАТ се от атрибутите по шаблон:</p>
<div class="namechips">
 <span class="nchip nc1" data-w="1">Бранд</span><span>+</span>
 <span class="nchip nc2" data-w="2">Материал <small>(прилагателно)</small></span><span>+</span>
 <span class="nchip nc3" data-w="3">Форма</span><span>+</span>
 <span class="nchip nc4" data-w="4">ТИП</span><span>+</span>
 <span class="nchip nc5" data-w="5">Размер</span>
 <span class="muted" style="font-size:.72rem">← задръж мишката върху част</span>
</div>
<div class="namestr">
 <span class="w1" style="color:#2c4a8a">Alkan Züccaciye</span>
 <span class="w2" style="color:#1d6b2a">Акрилен</span>
 <span class="w3" style="color:#8a5a12">правоъгълен</span>
 <b class="w4" style="color:#8c1d2f">капак</b>
 <span class="w5" style="color:#5b3a8a">34,5×54,5 см</span>
 <span class="muted">← мъжки род: акрил<b>ен</b></span>
</div>
<div class="namestr">
 <span class="w1" style="color:#2c4a8a">HORECANO</span>
 <span class="w2" style="color:#1d6b2a">Метална</span>
 <span class="w3" style="color:#8a5a12">кръгла</span>
 <b class="w4" style="color:#8c1d2f">купа</b>
 <span class="w5" style="color:#5b3a8a">24 см</span>
 <span class="muted">← женски род: метал<b>на</b></span>
</div>
<p>• Прилагателните се съгласуват по род с типа (акрил<b>ен</b> капак / акрил<b>на</b>
купа / акрил<b>но</b> кошче) — автоматично.<br>
• Синонимните типове са уеднаквени: дозатор/пурер/диспенсър → всички са „Дозатор“.<br>
• Ако РЕДАКТИРАШ име на ръка, то се „закотвя“ — никой шаблон не го пипа повече.<br>
• Правилата (шаблони по тип, сезонни преименувания, Ø за кръгли и т.н.) се управляват на
страницата <a href="/naming">Именуване</a> — по-скоро за собственика, но е полезно да знаеш
откъде идват имената.</p>
</div>

<h2 id="pages">8. Всички страници (менюто горе)</h2>
<div class="card">
<table>
<tr><th>Страница</th><th>Какво има там</th></tr>
<tr><td><a href="/">Преглед по етапи</a></td><td><b>Основната ти работа</b> — редовете от карти, Одобри/Редактирай</td></tr>
<tr><td><a href="/classic">Класически изглед</a></td><td>Старият изглед с клавиши <kbd>A</kbd> одобри · <kbd>E</kbd> редактирай · <kbd>J</kbd>/<kbd>K</kbd> напред/назад</td></tr>
<tr><td>🕘 История (линк на всяка карта)</td><td>Пълната хронология на продукта — всяка версия от касата до днес</td></tr>
<tr><td><a href="/naming">Именуване</a></td><td>Правилата за сглобяване на имена (шаблони, чипове, пре-рендиране)</td></tr>
<tr><td><a href="/vocab">Типове</a></td><td>Речникът „суров тип → каноничен тип“ (610 → 135). Ако видиш продукт с грешен тип, тук се оправя съответствието</td></tr>
<tr><td><a href="/brands">Брандове</a></td><td>Речникът на истинските марки. Може да добавяш/триеш. Доставчиците са блокирани</td></tr>
<tr><td><a href="/schema">Категории</a></td><td>Категориите и филтърните групи на магазина (само за четене)</td></tr>
<tr><td><a href="/lessons">Уроци</a></td><td>Правила, изведени от ТВОИТЕ редакции — с бутон „Приложи“ те влизат в инструкциите на AI агентите</td></tr>
<tr><td><a href="/dupes">Дубликати</a></td><td>Групи възможни дубликати — „Свържи като варианти“ или „Не е дубликат“</td></tr>
<tr><td><a href="/readiness">Готовност</a></td><td>Колко продукта са готови/одобрени и какво блокира останалите</td></tr>
<tr><td><a href="/ops">Обработка</a></td><td>На живо: темпо на обработката, модели, разходи</td></tr>
</table>
</div>

<h2 id="storage">9. Как се съхранява всичко</h2>
<div class="card">

<div class="timeline">
 <div class="tstep"><b>Каса</b><br>суров запис</div>
 <div class="tstep"><b>Доставчик</b><br>свалени данни</div>
 <div class="tstep"><b>AI обогатяване</b><br>текст + атрибути</div>
 <div class="tstep"><b>Проверки</b><br>снимка · марка</div>
 <div class="tstep"><b>Име</b><br>по конвенцията</div>
 <div class="tstep"><b>AI рецензент</b><br>предложение</div>
 <div class="tstep hum"><b>ТИ</b><br>редакция + ✓</div>
 <div class="tstep hum"><b>Магазин</b><br>публикуван</div>
</div>

<p>Всяка промяна — от AI или от теб — е <b>нова версия</b>, старите никога не се губят.
Базата пази пълната история: суровият запис от касата → данните от доставчика → всяка AI
стъпка → твоите редакции. Затова картите могат да показват какво точно е променила всяка
стъпка. „🕘 История“ на картата показва всичко за конкретния продукт.</p>
<p>Одобрението ти се записва отделно и е неприкосновено — AI рецензентът ти няма право да
го промени или замести.</p>
</div>

<h2 id="flags">10. Червени флагове — най-честите реални проблеми</h2>
<div class="card">
<details class="flag"><summary>🚩 <b>Доставчик като бранд</b> — Levena, Mira-N, Egera, Vertex не са марки <span class="muted">(пример)</span></summary><div class="fix"><div class="w">Бранд: "Levena" <span class="muted">(от водния знак на снимката)</span></div><div class="r">Бранд: "" — празно, или истинската марка, ако се чете на снимката/в източника</div></div></details>
<details class="flag"><summary>🚩 <b>Измислици в описанието</b> — конкретика без доказателство <span class="muted">(пример)</span></summary><div class="fix"><div class="w">„изработена от неръждаема стомана 18/10, подходяща за съдомиялна“ — а на снимката е пластмаса</div><div class="r">„изработена от здрава пластмаса“ — само това, което се вижда или е в източника</div></div></details>
<details class="flag"><summary>🚩 <b>Руски думи / русизми</b> <span class="muted">(пример)</span></summary><div class="fix"><div class="w">„герметичен съд за съхранение на посуда“</div><div class="r">„херметичен съд за съхранение на съдове“</div></div></details>
<details class="flag"><summary>🚩 <b>Каталожни номера и кодове в името</b> <span class="muted">(пример)</span></summary><div class="fix"><div class="w">„Купа E2483 26 см (3067.R)“</div><div class="r">„Купа 26 см“ — кодът остава само в полето Каталожен номер</div></div></details>
<details class="flag"><summary>🚩 <b>Грешен тип</b> — оправи атрибута, името се сглобява само <span class="muted">(пример)</span></summary><div class="fix"><div class="w">Тип: „Контейнер“ за вакуумна торба → име „…Контейнер…“</div><div class="r">Тип: „Торба“ → името се пресглобява вярно от атрибутите</div></div></details>
<details class="flag"><summary>🚩 <b>Размер срещу обем</b> — прецени кое е полезно за клиента <span class="muted">(пример)</span></summary><div class="fix"><div class="w">„Метален кош 25,2×25 см“ — технически вярно, но кошовете се избират по обем</div><div class="r">„Метален кош 12 л“ — обемът е по-полезен; и двете стойности остават в атрибутите</div></div></details>
<details class="flag"><summary>🚩 <b>Свързани, които не са варианти</b> <span class="muted">(пример)</span></summary><div class="fix"><div class="w">Свързани: чаша + чиния от същата серия</div><div class="r">Свързани: същият модел в друг цвят/размер (сива, кафява изтривалка)</div></div></details>
<details class="flag"><summary>🚩 <b>Снимка ≠ текст</b> — снимката е истината <span class="muted">(пример)</span></summary><div class="fix"><div class="w">Текст: „кръгла форма“ · Снимка: правоъгълна</div><div class="r">Коригирай Форма по снимката → името и описанието се оправят</div></div></details>
</div>

<div class="card" style="border-left:3px solid var(--ok)">
<p><b>Накратко:</b> гледаш продукт → сверяваш със снимката и източника → Одобри или
Редактирай+Одобри. Ти си финалният филтър за качество и не можеш да счупиш нищо —
всичко се пази и всичко се връща. При съмнение: по-добре поправи или остави за питане,
отколкото да одобриш нещо съмнително.</p>
</div>
"""
    js_code = r"""

const LINKS = [
 ["g-name","t-title","#c04747"], ["g-desc","t-desc","#8a5a12"],
 ["g-meta","t-google","#5f6b7a"], ["g-attr","t-attr","#2c4a8a"],
 ["g-rel","t-rel","#5b3a8a"], ["g-price","t-price","#1d6b2a"],
 ["sacred-line","g-price","#1d6b2a"], ["mk-cur","t-shop","#186034"]];
let ov = null;
function rectOf(el){ const r = el.getBoundingClientRect();
  return {x:r.left+window.scrollX, y:r.top+window.scrollY, w:r.width, h:r.height}; }
function drawLinks(){
  try{
    if (ov) ov.remove();
    document.body.style.position = "relative";
    ov = document.createElementNS("http://www.w3.org/2000/svg","svg");
    ov.id = "linkoverlay";
    const W = document.documentElement.scrollWidth, H = document.documentElement.scrollHeight;
    ov.setAttribute("width", W); ov.setAttribute("height", H);
    ov.innerHTML = '<defs>' + LINKS.map((l,i) =>
      '<marker id="lm'+i+'" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">' +
      '<path d="M0,0 L10,5 L0,10 z" fill="'+l[2]+'"/></marker>').join('') + '</defs>';
    LINKS.forEach((l, i) => {
      const a = document.getElementById(l[0]), b = document.getElementById(l[1]);
      if (!a || !b) return;
      const ra = rectOf(a), rb = rectOf(b);
      const sx = ra.x + ra.w, sy = ra.y + ra.h/2;
      const ex = rb.x + rb.w + 6, ey = rb.y + rb.h/2;
      // right-margin gutter, fanned per link but CLAMPED to the visible width so no
      // curve ever swings offscreen and "arrives from nowhere"
      const maxX = document.documentElement.clientWidth - 28;
      const gx = Math.min(Math.max(sx, ex) + 90 + i*22, maxX);
      const p = document.createElementNS("http://www.w3.org/2000/svg","path");
      p.setAttribute("d", "M"+sx+","+sy+" C "+gx+","+sy+" "+gx+","+ey+" "+(ex+8)+","+ey);
      p.setAttribute("stroke", l[2]);
      p.setAttribute("class", "lnk");
      p.dataset.link = i;
      ov.appendChild(p);
      // invisible by default; on hover it DRAWS ITSELF from source toward target,
      // then switches to the flowing-dash style while the hover lasts
      let drawTimer = null;
      const show = () => {
        const L = p.getTotalLength();
        p.classList.remove("flowing");
        p.style.transition = "none";
        p.setAttribute("stroke-dasharray", L);
        p.setAttribute("stroke-dashoffset", L);
        p.removeAttribute("marker-end");
        p.classList.add("drawing");
        p.getBoundingClientRect();                       // reflow so the transition runs
        p.style.transition = "stroke-dashoffset .65s ease-out";
        p.setAttribute("stroke-dashoffset", "0");
        drawTimer = setTimeout(() => {                   // arrival: arrowhead + flow
          p.style.transition = "none";
          p.setAttribute("stroke-dasharray", "7 5");
          p.removeAttribute("stroke-dashoffset");
          p.setAttribute("marker-end", "url(#lm"+i+")");
          p.classList.add("flowing");
        }, 660);
        document.getElementById(l[1]).classList.add("tgt-hl");
      };
      const hide = () => {
        clearTimeout(drawTimer);
        p.classList.remove("drawing","flowing");
        p.style.transition = "none";
        p.removeAttribute("stroke-dashoffset");
        p.removeAttribute("marker-end");
        document.getElementById(l[1]).classList.remove("tgt-hl");
      };
      [a, b].forEach(el => {
        el.addEventListener("mouseenter", show);
        el.addEventListener("mouseleave", hide);
      });
    });
    document.body.appendChild(ov);
  }catch(e){}
}
window.addEventListener("load", () => setTimeout(drawLinks, 400));
let rT; window.addEventListener("resize", () => { clearTimeout(rT); rT = setTimeout(drawLinks, 300); });
// name-part hover: chip <-> words in the example names
document.querySelectorAll(".nchip[data-w]").forEach(ch => {
  const cls = ".w" + ch.dataset.w;
  ch.addEventListener("mouseenter", () => document.querySelectorAll(cls).forEach(w => w.classList.add("glow")));
  ch.addEventListener("mouseleave", () => document.querySelectorAll(cls).forEach(w => w.classList.remove("glow")));
});
// timeline: reveal steps one by one when scrolled into view
const steps = [...document.querySelectorAll(".tstep")];
let tlDone = false;
function revealTimeline(){
  if (tlDone || !steps.length) return;
  const r = steps[0].getBoundingClientRect();
  if (r.top < window.innerHeight - 60 && r.bottom > 0){
    tlDone = true;
    steps.forEach((st, i) => setTimeout(() => st.classList.add("vis"), i * 160));
  }
}
window.addEventListener("scroll", revealTimeline, {passive: true});
setTimeout(revealTimeline, 600);
// TOC scroll-spy
const secs = [...document.querySelectorAll("h2[id]")];
const tocs = [...document.querySelectorAll(".toc a")];
window.addEventListener("scroll", () => {
  let cur = secs[0];
  secs.forEach(h => { if (h.getBoundingClientRect().top < 130) cur = h; });
  tocs.forEach(a => a.classList.toggle("on", a.getAttribute("href") === "#" + cur.id));
}, {passive: true});
// live project stats
fetch("/api/stats").then(r => r.json()).then(d => {
  document.getElementById("st-enr").textContent = d.enriched + " / " + d.total;
  document.getElementById("st-appr").textContent = d.approved;
  document.getElementById("st-sugg").textContent = d.suggested;
}).catch(() => {});
// details open animation is native; expanding a flag re-lays the page -> redraw arrows
document.querySelectorAll("details.flag").forEach(d => d.addEventListener("toggle", () => setTimeout(drawLinks, 60)));
// category <-> attributes <-> name rolling in sync every 2s
const ROT = [
 {cat:"Изтривалки", brand:"—", attrs:"Тип: Изтривалка<br>Материал: Кокос<br>Размер: 40×60 см<br>Цвят: Бежов",
  name:"Входна изтривалка WELCOME 40x60 см – Бежова / Кокос"},
 {cat:"Чаши", brand:"Bormioli Rocco", attrs:"Тип: Чаша<br>Материал: Стъкло<br>Обем: 350 мл<br>Цвят: Прозрачен",
  name:"Bormioli Rocco Стъклена чаша 350 мл"},
 {cat:"Тигани", brand:"Tefal", attrs:"Тип: Тиган<br>Материал: Алуминий<br>Диаметър: Ø28 см<br>Покритие: Незалепващо",
  name:"Tefal Алуминиев тиган Ø28 см"}];
let ri = 0;
setInterval(() => {
  ri = (ri + 1) % ROT.length;
  const els = ["rot-cat","rot-attr","rot-name","rot-brand"].map(id => document.getElementById(id));
  if (els.some(e => !e)) return;
  els.forEach(e => e.classList.add("out"));
  ["g-cat","g-attr","g-name"].forEach(id => document.getElementById(id).classList.add("tick"));
  setTimeout(() => {
    els[0].textContent = ROT[ri].cat;
    els[1].innerHTML = ROT[ri].attrs;
    els[2].textContent = ROT[ri].name;
    els[3].textContent = ROT[ri].brand;
    els.forEach(e => e.classList.remove("out"));
    setTimeout(() => ["g-cat","g-attr","g-name"].forEach(id =>
      document.getElementById(id).classList.remove("tick")), 500);
  }, 320);
}, 5000);


"""
    return _SHELL.format(title="Помощ — наръчник на редактора", body=body, js=js_code)
