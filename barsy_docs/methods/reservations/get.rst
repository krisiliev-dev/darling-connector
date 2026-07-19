.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reservations_get
===========================================================
Преглед на резервация

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/reservation </barsy.help/210-dictionary/reservation.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълни данни за конкретна `резервация </barsy.help/210-dictionary/reservation.html>`__ — `клиент </barsy.help/210-dictionary/client.html>`__, място, час на начало/край, брой персони, бележки, статус, общи суми. Чрез `extra_properties` могат да се поискат допълнителни секции като поръчки (`orders`), направени плащания (`res_payments`) и създадените от `резервацията </barsy.help/210-dictionary/reservation.html>`__ `сметки </barsy.help/210-dictionary/account.html>`__ (`res_accounts`). Достъпен е и за публичен контекст (логнат `клиент </barsy.help/210-dictionary/client.html>`__ проверява своя `резервация </barsy.help/210-dictionary/reservation.html>`__ от уебсайт) — там данните се ограничават до тези, които `клиентът </barsy.help/210-dictionary/client.html>`__ има право да види.

Типични случаи: домакин в ресторант проверява детайли на пристигаща `резервация </barsy.help/210-dictionary/reservation.html>`__, `клиент </barsy.help/210-dictionary/client.html>`__ в публичния портал вижда статуса на своята `резервация </barsy.help/210-dictionary/reservation.html>`__, потвърждение по email с детайли преди визита.

**Име**: Reservations_get
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
   * - **$reservation_id**
     - *int*
     - 
   * - **$extra_properties**
     - *array*
     - Допълнителни данни за `резервациите </barsy.help/210-dictionary/reservation.html>`__

			* **orders** - *Инфорамция за поръчките в резервацита*
			* **res_payments** - Информация за плащанията към `резервацията </barsy.help/210-dictionary/reservation.html>`__
			* **res_accounts** - Информация за `сметките </barsy.help/210-dictionary/account.html>`__ към `резервацията </barsy.help/210-dictionary/reservation.html>`__ **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ReservationData_                                                       
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

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

     .. literalinclude:: ../../sources/reservations_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reservations_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reservations_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reservations_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reservations_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reservations_get/barsy_api_client_simple.php
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

