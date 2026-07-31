.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CompaniesListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Companies\\Data\\CompaniesListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$company_id**
     - *int*
     - 
     - Филтър по ID на `фирма </barsy.help/210-dictionary/company.html>`__

			 пример: "1" ( виж: :doc:`../methods/companies/get` )
   * - **$company_name**
     - *string*
     - 
     - Филтър по име на `фирма </barsy.help/210-dictionary/company.html>`__.

			*Намира и при частично съвпадение*

			 пример: "\"test\""
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по флаг за изтрита `фирма </barsy.help/210-dictionary/company.html>`__.

			*Стойност -1 премахва филтъра*

			 пример: "0"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/companies/getlist`

