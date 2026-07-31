.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Invoices_get
===========================================================
Преглед на фактура

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/invoice </barsy.help/210-dictionary/invoice.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълни данни за конкретна `фактура </barsy.help/210-dictionary/invoice.html>`__ по неговото ID — основни данни (номер, серия, тип, дата, статус), продавач и получател с фирмени данни, банкова `сметка </barsy.help/210-dictionary/account.html>`__, `артикули </barsy.help/210-dictionary/article.html>`__ с количества и единични цени, ДДС групи, общи суми, свързани документи (плащания, обвързани `сметки </barsy.help/210-dictionary/account.html>`__, родителски документи). Endpoint-ът поддържа автоматично преобразуване на изхода в различни печатни формати (PDF, HTML, Excel, CSV, XML, JSON) чрез смяна на типа на отговора.

Типични случаи: преглед на `фактура </barsy.help/210-dictionary/invoice.html>`__ в админ панела, печат на копие за `клиент </barsy.help/210-dictionary/client.html>`__, експорт към счетоводна система, автоматизирано изпращане по email на издадена `фактура </barsy.help/210-dictionary/invoice.html>`__.

**Име**: Invoices_get
**Категория**: Documents


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$inv_id**
     - *int*
     - ID на `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$copy**
     - *int*
     -  **По подразбиране:** 0
   * - **$extra_elements**
     - *array*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
InvoiceData_                                                           
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

InvoiceData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoiceData

   * - Параметър
     - Тип
     - Описание
   * - **$inv_id**
     - *int*
     - ID на `фактурата </barsy.help/210-dictionary/invoice.html>`__ (вътрешна номенклатура)
   * - **$inv_sid**
     - *string*
     - SID на `фактурата </barsy.help/210-dictionary/invoice.html>`__ (вътрешна номенклатура кодирана)
   * - **$inv_num**
     - *string*
     - 
   * - **$linked_accounts_num**
     - 
     - 
   * - **$type_id**
     - *int*
     - Тип на документа (`фактура </barsy.help/210-dictionary/invoice.html>`__, проформа, дебитно/кредитно известие, стокова ...) **По подразбиране:** 1
   * - **$type_name**
     - *string*
     - Тип на документа
   * - **$parent_num**
     - *string*
     - Номер на документ, по който е издаден този
   * - **$produce_date**
     - *string*
     - Дата на издаване
   * - **$create_date**
     - *string*
     - Дата на създаване
   * - **$term_date**
     - *string*
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$payment_date**
     - *string*
     - Дата на събитие
   * - **$paymethod_id**
     - 
     - 
   * - **$paymethod_name**
     - 
     - 
   * - **$is_anulate**
     - *int*
     - Флаг дали `фактурата </barsy.help/210-dictionary/invoice.html>`__ е анулирана **По подразбиране:** 0
   * - **$total_all_string**
     - *string*
     - Словом на сумата на `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$total_dds_string**
     - *string*
     - Словом на сумата на ДДС
   * - **$with_tax**
     - *int*
     - Флаг дали при печат да се печатат `артикулите </barsy.help/210-dictionary/article.html>`__ с ед.цени с ДДС **По подразбиране:** 0
   * - **$seller_name**
     - *string*
     - Име на издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$receiver_name**
     - *string*
     - Име на получил `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$additional_text**
     - *string*
     - Допълнителен текст към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$free_text**
     - *string*
     - Свободен текст към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_code**
     - *int*
     - Уникален код на издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_company_id**
     - *int*
     - ID на издател на `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_bank_account_id**
     - *int*
     - ID на банкова `сметка </barsy.help/210-dictionary/account.html>`__ за която е `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ (номенклатура на Barsy)
   * - **$client**
     - ClientData_ 
     - Данни за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$barsy_id**
     - *int*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който е издадена `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$user_id**
     - *int*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$accounts**
     - *array*
     - Списък с прикачените `сметки </barsy.help/210-dictionary/account.html>`__ към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_id**
     - *int*
     - 
   * - **$receiver_id**
     - *int*
     - 
   * - **$client_name**
     - 
     - 
   * - **$email**
     - 
     - 
   * - **$currency**
     - 
     - 
   * - **$seller**
     - InvoiceCompanyData_ 
     - Данни за получател
   * - **$receiver**
     - InvoiceCompanyData_ 
     - Данни за `доставчик </barsy.help/210-dictionary/supplier.html>`__
   * - **$parent**
     - 
     - 
   * - **$bank_account_id**
     - *int*
     - 
   * - **$bank_account**
     - InvoiceBankAccountData_ 
     - 
   * - **$seller_pop_name**
     - 
     - 
   * - **$paymethod_version_id**
     - 
     - 
   * - **$deal_id**
     - 
     - 
   * - **$deal_title**
     - 
     - 
   * - **$client_order_ids**
     - *string*
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ фигуриращи в `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$detailed_client_order_ids**
     - *string*
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ с дата на издаването им фигуриращи в `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$items**
     - InvoiceItemData_ []
     - Списък с `артикулите </barsy.help/210-dictionary/article.html>`__ към `фактурата </barsy.help/210-dictionary/invoice.html>`__ **По подразбиране:** []
   * - **$total**
     - *float*
     - Обсща сума на `фактурата </barsy.help/210-dictionary/invoice.html>`__ в системната валута **По подразбиране:** 0
   * - **$total_sum**
     - *float*
     - Обща сума с ДДС (ако се начислява) в систманата валута **По подразбиране:** 0
   * - **$total_neto**
     - *float*
     - Обща сума без ДДС в системната валута **По подразбиране:** 0
   * - **$total_dds**
     - *float*
     - Сума на ДДС в системната валута **По подразбиране:** 0
   * - **$total_all**
     - *float*
     -  **По подразбиране:** 0
   * - **$discount**
     - *float*
     -  **По подразбиране:** 0
   * - **$discount_sum**
     - 
     -  **По подразбиране:** 0
   * - **$initial_total**
     - 
     -  **По подразбиране:** 0
   * - **$tax_totals_by_tax**
     - 
     -  **По подразбиране:** []
   * - **$tax_neto_by_tax**
     - 
     -  **По подразбиране:** []
   * - **$parent_inv_id**
     - *int*
     - 
   * - **$total_remain**
     - *float*
     - 
   * - **$person_id**
     - *int*
     - 
   * - **$person_name**
     - *string*
     - 
   * - **$currency_id**
     - *int*
     - 
   * - **$currency_rate**
     - *float*
     - 

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

