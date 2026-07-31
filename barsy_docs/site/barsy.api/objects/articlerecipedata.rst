.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleRecipeData
======================================================================================
Данни за рецепта към артикул

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticleRecipeData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$composite**
     - *int*
     - 1
     - Тип на рецептата [1=При приключване на `сметка </barsy.help/210-dictionary/account.html>`__; -1=При `производство </barsy.help/210-dictionary/storeproduction.html>`__]
   * - **$amount_prod**
     - *float*
     - 1
     - Получено количество от `производството </barsy.help/210-dictionary/storeproduction.html>`__ на тази рецепта
   * - **$recipe_description**
     - *string*
     - 
     - Описание на рецептата (свободен текст)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articles/save_recipe`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

