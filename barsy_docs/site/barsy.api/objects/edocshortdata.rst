.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

eDocShortData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Edocs\\Data\\eDocShortData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$type**
     - *string*
     - 
     - Тип на документа
   * - **$doc_id**
     - *int*
     - 
     - ID на документ
   * - **$date**
     - *datetime*
     - 
     - Датата на която е създаден документа

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$total**
     - *float*
     - 
     - Обща сума за `сметка </barsy.help/210-dictionary/account.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/edocs/getlist`

