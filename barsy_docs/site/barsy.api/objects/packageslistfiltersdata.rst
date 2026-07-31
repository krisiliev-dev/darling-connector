.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PackagesListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Packages\\Data\\PackagesListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$package_id**
     - *int*
     - 
     - Филтър по ID на разфасовка

			 пример: "1" ( виж: :doc:`../methods/packages/get` )
   * - **$package_name**
     - *string*
     - 
     - Филтър по име на разфасовка.

			*Намира и при частично съвпадение*

			 пример: "\"\\u041a\\u0430\\u0441\\u0430\""
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по флаг за изтрита разфасовка.

			*Стойност -1 премахва филтъра*

			 пример: "0"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/packages/getlist`

