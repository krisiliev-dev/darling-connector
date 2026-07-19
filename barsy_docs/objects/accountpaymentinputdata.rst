.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

AccountPaymentInputData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Payments\\Data\\AccountPaymentInputData


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
     - Платена сума (подава се в оригиналната валута в която е извършено `плащането </barsy.help/210-dictionary/payment.html>`__)

			 пример: "1.34"
   * - **$currency_id**
     - *int*
     - 
     - ID на валута (ако не е подадено - ползва се по подразбиране за инсталацията) ( виж: :doc:`../methods/currencies/getlist` )
   * - **$req_value**
     - *string*
     - 
     - Необходима допълнителна информация към `плащането </barsy.help/210-dictionary/payment.html>`__ (настройва се в конкретния начина на `плащане </barsy.help/210-dictionary/payment.html>`__)
   * - **$payment_data**
     - *string*
     - 
     - Допълнително данни за `плащането </barsy.help/210-dictionary/payment.html>`__

			 пример: "\"free text\""
   * - **$transaction_id**
     - *string*
     - 
     - Номер на транзакция

			 пример: "123456643452"
   * - **$ref_num**
     - *string*
     - 
     - Референтен номер
   * - **$description**
     - *string*
     - 
     - Свободен текст
   * - **$actual_paid_sum**
     - *float*
     - 
     - Платена сума преди връщане на ресто
   * - **$storno_sum**
     - *float*
     - 
     - Сума за сторниране.

			Ползваме се при сторниране на плащания. Може да е по-малко от сумата на `плащане </barsy.help/210-dictionary/payment.html>`__, което се сторнира, но не може да е повече.
   * - **$storno_of_account_id**
     - *int*
     - 
     - Коя е `сметката </barsy.help/210-dictionary/account.html>`__ от която се сторнира.

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/place`

