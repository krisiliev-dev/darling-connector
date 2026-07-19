.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_sales_by_orders_details
===========================================================
Подробни продажби по поръчки

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/112_by_Sales/index </barsy.help/110-admin/170-reports/112_by_Sales/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Разширена версия на справката `Reports_sales_by_orders` — за всяка поръчка връща поредово раздропируване на всички продадени `артикули </barsy.help/210-dictionary/article.html>`__, единични цени, отстъпки, `модификатори </barsy.help/210-dictionary/modificator.html>`__. Резултатът е плосък списък с реални продажни редове, удобен за детайлен счетоводен анализ или връзка с фискални бележки.

Типични случаи: детайлен експорт за external BI, реконсилиейшън на фискални операции, разследване на оплаквания от `клиент </barsy.help/210-dictionary/client.html>`__ с пълни редове на `сметката </barsy.help/210-dictionary/account.html>`__, експорт за счетоводна оптимизация по `артикули </barsy.help/210-dictionary/article.html>`__.

**Име**: Reports_sales_by_orders_details
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
     - ReportsSalesByOrdersDetailsFilters_ 
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

			* **order_id** - *ID*
			* **date** - Дата поръчка (Дата на поръчване на конкретния `артикул </barsy.help/210-dictionary/article.html>`__)
			* **barsy** - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **pos_name** - `Каса </barsy.help/210-dictionary/pos.html>`__
			* **user_name** - `Потребител </barsy.help/210-dictionary/user.html>`__
			* **served_name** - *Обслужил*
			* **client_name** - `Клиент </barsy.help/210-dictionary/client.html>`__
			* **client_email** - *Имейл*
			* **client_group** - *Клиентска група*
			* **person_name** - `Представител </barsy.help/210-dictionary/person.html>`__
			* **article_name** - `Артикул </barsy.help/210-dictionary/article.html>`__
			* **process_time** - Зададено време (Зададеното време за обработка се взема от настройките на `артикула </barsy.help/210-dictionary/article.html>`__, а ако не е зададено там, от настройката на `потока </barsy.help/210-dictionary/flow.html>`__)
			* **full_duration** - *Обща продължителност (Показва времето от създаването на поръчката до нейното приключване)*
			* **sum_status_duration_time** - *Реална продължителност (Реалната продължителност се калкулира от времето, в което поръчката е била със статус маркиран като "Реално създаване в поръчка")*
			* **overdue** - Закъснение (Разликата от зададеното време за приготвяне на `артикула </barsy.help/210-dictionary/article.html>`__ и реалната продължителност на поръчката)
			* **lot_value** - *Партида*
			* **barcode** - Баркод (Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **amount_unit** - Единица `продажба </barsy.help/210-dictionary/sale.html>`__ (Количество, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при единична `продажба </barsy.help/210-dictionary/sale.html>`__)
			* **export_id** - *Експортен идентификатор (Идентификатор за експорт към външни системи)*
			* **ref_num** - Референтен номер (Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **cat_name** - `Категория </barsy.help/210-dictionary/category.html>`__
			* **cat_path** - `Категория </barsy.help/210-dictionary/category.html>`__ път
			* **cat_names** - `Категории </barsy.help/210-dictionary/category.html>`__
			* **cat_paths** - `Категория </barsy.help/210-dictionary/category.html>`__ път
			* **current_price** - *Ед. цена*
			* **current_price__sec_curr** - *Ед. цена (Български лев)*
			* **current_price_no_dds** - *Ед.цена без ДДС*
			* **current_price_no_dds__sec_curr** - *Ед.цена без ДДС (Български лев)*
			* **tax** - *ДДС*
			* **amount** - *Продадено количество*
			* **store_amount** - *Складови бройки*
			* **discounts** - *Отстъпки сума*
			* **discounts__sec_curr** - *Отстъпки сума (Български лев)*
			* **total** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума
			* **total__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
			* **total_no_dds** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС
			* **total_no_dds__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС (Български лев)
			* **dds_total** - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума
			* **dds_total__sec_curr** - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
			* **delivery_total** - *Сума себест (без ДДС)*
			* **delivery_total__sec_curr** - *Сума себест (без ДДС) (Български лев)*
			* **delivery_total_dds** - *Сума себест (+ДДС) (Себестойност с ДДС)*
			* **delivery_total_dds__sec_curr** - *Сума себест (+ДДС) (Български лев) (Себестойност с ДДС)*
			* **comision** - Комисионни сума 1 (Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ преди отстъпката)
			* **comision__sec_curr** - Комисионни сума 1 (Български лев) (Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ преди отстъпката)
			* **comision_with_discount** - Комисионни сума 2 (Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ след отстъпката)
			* **comision_with_discount__sec_curr** - Комисионни сума 2 (Български лев) (Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ след отстъпката)
			* **grand_total_dds_exc** - Печалба (Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС)
			* **grand_total_dds_exc__sec_curr** - Печалба (Български лев) (Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС)
			* **actual_price_base** - Базова цена (Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
			* **actual_price_base__sec_curr** - Базова цена (Български лев) (Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
			* **actual_price_base_total** - *Сума баз. цена (Сумата на количеството и базова цена без отстъпки)*
			* **actual_price_base_total__sec_curr** - *Сума баз. цена (Български лев) (Сумата на количеството и базова цена без отстъпки)*
			* **total_actual_price_base** - Сума баз. цена с активни отстъпки (Сума по базова цена с извадени отстъпки за `сметка </barsy.help/210-dictionary/account.html>`__ и `артикул </barsy.help/210-dictionary/article.html>`__, но без `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **total_actual_price_base__sec_curr** - Сума баз. цена с активни отстъпки (Български лев) (Сума по базова цена с извадени отстъпки за `сметка </barsy.help/210-dictionary/account.html>`__ и `артикул </barsy.help/210-dictionary/article.html>`__, но без `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **pricelist_name** - `Ценови правила </barsy.help/210-dictionary/pricelist.html>`__ (Списък от `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, въздействали на продажната цена)
			* **price_after_pricelist_diff** - Сума разлика след `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ (Сумарна разликата между базовата цена и цената след приложено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **price_after_pricelist_diff__sec_curr** - Сума разлика след `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ (Български лев) (Сумарна разликата между базовата цена и цената след приложено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__)
			* **base_discount** - *Базова отстъпка (Процентно отношение между базовата продажна цена и реалната такава)*
			* **total_discount** - *Пълна отстъпка/надценка*
			* **total_discount__sec_curr** - *Пълна отстъпка/надценка (Български лев)*
			* **paymethod_name** - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__
			* **account_id** - `Сметка </barsy.help/210-dictionary/account.html>`__ №
			* **ref_date** - Документ дата (Документална дата на `продажба </barsy.help/210-dictionary/sale.html>`__. Ако не е зададена нарочна се използва датата на закриване)
			* **account_create_date** - `Сметка </barsy.help/210-dictionary/account.html>`__ открита
			* **account_close_date** - `Сметка </barsy.help/210-dictionary/account.html>`__ закрита
			* **client_id**
			* **article_id**
			* **account_alias** - *Заглавие*
			* **card_num** - *Карта №* **По подразбиране:** ["order_id","date","barsy","article_name","current_price","amount","total"]
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
ReportsSalesByOrdersDetailsResultData_                                 Обект с данни за резултатите
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsSalesByOrdersDetailsFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByOrdersDetailsFilters

   * - Параметър
     - Тип
     - Описание
   * - **$ref_date**
     - *string*
     - *Филтриране на редовете за избран период* **По подразбиране:** ["2026-07-01"]
   * - **$barsys**
     - *string*
     - Филтриране по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
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
   * - **$pos_id**
     - *string*
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
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
   * - **$role_id**
     - *string*
     - Филтриране по `роля </barsy.help/210-dictionary/role.html>`__ ( виж: :doc:`../roles/getlist` )
   * - **$paymethod_id**
     - *string*
     - Филтриране по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

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
   * - **$status**
     - *string*
     - `Сметки </barsy.help/210-dictionary/account.html>`__

			* **0** - *Отворени*
			* **1** - *Затворени* **По подразбиране:** 1
   * - **$cprice_less_cprice**
     - *string*
     - *Продажна цена < от себестойност (+ДДС)*
   * - **$card_num**
     - *string*
     - *Карта №*
   * - **$details**
     - *string*
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articledetails/gettree` )
   * - **$order_parent_id**
     - *string*
     - *Комбо Меню*

			* **1** - *участва в комбо меню*
			* **2** - *е комбо меню*
			* **3** - *не участва в комбо меню*
   * - **$overdue**
     - *string*
     - *Само просрочени поръчки*
   * - **$fx**
     - *string*
     - Вид `плащане </barsy.help/210-dictionary/payment.html>`__

			* **0** - *Нефискални*
			* **1** - *Фискални*
   * - **$account_alias**
     - *string*
     - Търсене по заглавие на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$served_by**
     - *string*
     - *Филтриране по обслужил* ( виж: :doc:`../users/getlist` )
   * - **$current_pricelist_id**
     - *string*
     - `Ценови правила </barsy.help/210-dictionary/pricelist.html>`__

			* **1** - *Test*
			* **2** - *тест*
			* **3** - *Тест*
			* **4** - Стоп `продажба </barsy.help/210-dictionary/sale.html>`__
			* **5** - *цени*
			* **6** - *Данъчна ставка за зареждания*
			* **7** - *Данъчна ставка за доставка*
			* **8** - *Данъчна ставка за зареждания*
			* **9** - *Данъчна ставка за доставка*
			* **10** - *Данъчна ставка за доставка*
			* **11** - *Данъчна ставка за доставка*
			* **12** - *Данъчна ставка за зареждания*
			* **13** - *Данъчна ставка за зареждания*
   * - **$article_type**
     - *string*
     - Филтриране по вид `артикул </barsy.help/210-dictionary/article.html>`__

			* **1** - `Продажба </barsy.help/210-dictionary/sale.html>`__ на `артикул </barsy.help/210-dictionary/article.html>`__
			* **2** - `Продажба </barsy.help/210-dictionary/sale.html>`__ на пакетна карта
			* **3** - Авансово `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-1** - *Ползване на пакетна карта*
			* **5** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__ на кл.портфейл
			* **6** - *Бакшиш*

-----

ReportsSalesByOrdersDetailsResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByOrdersDetailsResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$order_id**
     - *int*
     - *ID*
   * - **$date**
     - *string*
     - Дата на поръчване на конкретния `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$barsy**
     - *string*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$pos_name**
     - *string*
     - `Каса </barsy.help/210-dictionary/pos.html>`__
   * - **$user_name**
     - *string*
     - `Потребител </barsy.help/210-dictionary/user.html>`__
   * - **$served_name**
     - *string*
     - *Обслужил*
   * - **$client_name**
     - *string*
     - `Клиент </barsy.help/210-dictionary/client.html>`__
   * - **$client_email**
     - *string*
     - *Имейл*
   * - **$client_group**
     - *string*
     - *Клиентска група*
   * - **$person_name**
     - *string*
     - `Представител </barsy.help/210-dictionary/person.html>`__
   * - **$article_name**
     - *string*
     - `Артикул </barsy.help/210-dictionary/article.html>`__
   * - **$process_time**
     - *string*
     - Зададеното време за обработка се взема от настройките на `артикула </barsy.help/210-dictionary/article.html>`__, а ако не е зададено там, от настройката на `потока </barsy.help/210-dictionary/flow.html>`__
   * - **$full_duration**
     - *string*
     - *Показва времето от създаването на поръчката до нейното приключване*
   * - **$sum_status_duration_time**
     - *string*
     - *Реалната продължителност се калкулира от времето, в което поръчката е била със статус маркиран като "Реално създаване в поръчка"*
   * - **$overdue**
     - *string*
     - Разликата от зададеното време за приготвяне на `артикула </barsy.help/210-dictionary/article.html>`__ и реалната продължителност на поръчката
   * - **$lot_value**
     - *string*
     - *Партида*
   * - **$barcode**
     - *string*
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
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
   * - **$export_id**
     - *string*
     - *Идентификатор за експорт към външни системи*
   * - **$ref_num**
     - *string*
     - Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$cat_name**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_path**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__ път
   * - **$cat_names**
     - *string*
     - `Категории </barsy.help/210-dictionary/category.html>`__
   * - **$cat_paths**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__ път
   * - **$current_price**
     - *string*
     - *Ед. цена*
   * - **$current_price__sec_curr**
     - *string*
     - *Ед. цена (Български лев)*
   * - **$current_price_no_dds**
     - *string*
     - *Ед.цена без ДДС*
   * - **$current_price_no_dds__sec_curr**
     - *string*
     - *Ед.цена без ДДС (Български лев)*
   * - **$tax**
     - *string*
     - *ДДС*
   * - **$amount**
     - *string*
     - *Продадено количество*
   * - **$store_amount**
     - *string*
     - *Складови бройки*
   * - **$discounts**
     - *string*
     - *Отстъпки сума*
   * - **$discounts__sec_curr**
     - *string*
     - *Отстъпки сума (Български лев)*
   * - **$total**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума
   * - **$total__sec_curr**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
   * - **$total_no_dds**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС
   * - **$total_no_dds__sec_curr**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС (Български лев)
   * - **$dds_total**
     - *string*
     - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума
   * - **$dds_total__sec_curr**
     - *string*
     - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
   * - **$delivery_total**
     - *string*
     - *Сума себест (без ДДС)*
   * - **$delivery_total__sec_curr**
     - *string*
     - *Сума себест (без ДДС) (Български лев)*
   * - **$delivery_total_dds**
     - *string*
     - *Себестойност с ДДС*
   * - **$delivery_total_dds__sec_curr**
     - *string*
     - *Себестойност с ДДС*
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
   * - **$grand_total_dds_exc**
     - *string*
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$grand_total_dds_exc__sec_curr**
     - *string*
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$actual_price_base**
     - *string*
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$actual_price_base__sec_curr**
     - *string*
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$actual_price_base_total**
     - *string*
     - *Сумата на количеството и базова цена без отстъпки*
   * - **$actual_price_base_total__sec_curr**
     - *string*
     - *Сумата на количеството и базова цена без отстъпки*
   * - **$total_actual_price_base**
     - *string*
     - Сума по базова цена с извадени отстъпки за `сметка </barsy.help/210-dictionary/account.html>`__ и `артикул </barsy.help/210-dictionary/article.html>`__, но без `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$total_actual_price_base__sec_curr**
     - *string*
     - Сума по базова цена с извадени отстъпки за `сметка </barsy.help/210-dictionary/account.html>`__ и `артикул </barsy.help/210-dictionary/article.html>`__, но без `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$pricelist_name**
     - *string*
     - Списък от `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, въздействали на продажната цена
   * - **$price_after_pricelist_diff**
     - *string*
     - Сумарна разликата между базовата цена и цената след приложено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$price_after_pricelist_diff__sec_curr**
     - *string*
     - Сумарна разликата между базовата цена и цената след приложено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$base_discount**
     - *int*
     - *Процентно отношение между базовата продажна цена и реалната такава*
   * - **$total_discount**
     - *string*
     - *Пълна отстъпка/надценка*
   * - **$total_discount__sec_curr**
     - *string*
     - *Пълна отстъпка/надценка (Български лев)*
   * - **$paymethod_name**
     - *string*
     - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$account_id**
     - *int*
     - `Сметка </barsy.help/210-dictionary/account.html>`__ №
   * - **$ref_date**
     - *string*
     - Документална дата на `продажба </barsy.help/210-dictionary/sale.html>`__. Ако не е зададена нарочна се използва датата на закриване
   * - **$account_create_date**
     - *string*
     - `Сметка </barsy.help/210-dictionary/account.html>`__ открита
   * - **$account_close_date**
     - *string*
     - `Сметка </barsy.help/210-dictionary/account.html>`__ закрита
   * - **$client_id**
     - *string*
     - 
   * - **$article_id**
     - *string*
     - 
   * - **$account_alias**
     - *string*
     - *Заглавие*
   * - **$card_num**
     - *string*
     - *Карта №*

-----

ReportsSalesByOrdersDetailsResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByOrdersDetailsResultData

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
     - ReportsSalesByOrdersDetailsResultRowData_ []
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

     .. literalinclude:: ../../sources/reports_sales_by_orders_details/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_sales_by_orders_details/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_sales_by_orders_details/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_sales_by_orders_details/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_sales_by_orders_details/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_sales_by_orders_details/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Продажба </barsy.help/210-dictionary/sale.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

