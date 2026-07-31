.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsSalesByArticlesResultRowData
======================================================================================
Данни за резултата

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reports\\Data\\ReportsSalesByArticlesResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$article_id**
     - *int*
     - 
     - Номер на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$picture**
     - *string*
     - 
     - Снимка на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_name**
     - *string*
     - 
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$cat_name**
     - *string*
     - 
     - `Категория </barsy.help/210-dictionary/category.html>`__ (главна)
   * - **$cat_path**
     - *string*
     - 
     - `Категория </barsy.help/210-dictionary/category.html>`__ път(главна)
   * - **$cat_names**
     - *string*
     - 
     - Имена на `категории </barsy.help/210-dictionary/category.html>`__
   * - **$cat_paths**
     - *string*
     - 
     - Пътища на `категории </barsy.help/210-dictionary/category.html>`__
   * - **$detail_0**
     - *string*
     - 
     - *Алергени234*
   * - **$detail_1**
     - *string*
     - 
     - *Главен*
   * - **$detail_2**
     - *string*
     - 
     - *Друго*
   * - **$detail_3**
     - *string*
     - 
     - *Друго2*
   * - **$detail_4**
     - *string*
     - 
     - *Размер*
   * - **$amount_unit**
     - *string*
     - 1.000000000
     - Количество, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при единична `продажба </barsy.help/210-dictionary/sale.html>`__
   * - **$barcode**
     - *string*
     - 
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$code**
     - *string*
     - 
     - *Код за бързо избиране от клавиатура*
   * - **$ref_num**
     - *string*
     - 
     - Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$stream_name**
     - *string*
     - 
     - `Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_stream**
     - *string*
     - 
     - Текущ `поток </barsy.help/210-dictionary/flow.html>`__
   * - **$current_price**
     - *string*
     - 
     - Средна продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$current_price__sec_curr**
     - *string*
     - 
     - Средна продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$current_price_no_dds**
     - *string*
     - 
     - Средна продажна цена без ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$current_price_no_dds__sec_curr**
     - *string*
     - 
     - Средна продажна цена без ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$dds**
     - *string*
     - 
     - Средна ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$dds__sec_curr**
     - *string*
     - 
     - Средна ДДС на `артикула </barsy.help/210-dictionary/article.html>`__ за избрания период
   * - **$cnt**
     - *string*
     - 
     - *Сума на продадените единици (1 единица = 1 поръчка)*
   * - **$store_amount**
     - *string*
     - 
     - Сума на продадените складови количества (продадени единици * единица `продажба </barsy.help/210-dictionary/sale.html>`__)
   * - **$oborot**
     - *string*
     - 
     - Сума на реализиран оборот по продажни цени преди отстъпките на `артикул </barsy.help/210-dictionary/article.html>`__ и `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$oborot__sec_curr**
     - *string*
     - 
     - Сума на реализиран оборот по продажни цени преди отстъпките на `артикул </barsy.help/210-dictionary/article.html>`__ и `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$discounts**
     - *string*
     - 
     - Сума на направени отстъпки за този `артикул </barsy.help/210-dictionary/article.html>`__, акумулирани от отстъпка на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$discounts__sec_curr**
     - *string*
     - 
     - Сума на направени отстъпки за този `артикул </barsy.help/210-dictionary/article.html>`__, акумулирани от отстъпка на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total**
     - *string*
     - 
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total__sec_curr**
     - *string*
     - 
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total_no_dds**
     - *string*
     - 
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total_no_dds__sec_curr**
     - *string*
     - 
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total_no_dds_no_dis**
     - *string*
     - 
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС преди направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$total_no_dds_no_dis__sec_curr**
     - *string*
     - 
     - Крайна сума на `продажбите </barsy.help/210-dictionary/sale.html>`__ без ДДС преди направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$dds_total**
     - *string*
     - 
     - Крайна сума на ДДС от `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$dds_total__sec_curr**
     - *string*
     - 
     - Крайна сума на ДДС от `продажбите </barsy.help/210-dictionary/sale.html>`__ след направени отстъпки на `артикул </barsy.help/210-dictionary/article.html>`__ и на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$tax_id**
     - *string*
     - 
     - *ДДС група*

			 пример: "2"
   * - **$delivery_total**
     - *string*
     - 
     - *Сума себест (без ДДС)*
   * - **$delivery_total__sec_curr**
     - *string*
     - 
     - *Сума себест (без ДДС) (Български лев)*
   * - **$avg_delivery_price**
     - *string*
     - 
     - *Средна себестойност за единица*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - 
     - *Средна себестойност за единица (Български лев)*
   * - **$delivery_price**
     - *string*
     - 
     - Последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС)
   * - **$delivery_price__sec_curr**
     - *string*
     - 
     - Последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС) (Български лев)
   * - **$delivery_price_x_cnt**
     - *string*
     - 
     - Сумарно по последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС)
   * - **$delivery_price_x_cnt__sec_curr**
     - *string*
     - 
     - Сумарно по последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ (без ДДС) (Български лев)
   * - **$comision**
     - *string*
     - 
     - Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ преди отстъпката
   * - **$comision__sec_curr**
     - *string*
     - 
     - Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ преди отстъпката
   * - **$comision_with_discount**
     - *string*
     - 
     - Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ след отстъпката
   * - **$comision_with_discount__sec_curr**
     - *string*
     - 
     - Изчисляване върху сумата на `сметката </barsy.help/210-dictionary/account.html>`__ след отстъпката
   * - **$profit**
     - *string*
     - 
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ и себестойност
   * - **$profit__sec_curr**
     - *string*
     - 
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ и себестойност
   * - **$markup**
     - *string*
     - 
     - Процент надценка между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност
   * - **$margin**
     - *string*
     - 
     - *Марж*
   * - **$cost_to_oborot**
     - *string*
     - 
     - Средна себестойност без ДДС / `продажби </barsy.help/210-dictionary/sale.html>`__ оборот без ДДС умножено по 100
   * - **$min_profit_percent**
     - *string*
     - 
     - Продажната цена на `артикул </barsy.help/210-dictionary/article.html>`__ в `сметка </barsy.help/210-dictionary/account.html>`__ + всички отстъпки, да не пада под себестойността с ДДС на `артикул </barsy.help/210-dictionary/article.html>`__ + този %.
   * - **$below_min_profit**
     - *string*
     - 
     - Светва, когато надценката е по-малка от зададената минимална надбавка на `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "0"
   * - **$actual_price_base**
     - *string*
     - 
     - Базова `продажба </barsy.help/210-dictionary/sale.html>`__ цена на `артикул </barsy.help/210-dictionary/article.html>`__ преди налагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$actual_price_base__sec_curr**
     - *string*
     - 
     - Базова `продажба </barsy.help/210-dictionary/sale.html>`__ цена на `артикул </barsy.help/210-dictionary/article.html>`__ преди налагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$total_actual_price_base**
     - *string*
     - 
     - *Сума по базова цена с извадени отстъпки*
   * - **$total_actual_price_base__sec_curr**
     - *string*
     - 
     - *Сума по базова цена с извадени отстъпки*
   * - **$base_discount**
     - *int*
     - 
     - *Процентно отношение между базовата продажна цена и реалната такава*
   * - **$actual_base_total_diff**
     - *string*
     - 
     - *Разлика в € между реалната продажна цена и базовата такава умножени по количеството*
   * - **$actual_base_total_diff__sec_curr**
     - *string*
     - 
     - *Разлика в € между реалната продажна цена и базовата такава умножени по количеството*
   * - **$export_id**
     - *string*
     - 
     - *Идентификатор за експорт към външни системи*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/sales_by_articles`

