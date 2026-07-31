.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reservations_getpaymentlink
===========================================================
Линк за публично плащане

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/reservation </barsy.help/210-dictionary/reservation.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Генерира еднократен публичен URL, чрез който `клиентът </barsy.help/210-dictionary/client.html>`__ може да плати онлайн дължима сума по конкретна `резервация </barsy.help/210-dictionary/reservation.html>`__, без да е логнат в системата. Ако `резервацията </barsy.help/210-dictionary/reservation.html>`__ няма направени плащания и има конфигурирано капаро — сумата по подразбиране е капарото; иначе се ползва оставащата дължима сума. Конкретен метод на `плащане </barsy.help/210-dictionary/payment.html>`__ се избира с `paymethod_id` или `клиентът </barsy.help/210-dictionary/client.html>`__ избира сам. Линкът има срок на валидност (`exp_hours` или системна настройка).

Типични случаи: потвърждение на `резервация </barsy.help/210-dictionary/reservation.html>`__ по SMS/email с линк за капаро, B2B `клиент </barsy.help/210-dictionary/client.html>`__ получава линк за пълно `плащане </barsy.help/210-dictionary/payment.html>`__ преди голямо събитие, отложено `плащане </barsy.help/210-dictionary/payment.html>`__ на група гости след посещение.

**Име**: Reservations_getpaymentlink
**Категория**: Reservations


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
     - ID на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$request_sum**
     - *float*
     - Сума за `плащане </barsy.help/210-dictionary/payment.html>`__.

			*Ако не е подадена, се използва оставащата сума*
   * - **$paymethod_id**
     - *int*
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__.

			Ако не е подаден, `клиентът </barsy.help/210-dictionary/client.html>`__ избира сам
   * - **$exp_hours**
     - *float*
     - Валидност на линка в часове.

			*Ако не е подадена, се използва системната настройка*


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*string*                                                               Публичен URL за плащане
====================================================================== ======================================================================

----
 
Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reservations_getpaymentlink/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reservations_getpaymentlink/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reservations_getpaymentlink/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reservations_getpaymentlink/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reservations_getpaymentlink/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reservations_getpaymentlink/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Плащане </barsy.help/210-dictionary/payment.html>`__


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

