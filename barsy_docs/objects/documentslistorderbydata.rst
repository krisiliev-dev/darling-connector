.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

DocumentsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с документи (Documents_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като асоциативен масив колона⇒посока (напр. ["update_date" => "desc", "document_id" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Documents\\Data\\DocumentsListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - 
     - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
     - 
   * - **$document_id**
     - *string*
     - 
     - Подреждане по ID на документ
   * - **$doc_type_id**
     - *string*
     - 
     - Подреждане по тип документ
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$document_name**
     - *string*
     - 
     - Подреждане по име на документ
   * - **$doc_num**
     - *string*
     - 
     - Подреждане по номер на документ
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$create_date**
     - *string*
     - 
     - Подреждане по дата на създаване
   * - **$update_date**
     - *string*
     - 
     - Подреждане по дата на последна промяна
   * - **$ref_date**
     - *string*
     - 
     - Подреждане по вальор
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$status_id**
     - *string*
     - 
     - Подреждане по статус
   * - **$delete_flag**
     - *string*
     - 
     - Подреждане по флаг за изтрит
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$client_id**
     - *string*
     - 
     - Подреждане по `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$user_id**
     - *string*
     - 
     - Подреждане по `потребител </barsy.help/210-dictionary/user.html>`__-създател
   * - **$owner_id**
     - *string*
     - 
     - Подреждане по отговорник

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/documents/getlist`

