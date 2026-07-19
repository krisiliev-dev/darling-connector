.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CurrenciesListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Currencies\\Data\\CurrenciesListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$currency_id**
     - *int*
     - 
     - 
   * - **$currency_code**
     - *string*
     - 
     - 
   * - **$exclude_native**
     - *int*
     - 
     - Филтър флаг за това дали да се изключи основната валута
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по плаг дали валутата е изтрита
   * - **$is_secondary**
     - *int*
     - 
     - 
   * - **$is_current**
     - *int*
     - 
     - Текуща валута

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/currencies/getlist`

