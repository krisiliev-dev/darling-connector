.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_sales_by_articles
===========================================================
Продажби по артикули

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/112_by_Sales/index </barsy.help/110-admin/170-reports/112_by_Sales/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Агрегирана справка за реализирани `продажби </barsy.help/210-dictionary/sale.html>`__, групирана по `артикул </barsy.help/210-dictionary/article.html>`__ за избран период. За всеки `артикул </barsy.help/210-dictionary/article.html>`__ връща продадени количества, оборот, отстъпки, крайна сума с и без ДДС, себестойност, печалба, надценка и марж — в зависимост от правата на `потребителя </barsy.help/210-dictionary/user.html>`__. Поддържа разнообразни филтри: период и часови интервал, `склад </barsy.help/210-dictionary/store.html>`__/`каса </barsy.help/210-dictionary/pos.html>`__/`потребител </barsy.help/210-dictionary/user.html>`__/`роля </barsy.help/210-dictionary/role.html>`__, `клиент </barsy.help/210-dictionary/client.html>`__ и клиентска група, `поток </barsy.help/210-dictionary/flow.html>`__, ДДС група и регион, `доставчик </barsy.help/210-dictionary/supplier.html>`__, `категории </barsy.help/210-dictionary/category.html>`__, детайли на `артикул </barsy.help/210-dictionary/article.html>`__, метод на `плащане </barsy.help/210-dictionary/payment.html>`__, фактурирани `сметки </barsy.help/210-dictionary/account.html>`__, дни от седмицата.

Типични случаи: дневен/месечен отчет на най-продавани `артикули </barsy.help/210-dictionary/article.html>`__, анализ на маржа по `категории </barsy.help/210-dictionary/category.html>`__ за бизнес ревю, експорт към счетоводна система, проверка на ефект от ценова промоция. Резултатът може да бъде допълнително групиран по `категория </barsy.help/210-dictionary/category.html>`__, `поток </barsy.help/210-dictionary/flow.html>`__ или детайл на `артикул </barsy.help/210-dictionary/article.html>`__ и сортиран по произволна колона.

