.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleDetailsTreeGroupData
======================================================================================
Една група характеристики в дървото на характеристиките, заедно с принадлежащите ѝ характеристики.

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articledetails\\Data\\ArticleDetailsTreeGroupData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$group_name**
     - *string*
     - 
     - Име на групата характеристики
   * - **$group_id**
     - *int*
     - 
     - ID на групата характеристики
   * - **$details**
     - *ArticleDetailsTreeNodeData*
     - 
     - Характеристиките в групата, индексирани с ключ "k" + ID на характеристиката (напр. "k12")

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/gettree`

