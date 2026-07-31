.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreOutsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeouts\\Data\\StoreOutsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_out_id**
     - *int*
     - 
     - ID на `зареждане </barsy.help/210-dictionary/storeload.html>`__
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
     - Филтър по дата на създаване на документа
   * - **$close_date**
     - *datetime*
     - 
     - Филтър по дата на приключване на документа
   * - **$doc_date**
     - *datetime*
     - 
     - Филтър по документална дата на документа
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
     - Филтър по статус

			* **0** - *Отворено*
			* **1** - *Приключено*
   * - **$type_id**
     - *int*
     - 
     - Филтър по тип `изписване </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../methods/storeouts/types_getlist` )
   * - **$ref_id**
     - *int*
     - 
     - Филтър по референтен номер, свързващ анулиран с анулиращ документ
   * - **$anulate_flag**
     - *int*
     - 
     - Филтър флаг дали `изписването </barsy.help/210-dictionary/storeout.html>`__ е анулирано или анулиращо

			* **0** - *Не е анулиран*
			* **1** - *Анулиран*
			* **-1** - *Анулиращ*
   * - **$export_id**
     - *int*
     - 
     - Филтър по Export ID

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeouts/getlist`

