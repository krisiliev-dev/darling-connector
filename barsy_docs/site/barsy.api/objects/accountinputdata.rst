.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

AccountInputData
======================================================================================
Входящи данни за сметка

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Accounts\\Data\\AccountInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$uuid**
     - *string*
     - 
     - Уникален номер на `сметка </barsy.help/210-dictionary/account.html>`__.

			Подходящ за избягване на дублиране на `сметка </barsy.help/210-dictionary/account.html>`__. Ако не е подаден ще се генерира автоматично

			 пример: "\"a03a2c31-0b06-46fa-ba01-764954c1f43c\""
   * - **$client_id**
     - *integer*
     - 1
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ по barsy - ако няма, търси се дали има обект client (виж по-надолу), ако го няма - записва се към Анонимен (ID:1)

			 пример: "1" ( виж: :doc:`../methods/clients/getlist` )
   * - **$client**
     - *ClientInputData*
     - 
     - Данни за `клиента </barsy.help/210-dictionary/client.html>`__ (ако е нов или трябва да бъде разпознат)
   * - **$person_id**
     - *int*
     - 
     - ID на `представител </barsy.help/210-dictionary/person.html>`__

			 пример: "1" ( виж: :doc:`../methods/persons/getlist` )
   * - **$person**
     - *PersonInputData*
     - 
     - Данни за `представителя </barsy.help/210-dictionary/person.html>`__ (ако е нов или трябва да бъде разпознат)
   * - **$place_id**
     - *int*
     - 
     - ID на място/маса/стая/...

			 пример: "1" ( виж: :doc:`../methods/places/getlist` )
   * - **$discount**
     - *float*
     - 0
     - Отстъпка върху цялата `сметка </barsy.help/210-dictionary/account.html>`__

			 пример: "-10"
   * - **$ref_date**
     - *string*
     - 
     - Дата на документално извършване на сделката

			 пример: "\"2018-01-10\""
   * - **$persons**
     - *int*
     - 
     - Брой хора (посетители) към тази `сметка </barsy.help/210-dictionary/account.html>`__

			 пример: "3"
   * - **$delivery_address**
     - *DeliveryAddressInputData*
     - 
     - Адрес за доставка за тази `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$contact_name**
     - *string*
     - 
     - Лице за контакт за тази `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$phone**
     - *string*
     - 
     - Телефон за контакт към тази `сметка </barsy.help/210-dictionary/account.html>`__

			 пример: "89123223723"
   * - **$account_alias**
     - *string*
     - 
     - Заглавие на `сметката </barsy.help/210-dictionary/account.html>`__.

			Използва се за лесно разпознаване на `сметка </barsy.help/210-dictionary/account.html>`__. Визуализира се в списъци със `сметки </barsy.help/210-dictionary/account.html>`__
   * - **$description**
     - *string*
     - 
     - Свободен текст.

			Може да съдържа някакви допълнително описание към цялата `сметка </barsy.help/210-dictionary/account.html>`__ - печати се на бележката

			 пример: "\"\\u0421\\u0432\\u043e\\u0431\\u043e\\u0434\\u043d\\u0438 \\u0431\\u0435\\u043b\\u0435\\u0436\\u043a\\u0438\""
   * - **$notes**
     - *string*
     - 
     - Свободен текст.

			Може да съдържа някакви допълнително описание към цялата `сметка </barsy.help/210-dictionary/account.html>`__ - НЕ се печати на бележката
   * - **$tracking_number**
     - *string*
     - 
     - Номер на товарителница

			 пример: "1234566"
   * - **$speditor_id**
     - *int*
     - 
     - ID на спедитор

			 пример: "1"
   * - **$delivery_zone_id**
     - *int*
     - 
     - ID на зона за доставка
   * - **$paid_due_date**
     - *string*
     - 
     - Отложено `плащане </barsy.help/210-dictionary/payment.html>`__ до

			 пример: "\"2018-09-01 10:45\""
   * - **$storno_data**
     - *InputStornoData*
     - 
     - Данни за `сметка </barsy.help/210-dictionary/account.html>`__, която се сторнира с този `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$deal_id**
     - *integer*
     - 
     - ID на сделка по barsy.

			*Използва се за групиране на операции в обща група (сделка)*

			 пример: "1" ( виж: :doc:`../methods/deals/getlist` )
   * - **$calculate_orders_discount_flag**
     - *int*
     - 
     - Флаг за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ на отстъпката от `сметка </barsy.help/210-dictionary/account.html>`__ към поръчки
   * - **$skip_account_discount_recalculate_flag**
     - *int*
     - 0
     - Сигнал дали да се прескочи прилагането на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ тип Отстъпка-`сметка </barsy.help/210-dictionary/account.html>`__.
   * - **$client_order_id**
     - *int*
     - 
     - 
   * - **$external_source**
     - *object* | *int* | *null*
     - 
     - 
   * - **$additional_data**
     - *object*
     - 
     - 
   * - **$reservation_id**
     - *int*
     - 
     - 
   * - **$lang_id**
     - *string*
     - 
     - ID на език за `сметката </barsy.help/210-dictionary/account.html>`__.

			Ще принтира имената на `артикулите </barsy.help/210-dictionary/article.html>`__ на посочения език в фискалната бележка (ако има зададени такива).

			 пример: "\"bg_BG\"" ( виж: :doc:`../methods/languages/getlist` )
   * - **$calculate_start_date**
     - *bool*
     - false
     - Дали да се изчислява START_SERVICE_DATE на новите поръчки при запис на `сметка </barsy.help/210-dictionary/account.html>`__.

			Важи само за ресторантски `сметки </barsy.help/210-dictionary/account.html>`__ (delivery_type = no). При false (по подразбиране) START_SERVICE_DATE остава NULL — поръчките са видими веднага. При true системата изчислява старт на услугата на база бача и order_service_date.
   * - **$order_service_date**
     - *string*
     - 
     - Желано време за изпълнение на поръчките от текущия бач (само за ресторантски `сметки </barsy.help/210-dictionary/account.html>`__, delivery_type = no).

			*Ако е зададено, системата проверява дали поръчките могат да бъдат готови до тогава. Ако не може — хвърля грешка с най-ранното възможно време. Не се записва в базата.*
   * - **$delivery_date**
     - *string*
     - 
     - Дата на доставка (Подава се от `клиента </barsy.help/210-dictionary/client.html>`__).

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
     - Курс на валутата

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/createfromclientorder`
	 * :doc:`../methods/accounts/create`
	 * :doc:`../methods/accounts/place`

Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__

