.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Users_get
===========================================================
Подробни данни за потребител

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/user </barsy.help/210-dictionary/user.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълен запис за един `потребител </barsy.help/210-dictionary/user.html>`__ по неговото ID — потребителско име, име и фамилия, `роля </barsy.help/210-dictionary/role.html>`__ и асоциирани права, език, обекти и `каси </barsy.help/210-dictionary/pos.html>`__, до които има достъп, статус (активен/блокиран), дата на последен вход. Паролите и PIN кодовете НЕ се връщат в чист вид (само хешове за вътрешна употреба).

Типични случаи: визуализиране на профил на `потребител </barsy.help/210-dictionary/user.html>`__ в админ панела, проверка на правата за специфична операция, синхронизация на профил към външна HR/CRM система.

**Име**: Users_get
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
   * - **$user_id**
     - *int*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
UserData_                                                              
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

UserData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: UserData

   * - Параметър
     - Тип
     - Описание
   * - **$user_id**
     - *int*
     - 
   * - **$user_name**
     - *string*
     - 
   * - **$fname**
     - *string*
     - 
   * - **$lname**
     - *string*
     - 
   * - **$role_id**
     - *int*
     - 
   * - **$role_name**
     - *string*
     - 
   * - **$show_total**
     - *bool*
     - 
   * - **$max_discount**
     - *int*
     - 
   * - **$email**
     - 
     - 
   * - **$email_verification**
     - *int*
     - 
   * - **$pin**
     - 
     - 
   * - **$card_code**
     - 
     - 
   * - **$session_timeout**
     - 
     - 
   * - **$sales_auto_logout**
     - 
     - 
   * - **$articles_report**
     - 
     - 
   * - **$streams_report**
     - 
     - 
   * - **$print_totals**
     - *bool*
     - 
   * - **$description**
     - 
     - 
   * - **$delete_flag**
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
   * - **$picture**
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
   * - **$role_id_path**
     - 
     - 
   * - **$role_path**
     - 
     - 
   * - **$role_delete_flag**
     - 
     - 
   * - **$user_theme**
     - 
     - 
   * - **$max_credit_limit**
     - *float*
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
   * - **$reset_password**
     - *int*
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

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/users_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/users_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/users_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/users_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/users_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/users_get/barsy_api_client_simple.php
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

