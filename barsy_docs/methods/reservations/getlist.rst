.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reservations_getlist
===========================================================
Списък с резервации

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/reservation </barsy.help/210-dictionary/reservation.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с `резервации </barsy.help/210-dictionary/reservation.html>`__ с богат набор от филтри — по период (начало/край), място, `клиент </barsy.help/210-dictionary/client.html>`__, статус, обект, дата на създаване, наличие на капаро. Поддържа странициране, сортиране и `extra_properties` за обогатяване с информация за местата, обекта или допълнителни мета-данни. В публичен контекст филтрите автоматично се ограничават до `резервациите </barsy.help/210-dictionary/reservation.html>`__ на логнатия `клиент </barsy.help/210-dictionary/client.html>`__.

Типични случаи: домакински изглед "пристигащи `резервации </barsy.help/210-dictionary/reservation.html>`__ днес", календарен изглед на `резервациите </barsy.help/210-dictionary/reservation.html>`__ по места, личен профил на `клиент </barsy.help/210-dictionary/client.html>`__ с история на `резервациите </barsy.help/210-dictionary/reservation.html>`__, експорт за маркетингова кампания (например `клиенти </barsy.help/210-dictionary/client.html>`__ с минала `резервация </barsy.help/210-dictionary/reservation.html>`__ преди година).

**Име**: Reservations_getlist
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
   * - **$filters**
     - ReservationsListFiltersData_ 
     - Налични филтри за списъка
   * - **$extra_properties**
     - ReservationsListExtraPropertiesData_ 
     - Искане на допълнителни данни за всеки запис
   * - **$offset**
     - *int*
     - Номер на ред, от който да започне списъкът (странициране) **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - ReservationsListOrderByData_ 
     - Подреждане — низ, масив или обект колона⇒посока (напр. {"from_date":"asc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ReservationData_                                                       Списък от резервации с данни според исканите ($extra_properties)
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReservationsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReservationsListFiltersData

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
     - Филтър по id на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$user_id**
     - *int*
     - Филтър по id на `потребител </barsy.help/210-dictionary/user.html>`__ (създател) ( виж: :doc:`../users/getlist` )
   * - **$client_id**
     - *int*
     - Филтър по id на `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$create_date**
     - *datetime*
     - Филтър по дата на създаване
   * - **$last_update**
     - *datetime*
     - Филтър по дата на актуализация
   * - **$from_date**
     - *datetime*
     - Филтър по начална дата на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$to_date**
     - *datetime*
     - Филтър по крайна дата на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$date_window**
     - *datetime*
     - Филтър по "дата от до"
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$delete_flag**
     - *int*
     - Филтър по флаг "Изтрит" **По подразбиране:** 0
   * - **$reservations_today**
     - *bool*
     - Взима `резервациите </barsy.help/210-dictionary/reservation.html>`__ за деня
   * - **$status_and_interval**
     - *int* | *array*
     - Филтър по статус и сегашна дата + интервал 5 часа
   * - **$status_id**
     - *int* | *array*
     - Филтър по статус
   * - **$for_today**
     - *bool*
     - Филтър по днешният ден
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$q**
     - *string*
     - Smart search по име, телефон или `клиент </barsy.help/210-dictionary/client.html>`__
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$reservation_id**
     - *int*
     - Филтър по id на `резервация </barsy.help/210-dictionary/reservation.html>`__ ( виж: :doc:`../reservations/get` )

-----

ReservationsListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към `резервация </barsy.help/210-dictionary/reservation.html>`__. Всяка опция включва съответните колони към данните за
		*всеки запис. Основните данни се връщат винаги, останалите при стойност true.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReservationsListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$all**
     - *bool*
     - Пълни данни — места, обслужващи, суми по `резервацията </barsy.help/210-dictionary/reservation.html>`__ **По подразбиране:** false
   * - **$by_place**
     - *bool*
     - Данни по място — един ред на място; резултатът се групира по place_id **По подразбиране:** false
   * - **$barsy_name**
     - *bool*
     - Име на търговския обект ( виж: :doc:`../barsys/getlist` ) **По подразбиране:** false
   * - **$orders**
     - *bool*
     - `Артикули </barsy.help/210-dictionary/article.html>`__, включени в `резервацията </barsy.help/210-dictionary/reservation.html>`__ (зареждат се след основната заявка) **По подразбиране:** false

-----

ReservationsListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с `резервации </barsy.help/210-dictionary/reservation.html>`__ (Reservations_getlist).
		Подава се като низ ("from_date asc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReservationsListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - **$reservation_id**
     - *string*
     - Подреждане по ID на `резервация </barsy.help/210-dictionary/reservation.html>`__
   * - **$from_date**
     - *string*
     - Подреждане по начална дата
   * - **$to_date**
     - *string*
     - Подреждане по крайна дата
   * - **$create_date**
     - *string*
     - Подреждане по дата на създаване
   * - **$client_name**
     - *string*
     - Подреждане по име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$status_id**
     - *string*
     - Подреждане по статус

-----

ReservationData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReservationData

   * - Параметър
     - Тип
     - Описание
   * - **$reservation_id**
     - *int*
     - ID на `резервация </barsy.help/210-dictionary/reservation.html>`__
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__, за който е `резервацията </barsy.help/210-dictionary/reservation.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getlist` )
   * - **$client_group_id**
     - *int*
     - ID на група на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clientgroups/getlist` )
   * - **$user_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `резервацията </barsy.help/210-dictionary/reservation.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$person_id**
     - *int*
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../persons/getlist` )
   * - **$contact_name**
     - *string*
     - Лице за контакт към `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$phone**
     - *string*
     - Телефон за контакт към резеревацията
   * - **$from_date**
     - *string*
     - Начална дата на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$to_date**
     - *string*
     - Крайна дата на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$wait_interval**
     - *string*
     - Време за изчакване след начало на `резервацията </barsy.help/210-dictionary/reservation.html>`__, ако не е потвърдено идването
   * - **$caparo**
     - *float*
     - Сума, необходима за капариране на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$description**
     - *string*
     - Описание, свободен текст
   * - **$create_date**
     - *string*
     - Дата на създаване
   * - **$last_update**
     - *string*
     - Дата на последна актуализация
   * - **$status_id**
     - *int*
     - Статус на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$delete_flag**
     - *int*
     - Флаг за изтриване на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$persons**
     - *int*
     - Брой посетители към `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$discount**
     - *float*
     - Отстъпка в проценти на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$total_sum**
     - *float*
     - Сума на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$total_real**
     - *float*
     - Сума на `резервацията </barsy.help/210-dictionary/reservation.html>`__ след остъпка
   * - **$total_paid_sum**
     - *float*
     - Платена сума по `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$total_remain_sum**
     - *float*
     - Остатък за `плащане </barsy.help/210-dictionary/payment.html>`__

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

     .. literalinclude:: ../../sources/reservations_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reservations_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reservations_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reservations_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reservations_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reservations_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Резервация </barsy.help/210-dictionary/reservation.html>`__


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

