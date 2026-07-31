.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientInputData
======================================================================================
Данни за създаване или актуализиране на client

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clients\\Data\\ClientInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_name**
     - *string*
     - 
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ - трябва да бъде уникално в цялата система.

			*Може да бъде физическото име или друго синтетично име*

			 пример: "\"\\u0418\\u0432\\u0430\\u043d \\u0418\\u0432\\u0430\\u043d\\u043e\\u0432\""
   * - **$discount**
     - *string*
     - 0
     - Процент отстъпка/надценка за всички операции на `клиента </barsy.help/210-dictionary/client.html>`__ (ако числото е отрицателно-> отстъпка; ако е положително>надценка)

			 пример: "10"
   * - **$delete_flag**
     - *int*
     - 0
     - Флаг, дали `потребителя </barsy.help/210-dictionary/user.html>`__ е маркиран като изтрит

			 пример: "1"
   * - **$description**
     - *string*
     - 
     - Описание - свободен текст

			 пример: "\"\\\"test description\\\"\""
   * - **$tel**
     - *string*
     - 
     - Телефон за контакт

			 пример: "\"+359-88-987654321\""
   * - **$fax**
     - *string*
     - 
     - Факс за контакт

			 пример: "885345243"
   * - **$recom**
     - *string*
     - 
     - Препоръчан от

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
   * - **$client_code**
     - *string*
     - 
     - Клиентски код (на карта)

			 пример: "\"az3h8asn173bc91\""
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
   * - **$email**
     - *string*
     - 
     - Основен email на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "\"ivan@company.com\""
   * - **$credit_limit**
     - *float*
     - 
     - Кредитен лимит на `клиента </barsy.help/210-dictionary/client.html>`__ (стойност до която може да задлъжнява)

			 пример: "2000"
   * - **$allow_client_nocard**
     - *int*
     - 1
     - Разрешено използване профила без карта

			 пример: "1"
   * - **$allow_credit_nocard**
     - *int*
     - 1
     - Разрешено използване на клиентски портфейл без карта

			 пример: "1"
   * - **$allow_discount_nocard**
     - *int*
     - 1
     - Разрешено използване на отстъпка без карта

			 пример: "1"
   * - **$group_id**
     - *int*
     - 
     - Клиентска група, към която принадлежи `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1" ( виж: :doc:`../methods/clients/getgroups` )
   * - **$default_paymethod_id**
     - *int*
     - 
     - ID на предпочитан начин на `плащане </barsy.help/210-dictionary/payment.html>`__ за този `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$export_id**
     - *string*
     - 
     - ID за експорт към външни системи

			 пример: "3454"
   * - **$client_picture**
     - *string*
     - 
     - Основна снимка от наличните за този `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "\"client_picture.jpg\""
   * - **$client_pass**
     - *string*
     - 
     - Клиентска парола за вход в клиентския профил

			 пример: "\"q33r4\""
   * - **$client_auth**
     - *string*
     - 
     - Клиентско име за вход в клиентския профил

			 пример: "\"ivan\""
   * - **$client_source_id**
     - *int*
     - 
     - ID на източника, от където е намерен този `клиент </barsy.help/210-dictionary/client.html>`__/контакт.

			 пример: "323"
   * - **$recruit_client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, осигурил този `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "23"
   * - **$agent_client_id**
     - *int*
     - 
     - ID на агента, към който е този `клиент </barsy.help/210-dictionary/client.html>`__/контакт.

			 пример: "32"
   * - **$email_invoices**
     - *string*
     - 
     - Email за изпращане на `фактури </barsy.help/210-dictionary/invoice.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "\"invoices@company.com\""
   * - **$delivery_zone_id**
     - *int*
     - 
     - ID на зона за доставка
   * - **$ml_subscribed**
     - *int*
     - -2
     - Флаг дали `клиентът </barsy.help/210-dictionary/client.html>`__ е абониран за maillist

			 пример: "-2"
   * - **$paid_period**
     - *int*
     - 
     - Интервал от време(в минути) за отложено `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране

			 пример: "1000"
   * - **$receiver_name**
     - *string*
     - 
     - Име на получател

			 пример: "\"\\u0418\\u0432\\u0430\\u043d \\u041f\\u0435\\u0442\\u0440\\u043e\\u0432\""
   * - **$is_guest**
     - *int*
     - 0
     - Флаг за гост

			 пример: "0"
   * - **$delivery_address**
     - *DeliveryAddressInputData*
     - 
     - Адрес за доставка
   * - **$barsys**
     - *array*
     - 
     - Масив от ID-та на обекти, в които този `клиент </barsy.help/210-dictionary/client.html>`__ може да се ползва

			 пример: "[1,3,4]"
   * - **$default_person_id**
     - *int*
     - 
     - 
   * - **$bank_accounts**
     - *array*
     - 
     - 
   * - **$weight**
     - *int*
     - 
     - Подреба/тежест на `клиентите </barsy.help/210-dictionary/client.html>`__

			 пример: "9"
   * - **$client_color**
     - *string*
     - 
     - Цвят за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$gln**
     - *string*
     - 
     - GLN (Global Location Number) — 13-цифрен GS1 идентификатор на юридическото лице.

			*Ползва се за EDI обмен (Buyer/ILN в ORDER/INVOICE/DESADV документите)*

			 пример: "3800131391087"
   * - **$edi_supplier_code**
     - *string*
     - 
     - Номер на `доставчик </barsy.help/210-dictionary/supplier.html>`__ — кодът на нашата `фирма </barsy.help/210-dictionary/company.html>`__ в системата на този `клиент </barsy.help/210-dictionary/client.html>`__ (верига).

			*В EDI документите това е Seller/CodeByBuyer. Излиза и в печатните бланки*

			 пример: "11836"
   * - **$make_invoice_auto**
     - *int*
     - 
     - Автоматично създаване на `фактура </barsy.help/210-dictionary/invoice.html>`__ при постъпване на `плащане </barsy.help/210-dictionary/payment.html>`__ с VPOS: NULL (според групата), 0 (изключено), 1 (включено)
   * - **$send_invoice_auto**
     - *int*
     - 
     - Автоматично изпращане на `фактура </barsy.help/210-dictionary/invoice.html>`__ при генериране на такава: NULL (според групата), 0 (изключено), 1 (включено)
   * - **$lang_id**
     - *string*
     - 
     - Предпочитан език

			 пример: "\"en_US\""

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/createfromclientorder`
	 * :doc:`../methods/accounts/create`
	 * :doc:`../methods/accounts/place`
	 * :doc:`../methods/clients/create`
	 * :doc:`../methods/clients/update`
	 * :doc:`../methods/reservations/create`
	 * :doc:`../methods/reservations/update`

