.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Clients_getlistsmart
===========================================================
Умно търсене на клиенти

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
Контекстно търсене на `клиенти </barsy.help/210-dictionary/client.html>`__, оптимизирано за интерактивни сценарии. Подаденото име се търси едновременно по основно име, телефон, email, ЕИК/БУЛСТАТ, потребителско име и фирмено име — резултатът се връща обогатен с автоматично избрани полета (email, авторизация, телефон). Ако точно един `клиент </barsy.help/210-dictionary/client.html>`__ съвпада по специфично поле (например ЕИК), това поле се добавя към връзката, за да може клиентският UI да открои защо точно този запис е намерен.

Типични случаи: автокомплийт на `каса </barsy.help/210-dictionary/pos.html>`__ при набиране на телефон или име, бърза проверка дали `клиент </barsy.help/210-dictionary/client.html>`__ вече съществува преди да се отвори форма за регистрация, идентификация по ЕИК при фактуриране. За пълни таблични справки с филтри се ползва `Clients_getlist`.

**Име**: Clients_getlistsmart
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
     - 
   * - **$extra_properties**
     - ClientsListExtraPropertiesData_ 
     - 
   * - **$offset**
     - *int*
     -  **По подразбиране:** 0
   * - **$length**
     - *int*
     -  **По подразбиране:** 50
   * - **$page**
     - *int*
     -  **По подразбиране:** 0


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                
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

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clients_getlistsmart/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/clients_getlistsmart/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/clients_getlistsmart/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/clients_getlistsmart/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/clients_getlistsmart/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clients_getlistsmart/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Клиент </barsy.help/210-dictionary/client.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

