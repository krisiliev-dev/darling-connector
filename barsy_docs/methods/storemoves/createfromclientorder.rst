.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storemoves_createfromclientorder
===========================================================
Прехвърляне от клиентска заявка

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/storemove </barsy.help/210-dictionary/storemove.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Генерира ново складово `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ автоматично от съдържанието на `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ — `артикулите </barsy.help/210-dictionary/article.html>`__ и количествата се пренасят като редове в `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__, изходният и приемащият `склад </barsy.help/210-dictionary/store.html>`__ се вземат от подадените данни. Полезно за многосайтов бизнес, при който поръчката се поема в централен офис, но трябва да се обслужи от регионален `склад </barsy.help/210-dictionary/store.html>`__ чрез транзит.

Типични случаи: онлайн поръчка трябва да се изпрати към регионален разпределителен център преди финална доставка, корпоративна поръчка изисква подготовка на стоки от няколко `склада </barsy.help/210-dictionary/store.html>`__, кетъринг поръчка с `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ на материали към полевата кухня.

**Име**: Storemoves_createfromclientorder
**Категория**: Store


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$client_order_id**
     - *int*
     - 
   * - **$storemove**
     - StoreMoveCreateData_ 
     - Данни за `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на създаденото прехвърляне
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreMoveCreateData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMoveCreateData

   * - Параметър
     - Тип
     - Описание
   * - **$depot_id_left**
     - *int*
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, от който се изтелгя количество ( виж: :doc:`../depots/getlist` )
   * - **$depot_id_right**
     - *int*
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, в кой се прехвърля количество ( виж: :doc:`../depots/getlist` )
   * - **$doc_date**
     - *string*
     - 
   * - **$description**
     - *string*
     - 
   * - **$deal_id**
     - *string*
     -  ( виж: :doc:`../deals/getlist` )
   * - **$inspector_description**
     - *string*
     - 
   * - **$redirect_depot_id**
     - *int*
     - 

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

     .. literalinclude:: ../../sources/storemoves_createfromclientorder/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storemoves_createfromclientorder/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storemoves_createfromclientorder/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storemoves_createfromclientorder/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storemoves_createfromclientorder/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storemoves_createfromclientorder/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Клиентска заявка </barsy.help/210-dictionary/client-order.html>`__
 * `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__


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

