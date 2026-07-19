.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

eStructDataSourceAction
======================================================================================
Изгражда DataSource от подадено име на action. Стойностите се получават чрез викане на екшъна от клиента (външен рекуест).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*Екшънът трябва да връща стардартен списък от стойности - масив от обекти с указани filed_key и field_title*

*Class Lukanet\Lib\eStruct\Services\eStructDataSourceAction*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\eStruct\\Services\\eStructDataSourceAction


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$type**
     - 
     - 'action'
     - 
   * - **$class_name**
     - *string*
     - 
     - 
   * - **$extra_fields**
     - *array*
     - 
     - 
   * - **$target**
     - 
     - 
     - 
   * - **$field_key**
     - 
     - 'key'
     - 
   * - **$field_title**
     - 
     - 'title'
     - 
   * - **$values**
     - 
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/gettree`

Виж също
--------

 * `Клиент </barsy.help/210-dictionary/client.html>`__

