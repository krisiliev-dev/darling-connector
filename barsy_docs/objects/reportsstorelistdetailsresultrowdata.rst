.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsStoreListDetailsResultRowData
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
Lukanet\\Barsy\\Reports\\Data\\ReportsStoreListDetailsResultRowData


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
     - *Идентификатор на движението*
   * - **$article_id**
     - *string*
     - 
     - Идентификатор на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$date**
     - *string*
     - 
     - *Дата на операцията*
   * - **$ref_date**
     - *string*
     - 
     - *Вальор на операцията*
   * - **$article_name**
     - *string*
     - 
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$user_name**
     - *string*
     - 
     - `Потребител </barsy.help/210-dictionary/user.html>`__, извършил операцията
   * - **$depot_name**
     - *string*
     - 
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__ и `склад </barsy.help/210-dictionary/store.html>`__
   * - **$reason_name**
     - *string*
     - 
     - *Вид складова операция*
   * - **$amount**
     - *string*
     - 
     - *Количество по операцията*
   * - **$amount_sum**
     - *string*
     - 
     - *Количество след извършване на операцията. Показва се само ако е възможно*
   * - **$avg_delivery_price**
     - *string*
     - 
     - *Средно претеглена доставна цена без ДДС*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - 
     - *Средно претеглена доставна цена без ДДС*
   * - **$avg_delivery_price_sum**
     - *string*
     - 
     - *Сума по себестойност без ДДС*
   * - **$avg_delivery_price_sum__sec_curr**
     - *string*
     - 
     - *Сума по себестойност без ДДС*
   * - **$avg_delivery_price_plus_vat_sum**
     - *string*
     - 
     - *Сума по себестойност с ДДС*
   * - **$avg_delivery_price_plus_vat_sum__sec_curr**
     - *string*
     - 
     - *Сума по себестойност с ДДС*
   * - **$ref_id**
     - *string*
     - 
     - *Референтен номер на операцията*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/store_list_details`

