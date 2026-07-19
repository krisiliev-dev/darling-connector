.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PaymentGroupedData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Payments\\Data\\PaymentGroupedData


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
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$name**
     - *string*
     - 
     - Име на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$fx**
     - *string*
     - 
     - Флаг дали `плащането </barsy.help/210-dictionary/payment.html>`__ е фискално
   * - **$paid_sum**
     - *float*
     - 
     - Сума на плащанията от този начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$payments_count**
     - *float*
     - 
     - Сума на плащанията от този начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$export_id**
     - *string*
     - 
     - Export_id на методът за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$transaction_id**
     - *string*
     - 
     - Номер на трансакцията предоставена от пос терминала

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getbytaxes`
	 * :doc:`../methods/accounts/getlist`
	 * :doc:`../methods/accounts/get`
	 * :doc:`../methods/places/getlistwithaccountsonly`

