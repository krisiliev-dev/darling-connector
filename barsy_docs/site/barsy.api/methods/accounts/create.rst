.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Accounts_create
===========================================================
Създаване на нова сметка

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/account </barsy.help/210-dictionary/account.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира нова отворена `сметка </barsy.help/210-dictionary/account.html>`__ с подадените основни данни (`клиент </barsy.help/210-dictionary/client.html>`__, обект, маса/място, бележки, валута) и опционално първоначален списък с поръчани `артикули </barsy.help/210-dictionary/article.html>`__. `Сметката </barsy.help/210-dictionary/account.html>`__ остава отворена за допълнителни поръчки, плащания и редакции. За еднокрактно изпълнение на пълен сценарий (отваряне + поръчка + `плащане </barsy.help/210-dictionary/payment.html>`__ + приключване) използвайте `Accounts_place`, който е по-удобен за интеграции от типа "self-service" и онлайн поръчки.

Типични случаи: отваряне на маса в ресторант преди първа поръчка, започване на покупка на едро с дълъг каталог, отваряне на сервизна `сметка </barsy.help/210-dictionary/account.html>`__ с фиксирани условия преди допълване с `артикули </barsy.help/210-dictionary/article.html>`__ по време на обслужването.

**Име**: Accounts_create
**Категория**: Cashdesk


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$account**
     - AccountInputData_ 
     - Обект със свойства, описващи основните данни на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$rows**
     - OrderMakeData_ []
     - Масив от обекти, описващи `артикулите </barsy.help/210-dictionary/article.html>`__ в поръчката  - **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  Id на създадената сметка
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

AccountInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Входящи данни за `сметка </barsy.help/210-dictionary/account.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: AccountInputData

   * - Параметър
     - Тип
     - Описание
   * - **$uuid**
     - *string*
     - Уникален номер на `сметка </barsy.help/210-dictionary/account.html>`__.

			Подходящ за избягване на дублиране на `сметка </barsy.help/210-dictionary/account.html>`__. Ако не е подаден ще се генерира автоматично
   * - **$client_id**
     - *integer*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ по barsy - ако няма, търси се дали има обект client (виж по-надолу), ако го няма - записва се към Анонимен (ID:1) ( виж: :doc:`../clients/getlist` ) **По подразбиране:** 1
   * - **$client**
     - ClientInputData_ 
     - Данни за `клиента </barsy.help/210-dictionary/client.html>`__ (ако е нов или трябва да бъде разпознат)
   * - **$person_id**
     - *int*
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../persons/getlist` )
   * - **$person**
     - PersonInputData_ 
     - Данни за `представителя </barsy.help/210-dictionary/person.html>`__ (ако е нов или трябва да бъде разпознат)
   * - **$place_id**
     - *int*
     - ID на място/маса/стая/... ( виж: :doc:`../places/getlist` )
   * - **$discount**
     - *float*
     - Отстъпка върху цялата `сметка </barsy.help/210-dictionary/account.html>`__ **По подразбиране:** 0
   * - **$ref_date**
     - *string*
     - Дата на документално извършване на сделката
   * - **$persons**
     - *int*
     - Брой хора (посетители) към тази `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$delivery_address**
     - DeliveryAddressInputData_ 
     - Адрес за доставка за тази `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$contact_name**
     - *string*
     - Лице за контакт за тази `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$phone**
     - *string*
     - Телефон за контакт към тази `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$account_alias**
     - *string*
     - Заглавие на `сметката </barsy.help/210-dictionary/account.html>`__.

			Използва се за лесно разпознаване на `сметка </barsy.help/210-dictionary/account.html>`__. Визуализира се в списъци със `сметки </barsy.help/210-dictionary/account.html>`__
   * - **$description**
     - *string*
     - Свободен текст.

			Може да съдържа някакви допълнително описание към цялата `сметка </barsy.help/210-dictionary/account.html>`__ - печати се на бележката
   * - **$notes**
     - *string*
     - Свободен текст.

			Може да съдържа някакви допълнително описание към цялата `сметка </barsy.help/210-dictionary/account.html>`__ - НЕ се печати на бележката
   * - **$tracking_number**
     - *string*
     - Номер на товарителница
   * - **$speditor_id**
     - *int*
     - ID на спедитор
   * - **$delivery_zone_id**
     - *int*
     - ID на зона за доставка
   * - **$paid_due_date**
     - *string*
     - Отложено `плащане </barsy.help/210-dictionary/payment.html>`__ до
   * - **$storno_data**
     - InputStornoData_ 
     - Данни за `сметка </barsy.help/210-dictionary/account.html>`__, която се сторнира с този `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$deal_id**
     - *integer*
     - ID на сделка по barsy.

			*Използва се за групиране на операции в обща група (сделка)* ( виж: :doc:`../deals/getlist` )
   * - **$calculate_orders_discount_flag**
     - *int*
     - Флаг за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ на отстъпката от `сметка </barsy.help/210-dictionary/account.html>`__ към поръчки
   * - **$skip_account_discount_recalculate_flag**
     - *int*
     - Сигнал дали да се прескочи прилагането на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ тип Отстъпка-`сметка </barsy.help/210-dictionary/account.html>`__. **По подразбиране:** 0
   * - **$client_order_id**
     - *int*
     - 
   * - **$external_source**
     - *object* | *int* | *null*
     - 
   * - **$additional_data**
     - *object*
     - 
   * - **$reservation_id**
     - *int*
     - 
   * - **$lang_id**
     - *string*
     - ID на език за `сметката </barsy.help/210-dictionary/account.html>`__.

			Ще принтира имената на `артикулите </barsy.help/210-dictionary/article.html>`__ на посочения език в фискалната бележка (ако има зададени такива). ( виж: :doc:`../languages/getlist` )
   * - **$calculate_start_date**
     - *bool*
     - Дали да се изчислява START_SERVICE_DATE на новите поръчки при запис на `сметка </barsy.help/210-dictionary/account.html>`__.

			Важи само за ресторантски `сметки </barsy.help/210-dictionary/account.html>`__ (delivery_type = no). При false (по подразбиране) START_SERVICE_DATE остава NULL — поръчките са видими веднага. При true системата изчислява старт на услугата на база бача и order_service_date. **По подразбиране:** false
   * - **$order_service_date**
     - *string*
     - Желано време за изпълнение на поръчките от текущия бач (само за ресторантски `сметки </barsy.help/210-dictionary/account.html>`__, delivery_type = no).

			*Ако е зададено, системата проверява дали поръчките могат да бъдат готови до тогава. Ако не може — хвърля грешка с най-ранното възможно време. Не се записва в базата.*
   * - **$delivery_date**
     - *string*
     - Дата на доставка (Подава се от `клиента </barsy.help/210-dictionary/client.html>`__).
   * - **$currency_id**
     - *int*
     - ID на валута.

			*Ако е оставена непопълнена, ще се вземе системната валута* ( виж: :doc:`../currencies/getlist` )
   * - **$currency_rate**
     - *float*
     - Курс на валутата

-----

ClientInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за създаване или актуализиране на client

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientInputData

   * - Параметър
     - Тип
     - Описание
   * - **$client_name**
     - *string*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ - трябва да бъде уникално в цялата система.

			*Може да бъде физическото име или друго синтетично име*
   * - **$discount**
     - *string*
     - Процент отстъпка/надценка за всички операции на `клиента </barsy.help/210-dictionary/client.html>`__ (ако числото е отрицателно-> отстъпка; ако е положително>надценка) **По подразбиране:** 0
   * - **$delete_flag**
     - *int*
     - Флаг, дали `потребителя </barsy.help/210-dictionary/user.html>`__ е маркиран като изтрит **По подразбиране:** 0
   * - **$description**
     - *string*
     - Описание - свободен текст
   * - **$tel**
     - *string*
     - Телефон за контакт
   * - **$fax**
     - *string*
     - Факс за контакт
   * - **$recom**
     - *string*
     - Препоръчан от
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
   * - **$client_code**
     - *string*
     - Клиентски код (на карта)
   * - **$town**
     - *string*
     - Град
   * - **$zip**
     - *string*
     - Пощенски код
   * - **$email**
     - *string*
     - Основен email на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$credit_limit**
     - *float*
     - Кредитен лимит на `клиента </barsy.help/210-dictionary/client.html>`__ (стойност до която може да задлъжнява)
   * - **$allow_client_nocard**
     - *int*
     - Разрешено използване профила без карта **По подразбиране:** 1
   * - **$allow_credit_nocard**
     - *int*
     - Разрешено използване на клиентски портфейл без карта **По подразбиране:** 1
   * - **$allow_discount_nocard**
     - *int*
     - Разрешено използване на отстъпка без карта **По подразбиране:** 1
   * - **$group_id**
     - *int*
     - Клиентска група, към която принадлежи `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getgroups` )
   * - **$default_paymethod_id**
     - *int*
     - ID на предпочитан начин на `плащане </barsy.help/210-dictionary/payment.html>`__ за този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$export_id**
     - *string*
     - ID за експорт към външни системи
   * - **$client_picture**
     - *string*
     - Основна снимка от наличните за този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$client_pass**
     - *string*
     - Клиентска парола за вход в клиентския профил
   * - **$client_auth**
     - *string*
     - Клиентско име за вход в клиентския профил
   * - **$client_source_id**
     - *int*
     - ID на източника, от където е намерен този `клиент </barsy.help/210-dictionary/client.html>`__/контакт.
   * - **$recruit_client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, осигурил този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$agent_client_id**
     - *int*
     - ID на агента, към който е този `клиент </barsy.help/210-dictionary/client.html>`__/контакт.
   * - **$email_invoices**
     - *string*
     - Email за изпращане на `фактури </barsy.help/210-dictionary/invoice.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$delivery_zone_id**
     - *int*
     - ID на зона за доставка
   * - **$ml_subscribed**
     - *int*
     - Флаг дали `клиентът </barsy.help/210-dictionary/client.html>`__ е абониран за maillist **По подразбиране:** -2
   * - **$paid_period**
     - *int*
     - Интервал от време(в минути) за отложено `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране
   * - **$receiver_name**
     - *string*
     - Име на получател
   * - **$is_guest**
     - *int*
     - Флаг за гост **По подразбиране:** 0
   * - **$delivery_address**
     - DeliveryAddressInputData_ 
     - Адрес за доставка
   * - **$barsys**
     - *array*
     - Масив от ID-та на обекти, в които този `клиент </barsy.help/210-dictionary/client.html>`__ може да се ползва
   * - **$default_person_id**
     - *int*
     - 
   * - **$bank_accounts**
     - *array*
     - 
   * - **$weight**
     - *int*
     - Подреба/тежест на `клиентите </barsy.help/210-dictionary/client.html>`__
   * - **$client_color**
     - *string*
     - Цвят за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$gln**
     - *string*
     - GLN (Global Location Number) — 13-цифрен GS1 идентификатор на юридическото лице.

			*Ползва се за EDI обмен (Buyer/ILN в ORDER/INVOICE/DESADV документите)*
   * - **$edi_supplier_code**
     - *string*
     - Номер на `доставчик </barsy.help/210-dictionary/supplier.html>`__ — кодът на нашата `фирма </barsy.help/210-dictionary/company.html>`__ в системата на този `клиент </barsy.help/210-dictionary/client.html>`__ (верига).

			*В EDI документите това е Seller/CodeByBuyer. Излиза и в печатните бланки*
   * - **$make_invoice_auto**
     - *int*
     - Автоматично създаване на `фактура </barsy.help/210-dictionary/invoice.html>`__ при постъпване на `плащане </barsy.help/210-dictionary/payment.html>`__ с VPOS: NULL (според групата), 0 (изключено), 1 (включено)
   * - **$send_invoice_auto**
     - *int*
     - Автоматично изпращане на `фактура </barsy.help/210-dictionary/invoice.html>`__ при генериране на такава: NULL (според групата), 0 (изключено), 1 (включено)
   * - **$lang_id**
     - *string*
     - Предпочитан език

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

PersonInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PersonInputData

   * - Параметър
     - Тип
     - Описание
   * - **$person_name**
     - *string*
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, на който принадлежи `представителя </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../clients/getlist` )
   * - **$description**
     - *string*
     - Свободен текст
   * - **$type_id**
     - *int*
     - ID на типа на `представител </barsy.help/210-dictionary/person.html>`__ ( виж: ``*/`` ) **По подразбиране:** 1
   * - **$person_code**
     - *string*
     - Код на `представител </barsy.help/210-dictionary/person.html>`__.

			Използва се за индентификация на `представителя </barsy.help/210-dictionary/person.html>`__ чрез някакъв носител (например карта)
   * - **$delete_flag**
     - *int*
     - Флаг дали `представителя </barsy.help/210-dictionary/person.html>`__ е маркиран като изтрит **По подразбиране:** 0
   * - **$dynamic_input**
     - *object*
     - 

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

OrderMakeData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: OrderMakeData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *float*
     - Количество
   * - :deprecated:`$current_price`
     - *float*
     - Продажна цена (ако се пропусне - ще се използва текущата) :deprecated_text:`Отхвърлено: Използваме original_current_price вместо това поле`
   * - **$original_current_price**
     - *float*
     - Продажна цена (ако се пропусне - ще се използва текущата)
   * - **$discount**
     - *float*
     - Отстъпка/надценка в проценти на продажната цена на `артикул </barsy.help/210-dictionary/article.html>`__ в `сметка </barsy.help/210-dictionary/account.html>`__ (различно от отстъпка на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
   * - **$tax_id**
     - *int*
     - ДДС
   * - **$modificators**
     - ModificatorInputData_ []
     - 
   * - **$article_attributes**
     - ArticleAttributesSimpleData_ 
     - 
   * - **$supplements**
     - ArticleSupplementData_ []
     - Комбинирани `артикули </barsy.help/210-dictionary/article.html>`__
   * - **$storno_of_account_id**
     - *int*
     - Номер на `сметка </barsy.help/210-dictionary/account.html>`__ по което се сторнира тази поръчка (само при отрицателно количество)
   * - **$tax_region_id**
     - *int*
     - ID на данъчен регион

-----

ModificatorInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ModificatorInputData

   * - Параметър
     - Тип
     - Описание
   * - **$mod_name**
     - *string*
     - Име на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$description**
     - *string*
     - Описание на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_type**
     - *int*
     - Тип `модификатор </barsy.help/210-dictionary/modificator.html>`__

			* **1** - *Липсва описание*
			* **2** - *Липсва описание*

-----

ArticleAttributesSimpleData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleAttributesSimpleData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - 
   * - **$amount**
     - *float*
     - 
   * - **$attributes**
     - 
     - 

-----

ArticleSupplementData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleSupplementData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, в участва в комбо `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *float*
     - Количество на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо
   * - **$supplement_price**
     - *float*
     - цена на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо (ако не се подаде, се ползва зададената или изчислената)
   * - **$supplement_group_id**
     - *int*
     - ID на група на комбото, в която участва `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$discount**
     - *float*
     - Отстъпка на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо
   * - **$tax_id**
     - *int*
     - ДДС id на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$tax_region_id**
     - *int*
     - ID на тип доставка
   * - **$article_attributes**
     - *array*
     - Атрибути на `артикула </barsy.help/210-dictionary/article.html>`__ (при `артикули </barsy.help/210-dictionary/article.html>`__ с дефинирани атрибути — цвят, размер и т.н.).

			*Структура: [{article_id, amount, attributes: [{key, value}, ...]}]*
   * - **$lot_value**
     - *string*
     - Партида на supplement-а (за `артикули </barsy.help/210-dictionary/article.html>`__ с LOT_TYPE_ID > 1).
   * - **$supplement_article**
     - 
     - 

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

     .. literalinclude:: ../../sources/accounts_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/accounts_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/accounts_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/accounts_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/accounts_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/accounts_create/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__


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

