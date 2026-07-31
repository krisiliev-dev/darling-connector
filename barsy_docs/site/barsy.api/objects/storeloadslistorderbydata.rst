.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreLoadsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка със зареждания (Storeloads_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като низ ("date desc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeloads\\Data\\StoreLoadsListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_load_id**
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
   * - **$doc_num**
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
   * - **$depot_id**
     - 
     - 
     - 
   * - **$barsy_id**
     - 
     - 
     - 
   * - **$creator_id**
     - 
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeloads/getlist`

