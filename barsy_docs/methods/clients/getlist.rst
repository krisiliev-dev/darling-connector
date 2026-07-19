.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Clients_getlist
===========================================================
Списък с клиенти

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/100-catalog/clients/index </barsy.help/110-admin/100-catalog/clients/index.html>`__
	 * barsy.help: `210-dictionary/client </barsy.help/210-dictionary/client.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Универсален метод за извличане на списък с `клиенти </barsy.help/210-dictionary/client.html>`__ с богат набор от филтри — по име/телефон/email, клиентска група, статус, период на регистрация, наличие на активни `сметки </barsy.help/210-dictionary/account.html>`__/`абонаменти </barsy.help/210-dictionary/subscription.html>`__, кредитен баланс, обект. Поддържа странициране (`offset`, `length`) и допълнителни секции през `extra_properties` (баланс, последна покупка, контакти).

Типични случаи: попълване на клиентски листинг в админ панел, експорт за маркетингова кампания (например `клиенти </barsy.help/210-dictionary/client.html>`__ без покупки последните 6 месеца), синхронизация към CRM, изграждане на VIP сегмент по кредитен оборот. За кратко контекстно търсене (автокомплийт) виж `Clients_getlistsmart`.

**Име**: Clients_getlist
**Категория**: Catalog


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$filters**
     - ClientsListFiltersData_ 
     - Филтриране на резултатите по зададени критерии
   * - **$extra_properties**
     - ClientsListExtraPropertiesData_ 
     - Желани допълнителни колони за всеки `клиент </barsy.help/210-dictionary/client.html>`__ (виж класа)
   * - **$offset**
     - *int*
     -  **По подразбиране:** 0
   * - **$length**
     - *int*
     -  **По подразбиране:** 1000
   * - **$order_by**
     - ClientsListOrderByData_ 
     - Подреждане — низ, масив или обект колона⇒посока (напр. {"client_name":"asc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ClientData_                                                            
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ClientsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$barsy_id**
     - *int*
     - Филтър по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/get` , :doc:`../barsys/getlist` )
   * - **$client_group_id**
     - *int*
     - Филтър по ID на клиентска група ( виж: :doc:`../clientgroups/getlist` )
   * - **$delivery_zone_id**
     - *string*
     - Филтър по зона за доставка
   * - **$recruit_client_id**
     - *int*
     - Филтър по "Източник `клиент </barsy.help/210-dictionary/client.html>`__" ( виж: :doc:`../clients/get` , :doc:`../clients/getlist` )
   * - **$client_source_id**
     - *int*
     - Филтър по "Препоръчан от"
   * - **$agent_client_id**
     - *int*
     - Филтър по "Агент" ( виж: :doc:`../clients/get` , :doc:`../clients/getlist` )
   * - **$remote_ref_id**
     - *int*
     - Id на `клиента </barsy.help/210-dictionary/client.html>`__ в отдалечена система ( виж: :doc:`../remotesystems/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$client_id**
     - *int*
     - Филтър по ID на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$export_id**
     - *int*
     - Филтър по "Export ID"
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$client_name**
     - *string*
     - Филтър по име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$get_smart**
     - *string*
     - Филтър по име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$client_name_match_i**
     - *string*
     - Филтър по точно име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$tel**
     - *string*
     - Филтър по телефон на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$recommended**
     - *string*
     - Филтър по признака "Препоръчан"
   * - **$description**
     - *string*
     - Филтър по описание на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$client_code**
     - *string*
     - Филтър по клиентски код
   * - **$client_code_match**
     - *string*
     - Филтър по точно подаден клиентски код
   * - **$company_name**
     - *string*
     - Филтър по име на компания
   * - **$address**
     - *string*
     - Филтър по адрес
   * - **$bulstat**
     - *string*
     - Филтър по БУЛСТАТ
   * - **$vat_num**
     - *string*
     - Филтър по ДДС номер
   * - **$mol**
     - *string*
     - Филтър по MOL
   * - **$email**
     - *string*
     - Филтър по имейл

			*Намира съвпадение и по част от имейл адреса.*
   * - **$email_match**
     - *string*
     - Филтър по имейл по точно подадена стойност
   * - **$email_invoices**
     - *string*
     - Филтър по имейл за `фактура </barsy.help/210-dictionary/invoice.html>`__
   * - **$delivery_address**
     - *string*
     - Филтър по адрес за доставка
   * - **$index**
     - *string*
     - Филтър по символ
   * - **$email_invoices_smart**
     - *string*
     - Филтър по email за фактута
   * - **$client_auth**
     - *string*
     - Филтър по потребителско име
   * - **$client_auth_match**
     - *string*
     - Филтър по точно потребителско име
   * - **$query**
     - *string*
     - Филтър по текстово търсене
   * - **$zip**
     - *string*
     - Филтър по пощенски код
   * - **$town**
     - *string*
     - Филтър по град
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$client_create_date**
     - *string*
     - Филтър по дата на създаване на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$last_update**
     - *string*
     - Филтър по последен ъпдейт на `клиент </barsy.help/210-dictionary/client.html>`__.

			*Точна стойност.*
   * - **$remote_last_update**
     - *string*
     - Дата на последен ъпдейт в отдалечената система
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$discount**
     - *int*
     - Филтър по отстъпка на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$delete_flag**
     - *int*
     - Филтър по изтритите `клиенти </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** 0
   * - **$ml_subscribed**
     - *int*
     - Филтър по `абонамент </barsy.help/210-dictionary/subscription.html>`__ за бюлетин
   * - **$is_guest**
     - *int*
     - Филтър по флаг за гост
   * - **$hide_anonymous**
     - *int*
     - Скрива анонимния `клиент </barsy.help/210-dictionary/client.html>`__ (CLIENT_ID = 1) от резултата **По подразбиране:** 1
   * - **$for_remote_update**
     - *int*
     - Филтер по това дали `клиента </barsy.help/210-dictionary/client.html>`__ е за обновяване в отдалечената система
   * - **$credit_limit**
     - *float*
     - Филтер по клиентски лимит
   * - **$make_invoice_auto**
     - *float*
     - Филтър по автоматично създаване на `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$send_invoice_auto**
     - *float*
     - Филтър по автоматично изпращане на `фактури </barsy.help/210-dictionary/invoice.html>`__

-----

ClientsListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към `клиент </barsy.help/210-dictionary/client.html>`__. Всяка опция включва съответната колона към данните за всеки
		`клиент </barsy.help/210-dictionary/client.html>`__ от списъка. Основните данни се връщат винаги, а останалите при стойност true.

	*Приема и стария формат — списък с имена (напр. ["email","tel"]) — който се превежда към булеви флагове.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientsListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Основни данни`
     - 
     - 
   * - **$client_id**
     - *bool*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** true
   * - **$client_name**
     - *bool*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** true
   * - **$lang_id**
     - *bool*
     - ID на езика на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** true
   * - **$export_id**
     - *bool*
     - "Export ID" на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
   * - **$discount**
     - *bool*
     - Отстъпка на `клиента </barsy.help/210-dictionary/client.html>`__ (форматирана) **По подразбиране:** true
   * - **$make_invoice_auto**
     - *bool*
     - Автоматично създаване на `фактура </barsy.help/210-dictionary/invoice.html>`__

			Показва дали за `клиента </barsy.help/210-dictionary/client.html>`__ автоматично се създава `фактура </barsy.help/210-dictionary/invoice.html>`__. Взема се настройката на `клиента </barsy.help/210-dictionary/client.html>`__, при липса — тази на групата му, а накрая стойността по подразбиране. **По подразбиране:** false
   * - **$send_invoice_auto**
     - *bool*
     - Автоматично изпращане на `фактура </barsy.help/210-dictionary/invoice.html>`__

			Показва дали за `клиента </barsy.help/210-dictionary/client.html>`__ автоматично се изпраща `фактура </barsy.help/210-dictionary/invoice.html>`__. Взема се настройката на `клиента </barsy.help/210-dictionary/client.html>`__, при липса — тази на групата му, а накрая стойността по подразбиране. **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$group_id**
     - *bool*
     - ID на клиентската група **По подразбиране:** true
   * - **$recruit_client_id**
     - *bool*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__-източник ("Източник `клиент </barsy.help/210-dictionary/client.html>`__") **По подразбиране:** false
   * - **$client_source_id**
     - *bool*
     - ID на източника на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$agent_client_id**
     - *bool*
     - ID на агента на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
   * - **$tel**
     - *bool*
     - Телефон на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$email**
     - *bool*
     - Имейл на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$email_invoices**
     - *bool*
     - Имейл за `фактури </barsy.help/210-dictionary/invoice.html>`__ **По подразбиране:** false
   * - **$client_auth**
     - *bool*
     - Потребителско име на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$client_code**
     - *bool*
     - Клиентски код **По подразбиране:** false
   * - **$company_name**
     - *bool*
     - Име на компанията **По подразбиране:** false
   * - **$address**
     - *bool*
     - Адрес **По подразбиране:** false
   * - **$bulstat**
     - *bool*
     - БУЛСТАТ **По подразбиране:** false
   * - **$vat_num**
     - *bool*
     - ДДС номер **По подразбиране:** false
   * - **$mol**
     - *bool*
     - МОЛ **По подразбиране:** false
   * - **$town**
     - *bool*
     - Град **По подразбиране:** false
   * - **$zip**
     - *bool*
     - Пощенски код **По подразбиране:** false
   * - **$delivery_address**
     - *bool*
     - Адрес за доставка **По подразбиране:** false
   * - **$delivery_zone_id**
     - *bool*
     - Зона за доставка **По подразбиране:** false
   * - **$description**
     - *bool*
     - Описание/бележка за `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$ml_subscribed**
     - *bool*
     - Дали `клиентът </barsy.help/210-dictionary/client.html>`__ е абониран за бюлетин **По подразбиране:** false
   * - **$is_guest**
     - *bool*
     - Дали `клиентът </barsy.help/210-dictionary/client.html>`__ е гост **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
   * - **$client_create_date**
     - *bool*
     - Дата на създаване на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$last_update**
     - *bool*
     - Дата на последна промяна **По подразбиране:** false

-----

ClientsListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с `клиенти </barsy.help/210-dictionary/client.html>`__ (Clients_getlist).
		Подава се като асоциативен масив колона⇒посока (напр. ["client_name" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientsListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$client_id**
     - *string*
     - Подреждане по ID на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$export_id**
     - *string*
     - Подреждане по "Export ID"
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$client_name**
     - *string*
     - Подреждане по име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$tel**
     - *string*
     - Подреждане по телефон
   * - **$email**
     - *string*
     - Подреждане по имейл
   * - **$town**
     - *string*
     - Подреждане по град
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$group_id**
     - *string*
     - Подреждане по клиентска група
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$discount**
     - *string*
     - Подреждане по отстъпка
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$client_create_date**
     - *string*
     - Подреждане по дата на създаване
   * - **$last_update**
     - *string*
     - Подреждане по дата на последна промяна

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

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clients_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/clients_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/clients_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/clients_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/clients_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clients_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Клиент </barsy.help/210-dictionary/client.html>`__


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

