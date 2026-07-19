.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ModificatorsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reservations\\Data\\ModificatorsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$modificator_id**
     - *int*
     - 
     - Филтър по id на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$user_id**
     - *int*
     - 
     - Филтър по id на `потребител </barsy.help/210-dictionary/user.html>`__ (създател)
   * - **$mod_name**
     - *string*
     - 
     - Филтър по име на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$create_date**
     - *datetime*
     - 
     - Филтър по дата на създаване

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по флаг "Изтрит"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/modificators/getlist`

