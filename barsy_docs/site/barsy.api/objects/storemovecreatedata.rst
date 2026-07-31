.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreMoveCreateData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storemoves\\Data\\StoreMoveCreateData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$depot_id_left**
     - *int*
     - 
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, от който се изтелгя количество ( виж: :doc:`../methods/depots/getlist` )
   * - **$depot_id_right**
     - *int*
     - 
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, в кой се прехвърля количество ( виж: :doc:`../methods/depots/getlist` )
   * - **$doc_date**
     - *string*
     - 
     - 
   * - **$description**
     - *string*
     - 
     - 
   * - **$deal_id**
     - *string*
     - 
     -  ( виж: :doc:`../methods/deals/getlist` )
   * - **$inspector_description**
     - *string*
     - 
     - 
   * - **$redirect_depot_id**
     - *int*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storemoves/createfromclientorder`
	 * :doc:`../methods/storemoves/create`
	 * :doc:`../methods/storemoves/update`

