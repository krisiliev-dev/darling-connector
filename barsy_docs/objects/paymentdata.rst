.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PaymentData
======================================================================================
Данни за регистрирано плащане (приход или разход)

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Payments\\Data\\PaymentData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$operation**
     - *string*
     - 
     - Операция на `плащането </barsy.help/210-dictionary/payment.html>`__ (приход или разход)

			* **CRD** - *Приход*
			* **DBT** - *Разход*
   * - **$payment_id**
     - *int*
     - 
     - ID на `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../methods/barsys/getlist` )
   * - **$period_id**
     - *int*
     - 
     - ID на период (касова смяна)
   * - **$paymethod_id**
     - *int*
     - 
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$original_paid_sum**
     - *float*
     - 
     - Платена сума във валута на `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$paid_sum**
     - *float*
     - 
     - Платена сума в системна валута (изчислена от original_paid_sum и currency_rate)
   * - **$paid_used**
     - *float*
     - 
     - Използвана част от платената сума (асоциирана към `сметки </barsy.help/210-dictionary/account.html>`__, зареждания и др.)
   * - **$user_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, приел `плащането </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$client_id**
     - *int*
     - 
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__ (при приходни плащания) ( виж: :doc:`../methods/clients/getlist` )
   * - **$supplier_id**
     - *int*
     - 
     - ID на `доставчик </barsy.help/210-dictionary/supplier.html>`__ (при разходни плащания) ( виж: :doc:`../methods/suppliers/getlist` )
   * - **$create_date**
     - *string*
     - 
     - Дата на създаване на `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$ref_date**
     - *string*
     - 
     - Дата вальор (документна дата)
   * - **$delete_flag**
     - *int*
     - 
     - Флаг, дали `плащането </barsy.help/210-dictionary/payment.html>`__ е маркирано като изтрито

			* **0** - *активно*
			* **1** - *изтрито*
   * - **$fx**
     - *int*
     - 
     - Флаг, дали `плащането </barsy.help/210-dictionary/payment.html>`__ е фискално (извършва фискална операция)

			* **0** - *нефискално*
			* **1** - *фискално*
   * - **$confirmed**
     - *int*
     - 
     - Флаг за потвърдено `плащане </barsy.help/210-dictionary/payment.html>`__

			* **0** - *непотвърдено*
			* **1** - *потвърдено*
   * - **$ref_num**
     - *string*
     - 
     - Референтен номер (напр. банково извлечение)
   * - **$description**
     - *string*
     - 
     - Свободен текст / описание
   * - **$req_value**
     - *string*
     - 
     - Допълнителна информация към `плащането </barsy.help/210-dictionary/payment.html>`__ (настройва се в конкретния начин на `плащане </barsy.help/210-dictionary/payment.html>`__)
   * - **$payment_data**
     - *string* | *stdClass*
     - 
     - Допълнителни данни за `плащането </barsy.help/210-dictionary/payment.html>`__ (JSON обект)
   * - **$payment_print_data**
     - *string* | *stdClass*
     - 
     - Данни за печат на касова бележка (JSON обект)
   * - **$transaction_id**
     - *string*
     - 
     - Номер на транзакция (напр. от POS терминал)
   * - **$storno_sum**
     - *float*
     - 0
     - Сума на сторнираните плащания по това `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$storno_parent_id**
     - *int*
     - 
     - ID на родителско `плащане </barsy.help/210-dictionary/payment.html>`__ при сторно операция
   * - **$available_sum**
     - *float*
     - 
     - Неизползван остатък от платената сума
   * - **$currency_id**
     - *int*
     - 
     - ID на валута на `плащането </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../methods/currencies/getlist` )
   * - **$currency_rate**
     - *float*
     - 
     - Курс на валутата към момента на `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$provider_id**
     - *int*
     - 
     - ID на платежен оператор (VPOS, POS терминал и др.)
   * - **$type_id**
     - *int*
     - 
     - Тип на начина на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **-2** - *Служебен*
			* **-1** - *Неразпознат*
			* **1** - *В брой*
			* **2** - *Банка*
			* **3** - `Ваучер </barsy.help/210-dictionary/card.html>`__
			* **4** - *Чек*
			* **5** - *Карта (присъствена)*
			* **6** - *Карта (неприсъствена)*
			* **7** - *Други*
			* **8** - *Наложен платеж*
			* **9** - *Пощенски паричен превод*
			* **10** - barsy-`Ваучер </barsy.help/210-dictionary/card.html>`__ (фискален)
			* **11** - *Бонус програма*
			* **12** - barsy-`Ваучер </barsy.help/210-dictionary/card.html>`__ (нефискален)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getbytaxes`
	 * :doc:`../methods/accounts/getlist`
	 * :doc:`../methods/accounts/get`
	 * :doc:`../methods/places/getlistwithaccountsonly`

Виж също
--------

 * `Плащане </barsy.help/210-dictionary/payment.html>`__

