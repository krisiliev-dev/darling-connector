.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsStoreAmountsByDateAndBarsysResultRowData
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
Lukanet\\Barsy\\Reports\\Data\\ReportsStoreAmountsByDateAndBarsysResultRowData


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
   * - **$barcode**
     - *string*
     - 
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$master_cat_id**
     - *string*
     - 
     - Пълен път на главна `категория </barsy.help/210-dictionary/category.html>`__
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
   * - **$actual_price**
     - *string*
     - 
     - Продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ към избраната дата
   * - **$actual_price__sec_curr**
     - *string*
     - 
     - Продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ към избраната дата
   * - **$amount_unit**
     - *string*
     - 1.000000000
     - Количество, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при единична `продажба </barsy.help/210-dictionary/sale.html>`__
   * - **$ref_num**
     - *string*
     - 
     - Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$stream_name**
     - *string*
     - 
     - `Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$store_amount_2**
     - *string*
     - 
     - Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$store_amount_1**
     - *string*
     - 
     - Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$store_amount_3**
     - *string*
     - 
     - Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$amount**
     - *string*
     - 
     - *Общо налично количество към избраната дата*
   * - **$avg_delivery_price**
     - *string*
     - 
     - *Средно претеглена себестойност без ДДС към датата*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - 
     - *Средно претеглена себестойност без ДДС към датата*
   * - **$avg_delivery_price_sum**
     - *string*
     - 
     - *Обща сума по себестойност без ДДС за наличното количество*
   * - **$avg_delivery_price_sum__sec_curr**
     - *string*
     - 
     - *Обща сума по себестойност без ДДС за наличното количество*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/store_amounts_by_date_and_barsys`

