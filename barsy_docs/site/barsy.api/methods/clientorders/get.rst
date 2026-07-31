.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Clientorders_get
===========================================================
Преглед на клиентска заявка

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
Връща пълни данни за конкретна `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ по нейното ID — основни полета (`клиент </barsy.help/210-dictionary/client.html>`__, обект, дата на доставка, метод и адрес, бележки), текущ статус, общи суми (брутна, отстъпки, ДДС, нетна, платена, остатък), история на промените и информация за разрешените действия от страна на текущия `потребител </barsy.help/210-dictionary/user.html>`__ (`user_rights`). Самите редове с `артикули </barsy.help/210-dictionary/article.html>`__ и плащания се извличат с отделни методи.

Типични случаи: отваряне на детайлен изглед на заявка в админ панела, презареждане на актуалния статус в мобилно куриерско приложение, валидация преди приключване в `каса </barsy.help/210-dictionary/pos.html>`__.

**Име**: Clientorders_get
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
   * - **$client_order_id**
     - *int*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ClientOrderData_                                                       
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ClientOrderData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientOrderData

   * - Параметър
     - Тип
     - Описание
   * - **$client_order_id**
     - *int*
     - ID на `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__
   * - **$order_num**
     - *string*
     - Външен номер на `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ (различен от служебния)
   * - **$client_id**
     - *int*
     - Id на `клиент </barsy.help/210-dictionary/client.html>`__ по номенклатурата на barsy
   * - **$client_name**
     - *string*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ от заявката
   * - **$client_tel**
     - *string*
     - Телефонен номер на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_email**
     - *string*
     - Email адрес на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$contact_name**
     - *string*
     - Лице за контакт/получаване - може да се различава от името на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$group_id**
     - *int*
     - ID на клиентска група, към която принадлежи `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getgroups` )
   * - **$create_date**
     - *string*
     - Дата на създаване на заявката
   * - **$last_update**
     - *string*
     - Дата на последна промяна на заявката
   * - **$barsy_id**
     - *int*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който трябва да се изпрати поръчката за обработка
   * - **$barsy_name**
     - 
     - Име на търговския обект, в който трябва да се изпрати поръчката за обработка
   * - **$from_barsy_id**
     - *int*
     - ID на търговския обект, в който е създадена заявката ( виж: :doc:`../barsys/getlist` )
   * - **$from_barsy_name**
     - *string*
     - Име на търговския обект, в който е създадена заявката ( виж: :doc:`../barsys/getlist` )
   * - **$delivery_barsy_id**
     - *integer*
     - ID на търговския обект, от който ще се вземе поръчката.

			*Ако е пропуснато, се приема че ще се доставя до адрес за доставка* ( виж: :doc:`../barsys/getlist` )
   * - **$delivery_barsy_name**
     - *string*
     - Име на търговския обект, от който ще се вземе поръчката.

			*Ако е пропуснато, се приема че ще се доставя до адрес за доставка*
   * - **$delivery_address**
     - DeliveryAddressData_ 
     - Адрес за доставка
   * - **$delivery_date**
     - *datetime*
     - Дата за доставка, може да съдържа и час
   * - **$delivery_date_until**
     - *string*
     - Крайна дата/час за доставка - оформя интервал за доставка - от ‘delivery_date’ до ‘delivery_date_until’
   * - **$delivery_interval**
     - *string*
     - 
   * - **$user_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал заявката
   * - **$user_name**
     - *string*
     - Потребителско име на създателя на заявката
   * - **$total_sum**
     - *float*
     - Обща сума на заявката (преди отстъпката)
   * - **$total_real**
     - *float*
     - Обща сума на заявката (след отстъпката)
   * - **$total_paid_sum**
     - *float*
     - Платена сума по заявката
   * - **$total_remain_sum**
     - *float*
     - Оставаща сума за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$discount**
     - *float*
     - Отстъпка на цялата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$paymethod_id**
     - *integer*
     - ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ по номенклатура на barsy ( виж: :doc:`../paymentmethods/getlist` )
   * - **$preferred_paymethod_id**
     - *integer*
     - Предпочитан ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ по номенклатура на barsy ( виж: :doc:`../paymentmethods/getlist` )
   * - **$paymethod_name**
     - *string*
     - Име на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ на заявката ( виж: :doc:`../paymentmethods/getlist` )
   * - **$preferred_paymethod_name**
     - *string*
     - Име на предпочитан начина на `плащане </barsy.help/210-dictionary/payment.html>`__ на заявката ( виж: :doc:`../paymentmethods/getlist` )
   * - **$paymethod_public_name**
     - *string*
     - Публично име на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ на заявката ( виж: :doc:`../paymentmethods/getlist` )
   * - **$paymethod_description**
     - *string*
     - Описание на метода на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../paymentmethods/getlist` )
   * - **$extra_details**
     - *string*
     - Допълнителни детайли
   * - **$status_id**
     - *int*
     - ID на текущ статус на заявката ( виж: :doc:`../clientorders/getstatuslistdata` )
   * - **$status_name**
     - *string*
     - Текущ статус на заявката ( виж: :doc:`../clientorders/getstatuslistdata` )
   * - **$account_id**
     - *int*
     - ID на `сметка </barsy.help/210-dictionary/account.html>`__, създадена от тази `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ ( виж: :doc:`../accounts/get` )
   * - **$description**
     - *string*
     - Свободен текст
   * - **$tracking_number**
     - *string*
     - Номер на товарителница
   * - **$deal_id**
     - *int*
     - ID на свързана сделка
   * - **$deal_title**
     - *string*
     - Заглавие на свързаната сделка
   * - **$person_id**
     - *int*
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ към `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$person_name**
     - *string*
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$speditor_id**
     - *int*
     - ID на спедитора, избран за тази заявка ( виж: :doc:`../speditors/getlist` )
   * - **$article_count**
     - *int*
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в заявката
   * - **$can_edit_rows**
     - *int*
     - 
   * - **$ip_address**
     - *string*
     - IP адрес, от който е създадена заявката
   * - **$unp**
     - *string*
     - УНП на заявката
   * - **$user_rights**
     - ClientOrderUserRightsData_ 
     - 
   * - **$with_invoice**
     - *int*
     - Флаг, дали `клиента </barsy.help/210-dictionary/client.html>`__ желае `фактура </barsy.help/210-dictionary/invoice.html>`__ за заявката
   * - **$public_notes**
     - *string*
     - Бележки към заявката, публично видими от `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_lang_id**
     - *string*
     - Предпочитан език за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$currency_id**
     - *int*
     - 
   * - **$currency_rate**
     - *float*
     - 
   * - **$client_order_sid**
     - *string*
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

ClientOrderUserRightsData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientOrderUserRightsData

   * - Параметър
     - Тип
     - Описание
   * - **$edit**
     - *int*
     -  **По подразбиране:** 0
   * - **$change_status**
     - *int*
     -  **По подразбиране:** 0
   * - **$make_account**
     - *int*
     -  **По подразбиране:** 0

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

     .. literalinclude:: ../../sources/clientorders_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/clientorders_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/clientorders_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/clientorders_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/clientorders_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clientorders_get/barsy_api_client_simple.php
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

