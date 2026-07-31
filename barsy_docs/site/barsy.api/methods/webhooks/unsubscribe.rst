.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Webhooks_unsubscribe
===========================================================
Премахване на абонамент

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.api: `integrations/40-webhooks </barsy.api/integrations/40-webhooks.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Премахва Webhook `абонамент </barsy.help/210-dictionary/subscription.html>`__ за конкретен тип събитие (`event_type_id`) на текущия `потребител </barsy.help/210-dictionary/user.html>`__. След премахване системата престава да изпраща уведомления за това събитие. Действието е необратимо — за временно спиране без премахване виж `Webhooks_change_status` или `Webhooks_deactivate`.

Типични случаи: преместване на интеграцията към друг URL (отписване + ново абониране), окончателно прекратяване на интеграция при смяна на `доставчик </barsy.help/210-dictionary/supplier.html>`__, почистване след тестване.

**Име**: Webhooks_unsubscribe
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
   * - **$event_type_id**
     - *int*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*void*                                                                 
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

     .. literalinclude:: ../../sources/webhooks_unsubscribe/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/webhooks_unsubscribe/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/webhooks_unsubscribe/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/webhooks_unsubscribe/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/webhooks_unsubscribe/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/webhooks_unsubscribe/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Абонамент </barsy.help/210-dictionary/subscription.html>`__


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

