.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreProductionsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeproductions\\Data\\StoreProductionsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_production_id**
     - *int*
     - 
     - Филтър по ID на `производство </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - Филтър по "`Търговски обект </barsy.help/210-dictionary/barsy.html>`__" ( виж: :doc:`../methods/barsys/getlist` )
   * - **$depot_id**
     - *int*
     - 
     - Филтър по "`Склад </barsy.help/210-dictionary/store.html>`__" ( виж: :doc:`../methods/depots/getlist` )
   * - **$date**
     - *datetime*
     - 
     - Филтър по дата на създаване на `производството </barsy.help/210-dictionary/storeproduction.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$user_id**
     - *int*
     - 
     - Филтър по id на създател ( виж: :doc:`../methods/users/getlist` )
   * - **$user_name**
     - *string*
     - 
     - Филтър по име на създател ( виж: :doc:`../methods/users/getlist` )
   * - **$status**
     - *int*
     - 
     - Филтър по статус [0=Отворено, 1=Приключено]
   * - **$close_date**
     - *datetime*
     - 
     - Филтър по дата на приключване на `производството </barsy.help/210-dictionary/storeproduction.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeproductions/getlist`

