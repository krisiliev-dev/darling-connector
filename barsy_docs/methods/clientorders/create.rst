.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Clientorders_create
===========================================================
Създаване на клиентска заявка

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/client-order </barsy.help/210-dictionary/client-order.html>`__
	 * barsy.help: `110-admin/160-pos/client-orders/index </barsy.help/110-admin/160-pos/client-orders/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира нова `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ (предварителна поръчка от `клиент </barsy.help/210-dictionary/client.html>`__ за бъдеща обработка) с основните й данни — `клиент </barsy.help/210-dictionary/client.html>`__, обект на изпълнение, дата на доставка/обслужване, метод на доставка, адрес, бележки. Към заявката могат да се прикрепят редове с поръчвани `артикули </barsy.help/210-dictionary/article.html>`__ (количества, единични цени, отстъпки, `модификатори </barsy.help/210-dictionary/modificator.html>`__) и постъпили авансови плащания (капаро, депозит). Заявката е независима от `сметка </barsy.help/210-dictionary/account.html>`__/`каса </barsy.help/210-dictionary/pos.html>`__ — тя става "`сметка </barsy.help/210-dictionary/account.html>`__" чак при действителното й изпълнение.

Типични случаи: онлайн поръчка от уебсайт/мобилно приложение, поръчка по телефон за доставка, кетъринг заявка с дата на изпълнение в бъдеще, `резервация </barsy.help/210-dictionary/reservation.html>`__ с предварително `плащане </barsy.help/210-dictionary/payment.html>`__. След създаването могат да се изпратят webhook събития към интеграции (например `доставчик </barsy.help/210-dictionary/supplier.html>`__).

**Име**: Clientorders_create
**Категория**: Cashdesk,Top


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$order**
     - ClientOrderInputData_ 
     - Всички основни данни за заявката
   * - **$rows**
     - ClientOrderInputRowData_ []
     - Поръчки към заявката **По подразбиране:** []
   * - **$payments**
     - PaymentInputData_ []
     - Плащания, направени по `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__ **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на направената поръчка
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ClientOrderInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientOrderInputData

   * - Параметър
     - Тип
     - Описание
   * - **$client_order_id**
     - *int*
     - Вътрешно ID на `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__.

			*Ако не се подаде, ще се вземе следващия пореден (препоръчително да не се подава насилствено поради риск от колизия)*
   * - **$order_num**
     - *string*
     - Външен номер на `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ (различен от вътрешния)
   * - **$client**
     - ClientData_ 
     - Данни за нов `клиент </barsy.help/210-dictionary/client.html>`__ - ще бъде създаден или преизползван (ако съществува според настройката за уникалност на `клиентите </barsy.help/210-dictionary/client.html>`__)
   * - **$client_id**
     - *int*
     - Id на `клиент </barsy.help/210-dictionary/client.html>`__ по номенклатурата на barsy (ако не са подадени данни за `клиента </barsy.help/210-dictionary/client.html>`__) **По подразбиране:** 1
   * - **$person_id**
     - *int*
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ към `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../persons/getlist` )
   * - **$contact_name**
     - *string*
     - Лице за контакт/получаване - може да се различава от името на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_email**
     - *string*
     - email на получателя - може да се различава от името на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_tel**
     - *string*
     - телефон на получателя - може да се различава от името на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$discount**
     - *float*
     - Отстъпка в проценти върху цялата поръчка **По подразбиране:** 0
   * - **$barsy_id**
     - *int*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който се обработка поръчката в момента ( виж: :doc:`../barsys/getlist` )
   * - **$delivery_barsy_id**
     - *integer*
     - ID на търговския обект, от който ще се вземе поръчката.

			*Ако е пропуснато, се приема че ще се доставя до адрес, описан по-долу*
   * - **$delivery_address**
     - DeliveryAddressInputData_ 
     - Адрес за доставка
   * - **$delivery_date**
     - *datetime*
     - Дата за доставка, може да съдържа и час
   * - **$delivery_date_until**
     - *datetime*
     - Крайна дата/час за доставка - оформя интервал за доставка - от ‘delivery_date’ до ‘delivery_date_until’
   * - :deprecated:`$paymethod_id`
     - *integer*
     - ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ по номенклатура на barsy :deprecated_text:`Отхвърлено: Директното подаване на начин на плащане не е коректно. То се изчислява автоматично по подадените плащания. При нужда от свободна стойнсот може да се използва $preferred_paymethod_id`
   * - **$preferred_paymethod_id**
     - *integer*
     - Предпочитан ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ по номенклатура на barsy
   * - **$description**
     - *string*
     - Свободен текст
   * - **$tracking_number**
     - *string*
     - Номер на товарителница
   * - **$status_id**
     - *int*
     - ID на статус на поръчката (по подразбиране - Нова) ( виж: :doc:`../clientorders/getstatuslistdata` )
   * - **$extra_details**
     - *object*
     - Обект, съдържащ допълнителни данни за поръчката ( виж: :doc:`../forms/get` )
   * - **$with_invoice**
     - *int*
     - Флаг за желание за издаване на `фактура </barsy.help/210-dictionary/invoice.html>`__ след приключване на `сметката </barsy.help/210-dictionary/account.html>`__ от `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__

			* **0** - без `фактура </barsy.help/210-dictionary/invoice.html>`__
			* **1** - С `фактура </barsy.help/210-dictionary/invoice.html>`__ **По подразбиране:** 0
   * - **$public_notes**
     - *string*
     - Публични бележки / коментар от `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$paid_due_date**
     - *string*
     - Дата/Сток за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$deal_id**
     - *int*
     - ID на свързана сделка
   * - **$speditor_id**
     - *int*
     - ID на Спедитор ( виж: :doc:`../speditors/getlist` )
   * - **$currency_id**
     - *int*
     - ID на валута, в която са подадени единичните цени на `артикулите </barsy.help/210-dictionary/article.html>`__.

			*Ако е оставена непопълнена, ще се вземе системната валута* ( виж: :doc:`../currencies/getlist` )
   * - **$currency_rate**
     - *float*
     - Курс на валутата
   * - **$ip_address**
     - *string*
     - IP адрес на `клиента </barsy.help/210-dictionary/client.html>`__, от който е направена поръчка

