.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsSalesByTaxGroupsResultRowData
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
Lukanet\\Barsy\\Reports\\Data\\ReportsSalesByTaxGroupsResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$tax_id**
     - *int*
     - 
     - *ID*
   * - **$tax_name**
     - *string*
     - 
     - *ДДС група*
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
   * - **$comision**
     - *string*
     - 
     - *Комисионни сума*
   * - **$comision__sec_curr**
     - *string*
     - 
     - *Комисионни сума (Български лев)*
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
   * - **$total_actual_price_base**
     - *string*
     - 
     - *Сума по базова цена с извадени отстъпки*
   * - **$total_actual_price_base__sec_curr**
     - *string*
     - 
     - *Сума по базова цена с извадени отстъпки*
   * - **$current_pricelist_id**
     - *string*
     - 
     - Списък от `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, въздействали на продажната цена
   * - **$base_discount**
     - *int*
     - 
     - *Процентно отношение между базовата продажна цена и реалната такава*
   * - **$total_discount**
     - *string*
     - 
     - *Пълна отстъпка*
   * - **$total_discount__sec_curr**
     - *string*
     - 
     - *Пълна отстъпка (Български лев)*
   * - **$client_id**
     - *string*
     - 
     - 
   * - **$article_id**
     - *string*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/sales_by_tax_groups`

