.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

InvoicesListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към даден документ. Всяка опция включва съответната колона

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*към данните за всеки документ от списъка. Основните данни (base) се връщат винаги, а останалите се включват при стойност true.*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Invoices\\Data\\InvoicesListExtraPropertiesData


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
   * - :category_header:`Основни данни`
     - 
     - 
     - 
   * - **$inv_id**
     - *bool*
     - true
     - ID на документа (различно от номера на документа)
   * - **$inv_num**
     - *bool*
     - true
     - Номер на документа
   * - **$type_id**
     - *bool*
     - true
     - ID на типа на документа (`фактура </barsy.help/210-dictionary/invoice.html>`__, проформа, кредитно/дебитно известие и др.)
   * - **$parent_num**
     - *bool*
     - true
     - Номер на родителския документ (документа, към който е издаден)
   * - **$is_anulate**
     - *bool*
     - true
     - Флаг дали документът е анулиран
   * - **$type_name**
     - *bool*
     - false
     - Наименование на типа на документа

			 пример: "1"
   * - **$uuid**
     - *bool*
     - false
     - Уникален идентификатор (UUID) на документа

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
     - 
   * - **$total**
     - *bool*
     - true
     - Обща сума на документа
   * - **$total_neto**
     - *bool*
     - true
     - Обща сума без ДДС (нето)
   * - **$total_dds**
     - *bool*
     - true
     - Обща сума на начисленото ДДС
   * - **$total_all**
     - *bool*
     - true
     - Крайна сума за `плащане </barsy.help/210-dictionary/payment.html>`__ (с ДДС)
   * - **$discount**
     - *bool*
     - false
     - Отстъпка по документа

			 пример: "1"
   * - **$payments_paid_sum**
     - *bool*
     - false
     - Платена сума по документа

			сборът от плащанията по свързаните `сметки </barsy.help/210-dictionary/account.html>`__. Сравнена с крайната сума (total_all) показва дали документът е платен, частично платен или неплатен. Връща null/0, ако няма свързани плащания

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
     - *bool*
     - true
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, за когото е издаден документът ( виж: :doc:`../methods/clients/get` , :doc:`../methods/clients/getlist` )
   * - **$paymethod_id**
     - *bool*
     - true
     - ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$receiver_id**
     - *bool*
     - true
     - ID на получателя (`фирма </barsy.help/210-dictionary/company.html>`__) на документа
   * - **$client_name**
     - *bool*
     - false
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ по документа

			 пример: "1"
   * - **$seller_id**
     - *bool*
     - false
     - ID на продавача

			 пример: "1"
   * - **$bank_account_id**
     - *bool*
     - false
     - ID на банковата `сметка </barsy.help/210-dictionary/account.html>`__ на получателя

			 пример: "1"
   * - **$receiver_name**
     - *bool*
     - false
     - Име на получателя на документа

			 пример: "1"
   * - **$seller_bank_account_id**
     - *bool*
     - false
     - ID на банковата `сметка </barsy.help/210-dictionary/account.html>`__ на продавача

			 пример: "1"
   * - **$barsy_id**
     - *bool*
     - false
     - ID на търговския обект, издал документа

			 пример: "1" ( виж: :doc:`../methods/barsys/get` , :doc:`../methods/barsys/getlist` )
   * - **$seller_company_id**
     - *bool*
     - false
     - ID на `фирмата </barsy.help/210-dictionary/company.html>`__-продавач

			 пример: "1" ( виж: :doc:`../methods/companies/get` , :doc:`../methods/companies/getlist` )
   * - **$user_id**
     - *bool*
     - false
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа

			 пример: "1" ( виж: :doc:`../methods/users/get` , :doc:`../methods/users/getlist` )
   * - **$seller_name**
     - *bool*
     - false
     - Име на продавача

			 пример: "1"
   * - **$seller_code**
     - *bool*
     - false
     - Код на продавача

			 пример: "1"
   * - **$email**
     - *bool*
     - false
     - Имейл за изпращане на документа към `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
     - 
   * - **$term_date**
     - *bool*
     - true
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$additional_text**
     - *bool*
     - true
     - Допълнителен текст към документа
   * - **$free_text**
     - *bool*
     - true
     - Свободен текст към документа
   * - **$create_date**
     - *bool*
     - true
     - Дата на създаване на документа
   * - **$with_tax**
     - *bool*
     - false
     - Флаг дали документът е с включено ДДС

			 пример: "1"
   * - **$payment_date**
     - *bool*
     - false
     - Дата на `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "1"
   * - **$produce_date**
     - *bool*
     - false
     - Дата на издаване (данъчно събитие)

			 пример: "1"
   * - **$last_update**
     - *bool*
     - false
     - Дата на последна промяна на документа

			 пример: "1"
   * - **$export_id**
     - *bool*
     - false
     - ID за експорт, свързано с начина на `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "1"
   * - **$remote_system**
     - *bool*
     - false
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__, обвързана с документа в отдалечената система.

			*Изисква филтър "remote_id"*

			 пример: "1"
   * - **$remote_accounts**
     - *bool*
     - false
     - Референция на `сметката </barsy.help/210-dictionary/account.html>`__ в отдалечената система.

			*Изисква филтър "remote_id"*

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
     - 
   * - **$payment_ids**
     - *bool*
     - false
     - Списък с ID-та на плащанията по документа

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
     - 
   * - **$is_paid**
     - *bool*
     - false
     - Дали документът е напълно платен — платената сума по свързаните `сметки </barsy.help/210-dictionary/account.html>`__ покрива крайната сума (total_all)

			 пример: "1"
   * - **$payments_remain**
     - *bool*
     - false
     - Остатък за `плащане </barsy.help/210-dictionary/payment.html>`__ — крайната сума (total_all) минус платената сума по свързаните `сметки </barsy.help/210-dictionary/account.html>`__.

			*Стойност <= 0 означава напълно платен документ*

			 пример: "1"
   * - **$paymethod_name**
     - *bool*
     - false
     - Име на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ (с приоритет на версията на начина на `плащане </barsy.help/210-dictionary/payment.html>`__)

			 пример: "1"
   * - **$payment_type_id**
     - *bool*
     - false
     - Тип на `плащането </barsy.help/210-dictionary/payment.html>`__

			 пример: "1"
   * - **$parent_inv_id**
     - *bool*
     - false
     - ID на родителския документ (документа, по който е издаден този)

			 пример: "1" ( виж: :doc:`../methods/invoices/get` )
   * - **$barsy_name**
     - *bool*
     - false
     - Име на търговския обект, издал документа

			 пример: "1"
   * - **$seller_pop_name**
     - *bool*
     - false
     - POP име на продавача (`фирмата </barsy.help/210-dictionary/company.html>`__-издател)

			 пример: "1"
   * - **$currency_id**
     - *bool*
     - false
     - ID на валутата на документа

			 пример: "1" ( виж: :doc:`../methods/currencies/get` , :doc:`../methods/currencies/getlist` )
   * - **$currency_rate**
     - *bool*
     - false
     - Курс на валутата на документа спрямо системната валута

			 пример: "1"
   * - **$person_id**
     - *bool*
     - false
     - ID на лицето за контакт по документа

			 пример: "1" ( виж: :doc:`../methods/persons/get` , :doc:`../methods/persons/getlist` )
   * - **$person_name**
     - *bool*
     - false
     - Име на лицето за контакт по документа

			 пример: "1"
   * - **$deal_id**
     - *bool*
     - false
     - ID на сделката, към която е документът

			 пример: "1" ( виж: :doc:`../methods/deals/getlist` )
   * - **$deal_title**
     - *bool*
     - false
     - Наименование на сделката, към която е документът

			 пример: "1" ( виж: :doc:`../methods/deals/getlist` )
   * - **$linked_accounts_num**
     - *bool*
     - false
     - Брой `сметки </barsy.help/210-dictionary/account.html>`__, свързани с документа

			 пример: "1"
   * - **$client_order_ids**
     - *bool*
     - false
     - Списък с номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__, фигуриращи в документа

			 пример: "1"
   * - **$detailed_client_order_ids**
     - *bool*
     - false
     - Списък с номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ и датите им на издаване, фигуриращи в документа

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/invoices/getlist`

