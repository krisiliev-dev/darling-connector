.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Payments_getlist
===========================================================
Списък с плащания

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/payment </barsy.help/210-dictionary/payment.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с регистрирани плащания (приходи и разходи) с богат набор от филтри — по период, `клиент </barsy.help/210-dictionary/client.html>`__ или `доставчик </barsy.help/210-dictionary/supplier.html>`__, метод на `плащане </barsy.help/210-dictionary/payment.html>`__, `потребител </barsy.help/210-dictionary/user.html>`__-създател, обект, асоцииран обект (`сметка </barsy.help/210-dictionary/account.html>`__/`фактура </barsy.help/210-dictionary/invoice.html>`__/заявка/`резервация </barsy.help/210-dictionary/reservation.html>`__), сторнирани/нормални. Поддържа странициране, сортиране, и `extra_properties` за обогатяване с данни за свързаната касова бележка или `фактура </barsy.help/210-dictionary/invoice.html>`__, които често са нужни в счетоводна интеграция.

Типични случаи: дневен касов отчет на касиер, експорт за банков риконсилиейшън, справка за просрочени постъпления от B2B `клиенти </barsy.help/210-dictionary/client.html>`__, проверка на разходи към `доставчик </barsy.help/210-dictionary/supplier.html>`__ за конкретен период.

**Име**: Payments_getlist
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
     - PaymentsListFiltersData_ 
     - Налични филтри за списъка
   * - **$extra_properties**
     - *array*
     - Допълнителни данни към плащанията

			* **base** - *Базова информация*
			* **full** - *Допълнително информация различна от базовата*
			* **invoices** - Информация за `фактура </barsy.help/210-dictionary/invoice.html>`__, ако има свързано с `плащането </barsy.help/210-dictionary/payment.html>`__
			* **receipt_data** - Информация за касовата бележка, ако има свързано с `плащането </barsy.help/210-dictionary/payment.html>`__ **По подразбиране:** []
   * - **$offset**
     - *int*
     - Начален запис **По подразбиране:** 0
   * - **$length**
     - *int*
     - максимален брой върнати записи е един рекуест **По подразбиране:** 500
   * - **$order_by**
     - *string*
     - Сортираране по **По подразбиране:** 'payment_id'


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                Списък с направените плащания
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PaymentsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PaymentsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$payment_id**
     - *int*
     - 
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, направил `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$account_id**
     - *int*
     - ID на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$user_id**
     - *int*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, приел `плащането </barsy.help/210-dictionary/payment.html>`__
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$unused**
     - *int*
     - Взема само плащания, които не са изполвани напълно
   * - **$storno_available**
     - *int*
     - Взема само плащания, по които могат да се стонират суми
   * - **$has_paid_sum**
     - *int*
     - Да има някаква платена сума
   * - **$is_printed**
     - *int*
     - Дали `плащането </barsy.help/210-dictionary/payment.html>`__ е отпечатано/фискализирано

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

     .. literalinclude:: ../../sources/payments_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/payments_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/payments_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/payments_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/payments_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/payments_getlist/barsy_api_client_simple.php
     .. code-block:: bash


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

