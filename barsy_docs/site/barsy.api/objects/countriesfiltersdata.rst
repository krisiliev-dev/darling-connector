.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CountriesFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Destinations\\Data\\CountriesFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$country_name**
     - *string*
     - 
     - Филтър по име на страна

			 пример: "\"\\u0418\\u0441\\u043f\\u0430\\u043d\\u0438\\u044f\""
   * - **$country_id**
     - *string*
     - 
     - Филтър по двубуквен код на страна

			 пример: "\"BG\""
   * - **$country_code_3**
     - *string*
     - 
     - Филтър по трибуквен код на страна

			 пример: "\"BGR\""
   * - **$has_delivery**
     - *int*
     - 
     - Доставя се до тази страна

			 пример: "1"
   * - **$with_tax_groups_only**
     - *int*
     - 
     - Филтър по страни с познати за нас ДДС групи

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/destinations/getlistcountries`

