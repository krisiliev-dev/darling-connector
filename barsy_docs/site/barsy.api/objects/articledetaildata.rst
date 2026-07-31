.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleDetailData
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
Lukanet\\Barsy\\Articledetails\\Data\\ArticleDetailData


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
   * - **$detail_value**
     - *string*
     - 
     - Стойност на детайл
   * - **$key_id**
     - *int*
     - 
     - ID на стойност на детайл (празно за нова)
   * - **$detail_name**
     - *string*
     - 
     - Име на детайл (подава се за създаване на нов)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/get`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

