.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Pricelists_index
===========================================================
Списък с ценови правила

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pricelist </barsy.help/210-dictionary/pricelist.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с всички `ценови правила </barsy.help/210-dictionary/pricelist.html>`__ в системата (pricelists) с богат набор от филтри — по тип (продажна цена, отстъпка, бонус, `абонамент </barsy.help/210-dictionary/subscription.html>`__, доставка, `зареждане </barsy.help/210-dictionary/storeload.html>`__), група, статус, обект/`каса </barsy.help/210-dictionary/pos.html>`__, `артикул </barsy.help/210-dictionary/article.html>`__, `клиент </barsy.help/210-dictionary/client.html>`__ или клиентска група, регион, държава, `абонамент </barsy.help/210-dictionary/subscription.html>`__. `Ценовите правила </barsy.help/210-dictionary/pricelist.html>`__ са централният механизъм за гъвкаво ценообразуване — те се прилагат автоматично върху `сметките </barsy.help/210-dictionary/account.html>`__ според действащите критерии (време, контекст, `клиент </barsy.help/210-dictionary/client.html>`__). За всяко правило справката връща броя свързани `артикули </barsy.help/210-dictionary/article.html>`__/`клиенти </barsy.help/210-dictionary/client.html>`__/групи и текущия статус (активно/изчаквано/изтекло).

*Типични случаи: преглед на действащи промоции, одит на конфигурирани правила преди ценова кампания, експорт за анализ на ценова стратегия, идентификация на конфликтни правила с припокриваща се област на действие.*

