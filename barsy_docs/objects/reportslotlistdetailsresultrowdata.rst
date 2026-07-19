.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsLotListDetailsResultRowData
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
Lukanet\\Barsy\\Reports\\Data\\ReportsLotListDetailsResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$lot_detail_id**
     - *int*
     - 
     - *Идентификатор на партидно движение*
   * - **$article_id**
     - *string*
     - 
     - Идентификатор на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$create_date**
     - *string*
     - 
     - *Дата на движението*
   * - **$operation_doc_date**
     - *string*
     - 
     - *Дата-вальор на операцията*
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
   * - **$operation_ref_type**
     - *string*
     - 
     - *Тип складова операция*

			 пример: "\"AC\""
   * - **$lot_value**
     - *string*
     - 
     - *Номер/стойност на партида*
   * - **$lot_exp_date**
     - *string*
     - 
     - *Срок на годност на партидата*
   * - **$amount**
     - *string*
     - 
     - *Количество на движението*
   * - **$amount_sum**
     - *string*
     - 
     - *Количество след извършване на операцията. Показва се само ако е възможно*
   * - **$ref_id**
     - *string*
     - 
     - *Номер на операция-основание*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/lot_list_details`

