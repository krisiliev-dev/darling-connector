.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Users_getlist
===========================================================
Списък с потребители

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/user </barsy.help/210-dictionary/user.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с `потребителите </barsy.help/210-dictionary/user.html>`__ на системата с филтри по име, `роля </barsy.help/210-dictionary/role.html>`__, обект, активност, наличие на PIN. Поддържа странициране, сортиране и `extra_properties` за обогатяване с допълнителни секции (права, асоциирани обекти/`каси </barsy.help/210-dictionary/pos.html>`__, последна активност). Резултатът се ограничава спрямо правата на текущия `потребител </barsy.help/210-dictionary/user.html>`__ — например линеен мениджър вижда само `потребителите </barsy.help/210-dictionary/user.html>`__ в своите обекти.

Типични случаи: попълване на dropdown "`Потребител </barsy.help/210-dictionary/user.html>`__" при дефиниране на отговорност, листинг на `потребителите </barsy.help/210-dictionary/user.html>`__ в админ панела, експорт за HR/одит, филтриране в справки "`Продажби </barsy.help/210-dictionary/sale.html>`__ по `потребител </barsy.help/210-dictionary/user.html>`__".

**Име**: Users_getlist
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
     - UsersListFiltersData_ 
     - Налични филтри за списъка с `потребители </barsy.help/210-dictionary/user.html>`__
   * - **$extra_properties**
     - UsersListExtraPropertiesData_ 
     - Искане на допълнителни данни за всеки `потребител </barsy.help/210-dictionary/user.html>`__
   * - **$offset**
     - *int*
     - Номер на ред, от който да започне списъкът (странициране) **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - UsersListOrderByData_ 
     - Подреждане — обект колона⇒посока (напр. {"user_name":"asc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
UserData_                                                              Списък с потребители с данни според исканите ($extra_properties)
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

UsersListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: UsersListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$user_id**
     - *int*
     - Филтър по ID `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../users/get` , :doc:`../users/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$log_time**
     - *datetime*
     - Филтър по последно логване на `потребител </barsy.help/210-dictionary/user.html>`__
   * - **$create_date**
     - *datetime*
     - Филтър по дата на създаване на `потребител </barsy.help/210-dictionary/user.html>`__
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$user_name**
     - *string*
     - Филтър по име на `потребител </barsy.help/210-dictionary/user.html>`__.

			*Намира и при частично съвпадение*
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$role_id**
     - *int*
     - Филтър по ID на `роля </barsy.help/210-dictionary/role.html>`__ на `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../roles/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$delete_flag**
     - *int*
     - Филтър по флаг за изтрит **По подразбиране:** 0
   * - **$role_delete_flag**
     - *int*
     - Филтър по флаг за изтрита `роля </barsy.help/210-dictionary/role.html>`__ на `потребител </barsy.help/210-dictionary/user.html>`__
   * - **$no_system_users**
     - *int*
     - Филтър - изключва системните `потребители </barsy.help/210-dictionary/user.html>`__ (USER_ID <= 1)
   * - **$user_session**
     - *int*
     - Филтър по активна сесия на `потребителя </barsy.help/210-dictionary/user.html>`__ в текущия период/обект (изисква extra property user_session)
   * - **$has_pin**
     - *int*
     - Филтър - има ли `потребителят </barsy.help/210-dictionary/user.html>`__ зададен пин
   * - **$transfer_account_flag**
     - *int*
     - Филтър - право за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ на `сметка </barsy.help/210-dictionary/account.html>`__

-----

UsersListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към `потребител </barsy.help/210-dictionary/user.html>`__. Всяка опция включва съответната колона към данните за
		всеки `потребител </barsy.help/210-dictionary/user.html>`__ от списъка. Основните данни се връщат винаги, а останалите при стойност true.

.. list-table::
   :header-rows: 1
   :align: center
   :name: UsersListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Основни данни`
     - 
     - 
   * - **$user_id**
     - *bool*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** true
   * - **$user_name**
     - *bool*
     - Потребителско име (за вход) **По подразбиране:** true
   * - **$fname**
     - *bool*
     - Собствено име **По подразбиране:** true
   * - **$lname**
     - *bool*
     - Фамилия **По подразбиране:** true
   * - **$full_name**
     - *bool*
     - Пълно име (собствено + фамилия; ако липсват — потребителското име) **По подразбиране:** true
   * - **$role_id**
     - *bool*
     - ID на `ролята </barsy.help/210-dictionary/role.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../roles/getlist` ) **По подразбиране:** false
   * - **$role_name**
     - *bool*
     - Име на `ролята </barsy.help/210-dictionary/role.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** true
   * - **$description**
     - *bool*
     - Описание/бележка за `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$delete_flag**
     - *bool*
     - Флаг дали `потребителят </barsy.help/210-dictionary/user.html>`__ е изтрит **По подразбиране:** true
   * - **$picture**
     - *bool*
     - Изображение (аватар) на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$lang_id**
     - *bool*
     - ID на езика на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$system_contact**
     - *bool*
     - Дали `потребителят </barsy.help/210-dictionary/user.html>`__ е системен контакт **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
   * - **$show_total**
     - *bool*
     - Дали `потребителят </barsy.help/210-dictionary/user.html>`__ вижда тотали (обороти) **По подразбиране:** false
   * - **$max_discount**
     - *bool*
     - Максимална отстъпка, която `потребителят </barsy.help/210-dictionary/user.html>`__ може да дава **По подразбиране:** false
   * - **$max_credit_limit**
     - *bool*
     - Максимален кредитен лимит на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
   * - **$email**
     - *bool*
     - Имейл на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$email_verification**
     - *bool*
     - Статус на верификация на имейла **По подразбиране:** false
   * - **$pin**
     - *bool*
     - PIN код за вход **По подразбиране:** false
   * - **$card_code**
     - *bool*
     - Код на карта за вход **По подразбиране:** false
   * - **$remote_access**
     - *bool*
     - Право за отдалечен достъп **По подразбиране:** false
   * - **$session_timeout**
     - *bool*
     - Таймаут на сесията (в секунди) **По подразбиране:** false
   * - **$sales_auto_logout**
     - *bool*
     - Автоматичен изход след `продажба </barsy.help/210-dictionary/sale.html>`__ **По подразбиране:** false
   * - **$articles_report**
     - *bool*
     - Настройка за справка по `артикули </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - **$streams_report**
     - *bool*
     - Настройка за справка по `потоци </barsy.help/210-dictionary/flow.html>`__ **По подразбиране:** false
   * - **$print_totals**
     - *bool*
     - Настройка за печат на тотали **По подразбиране:** false
   * - **$phone**
     - *bool*
     - Телефон на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$has_password**
     - *bool*
     - Има ли `потребителят </barsy.help/210-dictionary/user.html>`__ зададена парола **По подразбиране:** false
   * - **$pager_num**
     - *bool*
     - Номер на пейджър **По подразбиране:** false
   * - **$print_totals_name**
     - *bool*
     - Текстово представяне на настройката за печат на тотали **По подразбиране:** false
   * - **$streams_report_name**
     - *bool*
     - Текстово представяне на настройката за справка по `потоци </barsy.help/210-dictionary/flow.html>`__ **По подразбиране:** false
   * - **$reset_password**
     - *bool*
     - Флаг дали се изисква смяна на паролата **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$barsys**
     - *bool*
     - Списък с ID на `търговските обекти </barsy.help/210-dictionary/barsy.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$barsys_names**
     - *bool*
     - Имена на `търговските обекти </barsy.help/210-dictionary/barsy.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$role_id_path**
     - *bool*
     - Път от ID-та на `ролите </barsy.help/210-dictionary/role.html>`__ (йерархия на `ролята </barsy.help/210-dictionary/role.html>`__) **По подразбиране:** false
   * - **$role_path**
     - *bool*
     - Път от имена на `ролите </barsy.help/210-dictionary/role.html>`__ (йерархия на `ролята </barsy.help/210-dictionary/role.html>`__) **По подразбиране:** false
   * - **$role_delete_flag**
     - *bool*
     - Флаг дали `ролята </barsy.help/210-dictionary/role.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__ е изтрита **По подразбиране:** false
   * - **$rights**
     - *bool*
     - Списък с правата (API действия) на `потребителя </barsy.help/210-dictionary/user.html>`__ според `ролята </barsy.help/210-dictionary/role.html>`__ му **По подразбиране:** false
   * - **$current_barsy_access**
     - *bool*
     - Има ли `потребителят </barsy.help/210-dictionary/user.html>`__ достъп до текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (изисква контекст на обект) **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
   * - **$create_date**
     - *bool*
     - Дата на създаване на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$last_update**
     - *bool*
     - Дата на последна промяна на `потребителя </barsy.help/210-dictionary/user.html>`__ **По подразбиране:** false
   * - **$user_session**
     - *bool*
     - Състояние на активната сесия на `потребителя </barsy.help/210-dictionary/user.html>`__ в текущия период/обект **По подразбиране:** false

-----

UsersListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с `потребители </barsy.help/210-dictionary/user.html>`__ (Users_getlist).
		Подава се като асоциативен масив колона⇒посока (напр. ["user_name" => "asc", "create_date" => "desc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

.. list-table::
   :header-rows: 1
   :align: center
   :name: UsersListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$user_id**
     - *string*
     - Подреждане по ID на `потребител </barsy.help/210-dictionary/user.html>`__
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$user_name**
     - *string*
     - Подреждане по потребителско име
   * - **$fname**
     - *string*
     - Подреждане по собствено име
   * - **$lname**
     - *string*
     - Подреждане по фамилия
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$role_id**
     - *string*
     - Подреждане по ID на `роля </barsy.help/210-dictionary/role.html>`__
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$create_date**
     - *string*
     - Подреждане по дата на създаване
   * - **$last_update**
     - *string*
     - Подреждане по дата на последна промяна
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$delete_flag**
     - *string*
     - Подреждане по флаг за изтрит
   * - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
   * - **$user_session**
     - *string*
     - Подреждане по състояние на активната сесия (изисква extra property user_session)

-----

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

     .. literalinclude:: ../../sources/users_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/users_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/users_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/users_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/users_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/users_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Потребител </barsy.help/210-dictionary/user.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 
 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

