.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreMovesListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storemoves\\Data\\StoreMovesListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$from_barsy_id**
     - *int*
     - 
     - Филтър по "от ТО"
   * - **$from_depot_id**
     - *int*
     - 
     - Филтър по "от `Склад </barsy.help/210-dictionary/store.html>`__"
   * - **$to_barsy_id**
     - *int*
     - 
     - Филтър по "до ТО"
   * - **$to_depot_id**
     - *int*
     - 
     - Филтър по "до `Склад </barsy.help/210-dictionary/store.html>`__"
   * - **$date**
     - *datetime*
     - 
     - Филтър по дата на създаване на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$creator_id**
     - *int*
     - 
     - Филтър по id на създател
   * - **$creator_name**
     - *string*
     - 
     - Филтър по име на създател
   * - **$inspector_id**
     - *int*
     - 
     - Филтър по id на приел
   * - **$inspector_name**
     - *string*
     - 
     - Филтър по име на приел
   * - **$status**
     - *int*
     - 
     - Филтър по статус

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storemoves/getlist`

