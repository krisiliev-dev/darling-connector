.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Barsys_getlist
===========================================================
Списък с търговски обекти

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/barsy </barsy.help/210-dictionary/barsy.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с конфигурираните `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ (barsys) в системата — физически локации/брандове, които изграждат мрежата. Параметърът `mode` контролира дали се връщат всички обекти (`all`) или само тези, до които текущият `потребител </barsy.help/210-dictionary/user.html>`__ има право на достъп (`restrict`, по подразбиране). За всеки обект: ID, име, адрес, асоциирано меню, валута, езици.

*Типични случаи: попълване на dropdown "Обект" в централен админ панел на multi-site бизнес, превключване между обекти за служители работещи в няколко локации, експорт за управленски справки на мрежата.*

**Име**: Barsys_getlist
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
   * - **$mode**
     - *string*
     - Флаг дали списъка да съдържа всички `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ или само тези, до които текущия `потребител </barsy.help/210-dictionary/user.html>`__ има достъп **По подразбиране:** 'restrict'


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                Списък от търговските обекти
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

     .. literalinclude:: ../../sources/barsys_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/barsys_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/barsys_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/barsys_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/barsys_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/barsys_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Търговски обект </barsy.help/210-dictionary/barsy.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

