.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StreamsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с потоци (Streams_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като асоциативен масив колона⇒посока (напр. ["name" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Streams\\Data\\StreamsListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$name**
     - *string*
     - 
     - Подреждане по име на `потока </barsy.help/210-dictionary/flow.html>`__
   * - **$order_in_receipt**
     - *string*
     - 
     - Подреждане по тежест в бележките
   * - **$stream_id**
     - *string*
     - 
     - Подреждане по ID на `потока </barsy.help/210-dictionary/flow.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/streams/getlist`

Виж също
--------

 * `Поток </barsy.help/210-dictionary/flow.html>`__

