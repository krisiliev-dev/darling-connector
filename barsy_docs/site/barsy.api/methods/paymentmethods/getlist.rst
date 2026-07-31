.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Paymentmethods_getlist
===========================================================
Списък с начини на плащане

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща наличните методи на `плащане </barsy.help/210-dictionary/payment.html>`__, конфигурирани в системата и разрешени за текущия `потребител </barsy.help/210-dictionary/user.html>`__ и контекст (admin или public). За всеки метод се връща ID, име, тип (брой, карта, банков превод, `ваучер </barsy.help/210-dictionary/card.html>`__, кредит, онлайн платежен оператор), икона, флагове за разрешено сторно/частично `плащане </barsy.help/210-dictionary/payment.html>`__, валута, асоциация с конкретно фискално устройство или платежен терминал. Резултатът се филтрира спрямо правата на `потребителя </barsy.help/210-dictionary/user.html>`__ и активността на платежния провайдър — например онлайн методи се показват само ако кредитната интеграция е здравословна.

Типични случаи: попълване на dropdown за избор на метод при затваряне на `сметка </barsy.help/210-dictionary/account.html>`__, избор на канал на `плащане </barsy.help/210-dictionary/payment.html>`__ в публичен payment link, проверка какви методи са разрешени за конкретна `каса </barsy.help/210-dictionary/pos.html>`__.

**Име**: Paymentmethods_getlist
**Категория**: Settings


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
     - PaymentMethodsListFiltersData_ 
     -  **По подразбиране:** []
   * - **$extra_properties**
     - PaymentMethodsExtraPropertiesData_ 
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PaymentMethodData_                                                     
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PaymentMethodsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PaymentMethodsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$return_mode**
     - *int*
     -  **По подразбиране:** 2
   * - **$paymethod_id**
     - *int*
     - Филтър по ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$barsy_id**
     - *int*
     - Филтър по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$role_id**
     - *int*
     - Филтър по `роля </barsy.help/210-dictionary/role.html>`__
   * - **$is_public**
     - *int*
     - Филтър по публичност на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ - филтира начини на `плащане </barsy.help/210-dictionary/payment.html>`__ разрешени за текущия публичен достъп, ако има такъв
   * - **$delete_flag**
     - *int*
     - Филтър дали е изтрит начин на `плащане </barsy.help/210-dictionary/payment.html>`__ **По подразбиране:** 0
   * - **$type_id**
     - *int*
     - Филтър по Тип
   * - **$has_provider**
     - *int*
     - 
   * - **$provider_name**
     - *string*
     - Филтрира по служебно име на външна система
   * - **$show_in_invoice**
     - *int*
     - Филтър по "дали начина на `плащане </barsy.help/210-dictionary/payment.html>`__ се показва във `фактура </barsy.help/210-dictionary/invoice.html>`__"
   * - **$storno_enable**
     - *int*
     - Филтър по флаг за възможност за задаване на сторно `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$country_id**
     - *int*
     - Филтър по страна на доставка
   * - **$currency_id**
     - *int*
     - Филтър по страна на доставка

-----

PaymentMethodsExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PaymentMethodsExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$public_name_ml**
     - *bool*
     - Обект с данни за превод на публичното име **По подразбиране:** false
   * - **$currencies**
     - *bool*
     - Валути **По подразбиране:** false
   * - **$provider_data**
     - *bool*
     -  **По подразбиране:** false

-----

PaymentMethodData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PaymentMethodData

   * - Параметър
     - Тип
     - Описание
   * - **$paymethod_id**
     - *int*
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$name**
     - *string*
     - Име на начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$fx**
     - *int*
     - Извършва ли фискална операция
   * - **$require_info**
     - *string*
     - 
   * - **$require_info_title**
     - *string*
     - 
   * - **$require_info_list_data_source**
     - *string*
     - Източник на списък с данни
   * - **$provider_id**
     - *int*
     - 
   * - **$description**
     - 
     - 
   * - **$pay_from_client_balance**
     - 
     - 
   * - **$public_name**
     - *string*
     - Публично име
   * - **$type_id**
     - *int*
     - 
   * - **$card_type_id**
     - *int*
     - Тип `плащане </barsy.help/210-dictionary/payment.html>`__ като Бонус програма и `Ваучер </barsy.help/210-dictionary/card.html>`__ са обвързани с различен вид карти.

			*В тази стойност пазим този типът на картата*
   * - **$settings**
     - 
     - 
   * - **$show_in_invoice**
     - *int*
     - 
   * - **$delete_flag**
     - *int*
     -  **По подразбиране:** 0
   * - **$deny_anonymous**
     - *int*
     -  **По подразбиране:** 0
   * - **$public_name_ml**
     - MultiLanguageData_ 
     - 
   * - **$currencies**
     - *array*
     - 

-----

MultiLanguageData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: MultiLanguageData

   * - Параметър
     - Тип
     - Описание
   * - **$bg_BG**
     - *string*
     - 
   * - **$en_US**
     - *string*
     - 
   * - **$de_DE**
     - *string*
     - 
   * - **$es_ES**
     - *string*
     - 
   * - **$fr_FR**
     - *string*
     - 
   * - **$it_IT**
     - *string*
     - 
   * - **$ro_RO**
     - *string*
     - 
   * - **$ru_RU**
     - *string*
     - 
   * - **$sr_RS**
     - *string*
     - 
   * - **$el_GR**
     - *string*
     - 
   * - **$tr_TR**
     - *string*
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

     .. literalinclude:: ../../sources/paymentmethods_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/paymentmethods_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/paymentmethods_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/paymentmethods_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/paymentmethods_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/paymentmethods_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Плащане </barsy.help/210-dictionary/payment.html>`__


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

