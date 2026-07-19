.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsSalesByAccountsResultRowData
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
Lukanet\\Barsy\\Reports\\Data\\ReportsSalesByAccountsResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$account_id**
     - *int*
     - 
     - `Сметка </barsy.help/210-dictionary/account.html>`__
   * - **$account_alias**
     - *string*
     - 
     - *Заглавие*
   * - **$create_date**
     - *string*
     - 
     - *Отворена*
   * - **$close_date**
     - *string*
     - 
     - *Закрита на*
   * - **$ref_date**
     - *string*
     - 
     - *Документ дата*
   * - **$barsy**
     - *string*
     - 
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$user_name**
     - *string*
     - 
     - `Потребител </barsy.help/210-dictionary/user.html>`__
   * - **$place_name**
     - *string*
     - 
     - *Място*
   * - **$persons**
     - *string*
     - 
     - *Хора*
   * - **$client_name**
     - *string*
     - 
     - `Клиент </barsy.help/210-dictionary/client.html>`__
   * - **$discount**
     - *int*
     - 
     - *Отстъпка*
   * - **$cnt**
     - *string*
     - 
     - *Продадени бройки*
   * - **$store_amount**
     - *string*
     - 
     - *Складови бройки*
   * - **$oborot**
     - *string*
     - 
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот
   * - **$oborot__sec_curr**
     - *string*
     - 
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот (Български лев)
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
   * - **$delivery_price_dds**
     - *string*
     - 
     - Себестойност с ДДС за единичен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$delivery_price_dds__sec_curr**
     - *string*
     - 
     - Себестойност с ДДС за единичен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$comision**
     - *string*
     - 
     - *Комисионни*
   * - **$comision__sec_curr**
     - *string*
     - 
     - *Комисионни (Български лев)*
   * - **$grand_total**
     - *string*
     - 
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$grand_total__sec_curr**
     - *string*
     - 
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$procent**
     - *string*
     - 
     - Процент надценка между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$total_actual_price_base**
     - *string*
     - 
     - *Сума по базова цена с извадени отстъпки*
   * - **$total_actual_price_base__sec_curr**
     - *string*
     - 
     - *Сума по базова цена с извадени отстъпки*
   * - **$actual_base_total_diff**
     - *string*
     - 
     - *Разлика в € между реалната продажна цена и базовата такава умножени по количеството*
   * - **$actual_base_total_diff__sec_curr**
     - *string*
     - 
     - *Разлика в € между реалната продажна цена и базовата такава умножени по количеството*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/sales_by_accounts`

