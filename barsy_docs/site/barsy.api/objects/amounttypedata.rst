.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

AmountTypeData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Amounttypes\\Data\\AmountTypeData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$amount_type_id**
     - *int*
     - 
     - ID на типа

			 пример: "1" ( виж: :doc:`../methods/amounttypes/getlist` )
   * - **$amount_type_name**
     - *string*
     - 
     - Име на типа

			 пример: "\"\\u041a\\u0438\\u043b\\u043e\\u0433\\u0440\\u0430\\u043c\"" ( виж: :doc:`../methods/amounttypes/getlist` )
   * - **$amount_type_name_short**
     - *string*
     - 
     - Кратко име на типа

			 пример: "\"\\u0431\\u0433\""
   * - **$time_interval**
     - *int*
     - 
     - 
   * - **$value_precision**
     - *float*
     - 
     - Точност след десетичния знак

			 пример: "2"
   * - **$export_id**
     - *string*
     - 
     - ID при експорт на тип - например за импорт в друга система

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/amounttypes/getlist`

