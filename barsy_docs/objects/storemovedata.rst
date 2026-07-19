.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreMoveData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storemoves\\Data\\StoreMoveData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_move_id**
     - 
     - 
     - 
   * - **$depot_id_left**
     - *int*
     - 
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, от който се изтелгя количество
   * - **$depot_id_right**
     - *int*
     - 
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, в кой се прехвърля количество
   * - **$doc_date**
     - *string*
     - 
     - 
   * - **$description**
     - *string*
     - 
     - 
   * - **$user_name**
     - *string*
     - 
     - `Потребител </barsy.help/210-dictionary/user.html>`__, създал `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$user_id**
     - *int*
     - 
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$inspector_user_name**
     - *string*
     - 
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, проверил `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$date**
     - *string*
     - 
     - Дата на създаване на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$inspector_description**
     - *string*
     - 
     - Description of the inspector
   * - **$status**
     - *string*
     - 
     - Статус на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$user_status**
     - *string*
     - 
     - Заглавие на статус
   * - **$close_date**
     - *string*
     - 
     - Дата за затваряне на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$from_barsy_id**
     - *int*
     - 
     - ID на изходящия `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$to_barsy_id**
     - *int*
     - 
     - ID на входящия `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$from_depot_name**
     - 
     - 
     - 
   * - **$to_depot_name**
     - 
     - 
     - 
   * - **$from_barsy_name**
     - 
     - 
     - 
   * - **$to_barsy_name**
     - 
     - 
     - 
   * - **$details**
     - *StoreMoveDetailData*
     - 
     - Детайли за `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storemoves/getlist`
	 * :doc:`../methods/storemoves/get`

