.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

eDocData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Edocs\\Data\\eDocData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$discount**
     - *float*
     - 
     - Обща отстъпка за `сметка </barsy.help/210-dictionary/account.html>`__ в проценти (отрицателна стойност -> отстъпка, положителна -> надценка)
   * - **$paymethod_id**
     - *int*
     - 
     - ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$client_name**
     - *string*
     - 
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__, асоциран с документа
   * - **$description**
     - *string*
     - 
     - Описание на документа - свободен текст
   * - **$orders**
     - *eDocOrderData*
     - 
     - Списък от `поръчки към сметка </barsy.help/210-dictionary/account-order.html>`__
   * - **$status**
     - *string*
     - 
     - Текущ статус на документа
   * - **$type**
     - *string*
     - 
     - Тип на документа
   * - **$doc_id**
     - *int*
     - 
     - ID на документ
   * - **$date**
     - *datetime*
     - 
     - Датата на която е създаден документа

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$total**
     - *float*
     - 
     - Обща сума за `сметка </barsy.help/210-dictionary/account.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/edocs/get_by_sid`
	 * :doc:`../methods/edocs/get`

