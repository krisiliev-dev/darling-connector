.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreproductionsMovementsResultRowData
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
Lukanet\\Barsy\\Storeproductions\\Data\\StoreproductionsMovementsResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_id**
     - *int*
     - 
     - *ID на складово движение*
   * - **$row_id**
     - *string*
     - 
     - *ID на запис в документа*
   * - **$article_name_prod**
     - *string*
     - 
     - Произведен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name**
     - *string*
     - 
     - Изтеглен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *string*
     - 
     - *Количество*
   * - **$avg_delivery_price**
     - *string*
     - 
     - *Себестойност (без ДДС)*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - 
     - *Себестойност (без ДДС) (Български лев)*
   * - **$dds_avg_delivery_price**
     - *string*
     - 
     - *Себестойност (+ДДС)*
   * - **$dds_avg_delivery_price__sec_curr**
     - *string*
     - 
     - *Себестойност (+ДДС) (Български лев)*
   * - **$avg_delivery_price_sum**
     - *string*
     - 
     - *Сума себест (без ДДС)*
   * - **$avg_delivery_price_sum__sec_curr**
     - *string*
     - 
     - *Сума себест (без ДДС) (Български лев)*
   * - **$dds_avg_delivery_price_sum**
     - *string*
     - 
     - *Сума себест (+ДДС)*
   * - **$dds_avg_delivery_price_sum__sec_curr**
     - *string*
     - 
     - *Сума себест (+ДДС) (Български лев)*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeproductions/movements`

