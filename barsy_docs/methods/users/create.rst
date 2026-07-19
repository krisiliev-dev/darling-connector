.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Users_create
===========================================================
Създаване на потребител

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/user </barsy.help/210-dictionary/user.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира нов `потребител </barsy.help/210-dictionary/user.html>`__ на системата (служител, оператор, мениджър) с основни данни — потребителско име, парола, PIN код (за бърз вход в POS), име и фамилия, `роля </barsy.help/210-dictionary/role.html>`__ (определя правата му), език на интерфейса, обекти и `каси </barsy.help/210-dictionary/pos.html>`__, до които има достъп. `Потребителят </barsy.help/210-dictionary/user.html>`__ се създава в контекста на текущия активен `потребител </barsy.help/210-dictionary/user.html>`__, който трябва да има право `users_edit`.

Типични случаи: добавяне на новонает служител, регистрация на нов касиер преди стартиране на смяна, импорт на `потребители </barsy.help/210-dictionary/user.html>`__ от HR система, създаване на тестов акаунт за обучение.

**Име**: Users_create
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
   * - **$user**
     - UserInputData_ 
     - Данни за `потребителя </barsy.help/210-dictionary/user.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на създадения потребител
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

UserInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: UserInputData

   * - Параметър
     - Тип
     - Описание
   * - **$barsys**
     - *array*
     - 
   * - **$user_posx_theme**
     - 
     - 
   * - **$user_admin_theme**
     - 
     - 
   * - **$user_name**
     - *string*
     - 
   * - **$fname**
     - 
     - 
   * - **$lname**
     - 
     - 
   * - **$email**
     - *string*
     - 
   * - **$role_id**
     - 
     - 
   * - **$lang_id**
     - *string*
     - 
   * - **$description**
     - 
     - 
   * - **$passwd**
     - 
     - 
   * - **$pin**
     - 
     - 
   * - **$phone**
     - 
     - 
   * - **$phone_private**
     - 
     - 
   * - **$phone_internal**
     - 
     - 
   * - **$phone_messanger**
     - 
     - 
   * - **$pager_num**
     - 
     - 
   * - **$card_code**
     - *string*
     - 
   * - **$max_discount**
     - 
     - 
   * - **$print_totals**
     - 
     -  **По подразбиране:** 0
   * - **$remote_access**
     - 
     -  **По подразбиране:** 0
   * - **$session_timeout**
     - 
     -  **По подразбиране:** 30
   * - **$sales_auto_logout**
     - *int*
     - 
   * - **$show_total**
     - 
     -  **По подразбиране:** 0
   * - **$streams_report**
     - 
     -  **По подразбиране:** 0
   * - **$articles_report**
     - 
     -  **По подразбиране:** 0
   * - **$delete_flag**
     - 
     -  **По подразбиране:** 0
   * - **$max_credit_limit**
     - 
     -  **По подразбиране:** 0
   * - **$system_contact**
     - 
     -  **По подразбиране:** 0
   * - **$reset_password**
     - 
     -  **По подразбиране:** 0
   * - **$user_theme**
     - 
     - 
   * - **$picture**
     - 
     - 
   * - **$passwd_attempts**
     - *int*
     -  **По подразбиране:** 0
   * - **$blocked_time**
     - *string*
     - 
   * - **$access_profile_id**
     - *int*
     - 
   * - **$max_markup**
     - *int*
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

     .. literalinclude:: ../../sources/users_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/users_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/users_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/users_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/users_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/users_create/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Потребител </barsy.help/210-dictionary/user.html>`__


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

