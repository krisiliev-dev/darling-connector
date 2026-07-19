.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Users_getcurrent
===========================================================
Текущ потребител

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/user </barsy.help/210-dictionary/user.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща данни за `потребителя </barsy.help/210-dictionary/user.html>`__, който е автентикиран в текущата сесия — ID, име, `роля </barsy.help/210-dictionary/role.html>`__, права, език, асоциирани обекти/`каси </barsy.help/210-dictionary/pos.html>`__, аватар. Не изисква специални права (`__no_rights_check__`) — всеки логнат `потребител </barsy.help/210-dictionary/user.html>`__ има право да види своя собствен профил. Често е първият endpoint, който се извиква след вход в системата за инициализация на UI.

Типични случаи: bootstrap на касов/админ интерфейс след вход, проверка дали сесията още е валидна, визуализиране на име на `потребителя </barsy.help/210-dictionary/user.html>`__ в горната лента, диагностика на разрешените права.

**Име**: Users_getcurrent
**Категория**: Catalog


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
UserCurrentData_                                                       
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

UserCurrentData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: UserCurrentData

   * - Параметър
     - Тип
     - Описание
   * - **$user_id**
     - *int*
     -  **По подразбиране:** -1
   * - **$original_user_id**
     - *int*
     - в него се пази ID на оригиналния `потребител </barsy.help/210-dictionary/user.html>`__ - това може да е само SU, когато е в режим да вижда системта, като друг `потребител </barsy.help/210-dictionary/user.html>`__
   * - **$user_name**
     - 
     -  **По подразбиране:** 'anonymous'
   * - **$fname**
     - 
     -  **По подразбиране:** 'Anonymous'
   * - **$lname**
     - 
     - 
   * - **$role_name**
     - 
     - 
   * - **$max_discount**
     - *int*
     -  **По подразбиране:** 0
   * - **$role_id**
     - *int*
     -  **По подразбиране:** 0
   * - **$role_cat_id**
     - *int*
     -  **По подразбиране:** 0
   * - **$show_total**
     - *bool*
     -  **По подразбиране:** false
   * - **$print_totals**
     - *bool*
     -  **По подразбиране:** false
   * - **$articles_report**
     - 
     -  **По подразбиране:** false
   * - **$streams_report**
     - 
     -  **По подразбиране:** false
   * - **$email**
     - 
     - 
   * - **$email_verification**
     - *int*
     - 
   * - **$auth_type**
     - *string*
     - 

			* **PIN** - *Липсва описание*
			* **ID** - *Липсва описание*
			* **PASS** - *Липсва описание*
			* **REMOTE_SYSTEM** - *Липсва описание*
			* **WEB_AUTHN** - *Липсва описание*
   * - **$sales_auto_logout**
     - 
     - 
   * - **$delete_flag**
     - 
     -  **По подразбиране:** 0
   * - **$picture**
     - 
     - 
   * - **$lang_id**
     - *string*
     - 
   * - **$user_theme**
     - 
     - 
   * - **$user_posx_theme**
     - 
     -  **По подразбиране:** 'white_theme'
   * - **$user_admin_theme**
     - 
     -  **По подразбиране:** 'white_theme'
   * - **$reports_limit**
     - 
     -  **По подразбиране:** 0
   * - **$session_timeout**
     - 
     - 
   * - **$reset_password**
     - 
     - 
   * - **$role_id_path**
     - 
     - 
   * - **$max_credit_limit**
     - 
     - 
   * - **$token_is_expired**
     - 
     - 
   * - **$token_label**
     - 
     - 
   * - **$access_profile_id**
     - *int*
     - 
   * - **$auth_remote_system**
     - RemoteSystemsData_ 
     - 
   * - **$blocked_time**
     - *string*
     - 
   * - **$max_markup**
     - *int*
     -  **По подразбиране:** 0
   * - **$card_code_login**
     - *bool*
     - 
   * - **$card_code_length**
     - *int*
     - 
   * - **$request_limiter**
     - *int*
     -  **По подразбиране:** 0
   * - **$request_limiter_1min**
     - *int*
     -  **По подразбиране:** 0
   * - **$has_pin**
     - *bool*
     - Флаг дали `потребителя </barsy.help/210-dictionary/user.html>`__ има ПИН
   * - **$pin**
     - 
     - 
   * - **$card_code**
     - 
     - 
   * - **$description**
     - 
     - 
   * - **$barsys**
     - 
     - 
   * - **$barsys_names**
     - 
     - 
   * - **$create_date**
     - 
     - 
   * - **$last_update**
     - 
     - 
   * - **$phone**
     - 
     - 
   * - **$has_password**
     - 
     - 
   * - **$pager_num**
     - 
     - 
   * - **$lang_name**
     - 
     - 
   * - **$role_path**
     - 
     - 
   * - **$role_delete_flag**
     - 
     - 
   * - **$rights**
     - *stdClass*
     - 
   * - **$system_contact**
     - *int*
     - 
   * - **$print_totals_name**
     - 
     - 
   * - **$streams_report_name**
     - 
     - 
   * - **$passwd_attempts**
     - *int*
     - 
   * - **$user_entity_id**
     - *string*
     - 
   * - **$poses**
     - *array* | *string*
     -  **По подразбиране:** []

-----

RemoteSystemsData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: RemoteSystemsData

   * - Параметър
     - Тип
     - Описание
   * - **$remote_id**
     - *int*
     - 
   * - **$name**
     - *string*
     - 
   * - **$url**
     - *string*
     - 
   * - **$user_name**
     - *string*
     - 
   * - **$passwd**
     - *string*
     - 
   * - **$trust_ssl**
     - *bool*
     - 
   * - **$class_name**
     - *string*
     - 
   * - **$protocol_id**
     - *int*
     - 
   * - **$protocol_name**
     - *string*
     - 
   * - **$settings**
     - *object*
     - 
   * - **$user_id**
     - *int*
     - 
   * - **$barsy_id**
     - *int*
     - 
   * - **$debug_mode**
     - *int*
     - 
   * - **$supported_actions**
     - *array*
     - 
   * - **$supplier_id**
     - *int*
     - 
   * - **$supplier_name**
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

     .. literalinclude:: ../../sources/users_getcurrent/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/users_getcurrent/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/users_getcurrent/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/users_getcurrent/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/users_getcurrent/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/users_getcurrent/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Потребител </barsy.help/210-dictionary/user.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