**Име**: Pricelists_index
**Категория**: Catalog


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$action_type**
     - *string*
     - Тип на върнатите данни

			* **content** - *структура на списъка*
			* **values** - *стойности на списъка* **По подразбиране:** 'content'
   * - **$filters**
     - PricelistsIndexFilters_ 
     - масив от налични филтри за този списък.

			*Всички са опционални* **По подразбиране:** []
   * - **$page_num**
     - *int*
     - Номер на желана страница **По подразбиране:** 1
   * - **$rows**
     - *int*
     - Брой реда на страница **По подразбиране:** 50
   * - **$order_by**
     - *string*
     - Сортиране по (името на колоната като елемент)
   * - **$order_dir**
     - *string*
     - Посока на сортиране

			* **asc** - *възходящо*
			* **desc** - *низходящо* **По подразбиране:** 'asc'
   * - **$columns**
     - *array* | *object*
     - Списък от колоните, които да бъдат включени в отговора (ако е празен, показва избрани по подразбиране)

			* **pricelist_id** - *ID*
			* **pricelist_name** - *Име*
			* **type_title** - *Тип (Тип на ценоразписа)*
			* **group_name** - *Група (Група ценоразписи)*
			* **periods_date** - *По дати (Период на действие по дати)*
			* **periods_time** - *По часове (Период на действие по часове)*
			* **modificator_type** - Тип ценови `модификатор </barsy.help/210-dictionary/modificator.html>`__ (Тип ценови `модификатор </barsy.help/210-dictionary/modificator.html>`__)
			* **modificator_round_type** - *Закръгляне (Закръгляне на изчислените цени)*
			* **articles_cnt** - Брой `артикули </barsy.help/210-dictionary/article.html>`__ (Брой `артикули </barsy.help/210-dictionary/article.html>`__ в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **clients_cnt** - Брой `клиенти </barsy.help/210-dictionary/client.html>`__ (Брой `клиенти </barsy.help/210-dictionary/client.html>`__ в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **client_groups_cnt** - Брой кл.групи (Брой клиентски групи в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **tax_regions_cnt** - Брой дан.рег (Брой типове доставка в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **countries_cnt** - Брой държави (Брой държави в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **subscriptions_cnt** - Брой аб.планове (Брой абонаментни планове в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **price_tax_mode** - *С ДДС (С включено ДДС или без ДДС)*
			* **create_date** - Дата на създаване (Дата на създаване на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **last_update** - Последна актуализация (Дата на последна актуализация на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **price_tax_id** - *ДДС група (ДДС група за ценоразписа)*
			* **weight** - *Тежест (Тежест/приоритет при застъпване)*
			* **current_status** - *В момента (Текущ статус (дали е активен в момента))* **По подразбиране:** ["pricelist_id","pricelist_name","type_title","periods_date","periods_time","modificator_type","articles_cnt","clients_cnt","client_groups_cnt","price_tax_id","weight","current_status"]
   * - **$search**
     - *string*
     - 
   * - **$params**
     - *mixed*
     - 
   * - **$active_struct_id**
     - *string*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PricelistsIndexResultData_                                             Обект с данни за резултатите
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PricelistsIndexFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: PricelistsIndexFilters

   * - Параметър
     - Тип
     - Описание
   * - **$pricelist_type_id**
     - *string*
     - *Филтриране по тип ценоразпис*

			* **1** - Цена - `артикули </barsy.help/210-dictionary/article.html>`__
			* **6** - Отстъпка `артикул </barsy.help/210-dictionary/article.html>`__
			* **3** - Отстъпка - `сметка </barsy.help/210-dictionary/account.html>`__
			* **2** - Бонус - `сметка </barsy.help/210-dictionary/account.html>`__
			* **5** - *Доставна цена*
			* **8** - Складова наличност - `артикул </barsy.help/210-dictionary/article.html>`__
			* **4** - Отстъпка - `абонамент </barsy.help/210-dictionary/subscription.html>`__
			* **7** - Цена - `артикул </barsy.help/210-dictionary/article.html>`__ `абонамент </barsy.help/210-dictionary/subscription.html>`__
			* **9** - *Бонус програма*
			* **10** - `Артикули </barsy.help/210-dictionary/article.html>`__ в `продажба </barsy.help/210-dictionary/sale.html>`__
			* **11** - Публични `артикули </barsy.help/210-dictionary/article.html>`__
   * - **$barsy_id**
     - *string*
     - За `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$modificator_value**
     - *string*
     - Стойност на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$current_status**
     - *string*
     - *Филтриране по статус*

			* **0** - *Чакащо*
			* **1** - *Активно*
			* **2** - *Неактивирано*
			* **3** - *Архивирано*
   * - **$pricelist_group_id**
     - *string*
     - *Група ценоразписи*

			* **1** - *Основна*
   * - **$article**
     - *string*
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../articles/search` )
   * - **$client_name**
     - *string*
     - Обхваща конкретен `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getlistsmart` )
   * - **$client_group_name**
     - *string*
     - *Филтриране по клиентска група* ( виж: :doc:`../clients/getgroups` )
   * - **$pos_id**
     - *string*
     - Този филтър се използва за правила, на които е присвоена `каса </barsy.help/210-dictionary/pos.html>`__. Ако искате да филтрирате по `търговски обект </barsy.help/210-dictionary/barsy.html>`__, използвайте филтъра „За `търговски обект </barsy.help/210-dictionary/barsy.html>`__“.
   * - **$tax_region_id**
     - *string*
     - *Тип доставка / данъчен регион*

			* **1** - *Употреба на място*
			* **2** - *Доставка до адрес*
			* **3** - *Взимане на място*
			* **4** - *Получаване от офис на куриер*
			* **5** - *За вкъщи*
   * - **$country_id**
     - *string*
     - *Обхваща държава*

			* **AD** - *Андора*
			* **AE** - *Обединени арабски емирства*
			* **AF** - *Афганистан*
			* **AG** - *Антигуа и Барбуда*
			* **AI** - *Ангуила*
			* **AL** - *Албания*
			* **AM** - *Армения*
			* **AO** - *Ангола*
			* **AQ** - *Антарктика*
			* **AR** - *Аржентина*
			* **AS** - *Американски Самоа*
			* **AT** - *Австрия*
			* **AU** - *Австралия*
			* **AW** - *Аруба*
			* **AX** - *Аландски острови*
			* **AZ** - *Азербайджан*
			* **BA** - *Босна и Херцеговина*
			* **BB** - *Барбадос*
			* **BD** - *Бангладеш*
			* **BE** - *Белгия*
			* **BF** - *Буркина Фасо*
			* **BG** - *България*
			* **BH** - *Бахрейн*
			* **BI** - *Бурунди*
			* **BJ** - *Бенин*
			* **BL** - *Сен Бартелеми*
			* **BM** - *Бермуда*
			* **BN** - *Бруней Дарусалам*
			* **BO** - *Боливия*
			* **BQ** - *Бонер*
			* **BR** - *Бразилия*
			* **BS** - *Бахами*
			* **BT** - *Бутан*
			* **BV** - *Боувет Айленд*
			* **BW** - *Ботсвана*
			* **BY** - *Беларус*
			* **BZ** - *Бразилия*
			* **CA** - *Канада*
			* **CC** - *Кокосови острови*
			* **CD** - *Демократична Република Конго*
			* **CF** - *Централноафриканска република*
			* **CG** - *Конго (Бразавил)*
			* **CH** - *Швейцария*
			* **CI** - *Кот д'Ивоар*
			* **CK** - *Острови Кук*
			* **CL** - *Чили*
			* **CM** - *Камерун*
			* **CN** - *Китай*
			* **CO** - *Колумбия*
			* **CR** - *Каста Рика*
			* **CU** - *Куба*
			* **CV** - *Кабо Верде*
			* **CW** - *Кюрасао*
			* **CX** - *Остров Рождество*
			* **CY** - *Кипър*
			* **CZ** - *Чехия*
			* **DE** - *Германия*
			* **DJ** - *Джибути*
			* **DK** - *Дания*
			* **DM** - *Доминика*
			* **DO** - *Доминиканската република*
			* **DZ** - *Алжир*
			* **EC** - *Еквадор*
			* **EE** - *Естония*
			* **EG** - *Египет*
			* **EH** - *Западна Сахара*
			* **ER** - *Еритрея*
			* **ES** - *Испания*
			* **ET** - *Етиопия*
			* **FI** - *Финландия*
			* **FJ** - *Фиджи*
			* **FK** - *Фолкландските острови (Малвините)*
			* **FM** - *Микронезия (Федерални щати)*
			* **FO** - *Фарьорски острови*
			* **FR** - *Франция*
			* **GA** - *Габон*
			* **GB** - *Обединено кралство Великобритания и Северна Ирландия*
			* **GD** - *Гренада*
			* **GE** - *Грузия*
			* **GF** - *Френска Гвиана*
			* **GG** - *Гърнзи*
			* **GH** - *Гана*
			* **GI** - *Гибралтар*
			* **GL** - *Гренландия*
			* **GM** - *Гамбия*
			* **GN** - *Гвинея*
			* **GP** - *Гваделупа*
			* **GQ** - *Екваториална Гвинея*
			* **GR** - *Гърция*
			* **GS** - *Южна Джорджия и Южните Сандвич острови*
			* **GT** - *Гватемала*
			* **GU** - *Гуам*
			* **GW** - *Гвинея-Бисау*
			* **GY** - *Гаяна*
			* **HK** - *Хонг Конг*
			* **HM** - *Острови Хърд и Макдоналд*
			* **HN** - *Хондурас*
			* **HR** - *Хърватска*
			* **HT** - *Хаити*
			* **HU** - *Унгария*
			* **ID** - *Индонезия*
			* **IE** - *Ирландия*
			* **IL** - *Израел*
			* **IM** - *Остров Ман*
			* **IN** - *Индия*
			* **IO** - *Британска територия в Индийския океан*
			* **IQ** - *Ирак*
			* **IR** - *Иран*
			* **IS** - *Исландия*
			* **IT** - *Италия*
			* **JE** - *Джърси*
			* **JM** - *Ямайка*
			* **JO** - *Йордан*
			* **JP** - *Япония*
			* **KE** - *Кения*
			* **KG** - *Киргизстан*
			* **KH** - *Камбоджа*
			* **KI** - *Кирибати*
			* **KM** - *Коморски острови*
			* **KN** - *Сейнт Китс и Невис*
			* **KP** - *Северна корея*
			* **KR** - *Република Корея*
			* **KW** - *Кувейт*
			* **KY** - *Кайманови острови*
			* **KZ** - *Казахстан*
			* **LA** - *Лаос*
			* **LB** - *Ливан*
			* **LC** - *Света Лусия*
			* **LI** - *Лихтенщайн*
			* **LK** - *Шри Ланка*
			* **LR** - *Либерия*
			* **LS** - *Лесото*
			* **LT** - *Литва*
			* **LU** - *Люксембург*
			* **LV** - *Латвия*
			* **LY** - *Либия*
			* **MA** - *Мароко*
			* **MC** - *Монако*
			* **MD** - *Молдова*
			* **ME** - *Черна гора*
			* **MF** - *Сен Мартин (френска част)*
			* **MG** - *Мадагаскар*
			* **MH** - *Маршаловите острови*
			* **MK** - *Северна Македония*
			* **ML** - *Мали*
			* **MM** - *Мианмар*
			* **MN** - *Монголия*
			* **MO** - *Макао*
			* **MP** - *Северни Мариански острови*
			* **MQ** - *Мартиника*
			* **MR** - *Мавритания*
			* **MS** - *Монсерат*
			* **MT** - *Малта*
			* **MU** - *Мавриций*
			* **MV** - *Малдивите*
			* **MW** - *Малави*
			* **MX** - *Мексико*
			* **MY** - *Малайзия*
			* **MZ** - *Мозамбик*
			* **NA** - *Намибия*
			* **NC** - *Нова Каледония*
			* **NE** - *Нигер*
			* **NF** - *Остров Норфолк*
			* **NG** - *Нигерия*
			* **NI** - *Никарагуа*
			* **NL** - *Нидерландия*
			* **NO** - *Норвегия*
			* **NP** - *Непал*
			* **NR** - *Науру*
			* **NU** - *Ниуе*
			* **NZ** - *Нова Зеландия*
			* **OM** - *Оман*
			* **PA** - *Панама*
			* **PE** - *Перу*
			* **PF** - *Френска полинезия*
			* **PG** - *Папуа-Нова Гвинея*
			* **PH** - *Филипините*
			* **PK** - *Пакистан*
			* **PL** - *Полша*
			* **PM** - *Сен Пиер и Микелон*
			* **PN** - *Питкърн*
			* **PR** - *Пуерто Рико*
			* **PS** - *Палестина, Щат*
			* **PT** - *Португалия*
			* **PW** - *Палау*
			* **PY** - *Парагвай*
			* **QA** - *Катар*
			* **RE** - *Реюнион*
			* **RO** - *Румъния*
			* **RS** - *Сърбия*
			* **RU** - *Русия*
			* **RW** - *Руанда*
			* **SA** - *Саудитска Арабия*
			* **SB** - *Соломоновите острови*
			* **SC** - *Сейшели*
			* **SD** - *Судан*
			* **SE** - *Швеция*
			* **SG** - *Сингапур*
			* **SH** - *Света Елена*
			* **SI** - *Словения*
			* **SJ** - *Ян Майен*
			* **SK** - *Словакия*
			* **SL** - *Сиера Леоне*
			* **SM** - *Сан Марино*
			* **SN** - *Сенегал*
			* **SO** - *Сомалия*
			* **SR** - *Суринам*
			* **SS** - *Южен Судан*
			* **ST** - *Сао Томе и Принсипи*
			* **SV** - *Ел Салвадор*
			* **SX** - *Синт Мартен (холандска част)*
			* **SY** - *Сирийска Арабска Република*
			* **SZ** - *Есватини*
			* **TC** - *Острови Търкс и Кайкос*
			* **TD** - *Чад*
			* **TF** - *Френски южни и антарктически територии*
			* **TG** - *Того*
			* **TH** - *Тайланд*
			* **TJ** - *Таджикистан*
			* **TK** - *Токелау*
			* **TL** - *Тимор-Лешти*
			* **TM** - *Туркменистан*
			* **TN** - *Тунис*
			* **TO** - *Тонга*
			* **TR** - *Турция*
			* **TT** - *Тринидад и Тобаго*
			* **TV** - *Тувалу*
			* **TW** - *Тайван (провинция Китай)*
			* **TZ** - *Танзания*
			* **UA** - *Украйна*
			* **UG** - *Уганда*
			* **UM** - *Отдалечени острови на САЩ*
			* **US** - *Съединени американски щати*
			* **UY** - *Уругвай*
			* **UZ** - *Узбекистан*
			* **VA** - *Ватикана*
			* **VC** - *Сейнт Винсент и Гренадини*
			* **VE** - *Венецуела (Боливарианска република)*
			* **VG** - *Вирджински острови (Великобритания)*
			* **VI** - *Вирджински острови (САЩ)*
			* **VN** - *Виетнам*
			* **VU** - *Вануату*
			* **WF** - *Уолис и Футуна*
			* **WS** - *Самоа*
			* **XK** - *Косово*
			* **YE** - *Йемен*
			* **YT** - *Майот*
			* **ZA** - *Южна Африка*
			* **ZM** - *Замбия*
			* **ZW** - *Зимбабве*
   * - **$subscription_id**
     - *string*
     - *Обхваща абонаментен план* ( виж: :doc:`../subscriptions/getlist` )

-----

PricelistsIndexResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: PricelistsIndexResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$pricelist_id**
     - *int*
     - *ID*
   * - **$pricelist_name**
     - *string*
     - *Име*
   * - **$type_title**
     - *string*
     - *Тип на ценоразписа*
   * - **$group_name**
     - *string*
     - *Група ценоразписи*
   * - **$periods_date**
     - *string*
     - *Период на действие по дати*
   * - **$periods_time**
     - *string*
     - *Период на действие по часове*
   * - **$modificator_type**
     - *string*
     - Тип ценови `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$modificator_round_type**
     - *string*
     - *Закръгляне на изчислените цени*
   * - **$articles_cnt**
     - *int*
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$clients_cnt**
     - *int*
     - Брой `клиенти </barsy.help/210-dictionary/client.html>`__ в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$client_groups_cnt**
     - *int*
     - Брой клиентски групи в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$tax_regions_cnt**
     - *int*
     - Брой типове доставка в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$countries_cnt**
     - *int*
     - Брой държави в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$subscriptions_cnt**
     - *int*
     - Брой абонаментни планове в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$price_tax_mode**
     - *string*
     - *С включено ДДС или без ДДС*
   * - **$create_date**
     - *string*
     - Дата на създаване на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$last_update**
     - *string*
     - Дата на последна актуализация на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$price_tax_id**
     - *string*
     - *ДДС група за ценоразписа*
   * - **$weight**
     - *int*
     - *Тежест/приоритет при застъпване*
   * - **$current_status**
     - *string*
     - *Текущ статус (дали е активен в момента)*

-----

PricelistsIndexResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PricelistsIndexResultData

   * - Параметър
     - Тип
     - Описание
   * - **$page_num**
     - *int*
     - Номер на текуща страница
   * - **$total**
     - *int*
     - Общ брой страници
   * - **$records**
     - *int*
     - Общ брой записи
   * - **$rows**
     - PricelistsIndexResultRowData_ []
     - Полета на всеки ред от списъка
   * - **$totals**
     - 
     - 
   * - **$filters_resume**
     - *array*
     - 

-----

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/pricelists_index/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/pricelists_index/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/pricelists_index/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/pricelists_index/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/pricelists_index/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/pricelists_index/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Ценово правило </barsy.help/210-dictionary/pricelist.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

