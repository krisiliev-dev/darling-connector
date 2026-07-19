.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientOrderData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clientorders\\Data\\ClientOrderData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_order_id**
     - *int*
     - 
     - ID на `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__
   * - **$order_num**
     - *string*
     - 
     - Външен номер на `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ (различен от служебния)
   * - **$client_id**
     - *int*
     - 
     - Id на `клиент </barsy.help/210-dictionary/client.html>`__ по номенклатурата на barsy
   * - **$client_name**
     - *string*
     - 
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ от заявката
   * - **$client_tel**
     - *string*
     - 
     - Телефонен номер на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_email**
     - *string*
     - 
     - Email адрес на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$contact_name**
     - *string*
     - 
     - Лице за контакт/получаване - може да се различава от името на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$group_id**
     - *int*
     - 
     - ID на клиентска група, към която принадлежи `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/clients/getgroups` )
   * - **$create_date**
     - *string*
     - 
     - Дата на създаване на заявката
   * - **$last_update**
     - *string*
     - 
     - Дата на последна промяна на заявката
   * - **$barsy_id**
     - *int*
     - 
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който трябва да се изпрати поръчката за обработка
   * - **$barsy_name**
     - 
     - 
     - Име на търговския обект, в който трябва да се изпрати поръчката за обработка
   * - **$from_barsy_id**
     - *int*
     - 
     - ID на търговския обект, в който е създадена заявката ( виж: :doc:`../methods/barsys/getlist` )
   * - **$from_barsy_name**
     - *string*
     - 
     - Име на търговския обект, в който е създадена заявката ( виж: :doc:`../methods/barsys/getlist` )
   * - **$delivery_barsy_id**
     - *integer*
     - 
     - ID на търговския обект, от който ще се вземе поръчката.

			*Ако е пропуснато, се приема че ще се доставя до адрес за доставка* ( виж: :doc:`../methods/barsys/getlist` )
   * - **$delivery_barsy_name**
     - *string*
     - 
     - Име на търговския обект, от който ще се вземе поръчката.

			*Ако е пропуснато, се приема че ще се доставя до адрес за доставка*
   * - **$delivery_address**
     - *DeliveryAddressData*
     - 
     - Адрес за доставка
   * - **$delivery_date**
     - *datetime*
     - 
     - Дата за доставка, може да съдържа и час

			 пример: "\"2014-11-21 18:00:00\""
   * - **$delivery_date_until**
     - *string*
     - 
     - Крайна дата/час за доставка - оформя интервал за доставка - от ‘delivery_date’ до ‘delivery_date_until’
   * - **$delivery_interval**
     - *string*
     - 
     - 
   * - **$user_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал заявката
   * - **$user_name**
     - *string*
     - 
     - Потребителско име на създателя на заявката
   * - **$total_sum**
     - *float*
     - 
     - Обща сума на заявката (преди отстъпката)
   * - **$total_real**
     - *float*
     - 
     - Обща сума на заявката (след отстъпката)
   * - **$total_paid_sum**
     - *float*
     - 
     - Платена сума по заявката
   * - **$total_remain_sum**
     - *float*
     - 
     - Оставаща сума за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$discount**
     - *float*
     - 
     - Отстъпка на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$paymethod_id**
     - *integer*
     - 
     - ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ по номенклатура на barsy ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$preferred_paymethod_id**
     - *integer*
     - 
     - Предпочитан ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ по номенклатура на barsy ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$paymethod_name**
     - *string*
     - 
     - Име на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ на заявката ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$preferred_paymethod_name**
     - *string*
     - 
     - Име на предпочитан начина на `плащане </barsy.help/210-dictionary/payment.html>`__ на заявката ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$paymethod_public_name**
     - *string*
     - 
     - Публично име на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ на заявката ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$paymethod_description**
     - *string*
     - 
     - Описание на метода на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$extra_details**
     - *string*
     - 
     - Допълнителни детайли
   * - **$status_id**
     - *int*
     - 
     - ID на текущ статус на заявката ( виж: :doc:`../methods/clientorders/getstatuslistdata` )
   * - **$status_name**
     - *string*
     - 
     - Текущ статус на заявката ( виж: :doc:`../methods/clientorders/getstatuslistdata` )
   * - **$account_id**
     - *int*
     - 
     - ID на `сметка </barsy.help/210-dictionary/account.html>`__, създадена от тази `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ ( виж: :doc:`../methods/accounts/get` )
   * - **$description**
     - *string*
     - 
     - Свободен текст

			 пример: "\"\\u0421\\u0432\\u043e\\u0431\\u043e\\u0434\\u0435\\u043d \\u0442\\u0435\\u043a\\u0441\\u0442\""
   * - **$tracking_number**
     - *string*
     - 
     - Номер на товарителница
   * - **$deal_id**
     - *int*
     - 
     - ID на свързана сделка
   * - **$deal_title**
     - *string*
     - 
     - Заглавие на свързаната сделка
   * - **$person_id**
     - *int*
     - 
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ към `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$person_name**
     - *string*
     - 
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$speditor_id**
     - *int*
     - 
     - ID на спедитора, избран за тази заявка ( виж: :doc:`../methods/speditors/getlist` )
   * - **$article_count**
     - *int*
     - 
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в заявката
   * - **$can_edit_rows**
     - *int*
     - 
     - 
   * - **$ip_address**
     - *string*
     - 
     - IP адрес, от който е създадена заявката
   * - **$unp**
     - *string*
     - 
     - УНП на заявката
   * - **$user_rights**
     - *ClientOrderUserRightsData*
     - 
     - 
   * - **$with_invoice**
     - *int*
     - 
     - Флаг, дали `клиента </barsy.help/210-dictionary/client.html>`__ желае `фактура </barsy.help/210-dictionary/invoice.html>`__ за заявката
   * - **$public_notes**
     - *string*
     - 
     - Бележки към заявката, публично видими от `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_lang_id**
     - *string*
     - 
     - Предпочитан език за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$currency_id**
     - *int*
     - 
     - 
   * - **$currency_rate**
     - *float*
     - 
     - 
   * - **$client_order_sid**
     - *string*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientorders/getlist`
	 * :doc:`../methods/clientorders/get`