-----

ClientData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientData

   * - Параметър
     - Тип
     - Описание
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_name**
     - *string*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ - трябва да бъде уникално в цялата система.

			*Може да бъде физическото име или друго синтетично име*
   * - **$discount**
     - *int*
     - Процент отстъпка/надценка за всички операции на `клиента </barsy.help/210-dictionary/client.html>`__ (ако числото е отрицателно-> отстъпка; ако е положително>надценка) **По подразбиране:** 0
   * - **$tel**
     - *string*
     - Телефон за контакт
   * - **$recom**
     - *string*
     - 
   * - **$company_name**
     - *string*
     - Име на юридическото лице
   * - **$address**
     - *string*
     - Адрес по регистрация
   * - **$bulstat**
     - *string*
     - ЕИК номер (Булстат)
   * - **$vat_num**
     - *string*
     - ДДС номер
   * - **$mol**
     - *string*
     - МОЛ
   * - **$town**
     - *string*
     - Град
   * - **$zip**
     - *string*
     - Пощенски код
   * - **$delivery_address**
     - DeliveryAddressData_ 
     - Адрес за доставка
   * - **$delivery_zone_id**
     - *string*
     - ID на зона за доставка
   * - **$client_create_date**
     - *datetime*
     - Дата на създаване на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$email**
     - *string*
     - Основен email на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$email_invoices**
     - *string*
     - email за изпращане на `фактури </barsy.help/210-dictionary/invoice.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_code**
     - *string*
     - Клиентски код (на карта)
   * - **$total_balance**
     - *float*
     - Текущ баланс на клиентския портфейл **По подразбиране:** 0
   * - **$credit_limit**
     - *float*
     - Кредитен лимит на `клиента </barsy.help/210-dictionary/client.html>`__ (стойност до която може да задлъжнява)
   * - **$paid_period**
     - *int*
     - Интервал от време(в минути) за отложено `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране
   * - **$allow_client_nocard**
     - *bool*
     - Разрешено използване профила без карта **По подразбиране:** 1
   * - **$allow_credit_nocard**
     - *bool*
     - Разрешено използване на клиентски портфейл без карта **По подразбиране:** 1
   * - **$allow_discount_nocard**
     - *bool*
     - Разрешено използване на отстъпка без карта **По подразбиране:** 1
   * - **$group_id**
     - *int*
     - Клиентска група, към която принадлежи `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getgroups` ) **По подразбиране:** 1
   * - **$client_picture**
     - *string*
     - Основна снимка от наличните за този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$last_update**
     - *datetime*
     - Дата на последна актуализация на данните за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$description**
     - *string*
     - Описание - свободен текст
   * - **$user_id**
     - *int*
     - ID на потребиетля, създал `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$delete_flag**
     - *int*
     - Флаг, дали `потребителя </barsy.help/210-dictionary/user.html>`__ е маркиран като изтрит **По подразбиране:** 0
   * - **$client_auth**
     - *string*
     - Клиентско име за вход в клиентския профил
   * - **$client_pass**
     - *string*
     - Клиентска парола за вход в клиентския профил
   * - **$export_id**
     - *int*
     - ID за експорт към външни системи
   * - **$default_paymethod_id**
     - *int*
     - ID на предпочитан начин на `плащане </barsy.help/210-dictionary/payment.html>`__ за този `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: ``Paymethods`` )
   * - **$client_source_id**
     - *int*
     - ID на източника, от където е намерен този `клиент </barsy.help/210-dictionary/client.html>`__/контакт
   * - **$recruit_client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, осигурил този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$ml_subscribed**
     - *int*
     - Флаг дали `клиентът </barsy.help/210-dictionary/client.html>`__ е абониран за maillist
   * - **$delivery_data**
     - *object*
     - Обект с информация за доставката (key=>value, пр. "city"=>"London")
   * - **$receiver_name**
     - *string*
     - Име на получател
   * - **$is_guest**
     - *bool*
     - Флаг за гост **По подразбиране:** 0
   * - **$lang_id**
     - 
     - 
   * - **$session_timeout**
     - 
     -  **По подразбиране:** 30
   * - **$make_invoice_auto**
     - *int*
     - 
   * - **$send_invoice_auto**
     - *int*
     - 

