.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

RevisionsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с ревизии (Revisions_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като низ ("date desc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Revisions\\Data\\RevisionsListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$rev_id**
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
   * - **$amount_date**
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

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/revisions/getlist`

Виж също
--------

 * `Ревизия </barsy.help/210-dictionary/revision.html>`__

