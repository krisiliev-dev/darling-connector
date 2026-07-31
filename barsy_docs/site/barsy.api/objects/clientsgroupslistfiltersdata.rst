.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientsGroupsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clients\\Data\\ClientsGroupsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_levels_enabled**
     - *int*
     - 
     - Филтър дали групата има "Участие в прагове"

			 пример: "1"
   * - **$delete_flag**
     - *int*
     - 
     - Филтър по изтритите групи

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientgroups/getlist`
	 * :doc:`../methods/clients/getgroups`