-----

DeliveryAddressData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Съдържа всички данни за адреса на `клиент </barsy.help/210-dictionary/client.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: DeliveryAddressData

   * - Параметър
     - Тип
     - Описание
   * - **$delivery_type**
     - *string*
     - Тип на доставката

			* **no** - *Без доставка*
			* **home** - *За вкъщи*
			* **address** - *Доставка до адрес*
			* **barsy** - Получаване от `търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **office** - *Получаване от офис на куриер* **По подразбиране:** 'no'
   * - **$country_name**
     - *string*
     - Име на държава
   * - **$country_id**
     - *string*
     - ID на държава
   * - **$dest_id**
     - *int*
     - ID на населено място ( виж: :doc:`../destinations/getlist` )
   * - **$address**
     - *string*
     - Адрес за доставка (кв,бул/ул,№,бл,вх,ет)
   * - **$address_neighborhood**
     - *string*
     - Квартал на адреса за доставка
   * - **$address_number**
     - *string*
     - Номер на улица/булевард за доставка
   * - **$address_building**
     - *string*
     - Блок за доставка
   * - **$address_entry**
     - *string*
     - Вход на блок за доставка
   * - **$address_floor**
     - *string*
     - Номер на етаж за доставка
   * - **$address_ap**
     - *string*
     - Номер на апартамент за доставка
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (ако типа на доставката е "Взимане от `търговски обект </barsy.help/210-dictionary/barsy.html>`__") ( виж: :doc:`../barsys/getlist` )
   * - **$speditor_id**
     - *int*
     - ID на спедитор ( виж: :doc:`../speditors/getlist` )
   * - **$office_id**
     - *int*
     - ID на офис на куриер по номенклатурата на съответния куриер ( виж: :doc:`../speditors/getofficelist` )
   * - **$office_type**
     - *string*
     - 
   * - **$coords**
     - *string*
     - Координати на адреса
   * - **$zip**
     - *string*
     - Пощенски код
   * - **$description**
     - *string*
     - Допълнителна информация към адреса за доставка

-----

DeliveryAddressInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за начина и локация на доставка

