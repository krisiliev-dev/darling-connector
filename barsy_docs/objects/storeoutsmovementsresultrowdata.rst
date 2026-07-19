.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreoutsMovementsResultRowData
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
Lukanet\\Barsy\\Storeouts\\Data\\StoreoutsMovementsResultRowData


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
   * - **$date**
     - *string*
     - 
     - *Дата*
   * - **$ref_date**
     - *string*
     - 
     - *Вальор*
   * - **$master_article_name**
     - *string*
     - 
     - Изписан `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name**
     - *string*
     - 
     - Изтеглен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *string*
     - 
     - *Количество*
   * - **$barsy_name**
     - *string*
     - 
     - *ТО*
   * - **$depot_name**
     - *string*
     - 
     - `Склад </barsy.help/210-dictionary/store.html>`__
   * - **$user_name**
     - *string*
     - 
     - `Потребител </barsy.help/210-dictionary/user.html>`__
   * - **$avg_delivery_price**
     - *string*
     - 
     - *Себестойност (без ДДС)*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - 
     - *Себестойност (без ДДС) (Български лев)*
   * - **$avg_delivery_price_sum**
     - *string*
     - 
     - *Сума себест (без ДДС)*
   * - **$avg_delivery_price_sum__sec_curr**
     - *string*
     - 
     - *Сума себест (без ДДС) (Български лев)*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeouts/movements`

