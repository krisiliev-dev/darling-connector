.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

TaxGroupsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Taxgroups\\Data\\TaxGroupsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$tax_id**
     - *int*
     - 
     - ID на ДДС група
   * - **$tax**
     - *int*
     - 
     - Процент на ДДС група
   * - **$tax_name**
     - *string*
     - 
     - Име на ДДС група
   * - **$is_default**
     - *int*
     - 
     - Дали се ползва по подразбиране
   * - **$tax_code**
     - *string*
     - 
     - Код на ДДС група
   * - **$country_id**
     - *array* | *string* | *null*
     - 
     - Държава на ДДС група

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/taxgroups/getlist`