.. list-table::
   :header-rows: 1
   :align: center
   :name: DeliveryAddressInputData

   * - Параметър
     - Тип
     - Описание
   * - **$delivery_type**
     - *string*
     - Тип на доставката

			* **no** - *Без доставка*
			* **home** - *За вкъщи*
			* **address** - *Доставка до адрес*
			* **barsy** - Получаване от `търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **office** - *Получаване от офис на куриер* **По подразбиране:** 'no'
   * - **$country_id**
     - *string*
     - ID на държава (двубуквен код, напр. "BG").

			*При подаден country_id системата го валидира срещу b_countries и попълва country_name. Приоритет: country_id > country_name.* ( виж: :doc:`../destinations/getlistcountries` )
   * - **$country_name**
     - *string*
     - Алтернатива на country_id — наименование на държавата (напр. "България").

			*Използва се само ако country_id НЕ е подаден. При намиране — попълва country_id автоматично. Ако не бъде намерена — не е грешка: стойността се записва в адреса както е подадена, но без country_id.  Приоритет: country_id > country_name.*
   * - **$dest_id**
     - *int*
     - ID на населено място от номенклатурата на Barsy.

			*При подаден dest_id системата го валидира срещу b_destinations и попълва dest_name_full; невалиден dest_id е грешка. Ако разполагате с ID по номенклатурата на куриер — подайте го в speditor_dest_id, не тук.  Приоритет при резолвиране: speditor_dest_id > dest_id > dest_name_full.* ( виж: :doc:`../destinations/getlist` )
   * - **$dest_name_full**
     - *string*
     - Алтернатива на dest_id — пълно наименование на населено място (напр. "гр. София").

			*Използва се само ако dest_id НЕ е подаден. Системата търси в следния ред: точно съвпадение по DEST_NAME, после LIKE по DEST_NAME, после точно съвпадение по DEST_NAME_FULL_TEXT, накрая LIKE по DEST_NAME_FULL_TEXT — при намиране попълва dest_id автоматично. Частично съвпадение се приема само ако е еднозначно (един кандидат). Ако не бъде намерено — не е грешка: стойността се записва в адреса както е подадена, но без dest_id.  Приоритет: dest_id > dest_name_full.*
   * - **$speditor_dest_id**
     - *int*
     - ID на населено място по номенклатурата на куриера (НЕ е Barsy DEST_ID).

			*Използва се когато куриерът подава своя city_id (напр. от собствен checkout widget или API). Изисква едновременно подаден speditor_id (или намерим speditor_name) — без разпознат куриер се хвърля грешка. Системата маппира speditor_dest_id към Barsy dest_id чрез таблица b_destination_speditors (SPEDITOR_REF_ID → DEST_ID); при липсващ mapping — грешка. При намиране — попълва dest_id и dest_name_full автоматично. Не се записва в базата — служи само за резолвиране.  Приоритет: speditor_dest_id > dest_id > dest_name_full.* ( виж: ``Speditors_GetList за стойността на speditor_id`` )
   * - **$address**
     - *string*
     - Адрес за доставка (бул/ул)
   * - **$address_neighborhood**
     - *string*
     - Квартал на адреса за доставка
   * - **$address_number**
     - *string*
     - Номер на улица/булевард за доставка
   * - **$address_building**
     - *string*
     - Блок за доставка
   * - **$address_entry**
     - *string*
     - Вход на блок за доставка
   * - **$address_floor**
     - *string*
     - Номер на етаж за доставка
   * - **$address_ap**
     - *string*
     - Номер на апартамент за доставка
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (ако типа на доставката е "Взимане от `търговски обект </barsy.help/210-dictionary/barsy.html>`__").

			*При подаден barsy_id системата го валидира и попълва barsy_name_address. Приоритет: barsy_id > barsy_name_address.* ( виж: :doc:`../barsys/getlist` )
   * - **$barsy_name_address**
     - *string*
     - Алтернатива на barsy_id — наименование на `търговски обект </barsy.help/210-dictionary/barsy.html>`__.

			*Използва се само ако barsy_id НЕ е подаден. Търси се първо по PUBLIC_NAME, след това по NAME (само сред неизтритите обекти). При намиране — попълва barsy_id, а тук се записва вътрешното NAME на обекта (PUBLIC_NAME служи само за търсене). Ако не бъде намерен — не е грешка: стойността се записва в адреса както е подадена, но без barsy_id.  Приоритет: barsy_id > barsy_name_address.*
   * - **$speditor_id**
     - *int*
     - ID на спедитор (ако типа на доставката е "Доставка с куриер").

			*При подаден speditor_id системата го валидира и попълва speditor_name. Приоритет: speditor_id > speditor_name.* ( виж: :doc:`../speditors/getlist` )
   * - **$speditor_name**
     - *string*
     - Алтернатива на speditor_id — наименование на куриера (напр. "Спиди").

			*Използва се само ако speditor_id НЕ е подаден. Търси се по точно съответствие (case-insensitive) само сред активните куриери. При намиране — попълва speditor_id автоматично. Ако не бъде намерен — не е грешка: стойността се записва в адреса както е подадена, но без speditor_id (освен ако е подаден и speditor_dest_id — тогава е грешка).  Приоритет: speditor_id > speditor_name.*
   * - **$office_id**
     - *int*
     - ID на офис на куриер по номенклатурата на съответния куриер ( виж: :doc:`../speditors/getofficelist` )
   * - **$office_type**
     - *string*
     - 
   * - **$zip**
     - *string*
     - Пощенски код
   * - **$coords**
     - *string*
     - Координати на адреса
   * - **$description**
     - *string*
     - Допълнителна информация към адреса за доставка

-----

ClientOrderInputRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientOrderInputRowData

   * - Параметър
     - Тип
     - Описание
   * - **$client_order_row**
     - *integer*
     - ID на реда (празно при подаване на нов ред в поръчката)
   * - **$article_id**
     - *integer*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ по номенклатура на barsy
   * - **$amount**
     - *float*
     - Желано количество - може да бъде дробно число до 9-ти знак
   * - **$current_price**
     - *float*
     - 
   * - **$original_price**
     - *float*
     - Единична цена на поръчката - ако не е подадена, ще бъде ползвана текущата цена за този `търговски обект </barsy.help/210-dictionary/barsy.html>`__/`клиент </barsy.help/210-dictionary/client.html>`__/`артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_id**
     - *int*
     - ID на данъчна група от номенклатурата им ( виж: :doc:`../taxgroups/getlist` )
   * - **$detail_notes**
     - *string*
     - Свободен текст - Може да съдържа някакви допълнително описание към конкретния `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$details**
     - FormFieldInputData_ []
     - Детайли към `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articles/get` , :doc:`../forms/get` )
   * - **$detail_status**
     - *int*
     -  **По подразбиране:** 1
   * - **$discount**
     - *float*
     - Отстъпка на ниво ред/`артикул </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** 0
   * - **$package_name**
     - *string*
     - Име на разфасовката (при използване на разфасовки)
   * - **$package_ratio**
     - *float*
     - Количеството в една разфасовка (при използване на разфасовки)

