.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clients\\Data\\ClientData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_name**
     - *string*
     - 
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ - трябва да бъде уникално в цялата система.

			*Може да бъде физическото име или друго синтетично име*

			 пример: "\"\\u0418\\u0432\\u0430\\u043d \\u0418\\u0432\\u0430\\u043d\\u043e\\u0432\""
   * - **$discount**
     - *int*
     - 0
     - Процент отстъпка/надценка за всички операции на `клиента </barsy.help/210-dictionary/client.html>`__ (ако числото е отрицателно-> отстъпка; ако е положително>надценка)

			 пример: "10"
   * - **$tel**
     - *string*
     - 
     - Телефон за контакт

			 пример: "\"+359-88-987654321\""
   * - **$recom**
     - *string*
     - 
     - 

			 пример: "\"\\u041f\\u0435\\u0442\\u044a\\u0440 \\u041f\\u0435\\u0442\\u0440\\u043e\\u0432\""
   * - **$company_name**
     - *string*
     - 
     - Име на юридическото лице

			 пример: "\"\\u0418\\u0432\\u0430\\u043d\\u043e\\u0432 \\u0415\\u041e\\u041e\\u0414\""
   * - **$address**
     - *string*
     - 
     - Адрес по регистрация

			 пример: "\"\\u0433\\u0440. \\u0421\\u043e\\u0444\\u0438\\u044f \\u0443\\u043b. \\u041d\\u0438\\u043a\\u043e\\u043b\\u0430 \\u0413\\u0430\\u0431\\u0440\\u043e\\u0432\\u0441\\u043a\\u0438 108\""
   * - **$bulstat**
     - *string*
     - 
     - ЕИК номер (Булстат)

			 пример: "131362023"
   * - **$vat_num**
     - *string*
     - 
     - ДДС номер

			 пример: "\"BG131362023\""
   * - **$mol**
     - *string*
     - 
     - МОЛ

			 пример: "\"\\u0418\\u0432\\u0430\\u043d \\u041f\\u0435\\u0442\\u0440\\u043e\\u0432\""
   * - **$town**
     - *string*
     - 
     - Град

			 пример: "\"\\u0421\\u043e\\u0444\\u0438\\u044f\""
   * - **$zip**
     - *string*
     - 
     - Пощенски код

			 пример: "1700"
   * - **$delivery_address**
     - *DeliveryAddressData*
     - 
     - Адрес за доставка
   * - **$delivery_zone_id**
     - *string*
     - 
     - ID на зона за доставка
   * - **$client_create_date**
     - *datetime*
     - 
     - Дата на създаване на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$email**
     - *string*
     - 
     - Основен email на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "\"ivan@company.com\""
   * - **$email_invoices**
     - *string*
     - 
     - email за изпращане на `фактури </barsy.help/210-dictionary/invoice.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "\"invoices@company.com\""
   * - **$client_code**
     - *string*
     - 
     - Клиентски код (на карта)

			 пример: "\"aj3j8asn173bc91\""
   * - **$total_balance**
     - *float*
     - 0
     - Текущ баланс на клиентския портфейл
   * - **$credit_limit**
     - *float*
     - 
     - Кредитен лимит на `клиента </barsy.help/210-dictionary/client.html>`__ (стойност до която може да задлъжнява)

			 пример: "2000"
   * - **$paid_period**
     - *int*
     - 
     - Интервал от време(в минути) за отложено `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране

			 пример: "10080"
   * - **$allow_client_nocard**
     - *bool*
     - 1
     - Разрешено използване профила без карта

			 пример: "1"
   * - **$allow_credit_nocard**
     - *bool*
     - 1
     - Разрешено използване на клиентски портфейл без карта

			 пример: "1"
   * - **$allow_discount_nocard**
     - *bool*
     - 1
     - Разрешено използване на отстъпка без карта

			 пример: "1"
   * - **$group_id**
     - *int*
     - 1
     - Клиентска група, към която принадлежи `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1" ( виж: :doc:`../methods/clients/getgroups` )
   * - **$client_picture**
     - *string*
     - 
     - Основна снимка от наличните за този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$last_update**
     - *datetime*
     - 
     - Дата на последна актуализация на данните за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$description**
     - *string*
     - 
     - Описание - свободен текст
   * - **$user_id**
     - *int*
     - 
     - ID на потребиетля, създал `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$delete_flag**
     - *int*
     - 0
     - Флаг, дали `потребителя </barsy.help/210-dictionary/user.html>`__ е маркиран като изтрит
   * - **$client_auth**
     - *string*
     - 
     - Клиентско име за вход в клиентския профил
   * - **$client_pass**
     - *string*
     - 
     - Клиентска парола за вход в клиентския профил
   * - **$export_id**
     - *int*
     - 
     - ID за експорт към външни системи
   * - **$default_paymethod_id**
     - *int*
     - 
     - ID на предпочитан начин на `плащане </barsy.help/210-dictionary/payment.html>`__ за този `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: ``Paymethods`` )
   * - **$client_source_id**
     - *int*
     - 
     - ID на източника, от където е намерен този `клиент </barsy.help/210-dictionary/client.html>`__/контакт
   * - **$recruit_client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, осигурил този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$ml_subscribed**
     - *int*
     - 
     - Флаг дали `клиентът </barsy.help/210-dictionary/client.html>`__ е абониран за maillist
   * - **$delivery_data**
     - *object*
     - 
     - Обект с информация за доставката (key=>value, пр. "city"=>"London")
   * - **$receiver_name**
     - *string*
     - 
     - Име на получател
   * - **$is_guest**
     - *bool*
     - 0
     - Флаг за гост
   * - **$lang_id**
     - 
     - 
     - 
   * - **$session_timeout**
     - 
     - 30
     - 
   * - **$make_invoice_auto**
     - *int*
     - 
     - 
   * - **$send_invoice_auto**
     - *int*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientorders/create`
	 * :doc:`../methods/clientorders/update`
	 * :doc:`../methods/clients/getlist`
	 * :doc:`../methods/clients/get`
	 * :doc:`../methods/invoices/get_by_sid`
	 * :doc:`../methods/invoices/getlist`
	 * :doc:`../methods/invoices/get`

