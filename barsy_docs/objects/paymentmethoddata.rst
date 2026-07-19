.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PaymentMethodData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Paymentmethods\\Data\\PaymentMethodData


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
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$name**
     - *string*
     - 
     - Име на начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$fx**
     - *int*
     - 
     - Извършва ли фискална операция
   * - **$require_info**
     - *string*
     - 
     - 
   * - **$require_info_title**
     - *string*
     - 
     - 
   * - **$require_info_list_data_source**
     - *string*
     - 
     - Източник на списък с данни

			 пример: "\"payment_provider\""
   * - **$provider_id**
     - *int*
     - 
     - 
   * - **$description**
     - 
     - 
     - 
   * - **$pay_from_client_balance**
     - 
     - 
     - 
   * - **$public_name**
     - *string*
     - 
     - Публично име
   * - **$type_id**
     - *int*
     - 
     - 
   * - **$card_type_id**
     - *int*
     - 
     - Тип `плащане </barsy.help/210-dictionary/payment.html>`__ като Бонус програма и `Ваучер </barsy.help/210-dictionary/card.html>`__ са обвързани с различен вид карти.

			*В тази стойност пазим този типът на картата*
   * - **$settings**
     - 
     - 
     - 
   * - **$show_in_invoice**
     - *int*
     - 
     - 
   * - **$delete_flag**
     - *int*
     - 0
     - 
   * - **$deny_anonymous**
     - *int*
     - 0
     - 
   * - **$public_name_ml**
     - *MultiLanguageData*
     - 
     - 
   * - **$currencies**
     - *array*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/paymentmethods/getlist`