-----

FormFieldInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: FormFieldInputData

   * - Параметър
     - Тип
     - Описание
   * - **$value**
     - *string*
     - Стойност на даденото поле от формуляра
   * - **$title**
     - *string*
     - Заглавие на даденото поле от формуляра

-----

PaymentInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PaymentInputData

   * - Параметър
     - Тип
     - Описание
   * - **$paymethod_id**
     - *int*
     - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../paymentmethods/getlist` )
   * - **$original_paid_sum**
     - *float*
     - Платена сума във валута
   * - **$currency_id**
     - *int*
     - ID на валута ( виж: :doc:`../currencies/getlist` )
   * - **$req_value**
     - *string*
     - Необходима допълнителна информация към `плащането </barsy.help/210-dictionary/payment.html>`__ (настройва се в конкретния начина на `плащане </barsy.help/210-dictionary/payment.html>`__)
   * - **$payment_data**
     - *object*
     - Допълнително данни за `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$transaction_id**
     - *string*
     - Номер на транзакция
   * - **$ref_num**
     - *string*
     - Референтен номер
   * - **$ref_date**
     - *string*
     - Дата вальор
   * - **$description**
     - *string*
     - Свободен текст
   * - **$receipt_data**
     - InputStornoData_ 
     - Данни за бележката на сторно `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$actual_paid_sum**
     - *float*
     - Платена сума преди връщане на ресто
   * - **$bank_account**
     - *string*
     - IBAN на платеца (при `плащане </barsy.help/210-dictionary/payment.html>`__ по банка)

-----

InputStornoData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InputStornoData

   * - Параметър
     - Тип
     - Описание
   * - **$storno_reason**
     - *string*
     - Причина за сторното

			* **return** - *Връщане / рекламация*
			* **mistake** - *Операторска грешка*
			* **reduction_tax_base** - *Намаление на данъчната основа* ( виж: :doc:`../accounts/getstornoreasons` )
   * - **$unp**
     - *string*
     - УНП на сторнираната бележка
   * - **$receipt_num**
     - *string*
     - Номер на сторнираната бележка
   * - **$receipt_date**
     - *string*
     - Дата на сторнираната бележка
   * - **$fm_num**
     - *string*
     - Номер на фискална памет на сторнираната бележка

-----

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clientorders_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/clientorders_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/clientorders_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/clientorders_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/clientorders_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clientorders_create/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Клиентска заявка </barsy.help/210-dictionary/client-order.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

