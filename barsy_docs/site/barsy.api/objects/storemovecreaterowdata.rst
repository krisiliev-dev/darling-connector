.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreMoveCreateRowData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storemoves\\Data\\StoreMoveCreateRowData


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
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "123"
   * - **$amount**
     - *float*
     - 
     - Количество, което ще се прехвърля от единия `склад </barsy.help/210-dictionary/store.html>`__ в другия

			 пример: "25"
   * - **$notes**
     - *string*
     - 
     - Свободни бележки за реда

			 пример: "\"\\u0421\\u0432\\u043e\\u0431\\u043e\\u0434\\u043d\\u0438 \\u0431\\u0435\\u043b\\u0435\\u0436\\u043a\\u0438\""
   * - **$received**
     - 
     - 
     - 
   * - **$row_id**
     - 
     - 
     - 
   * - **$lot_value**
     - *string*
     - 
     - Партида

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storemoves/create`
	 * :doc:`../methods/storemoves/update`

