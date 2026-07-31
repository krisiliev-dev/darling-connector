.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

AccountData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Accounts\\Data\\AccountData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$account_id**
     - *int*
     - 
     - ID на `сметка </barsy.help/210-dictionary/account.html>`__ - уникално за системата
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговските обект </barsy.help/210-dictionary/barsy.html>`__, в който е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$barsy_name**
     - *int*
     - 
     - Име на `търговските обект </barsy.help/210-dictionary/barsy.html>`__, в който е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$menu_id**
     - *int*
     - 
     - ID на каталог
   * - **$account_sid**
     - *int*
     - 
     - текстов идентификатор (ID) на `сметка </barsy.help/210-dictionary/account.html>`__ - уникално за системата
   * - **$create_date**
     - *string*
     - 
     - Дата на създаване на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$user_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, отговарящ текущо за `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$user_name**
     - *string*
     - 
     - Име на `потребител </barsy.help/210-dictionary/user.html>`__, отговарящ текущо за `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$place_id**
     - *int*
     - 
     - ID на място, към което е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$place_num**
     - *int*
     - 
     - Номер на място, към което е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$place_type**
     - *int*
     - 
     - ID на тип на мястото, към което е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$place_type_name**
     - *string*
     - 
     - Тип
   * - **$salon_name**
     - *string*
     - 
     - Име на салона, спрямо мястото
   * - **$status**
     - *int*
     - 
     - Статус на `сметката </barsy.help/210-dictionary/account.html>`__ (0=открира,1=закрита)
   * - **$is_locked**
     - *int*
     - 
     - Флаг за заключена `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$client_id**
     - *int*
     - 
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__, асоциран със `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$person_id**
     - *int*
     - 
     - ID на `представителя </barsy.help/210-dictionary/person.html>`__ за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$person_name**
     - *int*
     - 
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__ за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_name**
     - *string*
     - 
     - Име на `клиент </barsy.help/210-dictionary/client.html>`__, асоциран със `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$total_sum**
     - *float*
     - 
     - Пълен тотал на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$total_sum_curr**
     - *float*
     - 
     - 
   * - **$discount**
     - *float*
     - 
     - Процент отстъпка/надбавка на `сметката </barsy.help/210-dictionary/account.html>`__ (<0 отстъпка, >0 надбавка)
   * - **$skip_account_discount_recalculate_flag**
     - *int*
     - 0
     - Флаг дали да се прескочи прилагането на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ тип 3

			(Отстъпка-`сметка </barsy.help/210-dictionary/account.html>`__) върху DISCOUNT. Веднъж вдигнат, остава 1 за целия живот на `сметката </barsy.help/210-dictionary/account.html>`__ - правилото повече не се преприлага.
   * - **$close_date**
     - *string*
     - 
     - Дата на приключване на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$fx**
     - *int*
     - 
     - FX
   * - **$paymethod_id**
     - *string*
     - 
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$total_paid**
     - *float*
     - 
     - Общо платена сума по `сметката </barsy.help/210-dictionary/account.html>`__ спрямо плащанията
   * - **$total_paid_curr**
     - *float*
     - 
     - 
   * - **$total_real**
     - *float*
     - 
     - Сума на `сметката </barsy.help/210-dictionary/account.html>`__ с включена отстъпка/надбавка (т.е. краен тотал)
   * - **$total_real_curr**
     - *float*
     - 
     - 
   * - **$total_remain**
     - *float*
     - 
     - Сума на оттаващо за `плащане </barsy.help/210-dictionary/payment.html>`__ по тази `сметка </barsy.help/210-dictionary/account.html>`__ до този момент
   * - **$total_remain_curr**
     - *float*
     - 
     - 
   * - **$total_sum_after_row_discount**
     - *float*
     - 
     - Сума на `артикулите </barsy.help/210-dictionary/article.html>`__ с включена отстъпка на ниво поръчка
   * - **$total_sum_after_row_discount_curr**
     - *float*
     - 
     - 
   * - **$total_sum_storno**
     - *float*
     - 
     - Сума на сторнирани `артикули </barsy.help/210-dictionary/article.html>`__ (вкл. отстъпки)
   * - **$total_paid_sum_storno**
     - *float*
     - 
     - Сума на сторнирани плащания
   * - **$last_order_num**
     - *int*
     - 
     - Пореден номер на последна поръчка
   * - **$time_calculation**
     - *string*
     - 
     - Флаг за времево отчитане на мястото
   * - **$ref_date**
     - *string*
     - 
     - Документална дата на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$description**
     - *string*
     - 
     - Описание - свободен текст - видим в бележката към `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$notes**
     - *string*
     - 
     - Бележки - свободен текст - не се вижда от `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$account_alias**
     - *string*
     - 
     - Име на `сметката </barsy.help/210-dictionary/account.html>`__ - свободен текст
   * - **$delivery_address**
     - *DeliveryAddressData*
     - 
     - Данни за доставка
   * - **$contact_name**
     - *string*
     - 
     - Лице за контакт
   * - **$phone**
     - *string*
     - 
     - Телефон
   * - **$delivery_zone_id**
     - *string*
     - 
     - Зона за доставка
   * - **$tracking_number**
     - *string*
     - 
     - Номер на товарителница
   * - **$tracking_ref_id**
     - *string*
     - 
     - Номер на товарителница от външна система
   * - **$speditor_id**
     - *int*
     - 
     - ID на спедитора
   * - **$orders**
     - *OrderData*
     - 
     - Списък с `поръчките към сметката </barsy.help/210-dictionary/account-order.html>`__, групирани по `артикул </barsy.help/210-dictionary/article.html>`__, продажна цена, отстъпка, `модификатор </barsy.help/210-dictionary/modificator.html>`__, атрибути, ДДС (ако са поискани)
   * - **$orders_history**
     - *OrderData*
     - 
     - Списък с `поръчките към сметката </barsy.help/210-dictionary/account-order.html>`__ (ако са поискани)
   * - **$client_group_id**
     - *int*
     - 
     - ID на клиентска група
   * - **$pos_id**
     - *int*
     - 
     - 
   * - **$pos_name**
     - *string*
     - 
     - 
   * - **$close_pos_id**
     - *string*
     - 
     - 
   * - **$close_pos_name**
     - *string*
     - 
     - 
   * - **$period_id**
     - *int*
     - 
     - 
   * - **$persons**
     - *int*
     - 
     - Брой хора
   * - **$account_period**
     - *string*
     - 
     - Продължителност на `сметката </barsy.help/210-dictionary/account.html>`__ hh:mm:ss
   * - **$payment_name**
     - *string*
     - 
     - Начин на `плащането </barsy.help/210-dictionary/payment.html>`__ на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$paid_due_date**
     - *string*
     - 
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$account_num**
     - *string*
     - 
     - Пореден номер за текущия касов период
   * - **$unp**
     - *string*
     - 
     - Уникален номер на `продажбата </barsy.help/210-dictionary/sale.html>`__ (УНП) XXXХХХХХ-ZZZZ-0000001
   * - **$payments**
     - *PaymentGroupedData*
     - 
     - Списък със сумирани плащания по начин на `плащане </barsy.help/210-dictionary/payment.html>`__ към `сметката </barsy.help/210-dictionary/account.html>`__  (ако са поискани)
   * - **$payments_history**
     - *PaymentData*
     - 
     - Списък с всички плащания към `сметката </barsy.help/210-dictionary/account.html>`__  (ако са поискани)
   * - **$deal_id**
     - *int*
     - 
     - 
   * - **$deal_title**
     - *string*
     - 
     - 
   * - **$client_order_ids**
     - *string*
     - 
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ фигуриращи в `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$detailed_client_order_ids**
     - *string*
     - 
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ с дата на издаването им фигуриращи в `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$service_status_id**
     - *int*
     - 
     - Статус на обслужването на `сметката </barsy.help/210-dictionary/account.html>`__ - ID

			* **0** - *Липсва описание*
			* **1** - *Липсва описание*
			* **2** - *Липсва описание*
			* **3** - *Липсва описание*
			* **4** - *Липсва описание*
			* **5** - *Липсва описание*
			* **6** - *Липсва описание*
			* **100** - *Липсва описание*
   * - **$service_status_name**
     - *string*
     - 
     - Статус на обслужването на `сметката </barsy.help/210-dictionary/account.html>`__ - Име
   * - **$user_can_edit**
     - *bool*
     - 
     - Флаг дали текущия `потребител </barsy.help/210-dictionary/user.html>`__ може да редактира тази `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$additional_data**
     - *object*
     - 
     - 
   * - **$lang_id**
     - *string*
     - 
     - Език за `сметката </barsy.help/210-dictionary/account.html>`__ (в фискалната бележка ще има имената на `артикулите </barsy.help/210-dictionary/article.html>`__ и на посочения език )
   * - **$confirmation_output_screen_check**
     - *bool*
     - true
     - Проверка дали `сметката </barsy.help/210-dictionary/account.html>`__ може да се визуализира за потвърждение на екран-ът, който е отворена.
   * - **$preferred_paymethod_id**
     - *int*
     - 
     - 
   * - **$confirmation_outputs**
     - *object*
     - 
     - 
   * - **$delivery_date**
     - *string*
     - 
     - Дата на доставка (подадена от `клиента </barsy.help/210-dictionary/client.html>`__).

			 пример: "\"2025-09-01 10:45\""
   * - **$delivery_date_internal**
     - *string*
     - 
     - Дата на възможна доставка (изчислена от системата).

			 пример: "\"2025-09-01 10:45\""
   * - **$currency_id**
     - *int*
     - 
     - ID на валута.

			*Ако е оставена непопълнена, ще се вземе системната валута*

			 пример: "-1" ( виж: :doc:`../methods/currencies/getlist` )
   * - **$currency_rate**
     - *float*
     - 
     - Курс на валутата.

			*Ако остане непопълнена ще вземе валутата обвързана с currency_id*
   * - **$remote_id**
     - *int*
     - 
     - ID на отдалечена система ( виж: :doc:`../methods/remotesystems/getlist` )
   * - **$ref_id**
     - *int* | *string*
     - 
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__ в отдалчена система

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getbytaxes`
	 * :doc:`../methods/accounts/getlist`
	 * :doc:`../methods/accounts/get`
	 * :doc:`../methods/places/getlistwithaccountsonly`

