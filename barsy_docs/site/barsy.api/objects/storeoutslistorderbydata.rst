.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreOutsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с изписвания (Storeouts_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като низ ("date desc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeouts\\Data\\StoreOutsListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_out_id**
     - 
     - 
     - 
   * - **$date**
     - 
     - 
     - 
   * - **$close_date**
     - 
     - 
     - 
   * - **$doc_date**
     - 
     - 
     - 
   * - **$total_sum**
     - 
     - 
     - 
   * - **$status**
     - 
     - 
     - 
   * - **$type_id**
     - 
     - 
     - 
   * - **$depot_id**
     - 
     - 
     - 
   * - **$barsy_id**
     - 
     - 
     - 
   * - **$user_id**
     - 
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeouts/getlist`

