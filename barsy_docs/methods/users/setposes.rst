.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Users_setposes
===========================================================
Създаване на персонални каси

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pos </barsy.help/210-dictionary/pos.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Създава персонални POS `каси </barsy.help/210-dictionary/pos.html>`__ за конкретен `потребител </barsy.help/210-dictionary/user.html>`__ в посочените `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ (`needed_barsys`). Персоналната `каса </barsy.help/210-dictionary/pos.html>`__ е виртуална `каса </barsy.help/210-dictionary/pos.html>`__, която е "собственост" на `потребителя </barsy.help/210-dictionary/user.html>`__ — там `сметките </barsy.help/210-dictionary/account.html>`__ и приходите се записват под негово име, без значение от коя физическа `каса </barsy.help/210-dictionary/pos.html>`__ работи. Удобно за разнасящи се търговци, мобилни сервитьори, куриери.

Типични случаи: настройка на нов мобилен търговец със собствена виртуална `каса </barsy.help/210-dictionary/pos.html>`__, разпределение на разнасящи се персонала по обекти, миграция от споделени `каси </barsy.help/210-dictionary/pos.html>`__ към персонална отчетност.

**Име**: Users_setposes
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
   * - **$id**
     - *int*
     - 
   * - **$needed_barsys**
     - *array*
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

     .. literalinclude:: ../../sources/users_setposes/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/users_setposes/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/users_setposes/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/users_setposes/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/users_setposes/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/users_setposes/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Каса </barsy.help/210-dictionary/pos.html>`__


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

