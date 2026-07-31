.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Accounts_move
===========================================================
Прехвърляне на сметка

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/account </barsy.help/210-dictionary/account.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Прехвърля отворена `сметка </barsy.help/210-dictionary/account.html>`__ на друго място (маса/стая) и/или на друг обслужващ `потребител </barsy.help/210-dictionary/user.html>`__. При липса на право "директно `прехвърляне </barsy.help/210-dictionary/storemove.html>`__" новият `потребител </barsy.help/210-dictionary/user.html>`__ получава нотификация и трябва изрично да приеме `сметката </barsy.help/210-dictionary/account.html>`__ — едва тогава тя сменя притежателя си; до приемането остава видима и при двамата. Полезно при смени на персонала и преподреждане на гостите.

Типични случаи: смяна на смяна на касиерите — текущият оператор прехвърля отворените си `сметки </barsy.help/210-dictionary/account.html>`__ на сменящия го, разместване на гостите от една маса на друга при пристигане на `резервация </barsy.help/210-dictionary/reservation.html>`__, `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ на `сметка </barsy.help/210-dictionary/account.html>`__ от ресторант към хотелска стая.

**Име**: Accounts_move
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
   * - **$account_id**
     - *int*
     - ID на желаната `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$place_id**
     - *int*
     - ID на желаната ново място ( виж: :doc:`../places/getlist` )
   * - **$user_id**
     - *int*
     - ID на желан нов обслужващ `потребител </barsy.help/210-dictionary/user.html>`__ ("притежател" на `сметката </barsy.help/210-dictionary/account.html>`__).

			Ако липсва право "директно `прехвърляне </barsy.help/210-dictionary/storemove.html>`__", новия `потребител </barsy.help/210-dictionary/user.html>`__ първо трявба да я приеме ( виж: :doc:`../users/getlist` )


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  Няма
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

     .. literalinclude:: ../../sources/accounts_move/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/accounts_move/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/accounts_move/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/accounts_move/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/accounts_move/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/accounts_move/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__
 * `Сметка </barsy.help/210-dictionary/account.html>`__


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

