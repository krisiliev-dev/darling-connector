.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

InvoicesListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с документи (Invoices_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като асоциативен масив колона⇒посока (напр. ["create_date" => "desc", "inv_num" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Invoices\\Data\\InvoicesListOrderByData


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
   * - **$inv_id**
     - *string*
     - 
     - Подреждане по ID на документа
   * - **$inv_num**
     - *string*
     - 
     - Подреждане по номер на документа
   * - **$type_id**
     - *string*
     - 
     - Подреждане по тип на документа
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
   * - 
     - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
     - 
   * - **$total**
     - *string*
     - 
     - Подреждане по обща сума
   * - **$total_all**
     - *string*
     - 
     - Подреждане по крайна сума за `плащане </barsy.help/210-dictionary/payment.html>`__ (с ДДС)
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
   * - **$term_date**
     - *string*
     - 
     - Подреждане по срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$payment_date**
     - *string*
     - 
     - Подреждане по дата на `плащане </barsy.help/210-dictionary/payment.html>`__ (данъчно събитие)
   * - **$last_update**
     - *string*
     - 
     - Подреждане по дата на последна промяна

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/invoices/getlist`

