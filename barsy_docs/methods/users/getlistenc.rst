.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Users_getlistenc
===========================================================
Криптиран списък за POS

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/user </barsy.help/210-dictionary/user.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Специализирана форма на списъка с `потребители </barsy.help/210-dictionary/user.html>`__, оптимизирана за касов POS режим — връща минимален набор от данни (ID, кратък alias, език, основни права за `плащане </barsy.help/210-dictionary/payment.html>`__/`сметки </barsy.help/210-dictionary/account.html>`__/`клиенти </barsy.help/210-dictionary/client.html>`__) и хеширан PIN код (SHA-256 с poskey на `касата </barsy.help/210-dictionary/pos.html>`__), за да позволи offline валидация на PIN-а без да съхранява чистия код в касовия терминал. Endpoint-ът може да се ползва САМО от `каси </barsy.help/210-dictionary/pos.html>`__, регистрирани с уникален `poskey`.

Типични случаи: периодична синхронизация на потребителския списък от POS терминал, offline режим където `касата </barsy.help/210-dictionary/pos.html>`__ валидира PIN локално без мрежова заявка, протекция срещу извличане на пароли от пробит терминал.

**Име**: Users_getlistenc
**Категория**: Catalog


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

     .. literalinclude:: ../../sources/users_getlistenc/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/users_getlistenc/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/users_getlistenc/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/users_getlistenc/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/users_getlistenc/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/users_getlistenc/barsy_api_client_simple.php
     .. code-block:: bash


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