InvoiceCompanyData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoiceCompanyData

   * - Параметър
     - Тип
     - Описание
   * - **$company_id**
     - *int*
     - 
   * - **$company_name**
     - *string*
     - 
   * - **$identity_num**
     - *string*
     - 
   * - **$vat_num**
     - *string*
     - 
   * - **$mol**
     - *string*
     - 
   * - **$town**
     - *string*
     - 
   * - **$address**
     - *string*
     - 
   * - **$country_id**
     - *string*
     - 

-----

InvoiceBankAccountData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoiceBankAccountData

   * - Параметър
     - Тип
     - Описание
   * - **$account_id**
     - *int*
     - 
   * - **$company_id**
     - *int*
     - 
   * - **$account_name**
     - *string*
     - 
   * - **$bank_name**
     - *string*
     - 
   * - **$bic**
     - *string*
     - 
   * - **$iban**
     - *string*
     - 
   * - **$currency**
     - *string*
     - 

-----

InvoiceItemData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoiceItemData

   * - Параметър
     - Тип
     - Описание
   * - **$item_id**
     - *int*
     - 
   * - **$item_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - :deprecated:`$single_price`
     - *float*
     - Служебна стойност за единична цена без ДДС.

			*Изполвайте original_single_price* :deprecated_text:`Отхвърлено: */`
   * - **$original_single_price**
     - *float*
     - Единична цена без ДДС
   * - :deprecated:`$single_price_with_tax`
     - *float*
     - Служебна стойност за единична цена с ДДС.

			*Изполвайте original_single_price_with_tax* :deprecated_text:`Отхвърлено: */`
   * - **$original_single_price_with_tax**
     - *float*
     - Единична цена с ДДС
   * - **$quantity**
     - *float*
     - Колиество на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$line_total**
     - *float*
     - Тотал на цената спрямо това дали са поискани тотали в оригинална или системна валута и дали са с ДДС или без ДДС
   * - **$measure**
     - *string*
     - Мерна единица на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_id**
     - *int*
     - ДДС група на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax**
     - *int*
     - ДДС на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$inv_ref_num**
     - *string*
     - Референтен номер на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_reason**
     - *string*
     - 
   * - **$discount**
     - *float*
     -  **По подразбиране:** 0
   * - **$remote_ref_id**
     - *int*
     - Номер на `артикула </barsy.help/210-dictionary/article.html>`__ спрямо отдалечената система
   * - **$uuid**
     - *string*
     - Уникален номер на редър
   * - **$lot_value**
     - *string*
     - Номер на партида

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

     .. literalinclude:: ../../sources/invoices_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/invoices_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/invoices_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/invoices_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/invoices_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/invoices_get/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Фактура </barsy.help/210-dictionary/invoice.html>`__


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

