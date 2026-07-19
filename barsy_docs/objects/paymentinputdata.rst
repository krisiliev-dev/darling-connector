.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PaymentInputData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Payments\\Data\\PaymentInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$paymethod_id**
     - *int*
     - 
     - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "1" ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$original_paid_sum**
     - *float*
     - 
     - Платена сума във валута

			 пример: "1.34"
   * - **$currency_id**
     - *int*
     - 
     - ID на валута

			 пример: "1" ( виж: :doc:`../methods/currencies/getlist` )
   * - **$req_value**
     - *string*
     - 
     - Необходима допълнителна информация към `плащането </barsy.help/210-dictionary/payment.html>`__ (настройва се в конкретния начина на `плащане </barsy.help/210-dictionary/payment.html>`__)
   * - **$payment_data**
     - *object*
     - 
     - Допълнително данни за `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$transaction_id**
     - *string*
     - 
     - Номер на транзакция

			 пример: "123456643452"
   * - **$ref_num**
     - *string*
     - 
     - Референтен номер
   * - **$ref_date**
     - *string*
     - 
     - Дата вальор
   * - **$description**
     - *string*
     - 
     - Свободен текст
   * - **$receipt_data**
     - *InputStornoData*
     - 
     - Данни за бележката на сторно `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$actual_paid_sum**
     - *float*
     - 
     - Платена сума преди връщане на ресто
   * - **$bank_account**
     - *string*
     - 
     - IBAN на платеца (при `плащане </barsy.help/210-dictionary/payment.html>`__ по банка)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientorders/create`
	 * :doc:`../methods/reservations/create`

