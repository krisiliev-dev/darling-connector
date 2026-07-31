.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CategoryInputData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Categories\\Data\\CategoryInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$cat_name**
     - *string*
     - 
     - Име на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$cat_name_ml**
     - *MultiLanguageData*
     - 
     - Преводи на вътрешното ime на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$cat_name_public**
     - *MultiLanguageData*
     - 
     - Публично име на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$parent_id**
     - *int*
     - 
     - ID на родителска `категория </barsy.help/210-dictionary/category.html>`__.

			*Null ако няма родител (най-горно ниво)*
   * - **$category_icon**
     - *string*
     - 
     - Икона за `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$description**
     - *MultiLanguageData*
     - 
     - Свободен текст описание
   * - **$code**
     - *int*
     - 
     - Код за бързо избиране
   * - **$cat_picture**
     - *string*
     - 
     - 
   * - **$slug**
     - *string*
     - 
     - Публичен URL на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$cat_public_view**
     - *int*
     - 
     - Публичен изглед на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$remote_ref_id**
     - *string*
     - 
     - ID на отдалечена система
   * - **$remote_parent_ref_id**
     - *string*
     - 
     - ID на родител отдалечена система
   * - **$preferred_article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, предпочитан за `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$category_color**
     - *string*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/categories/create`
	 * :doc:`../methods/categories/update`

