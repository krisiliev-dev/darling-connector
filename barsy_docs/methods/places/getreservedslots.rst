.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Places_getreservedslots
===========================================================
Заети слотове на място

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/reservation </barsy.help/210-dictionary/reservation.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с резервираните времеви слотове за конкретно място (`place_id`) в избран период. Размерът на слотовете се определя от типа количество на мястото — например стая се резервира на нощувки, корт на часове, маса на интервал от 2 часа. Резултатът съдържа начало, край и идентификатор на `резервацията </barsy.help/210-dictionary/reservation.html>`__ за всеки зает слот.

Типични случаи: визуализиране на календар на `резервациите </barsy.help/210-dictionary/reservation.html>`__ за конкретна маса/стая, оператор търси най-близкия свободен слот за бърза `резервация </barsy.help/210-dictionary/reservation.html>`__, изграждане на ленти-времеви визуализатор тип Gantt.

**Име**: Places_getreservedslots
**Категория**: Settings


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$place_id**
     - *int*
     - ID на място
   * - **$from_date**
     - *string*
     - начална дата
   * - **$to_date**
     - *string*
     - крайна дата


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PlaceData_                                                             списък от обекти
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PlaceData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PlaceData

   * - Параметър
     - Тип
     - Описание
   * - **$place_id**
     - *int*
     - ID на текущото място
   * - **$place_type**
     - *int*
     - ID на типа на мястото
   * - **$place_num**
     - *int*
     - Номер на мястото (свободно избираем)
   * - **$pos**
     - *string*
     - Координати и размери на текущото място на схемата (x,y,w,h).
   * - **$type_name**
     - *string*
     - Тип на текущото място
   * - **$is_public**
     - *int*
     - Публично видомо ли е мястото
   * - **$picture**
     - *string*
     - Основна снимка
   * - **$salon_id**
     - *int*
     - ID на зона/салон, към която принадлежи текущото място
   * - **$salon_name**
     - *string*
     - Име на зона/салон, към която принадлежи текущото място
   * - **$accounts_count**
     - *int*
     - Брой отворени `сметка </barsy.help/210-dictionary/account.html>`__, асоцирани към мястото
   * - **$id**
     - *int*
     - 
   * - **$type**
     - *int*
     - 
   * - **$num**
     - *int*
     - 
   * - **$acc_count**
     - *int*
     - 
   * - **$name**
     - *string*
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

     .. literalinclude:: ../../sources/places_getreservedslots/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/places_getreservedslots/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/places_getreservedslots/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/places_getreservedslots/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/places_getreservedslots/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/places_getreservedslots/barsy_api_client_simple.php
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

