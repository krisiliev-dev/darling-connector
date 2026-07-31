.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreMovesListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с прехвърляния (Storemoves_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като низ ("date desc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storemoves\\Data\\StoreMovesListOrderByData


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
   * - **$date**
     - 
     - 
     - 
   * - **$doc_date**
     - 
     - 
     - 
   * - **$close_date**
     - 
     - 
     - 
   * - **$status**
     - 
     - 
     - 
   * - **$from_depot_id**
     - 
     - 
     - 
   * - **$to_depot_id**
     - 
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storemoves/getlist`

