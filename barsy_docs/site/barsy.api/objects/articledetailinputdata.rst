.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleDetailInputData
======================================================================================
Данни за създаване създаване/редактиране на детайл към артикул

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articledetails\\Data\\ArticleDetailInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$detail_id**
     - *int*
     - 
     - ID на детайл (празно за нов)
   * - **$detail_name**
     - *string*
     - 
     - Име на детайл (подава се за създаване на нов)

			 пример: "\"\\u0426\\u0432\\u044f\\u0442\""
   * - **$detail_value**
     - *string*
     - 
     - Стойност на детайл

			 пример: "\"\\u0447\\u0435\\u0440\\u0432\\u0435\\u043d\\u043e\""
   * - **$key_id**
     - *int*
     - 
     - ID на стойност на детайл (празно за нова)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/save`
	 * :doc:`../methods/articles/create`
	 * :doc:`../methods/articles/update`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

