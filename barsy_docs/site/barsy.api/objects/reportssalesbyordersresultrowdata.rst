.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsSalesByOrdersResultRowData
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
Lukanet\\Barsy\\Reports\\Data\\ReportsSalesByOrdersResultRowData


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
     - *Дата*
   * - **$ref_date**
     - *string*
     - 
     - *Вальор*
   * - **$barsy**
     - *string*
     - 
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$user_name**
     - *string*
     - 
     - `Потребител </barsy.help/210-dictionary/user.html>`__
   * - **$salon_name**
     - *string*
     - 
     - *Салон*
   * - **$place_name**
     - *string*
     - 
     - *Място*
   * - **$stream_name**
     - *string*
     - 
     - `Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$client_name**
     - *string*
     - 
     - `Клиент </barsy.help/210-dictionary/client.html>`__
   * - **$client_email**
     - *string*
     - 
     - *Имейл*
   * - **$article_name**
     - *string*
     - 
     - `Артикул </barsy.help/210-dictionary/article.html>`__
   * - **$barcode**
     - *string*
     - 
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$export_id**
     - *string*
     - 
     - *Идентификатор за експорт към външни системи*
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
   * - **$current_price**
     - *string*
     - 
     - *Ед. цена*
   * - **$current_price__sec_curr**
     - *string*
     - 
     - *Ед. цена (Български лев)*
   * - **$amount**
     - *string*
     - 
     - *Количество*
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
   * - **$delivery_total**
     - *string*
     - 
     - *Себестойност сума (без ДДС)*
   * - **$delivery_total__sec_curr**
     - *string*
     - 
     - *Себестойност сума (без ДДС) (Български лев)*
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
     - *Комисионни сума*
   * - **$comision__sec_curr**
     - *string*
     - 
     - *Комисионни сума (Български лев)*
   * - **$grand_total**
     - *string*
     - 
     - *Печалба при себестойност без ДДС*
   * - **$grand_total__sec_curr**
     - *string*
     - 
     - *Печалба при себестойност без ДДС*
   * - **$actual_price_base**
     - *string*
     - 
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$actual_price_base__sec_curr**
     - *string*
     - 
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
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
   * - **$paymethod_name**
     - *string*
     - 
     - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$account_id**
     - *int*
     - 
     - `Сметка </barsy.help/210-dictionary/account.html>`__ №
   * - **$account_close_date**
     - *string*
     - 
     - *Закрита*
   * - **$inv_num**
     - *string*
     - 
     - Номера на `фактури </barsy.help/210-dictionary/invoice.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/sales_by_orders`

