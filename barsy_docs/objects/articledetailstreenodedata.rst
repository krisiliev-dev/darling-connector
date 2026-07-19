.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleDetailsTreeNodeData
======================================================================================
Една характеристика (детайл) в дървото на характеристиките.

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Свойствата `values` и `data_source` са взаимно изключващи се и се връщат само когато са поискани възможните стойности (extra_properties "values"): малък набор стойности → `values`; голям набор или характеристика тип "autocomplete" → `data_source` (източник за подсказване).

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articledetails\\Data\\ArticleDetailsTreeNodeData


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
     - Име на характеристиката
   * - **$type**
     - *string*
     - 
     - Тип на въвеждане ("text", "select", "autocomplete", "checkbox", "date", "datetime")
   * - **$parent_id**
     - *int*
     - 
     - ID на родителската характеристика (0, ако няма родител)
   * - **$values**
     - *string*
     - 
     - Възможни стойности на характеристиката.

			*Връща се само при поискани стойности и малък набор*
   * - **$data_source**
     - *eStructDataSourceAction*
     - 
     - Източник за подсказване на стойности.

			Връща се вместо `values` при голям набор или тип "autocomplete"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/gettree`

