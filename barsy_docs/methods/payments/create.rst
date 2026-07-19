.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Payments_create
===========================================================
Създаване на плащане

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/payment </barsy.help/210-dictionary/payment.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира ново парично движение (приход или разход) в системата с подаден метод на `плащане </barsy.help/210-dictionary/payment.html>`__, сума, `клиент </barsy.help/210-dictionary/client.html>`__, документална дата и референтен номер. `Плащането </barsy.help/210-dictionary/payment.html>`__ може да остане самостоятелно или да се асоциира с една или повече `сметки </barsy.help/210-dictionary/account.html>`__ чрез масива `accounts` — тогава внесената сума се разпределя върху остатъците им. По същия начин през специализирани полета може да се прикачи към `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__, `резервация </barsy.help/210-dictionary/reservation.html>`__ или складово `зареждане </barsy.help/210-dictionary/storeload.html>`__ (за разход към `доставчик </barsy.help/210-dictionary/supplier.html>`__).

Типични случаи: внасяне на капаро за бъдеща поръчка, авансово `плащане </barsy.help/210-dictionary/payment.html>`__ към `доставчик </barsy.help/210-dictionary/supplier.html>`__ преди доставка, кеш погасяване на стар дълг на корпоративен `клиент </barsy.help/210-dictionary/client.html>`__, постъпление от банково извлечение което се разнася върху неплатени `фактури </barsy.help/210-dictionary/invoice.html>`__.

**Име**: Payments_create
**Категория**: Cashdesk,Top


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$paid_sum**
     - *float*
     - Платена сума
   * - **$client_id**
     - *int*
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../payments/create` )
   * - **$paymethod_id**
     - *int*
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$description**
     - *string*
     - Свободен текст
   * - **$ref_num**
     - *string*
     - Референтен номер (свободен текст)
   * - **$ref_date**
     - *datetime*
     - Документална дата на събитието (Само ако се различава от текущата)
   * - **$accounts**
     - *array*
     - Списък с account_id на `сметки </barsy.help/210-dictionary/account.html>`__ за свързване към това `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$payment_type**
     - *string*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на плащането
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

     .. literalinclude:: ../../sources/payments_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/payments_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/payments_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/payments_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/payments_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/payments_create/barsy_api_client_simple.php
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

