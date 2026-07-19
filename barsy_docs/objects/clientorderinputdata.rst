.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientOrderInputData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clientorders\\Data\\ClientOrderInputData


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
     - Вътрешно ID на `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__.

			*Ако не се подаде, ще се вземе следващия пореден (препоръчително да не се подава насилствено поради риск от колизия)*
   * - **$order_num**
     - *string*
     - 
     - Външен номер на `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ (различен от вътрешния)

			 пример: "3547"
   * - **$client**
     - *ClientData*
     - 
     - Данни за нов `клиент </barsy.help/210-dictionary/client.html>`__ - ще бъде създаден или преизползван (ако съществува според настройката за уникалност на `клиентите </barsy.help/210-dictionary/client.html>`__)
   * - **$client_id**
     - *int*
     - 1
     - Id на `клиент </barsy.help/210-dictionary/client.html>`__ по номенклатурата на barsy (ако не са подадени данни за `клиента </barsy.help/210-dictionary/client.html>`__)

			 пример: "1"
   * - **$person_id**
     - *int*
     - 
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ към `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/persons/getlist` )
   * - **$contact_name**
     - *string*
     - 
     - Лице за контакт/получаване - може да се различава от името на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "\"\\u0412\\u0430\\u0441\\u0438\\u043b \\u041f\\u0435\\u0442\\u0440\\u043e\\u0432\""
   * - **$client_email**
     - *string*
     - 
     - email на получателя - може да се различава от името на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "\"vasil@petrov.com\""
   * - **$client_tel**
     - *string*
     - 
     - телефон на получателя - може да се различава от името на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "\"+359-88-7654321\""
   * - **$discount**
     - *float*
     - 0
     - Отстъпка в проценти върху цялата поръчка

			 пример: "0"
   * - **$barsy_id**
     - *int*
     - 
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който се обработка поръчката в момента ( виж: :doc:`../methods/barsys/getlist` )
   * - **$delivery_barsy_id**
     - *integer*
     - 
     - ID на търговския обект, от който ще се вземе поръчката.

			*Ако е пропуснато, се приема че ще се доставя до адрес, описан по-долу*

			 пример: "1"
   * - **$delivery_address**
     - *DeliveryAddressInputData*
     - 
     - Адрес за доставка
   * - **$delivery_date**
     - *datetime*
     - 
     - Дата за доставка, може да съдържа и час

			 пример: "\"2014-11-21 18:00:00\""
   * - **$delivery_date_until**
     - *datetime*
     - 
     - Крайна дата/час за доставка - оформя интервал за доставка - от ‘delivery_date’ до ‘delivery_date_until’

			 пример: "\"2014-11-21 19:00:00\""
   * - :deprecated:`$paymethod_id`
     - *integer*
     - 
     - ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ по номенклатура на barsy :deprecated_text:`Отхвърлено: Директното подаване на начин на плащане не е коректно. То се изчислява автоматично по подадените плащания. При нужда от свободна стойнсот може да се използва $preferred_paymethod_id`

			 пример: "1"
   * - **$preferred_paymethod_id**
     - *integer*
     - 
     - Предпочитан ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ по номенклатура на barsy

			 пример: "1"
   * - **$description**
     - *string*
     - 
     - Свободен текст

			 пример: "\"\\u0421\\u0432\\u043e\\u0431\\u043e\\u0434\\u0435\\u043d \\u0442\\u0435\\u043a\\u0441\\u0442\""
   * - **$tracking_number**
     - *string*
     - 
     - Номер на товарителница
   * - **$status_id**
     - *int*
     - 
     - ID на статус на поръчката (по подразбиране - Нова) ( виж: :doc:`../methods/clientorders/getstatuslistdata` )
   * - **$extra_details**
     - *object*
     - 
     - Обект, съдържащ допълнителни данни за поръчката ( виж: :doc:`../methods/forms/get` )
   * - **$with_invoice**
     - *int*
     - 0
     - Флаг за желание за издаване на `фактура </barsy.help/210-dictionary/invoice.html>`__ след приключване на `сметката </barsy.help/210-dictionary/account.html>`__ от `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__

			* **0** - без `фактура </barsy.help/210-dictionary/invoice.html>`__
			* **1** - С `фактура </barsy.help/210-dictionary/invoice.html>`__

			 пример: "1"
   * - **$public_notes**
     - *string*
     - 
     - Публични бележки / коментар от `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "\"\\u041f\\u043e \\u0432\\u044a\\u0437\\u043c\\u043e\\u0436\\u043d\\u043e\\u0441\\u0442 \\u0434\\u0430 \\u0441\\u0435 \\u0434\\u043e\\u0441\\u0442\\u0430\\u0432\\u0438 \\u0432 \\u041f\\u0435\\u0442\\u044a\\u043a\""
   * - **$paid_due_date**
     - *string*
     - 
     - Дата/Сток за `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "\"2020-01-01 00:00:00\""
   * - **$deal_id**
     - *int*
     - 
     - ID на свързана сделка
   * - **$speditor_id**
     - *int*
     - 
     - ID на Спедитор ( виж: :doc:`../methods/speditors/getlist` )
   * - **$currency_id**
     - *int*
     - 
     - ID на валута, в която са подадени единичните цени на `артикулите </barsy.help/210-dictionary/article.html>`__.

			*Ако е оставена непопълнена, ще се вземе системната валута* ( виж: :doc:`../methods/currencies/getlist` )
   * - **$currency_rate**
     - *float*
     - 
     - Курс на валутата
   * - **$ip_address**
     - *string*
     - 
     - IP адрес на `клиента </barsy.help/210-dictionary/client.html>`__, от който е направена поръчка

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientorders/create`
	 * :doc:`../methods/clientorders/update`

