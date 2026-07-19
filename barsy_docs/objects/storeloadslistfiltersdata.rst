.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreLoadsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeloads\\Data\\StoreLoadsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_load_id**
     - *int*
     - 
     - ID на `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - Филтър по "`Търговски обект </barsy.help/210-dictionary/barsy.html>`__" в който е направено `зареждането </barsy.help/210-dictionary/storeload.html>`__ ( виж: :doc:`../methods/barsys/getlist` )
   * - **$depot_id**
     - *int*
     - 
     - Филтър по "`Склад </barsy.help/210-dictionary/store.html>`__" в който е направено `зареждането </barsy.help/210-dictionary/storeload.html>`__ ( виж: :doc:`../methods/depots/getlist` )
   * - **$date**
     - *datetime*
     - 
     - Филтър по дата на създаване на документа

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$doc_date**
     - *datetime*
     - 
     - Филтър по дата на документа, по които е направена операцията

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$creator_id**
     - *int*
     - 
     - Филтър по ID на създател на операцията ( виж: :doc:`../methods/users/getlist` )
   * - **$user_name**
     - *string*
     - 
     - Филтър по име на създател на операцията ( виж: :doc:`../methods/users/getlist` )
   * - **$status**
     - *int*
     - 
     - Филтър по статус

			* **0** - *Отворено*
			* **1** - *Приключено*
   * - **$last_update**
     - *datetime*
     - 
     - Дата на последно обновяване на `зареждането </barsy.help/210-dictionary/storeload.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$operation_type**
     - *int*
     - 
     - Операция на `зареждането </barsy.help/210-dictionary/storeload.html>`__ (1: `Зареждане </barsy.help/210-dictionary/storeload.html>`__ на стока, 2: Връщане на стока)
   * - **$doc_type_id**
     - *int*
     - 
     - Тип на документа ( виж: :doc:`../methods/storeloads/getdocumenttypes` )
   * - **$remote_id**
     - *int*
     - 
     - Номер на отдалечената система ( виж: :doc:`../methods/remotesystems/getlist` )

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeloads/getlist`

