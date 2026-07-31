.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CategoriesListFilterData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Categories\\Data\\CategoriesListFilterData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$parent_id**
     - *int*
     - 
     - Филтър по `категория </barsy.help/210-dictionary/category.html>`__ и всички вътрешни на нея като филтрирането не се свежда до `артикули </barsy.help/210-dictionary/article.html>`__ а пряко по `категориите </barsy.help/210-dictionary/category.html>`__

			 пример: "1"
   * - **$remote_ref_id**
     - *int*
     - 
     - Филтър по ID на `категорията </barsy.help/210-dictionary/category.html>`__ в отдалечена система

			 пример: "1"
   * - **$remote_id**
     - *int*
     - 
     - Филтър по ID на отдалечена система

			 пример: "1"
   * - **$for_remote_update**
     - *bool*
     - false
     - Филтър по това, дали `категорията </barsy.help/210-dictionary/category.html>`__ е обновявана в Барси

			 пример: "1"
   * - **$menu_id**
     - *int*
     - 
     - Филтър id на каталог

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/categories/getlist`

