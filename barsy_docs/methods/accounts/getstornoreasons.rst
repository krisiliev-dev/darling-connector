.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Accounts_getstornoreasons
===========================================================
Причини за сторниране

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/account </barsy.help/210-dictionary/account.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък със стандартизираните причини за сторно операция, които системата задължително изпраща към фискалното устройство — например "Операторска грешка", "Връщане от `клиент </barsy.help/210-dictionary/client.html>`__", "Промяна на цена". Списъкът отговаря на регулаторните изисквания (Наредба Н-18 за България) и трябва да се избере коректна причина при всяко сторно, иначе фискалното устройство ще откаже операцията.

Типични случаи: попълване на dropdown в потвърждаващ диалог преди `Accounts_storno`, проверка дали `потребителят </barsy.help/210-dictionary/user.html>`__ е избрал валидна причина преди да позволи финализирането на сторното.

**Име**: Accounts_getstornoreasons
**Категория**: Cashdesk


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                
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

     .. literalinclude:: ../../sources/accounts_getstornoreasons/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/accounts_getstornoreasons/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/accounts_getstornoreasons/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/accounts_getstornoreasons/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/accounts_getstornoreasons/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/accounts_getstornoreasons/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

