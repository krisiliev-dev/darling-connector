.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsSalesByOrdersDetailsResultRowData
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
Lukanet\\Barsy\\Reports\\Data\\ReportsSalesByOrdersDetailsResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$order_id**
     - *int*
     - 
     - *ID*
   * - **$date**
     - *string*
     - 
     - Дата на поръчване на конкретния `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$barsy**
     - *string*
     - 
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$pos_name**
     - *string*
     - 
     - `Каса </barsy.help/210-dictionary/pos.html>`__
   * - **$user_name**
     - *string*
     - 
     - `Потребител </barsy.help/210-dictionary/user.html>`__
   * - **$served_name**
     - *string*
     - 
     - *Обслужил*
   * - **$client_name**
     - *string*
     - 
     - `Клиент </barsy.help/210-dictionary/client.html>`__
   * - **$client_email**
     - *string*
     - 
     - *Имейл*
   * - **$client_group**
     - *string*
     - 
     - *Клиентска група*
   * - **$person_name**
     - *string*
     - 
     - `Представител </barsy.help/210-dictionary/person.html>`__
   * - **$article_name**
     - *string*
     - 
     - `Артикул </barsy.help/210-dictionary/article.html>`__
   * - **$process_time**
     - *string*
     - 
     - Зададеното време за обработка се взема от настройките на `артикула </barsy.help/210-dictionary/article.html>`__, а ако не е зададено там, от настройката на `потока </barsy.help/210-dictionary/flow.html>`__
   * - **$full_duration**
     - *string*
     - 
     - *Показва времето от създаването на поръчката до нейното приключване*
   * - **$sum_status_duration_time**
     - *string*
     - 
     - *Реалната продължителност се калкулира от времето, в което поръчката е била със статус маркиран като "Реално създаване в поръчка"*
   * - **$overdue**
     - *string*
     - 
     - Разликата от зададеното време за приготвяне на `артикула </barsy.help/210-dictionary/article.html>`__ и реалната продължителност на поръчката
   * - **$lot_value**
     - *string*
     - 
     - *Партида*
   * - **$barcode**
     - *string*
     - 
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
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
   * - **$export_id**
     - *string*
     - 
     - *Идентификатор за експорт към външни системи*
   * - **$ref_num**
     - *string*
     - 
     - Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$cat_name**
     - *string*
     - 
     - `Категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_path**
     - *string*
     - 
     - `Категория </barsy.help/210-dictionary/category.html>`__ път
   * - **$cat_names**
     - *string*
     - 
     - `Категории </barsy.help/210-dictionary/category.html>`__
   * - **$cat_paths**
     - *string*
     - 
     - `Категория </barsy.help/210-dictionary/category.html>`__ път
   * - **$current_price**
     - *string*
     - 
     - *Ед. цена*
   * - **$current_price__sec_curr**
     - *string*
     - 
     - *Ед. цена (Български лев)*
   * - **$current_price_no_dds**
     - *string*
     - 
     - *Ед.цена без ДДС*
   * - **$current_price_no_dds__sec_curr**
     - *string*
     - 
     - *Ед.цена без ДДС (Български лев)*
   * - **$tax**
     - *string*
     - 
     - *ДДС*
   * - **$amount**
     - *string*
     - 
     - *Продадено количество*
   * - **$store_amount**
     - *string*
     - 
     - *Складови бройки*
   * - **$discounts**
     - *string*
     - 
     - *Отстъпки сума*
   * - **$discounts__sec_curr**
     - *string*
     - 
     - *Отстъпки сума (Български лев)*
   * - **$total**
     - *string*
     - 
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума
   * - **$total__sec_curr**
     - *string*
     - 
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
   * - **$total_no_dds**
     - *string*
     - 
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС
   * - **$total_no_dds__sec_curr**
     - *string*
     - 
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС (Български лев)
   * - **$dds_total**
     - *string*
     - 
     - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума
   * - **$dds_total__sec_curr**
     - *string*
     - 
     - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
   * - **$delivery_total**
     - *string*
     - 
     - *Сума себест (без ДДС)*
   * - **$delivery_total__sec_curr**
     - *string*
     - 
     - *Сума себест (без ДДС) (Български лев)*
   * - **$delivery_total_dds**
     - *string*
     - 
     - *Себестойност с ДДС*
   * - **$delivery_total_dds__sec_curr**
     - *string*
     - 
     - *Себестойност с ДДС*
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
   * - **$grand_total_dds_exc**
     - *string*
     - 
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$grand_total_dds_exc__sec_curr**
     - *string*
     - 
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$actual_price_base**
     - *string*
     - 
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$actual_price_base__sec_curr**
     - *string*
     - 
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$actual_price_base_total**
     - *string*
     - 
     - *Сумата на количеството и базова цена без отстъпки*
   * - **$actual_price_base_total__sec_curr**
     - *string*
     - 
     - *Сумата на количеството и базова цена без отстъпки*
   * - **$total_actual_price_base**
     - *string*
     - 
     - Сума по базова цена с извадени отстъпки за `сметка </barsy.help/210-dictionary/account.html>`__ и `артикул </barsy.help/210-dictionary/article.html>`__, но без `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$total_actual_price_base__sec_curr**
     - *string*
     - 
     - Сума по базова цена с извадени отстъпки за `сметка </barsy.help/210-dictionary/account.html>`__ и `артикул </barsy.help/210-dictionary/article.html>`__, но без `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$pricelist_name**
     - *string*
     - 
     - Списък от `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, въздействали на продажната цена
   * - **$price_after_pricelist_diff**
     - *string*
     - 
     - Сумарна разликата между базовата цена и цената след приложено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$price_after_pricelist_diff__sec_curr**
     - *string*
     - 
     - Сумарна разликата между базовата цена и цената след приложено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$base_discount**
     - *int*
     - 
     - *Процентно отношение между базовата продажна цена и реалната такава*
   * - **$total_discount**
     - *string*
     - 
     - *Пълна отстъпка/надценка*
   * - **$total_discount__sec_curr**
     - *string*
     - 
     - *Пълна отстъпка/надценка (Български лев)*
   * - **$paymethod_name**
     - *string*
     - 
     - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$account_id**
     - *int*
     - 
     - `Сметка </barsy.help/210-dictionary/account.html>`__ №
   * - **$ref_date**
     - *string*
     - 
     - Документална дата на `продажба </barsy.help/210-dictionary/sale.html>`__. Ако не е зададена нарочна се използва датата на закриване
   * - **$account_create_date**
     - *string*
     - 
     - `Сметка </barsy.help/210-dictionary/account.html>`__ открита
   * - **$account_close_date**
     - *string*
     - 
     - `Сметка </barsy.help/210-dictionary/account.html>`__ закрита
   * - **$client_id**
     - *string*
     - 
     - 
   * - **$article_id**
     - *string*
     - 
     - 
   * - **$account_alias**
     - *string*
     - 
     - *Заглавие*
   * - **$card_num**
     - *string*
     - 
     - *Карта №*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/sales_by_orders_details`

