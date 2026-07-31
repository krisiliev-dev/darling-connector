.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreProductionData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeproductions\\Data\\StoreProductionData


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
     - ID на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../methods/barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - 
     - Име на търговския обект
   * - **$depot_id**
     - *int*
     - 
     - ID на `склад </barsy.help/210-dictionary/store.html>`__, в който е произведено ( виж: :doc:`../methods/depots/getlist` )
   * - **$status**
     - *int*
     - 
     - Статус на `производството </barsy.help/210-dictionary/storeproduction.html>`__ [0=Отворено, 1=Приключено]
   * - **$date**
     - *string*
     - 
     - Дата на създаване на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$close_date**
     - *string*
     - 
     - Дата на приключване на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$doc_date**
     - *string*
     - 
     - Документална дата на операцията
   * - **$description**
     - *string*
     - 
     - Описание на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$user_name**
     - *string*
     - 
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$user_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$total_rows**
     - *float*
     - 
     - Брой редове в `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$anulate_flag**
     - *bool*
     - 
     - Флаг дали е анулирано
   * - **$details**
     - *array*
     - 
     - Списък с редовете към `производството </barsy.help/210-dictionary/storeproduction.html>`__ (ако са поискани)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeproductions/getlist`

