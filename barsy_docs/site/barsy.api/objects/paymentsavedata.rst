.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PaymentSaveData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Payments\\Data\\PaymentSaveData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$payment_id**
     - *int*
     - 
     - 
   * - **$paymethod_id**
     - *int*
     - 
     - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "1" ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - :deprecated:`$paid_sum`
     - *float*
     - 
     - Платена сума(старо) :deprecated_text:`Отхвърлено: * @test_value 1.34`

			 пример: "1.34"
   * - **$original_paid_sum**
     - *float*
     - 
     - Платена сума във валута

			 пример: "1.34"
   * - **$storno_sum**
     - *float*
     - 
     - Сума за сторниране

			 пример: "1.34"
   * - **$storno_of_account_id**
     - *int*
     - 
     - account_id на сторното
   * - **$req_value**
     - *string*
     - 
     - Необходима информация към `плащането </barsy.help/210-dictionary/payment.html>`__ (настройва се в конкретния начина на `плащане </barsy.help/210-dictionary/payment.html>`__)
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
   * - **$currency_id**
     - *int*
     - 
     - ID на валута.

			*Ако е оставена непопълнена, ще се вземе системната валута*

			 пример: "-1" ( виж: :doc:`../methods/currencies/getlist` )
   * - **$payment_request_id**
     - *int*
     - 
     - ID на payment request (VPOS плащания)
   * - **$link_type**
     - *string*
     - 'use'
     - 
   * - **$barsy_id**
     - *int*
     - 
     - 
   * - **$pos_id**
     - *int*
     - 
     - 
   * - **$period_id**
     - *int*
     - 
     - 
   * - **$user_id**
     - *int*
     - 
     - 
   * - **$confirmed**
     - *int*
     - 
     - 
   * - **$storno_parent_id**
     - *int*
     - 
     - 
   * - **$accounts**
     - *array*
     - 
     - 
   * - **$reservations**
     - *array*
     - 
     - 
   * - **$client_orders**
     - *array*
     - 
     - 
   * - **$invoice_data**
     - 
     - 
     - 
   * - **$payment_type**
     - *string*
     - 'accounts'
     - 
   * - **$target_payment_id_storno**
     - *int*
     - 
     - 
   * - **$storno_data**
     - *StornoData*
     - 
     - 
   * - **$bank_account**
     - *string*
     - 
     - IBAN когато се прави `плащане </barsy.help/210-dictionary/payment.html>`__ от извлечение от банка.

			*После го записваме в b_clients.BANK_ACCOUNTS*
   * - **$client_id**
     - *int*
     - 
     - 
   * - **$operation**
     - *string*
     - 'CRD'
     - Операция на `плащането </barsy.help/210-dictionary/payment.html>`__ (Приход, Разход или Трансфер)

			* **CRD** - *Приход*
			* **DBT** - *Разход*
   * - **$supplier_id**
     - *int*
     - 
     - Връзка на `плащането </barsy.help/210-dictionary/payment.html>`__ с `доставчик </barsy.help/210-dictionary/supplier.html>`__
   * - **$storeloads**
     - *array*
     - 
     - Зареждания за които се отнася `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$store_load_transaction**
     - *string*
     - 
     - Вид на транзакцията на `плащането </barsy.help/210-dictionary/payment.html>`__ към `доставчик </barsy.help/210-dictionary/supplier.html>`__.

			*Дали да е по конкретен документ/и или да няма*

			* **store_load** - *Липсва описание*
			* **no_doc** - *Липсва описание*
   * - **$payment_data**
     - *object*
     - 
     - 
   * - **$ignore_advanced_payment_set**
     - *bool*
     - false
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/createfromclientorder`

