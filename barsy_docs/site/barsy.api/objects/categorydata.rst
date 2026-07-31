.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CategoryData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Categories\\Data\\CategoryData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$cat_id**
     - *int*
     - 
     - ID на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$parent_id**
     - *int*
     - 
     - ID на родителска `категория </barsy.help/210-dictionary/category.html>`__ (null за главна `категория </barsy.help/210-dictionary/category.html>`__)
   * - **$cat_name**
     - *string*
     - 
     - Име на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_name_ml**
     - *object*
     - 
     - Всички преводи на вътрешното ime на `категорията </barsy.help/210-dictionary/category.html>`__ (за активните езици)
   * - **$cat_name_public**
     - *string*
     - 
     - Публично има на `категорията </barsy.help/210-dictionary/category.html>`__ (за текущия език)
   * - **$cat_name_public_ml**
     - *string*
     - 
     - Всички преводи на публично има на `категорията </barsy.help/210-dictionary/category.html>`__ (за активните езици)
   * - **$cat_type**
     - *int*
     - 
     - Тип на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_path**
     - *string*
     - 
     - Пълен път на `категория </barsy.help/210-dictionary/category.html>`__ от основна
   * - **$description**
     - *string*
     - 
     - Описание на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$description_ml**
     - *string*
     - 
     - Всички преводи на описание на `категория </barsy.help/210-dictionary/category.html>`__ (на активните езици)
   * - **$child_articles_cnt**
     - *int*
     - 
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в `категорията </barsy.help/210-dictionary/category.html>`__ и нейните под `категории </barsy.help/210-dictionary/category.html>`__
   * - **$cat_picture**
     - *string*
     - 
     - Основна картинка на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$code**
     - *string*
     - 
     - код за бързо избиране на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$slug**
     - *string*
     - 
     - Публично URL на `категорията </barsy.help/210-dictionary/category.html>`__ (за електронен магазин)
   * - **$category_icon**
     - *string*
     - 
     - Икона за `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$cat_public_view**
     - *int*
     - 
     - Режим на визуализиране на `категорията </barsy.help/210-dictionary/category.html>`__ в публично меню
   * - **$cat_path_ids**
     - *string*
     - 
     - Път до `категорията </barsy.help/210-dictionary/category.html>`__ от основна, описан с id-та на родителските `категории </barsy.help/210-dictionary/category.html>`__
   * - **$remote_id**
     - *int*
     - 
     - ID на отдалечена система
   * - **$remote_ref_id**
     - *int*
     - 
     - ID на `категорията </barsy.help/210-dictionary/category.html>`__ в отдалечена система
   * - **$preferred_article_id**
     - *int*
     - 
     - ID на предпочитан `артикул </barsy.help/210-dictionary/article.html>`__ за `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$category_color**
     - *string*
     - 
     - Цвят на `категорията </barsy.help/210-dictionary/category.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/categories/getalltree`
	 * :doc:`../methods/categories/getlist`
	 * :doc:`../methods/categories/get`
	 * :doc:`../methods/categories/gettree`
	 * :doc:`../methods/categories/print`
	 * :doc:`../methods/edocs/get_catalog`

