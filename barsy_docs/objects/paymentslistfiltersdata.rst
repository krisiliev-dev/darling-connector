.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PaymentsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Payments\\Data\\PaymentsListFiltersData


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
   * - **$payment_id**
     - *int*
     - 
     - 

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, направил `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$account_id**
     - *int*
     - 
     - ID на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$user_id**
     - *int*
     - 
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, приел `плащането </barsy.help/210-dictionary/payment.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$unused**
     - *int*
     - 
     - Взема само плащания, които не са изполвани напълно

			 пример: "1"
   * - **$storno_available**
     - *int*
     - 
     - Взема само плащания, по които могат да се стонират суми

			 пример: "1"
   * - **$has_paid_sum**
     - *int*
     - 
     - Да има някаква платена сума

			 пример: "1"
   * - **$is_printed**
     - *int*
     - 
     - Дали `плащането </barsy.help/210-dictionary/payment.html>`__ е отпечатано/фискализирано

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/payments/getlist`

