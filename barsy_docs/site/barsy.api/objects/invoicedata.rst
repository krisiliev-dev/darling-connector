.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

InvoiceData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Invoices\\Data\\InvoiceData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$inv_id**
     - *int*
     - 
     - ID на `фактурата </barsy.help/210-dictionary/invoice.html>`__ (вътрешна номенклатура)
   * - **$inv_sid**
     - *string*
     - 
     - SID на `фактурата </barsy.help/210-dictionary/invoice.html>`__ (вътрешна номенклатура кодирана)
   * - **$inv_num**
     - *string*
     - 
     - 
   * - **$linked_accounts_num**
     - 
     - 
     - 
   * - **$type_id**
     - *int*
     - 1
     - Тип на документа (`фактура </barsy.help/210-dictionary/invoice.html>`__, проформа, дебитно/кредитно известие, стокова ...)
   * - **$type_name**
     - *string*
     - 
     - Тип на документа
   * - **$parent_num**
     - *string*
     - 
     - Номер на документ, по който е издаден този
   * - **$produce_date**
     - *string*
     - 
     - Дата на издаване
   * - **$create_date**
     - *string*
     - 
     - Дата на създаване
   * - **$term_date**
     - *string*
     - 
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$payment_date**
     - *string*
     - 
     - Дата на събитие
   * - **$paymethod_id**
     - 
     - 
     - 
   * - **$paymethod_name**
     - 
     - 
     - 
   * - **$is_anulate**
     - *int*
     - 0
     - Флаг дали `фактурата </barsy.help/210-dictionary/invoice.html>`__ е анулирана
   * - **$total_all_string**
     - *string*
     - 
     - Словом на сумата на `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$total_dds_string**
     - *string*
     - 
     - Словом на сумата на ДДС
   * - **$with_tax**
     - *int*
     - 0
     - Флаг дали при печат да се печатат `артикулите </barsy.help/210-dictionary/article.html>`__ с ед.цени с ДДС
   * - **$seller_name**
     - *string*
     - 
     - Име на издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$receiver_name**
     - *string*
     - 
     - Име на получил `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$additional_text**
     - *string*
     - 
     - Допълнителен текст към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$free_text**
     - *string*
     - 
     - Свободен текст към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_code**
     - *int*
     - 
     - Уникален код на издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_company_id**
     - *int*
     - 
     - ID на издател на `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_bank_account_id**
     - *int*
     - 
     - ID на банкова `сметка </barsy.help/210-dictionary/account.html>`__ за която е `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ (номенклатура на Barsy)
   * - **$client**
     - *ClientData*
     - 
     - Данни за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който е издадена `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$user_id**
     - *int*
     - 
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$accounts**
     - *array*
     - 
     - Списък с прикачените `сметки </barsy.help/210-dictionary/account.html>`__ към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_id**
     - *int*
     - 
     - 
   * - **$receiver_id**
     - *int*
     - 
     - 
   * - **$client_name**
     - 
     - 
     - 
   * - **$email**
     - 
     - 
     - 
   * - **$currency**
     - 
     - 
     - 
   * - **$seller**
     - *InvoiceCompanyData*
     - 
     - Данни за получател
   * - **$receiver**
     - *InvoiceCompanyData*
     - 
     - Данни за `доставчик </barsy.help/210-dictionary/supplier.html>`__
   * - **$parent**
     - 
     - 
     - 
   * - **$bank_account_id**
     - *int*
     - 
     - 
   * - **$bank_account**
     - *InvoiceBankAccountData*
     - 
     - 
   * - **$seller_pop_name**
     - 
     - 
     - 
   * - **$paymethod_version_id**
     - 
     - 
     - 
   * - **$deal_id**
     - 
     - 
     - 
   * - **$deal_title**
     - 
     - 
     - 
   * - **$client_order_ids**
     - *string*
     - 
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ фигуриращи в `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$detailed_client_order_ids**
     - *string*
     - 
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ с дата на издаването им фигуриращи в `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$items**
     - *InvoiceItemData*
     - []
     - Списък с `артикулите </barsy.help/210-dictionary/article.html>`__ към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$total**
     - *float*
     - 0
     - Обсща сума на `фактурата </barsy.help/210-dictionary/invoice.html>`__ в системната валута
   * - **$total_sum**
     - *float*
     - 0
     - Обща сума с ДДС (ако се начислява) в систманата валута
   * - **$total_neto**
     - *float*
     - 0
     - Обща сума без ДДС в системната валута
   * - **$total_dds**
     - *float*
     - 0
     - Сума на ДДС в системната валута
   * - **$total_all**
     - *float*
     - 0
     - 
   * - **$discount**
     - *float*
     - 0
     - 
   * - **$discount_sum**
     - 
     - 0
     - 
   * - **$initial_total**
     - 
     - 0
     - 
   * - **$tax_totals_by_tax**
     - 
     - []
     - 
   * - **$tax_neto_by_tax**
     - 
     - []
     - 
   * - **$parent_inv_id**
     - *int*
     - 
     - 
   * - **$total_remain**
     - *float*
     - 
     - 
   * - **$person_id**
     - *int*
     - 
     - 
   * - **$person_name**
     - *string*
     - 
     - 
   * - **$currency_id**
     - *int*
     - 
     - 
   * - **$currency_rate**
     - *float*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/invoices/get_by_sid`
	 * :doc:`../methods/invoices/getlist`
	 * :doc:`../methods/invoices/get`