**Име**: Reports_sales_by_articles
**Категория**: Reports


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
     - ReportsSalesByArticlesFilters_ 
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

			* **article_id** - `Артикул </barsy.help/210-dictionary/article.html>`__ ID (Номер на `артикул </barsy.help/210-dictionary/article.html>`__)
			* **picture** - Снимка (Снимка на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **article_name** - Име на `артикул </barsy.help/210-dictionary/article.html>`__
			* **cat_name** - `Категория </barsy.help/210-dictionary/category.html>`__ (главна)
			* **cat_path** - `Категория </barsy.help/210-dictionary/category.html>`__ път(главна)
			* **cat_names** - `Категории </barsy.help/210-dictionary/category.html>`__ (Имена на `категории </barsy.help/210-dictionary/category.html>`__)
			* **cat_paths** - `Категории </barsy.help/210-dictionary/category.html>`__ пътища (Пътища на `категории </barsy.help/210-dictionary/category.html>`__)
			* **amount_unit** - Единица `продажба </barsy.help/210-dictionary/sale.html>`__ (Количество, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при единична `продажба </barsy.help/210-dictionary/sale.html>`__)
			* **barcode** - Баркод (Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **code** - *Код (Код за бързо избиране от клавиатура)*
			* **ref_num** - Референтен номер (Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **stream_name** - `Поток </barsy.help/210-dictionary/flow.html>`__ (`Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **current_stream** - Текущ `поток </barsy.help/210-dictionary/flow.html>`__
			* **current_price** - Ед. цена (Средна продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период)
			* **current_price__sec_curr** - Ед. цена (Български лев) (Средна продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период)
			* **current_price_no_dds** - Ед.цена без ДДС (Средна продажна цена без ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период)
			* **current_price_no_dds__sec_curr** - Ед.цена без ДДС (Български лев) (Средна продажна цена без ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период)
			* **dds** - ДДС ед.цена (Средна ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период)
			* **dds__sec_curr** - ДДС ед.цена (Български лев) (Средна ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период)
			* **cnt** - *Продадени бройки (Сума на продадените единици (1 единица = 1 поръчка))*
			* **store_amount** - Складови бройки (Сума на продадените складови количества (продадени единици * единица `продажба </barsy.help/210-dictionary/sale.html>`__))
			* **oborot** - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот (Сума на реализиран оборот по продажни цени преди отстъпките на `артикул </barsy.help/210-dictionary/article.html>`__ и `сметка </barsy.help/210-dictionary/account.html>`__)
			* **oborot__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот (Български лев) (Сума на реализиран оборот по продажни цени преди отстъпките на `артикул </barsy.help/210-dictionary/article.html>`__ и `сметка </barsy.help/210-dictionary/account.html>`__)
			* **discounts** - Отстъпки сума (Сума на направени отстъпки за този `артикул </barsy.help/210-dictionary/article.html>`__, акумулирани от отстъпка на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **discounts__sec_curr** - Отстъпки сума (Български лев) (Сума на направени отстъпки за този `артикул </barsy.help/210-dictionary/article.html>`__, акумулирани от отстъпка на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **total** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума (Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **total__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев) (Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **total_no_dds** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС (Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **total_no_dds__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС (Български лев) (Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **total_no_dds_no_dis** - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот без ДДС без отстъпка (Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС преди направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **total_no_dds_no_dis__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот без ДДС без отстъпка (Български лев) (Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС преди направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **dds_total** - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума (Крайна сума на ДДС от `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **dds_total__sec_curr** - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев) (Крайна сума на ДДС от `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
			* **tax_id** - *ДДС група*
			* **delivery_total** - *Сума себест (без ДДС)*
			* **delivery_total__sec_curr** - *Сума себест (без ДДС) (Български лев)*
			* **avg_delivery_price** - *Средна себестойност за единица*
			* **avg_delivery_price__sec_curr** - *Средна себестойност за единица (Български лев)*
			* **delivery_price** - Последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС)
			* **delivery_price__sec_curr** - Последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС) (Български лев)
			* **delivery_price_x_cnt** - Сумарно по последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС)
			* **delivery_price_x_cnt__sec_curr** - Сумарно по последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС) (Български лев)
			* **comision** - Комисионни 1 (Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ преди отстъпката)
			* **comision__sec_curr** - Комисионни 1 (Български лев) (Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ преди отстъпката)
			* **comision_with_discount** - Комисионни 2 (Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ след отстъпката)
			* **comision_with_discount__sec_curr** - Комисионни 2 (Български лев) (Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ след отстъпката)
			* **profit** - Печалба (Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ и себестойност)
			* **profit__sec_curr** - Печалба (Български лев) (Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ и себестойност)
			* **markup** - Надценка (Процент надценка между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност)
			* **margin** - *Марж*
			* **cost_to_oborot** - Себест/Оборот без ДДС (Средна себестойност без ДДС / `продажби </barsy.help/210-dictionary/sale.html>`__ оборот без ДДС умножено по 100)
			* **min_profit_percent** - Минимална надбавка (Продажната цена на `артикул </barsy.help/210-dictionary/article.html>`__ в `сметка </barsy.help/210-dictionary/account.html>`__ + всички отстъпки, да не пада под себестойността с ДДС на `артикул </barsy.help/210-dictionary/article.html>`__ + този %.)
			* **below_min_profit** - Под минимална надбавка (Светва, когато надценката е по-малка от зададената минимална надбавка на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **actual_price_base** - Базова цена (Базова `продажба </barsy.help/210-dictionary/sale.html>`__ цена на `артикул </barsy.help/210-dictionary/article.html>`__ преди налагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
			* **actual_price_base__sec_curr** - Базова цена (Български лев) (Базова `продажба </barsy.help/210-dictionary/sale.html>`__ цена на `артикул </barsy.help/210-dictionary/article.html>`__ преди налагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
			* **total_actual_price_base** - *Сума баз. цена (Сума по базова цена с извадени отстъпки)*
			* **total_actual_price_base__sec_curr** - *Сума баз. цена (Български лев) (Сума по базова цена с извадени отстъпки)*
			* **base_discount** - *Базова отстъпка (Процентно отношение между базовата продажна цена и реалната такава)*
			* **actual_base_total_diff** - *Разлика € (Разлика в € между реалната продажна цена и базовата такава умножени по количеството)*
			* **actual_base_total_diff__sec_curr** - *Разлика € (Български лев) (Разлика в € между реалната продажна цена и базовата такава умножени по количеството)*
			* **export_id** - *Експортен идентификатор (Идентификатор за експорт към външни системи)* **По подразбиране:** ["article_id","article_name","amount_unit","stream_name","current_price","cnt","oborot","discounts","total","total_no_dds","delivery_total"]
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
ReportsSalesByArticlesResultData_                                      Обект с данни за резултатите
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsSalesByArticlesFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByArticlesFilters

   * - Параметър
     - Тип
     - Описание
   * - **$ref_date**
     - *string*
     - *Филтриране на редовете за избран период* **По подразбиране:** ["2026-07-01"]
   * - **$time_interval**
     - *string*
     - Часови интервал на `продажбите </barsy.help/210-dictionary/sale.html>`__
   * - **$barsys_depots**
     - *string*
     - `Търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове
   * - **$article_name**
     - *string*
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../articles/search` )
   * - **$cat_id**
     - *string*
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../categories/gettree` )
   * - **$stream_id**
     - *string*
     - Филтриране по `поток </barsy.help/210-dictionary/flow.html>`__

			* **4** - *Remote*
			* **2** - Втори `поток </barsy.help/210-dictionary/flow.html>`__
			* **1** - *Основен*
			* **3** - трети `поток </barsy.help/210-dictionary/flow.html>`__
   * - **$order_pos_id**
     - *string*
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$create_pos_id**
     - *string*
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$close_pos_id**
     - *string*
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$role_id**
     - *string*
     - Филтриране по `роля </barsy.help/210-dictionary/role.html>`__ ( виж: :doc:`../roles/getlist` )
   * - **$client**
     - *string*
     - Търсене по `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getlistsmart` )
   * - **$person**
     - *string*
     - Филтриране по `представител </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../persons/getlist` )
   * - **$client_group_id**
     - *string*
     - *Филтриране по клиентска група* ( виж: :doc:`../clients/getgroups` )
   * - **$user_id**
     - *string*
     - Филтриране по `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$paymethod_id**
     - *string*
     - Филтриране по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **0** - Без `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-5** - *Смесено*
			* **1** - *В брой*
			* **2** - *Карта*
   * - **$tax_id**
     - *string*
     - *Филтриране по ДДС група*

			* **2** - *20% (Б)*
			* **1** - *0% (А)*
			* **3** - *20% (В)*
			* **4** - *9% (Г)*
			* **12** - *7%*
			* **100** - *0% (Без ДДС)*
   * - **$tax_region_id**
     - *string*
     - *Тип доставка / данъчен регион*

			* **1** - *Употреба на място*
			* **2** - *Доставка до адрес*
			* **3** - *Взимане на място*
			* **4** - *Получаване от офис на куриер*
			* **5** - *За вкъщи*
   * - **$article_type**
     - *string*
     - Филтриране по вид `артикул </barsy.help/210-dictionary/article.html>`__

			* **1** - `Продажба </barsy.help/210-dictionary/sale.html>`__ на `артикул </barsy.help/210-dictionary/article.html>`__
			* **2** - `Продажба </barsy.help/210-dictionary/sale.html>`__ на пакетна карта
			* **3** - Авансово `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-1** - *Ползване на пакетна карта*
			* **5** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__ на кл.портфейл
			* **6** - *Бакшиш* **По подразбиране:** [-1,1,2,5,6]
   * - **$supplier_id**
     - *string*
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../suppliers/getlist` )
   * - **$details**
     - *string*
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articledetails/gettree` )
   * - **$account_alias**
     - *string*
     - Търсене по заглавие на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$invoices**
     - *string*
     - Само `сметки </barsy.help/210-dictionary/account.html>`__ без `фактура </barsy.help/210-dictionary/invoice.html>`__
   * - **$periods_weekdays**
     - *string*
     - *По ден от седмицата*

			* **2** - *Понеделник*
			* **3** - *Вторник*
			* **4** - *Сряда*
			* **5** - *Четвъртък*
			* **6** - *Петък*
			* **7** - *Събота*
			* **1** - *Неделя*
   * - **$invoiced_accs**
     - *string*
     - Филтърът прави връзка със `сметки </barsy.help/210-dictionary/account.html>`__ и `фактури </barsy.help/210-dictionary/invoice.html>`__, като взима предвид всички видове `фактури </barsy.help/210-dictionary/invoice.html>`__ без проформите

			* **only_invoiced** - *Само фактурираните*
			* **exclude_invoiced** - *Изключи фактурираните*
   * - **$order_parent_id**
     - *string*
     - *Комбо Меню*

			* **1** - *участва в комбо меню*
			* **2** - *е комбо меню*
			* **3** - *не участва в комбо меню*
   * - **$delivery_address_country**
     - *string*
     - *Държава за доставка*
   * - **$place_id**
     - *string*
     - *Място*
   * - **$parents**
     - *string*
     - Филтриране по групови `артикули </barsy.help/210-dictionary/article.html>`__

			* **P** - *+ Родители*
			* **C** - *+ Деца*
			* **PC** - *+ Родители + Деца*
			* **N** - Без групови `артикули </barsy.help/210-dictionary/article.html>`__
			* **OP** - *Само Родители*
			* **OPC** - *Само Родители и деца*
   * - **$composite**
     - *string*
     - *Рецепта*

			* **0** - *Няма*
			* **1** - Има (при `продажба </barsy.help/210-dictionary/sale.html>`__)
			* **-1** - Има (при `производство </barsy.help/210-dictionary/storeproduction.html>`__)

-----

ReportsSalesByArticlesResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByArticlesResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - Номер на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$picture**
     - *string*
     - Снимка на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$cat_name**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__ (главна)
   * - **$cat_path**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__ път(главна)
   * - **$cat_names**
     - *string*
     - Имена на `категории </barsy.help/210-dictionary/category.html>`__
   * - **$cat_paths**
     - *string*
     - Пътища на `категории </barsy.help/210-dictionary/category.html>`__
   * - **$detail_0**
     - *string*
     - *Алергени234*
   * - **$detail_1**
     - *string*
     - *Главен*
   * - **$detail_2**
     - *string*
     - *Друго*
   * - **$detail_3**
     - *string*
     - *Друго2*
   * - **$detail_4**
     - *string*
     - *Размер*
   * - **$amount_unit**
     - *string*
     - Количество, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при единична `продажба </barsy.help/210-dictionary/sale.html>`__ **По подразбиране:** 1.000000000
   * - **$barcode**
     - *string*
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$code**
     - *string*
     - *Код за бързо избиране от клавиатура*
   * - **$ref_num**
     - *string*
     - Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$stream_name**
     - *string*
     - `Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_stream**
     - *string*
     - Текущ `поток </barsy.help/210-dictionary/flow.html>`__
   * - **$current_price**
     - *string*
     - Средна продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$current_price__sec_curr**
     - *string*
     - Средна продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$current_price_no_dds**
     - *string*
     - Средна продажна цена без ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$current_price_no_dds__sec_curr**
     - *string*
     - Средна продажна цена без ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$dds**
     - *string*
     - Средна ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$dds__sec_curr**
     - *string*
     - Средна ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$cnt**
     - *string*
     - *Сума на продадените единици (1 единица = 1 поръчка)*
   * - **$store_amount**
     - *string*
     - Сума на продадените складови количества (продадени единици * единица `продажба </barsy.help/210-dictionary/sale.html>`__)
   * - **$oborot**
     - *string*
     - Сума на реализиран оборот по продажни цени преди отстъпките на `артикул </barsy.help/210-dictionary/article.html>`__ и `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$oborot__sec_curr**
     - *string*
     - Сума на реализиран оборот по продажни цени преди отстъпките на `артикул </barsy.help/210-dictionary/article.html>`__ и `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$discounts**
     - *string*
     - Сума на направени отстъпки за този `артикул </barsy.help/210-dictionary/article.html>`__, акумулирани от отстъпка на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$discounts__sec_curr**
     - *string*
     - Сума на направени отстъпки за този `артикул </barsy.help/210-dictionary/article.html>`__, акумулирани от отстъпка на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total**
     - *string*
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total__sec_curr**
     - *string*
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total_no_dds**
     - *string*
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total_no_dds__sec_curr**
     - *string*
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total_no_dds_no_dis**
     - *string*
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС преди направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total_no_dds_no_dis__sec_curr**
     - *string*
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС преди направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$dds_total**
     - *string*
     - Крайна сума на ДДС от `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$dds_total__sec_curr**
     - *string*
     - Крайна сума на ДДС от `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$tax_id**
     - *string*
     - *ДДС група*
   * - **$delivery_total**
     - *string*
     - *Сума себест (без ДДС)*
   * - **$delivery_total__sec_curr**
     - *string*
     - *Сума себест (без ДДС) (Български лев)*
   * - **$avg_delivery_price**
     - *string*
     - *Средна себестойност за единица*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - *Средна себестойност за единица (Български лев)*
   * - **$delivery_price**
     - *string*
     - Последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС)
   * - **$delivery_price__sec_curr**
     - *string*
     - Последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС) (Български лев)
   * - **$delivery_price_x_cnt**
     - *string*
     - Сумарно по последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС)
   * - **$delivery_price_x_cnt__sec_curr**
     - *string*
     - Сумарно по последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС) (Български лев)
   * - **$comision**
     - *string*
     - Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ преди отстъпката
   * - **$comision__sec_curr**
     - *string*
     - Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ преди отстъпката
   * - **$comision_with_discount**
     - *string*
     - Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ след отстъпката
   * - **$comision_with_discount__sec_curr**
     - *string*
     - Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ след отстъпката
   * - **$profit**
     - *string*
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ и себестойност
   * - **$profit__sec_curr**
     - *string*
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ и себестойност
   * - **$markup**
     - *string*
     - Процент надценка между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност
   * - **$margin**
     - *string*
     - *Марж*
   * - **$cost_to_oborot**
     - *string*
     - Средна себестойност без ДДС / `продажби </barsy.help/210-dictionary/sale.html>`__ оборот без ДДС умножено по 100
   * - **$min_profit_percent**
     - *string*
     - Продажната цена на `артикул </barsy.help/210-dictionary/article.html>`__ в `сметка </barsy.help/210-dictionary/account.html>`__ + всички отстъпки, да не пада под себестойността с ДДС на `артикул </barsy.help/210-dictionary/article.html>`__ + този %.
   * - **$below_min_profit**
     - *string*
     - Светва, когато надценката е по-малка от зададената минимална надбавка на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$actual_price_base**
     - *string*
     - Базова `продажба </barsy.help/210-dictionary/sale.html>`__ цена на `артикул </barsy.help/210-dictionary/article.html>`__ преди налагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$actual_price_base__sec_curr**
     - *string*
     - Базова `продажба </barsy.help/210-dictionary/sale.html>`__ цена на `артикул </barsy.help/210-dictionary/article.html>`__ преди налагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$total_actual_price_base**
     - *string*
     - *Сума по базова цена с извадени отстъпки*
   * - **$total_actual_price_base__sec_curr**
     - *string*
     - *Сума по базова цена с извадени отстъпки*
   * - **$base_discount**
     - *int*
     - *Процентно отношение между базовата продажна цена и реалната такава*
   * - **$actual_base_total_diff**
     - *string*
     - *Разлика в € между реалната продажна цена и базовата такава умножени по количеството*
   * - **$actual_base_total_diff__sec_curr**
     - *string*
     - *Разлика в € между реалната продажна цена и базовата такава умножени по количеството*
   * - **$export_id**
     - *string*
     - *Идентификатор за експорт към външни системи*

-----

ReportsSalesByArticlesResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByArticlesResultData

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
     - ReportsSalesByArticlesResultRowData_ []
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

     .. literalinclude:: ../../sources/reports_sales_by_articles/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_sales_by_articles/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_sales_by_articles/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_sales_by_articles/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_sales_by_articles/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_sales_by_articles/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__
 * `Продажба </barsy.help/210-dictionary/sale.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

