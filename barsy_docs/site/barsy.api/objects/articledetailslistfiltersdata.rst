.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleDetailsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articledetails\\Data\\ArticleDetailsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$detail_name**
     - *string*
     - 
     - Филтър по име на характеристиката.

			*Намира и при частично съвпадение*

			 пример: "\"\\u0426\\u0432\\u044f\\u0442\""
   * - **$menu_id**
     - *int*
     - 
     - Филтър дали id на каталог

			 пример: "1"
   * - **$is_service**
     - *int*
     - 0
     - Филтър дали е услуга

			 пример: "1"
   * - **$type**
     - *string*
     - 
     - Филтър по тип на характеристиката

			 пример: "\"text\""
   * - **$group_id**
     - *int*
     - 
     - Филтър по ID група

			 пример: "1"
   * - **$special_type**
     - *string*
     - 
     - Филтър по специален тип ("expiration_days", "master_article")

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/getlist`
	 * :doc:`../methods/articledetails/gettree`

