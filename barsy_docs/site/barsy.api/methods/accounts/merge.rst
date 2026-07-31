.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Accounts_merge
===========================================================
Сливане на сметки

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/account </barsy.help/210-dictionary/account.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Слива няколко отворени `сметки </barsy.help/210-dictionary/account.html>`__ в една обща. `Артикулите </barsy.help/210-dictionary/article.html>`__ от всички подадени `сметки </barsy.help/210-dictionary/account.html>`__ се прехвърлят в най-старата (по дата на отваряне) от тях; останалите `сметки </barsy.help/210-dictionary/account.html>`__ се затварят празни, без поръчки. Запазват се връзките с `клиент </barsy.help/210-dictionary/client.html>`__/обект на най-старата `сметка </barsy.help/210-dictionary/account.html>`__. `Сметки </barsy.help/210-dictionary/account.html>`__ в затворен или фискално маркиран статус не могат да се сливат — за тях е нужно първо сторниране.

Типични случаи: обединяване на отделни маси при преместване на група посетители на една обща, обединение на отворени `сметки </barsy.help/210-dictionary/account.html>`__ на един `клиент </barsy.help/210-dictionary/client.html>`__ в едно общо `плащане </barsy.help/210-dictionary/payment.html>`__ преди приключване, корекция след погрешно разделена `сметка </barsy.help/210-dictionary/account.html>`__. За сливане по конкретен `клиент </barsy.help/210-dictionary/client.html>`__ или място виж `Accounts_mergebyclientid`/`Accounts_mergebyplaceid`.

**Име**: Accounts_merge
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
   * - **$accounts**
     - *array*
     - Списък от ID-та на `сметка </barsy.help/210-dictionary/account.html>`__ за сливане **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на общата сметка
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

     .. literalinclude:: ../../sources/accounts_merge/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/accounts_merge/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/accounts_merge/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/accounts_merge/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/accounts_merge/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/accounts_merge/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

