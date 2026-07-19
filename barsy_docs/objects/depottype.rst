.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

DepotType
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Depots\\Data\\DepotType


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$depot_id**
     - *int*
     - 
     - ID на `склада </barsy.help/210-dictionary/store.html>`__
   * - **$depot_name**
     - *string*
     - 
     - Име на `склада </barsy.help/210-dictionary/store.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - ID на търговския обект ( виж: :doc:`../methods/barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - 
     - Име на търговския обект
   * - **$depot_group_id**
     - *int*
     - 
     - ID на групата, към която принадлежи `склада </barsy.help/210-dictionary/store.html>`__
   * - **$group_name**
     - *string*
     - 
     - Име на складовата група, към която принадлежи `склада </barsy.help/210-dictionary/store.html>`__
   * - **$description**
     - *string*
     - 
     - Описание на `склада </barsy.help/210-dictionary/store.html>`__
   * - **$delete_flag**
     - *bool*
     - 
     - Флаг дали `склада </barsy.help/210-dictionary/store.html>`__ е маркиран като изтрит
   * - **$can_load**
     - *bool*
     - 
     - Флаг дали `склада </barsy.help/210-dictionary/store.html>`__ може да се зарежда чрез операция "`Зареждане </barsy.help/210-dictionary/storeload.html>`__"
   * - **$can_move_outside**
     - *bool*
     - 
     - Флаг дали от `склада </barsy.help/210-dictionary/store.html>`__ може да бъде извършено `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ от и към външни складове (в други `търговски обекти </barsy.help/210-dictionary/barsy.html>`__)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/depots/getlistcurrent`
	 * :doc:`../methods/depots/getlist`

