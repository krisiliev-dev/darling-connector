.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleRecipeRowData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticleRecipeRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$sub_article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__-съставка
   * - **$part**
     - *float*
     - 
     - Количество, с което участва `артикула </barsy.help/210-dictionary/article.html>`__ в рецептата и се изтегля от `склад </barsy.help/210-dictionary/store.html>`__ при изпълнение на рецептата
   * - **$part_after**
     - *float*
     - 
     - Количество, се влага реално в крайния продукт при изпълнение на рецептата (за справки)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articles/save_recipe`

