.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Places_searchavailable
===========================================================
Свободни места за период

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/reservation </barsy.help/210-dictionary/reservation.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с местата, които НЕ са резервирани в посочения времеви интервал и имат достатъчен капацитет за поисканите групи от персони. Параметърът `persons` е масив (например `[2, 4, 6]`) — методът намира всички места, които могат да настанят поне една от групите. Логиката отчита: припокриване с други `резервации </barsy.help/210-dictionary/reservation.html>`__, минимално време между `резервации </barsy.help/210-dictionary/reservation.html>`__ (буфер), работно време на обекта, тип на мястото.

Типични случаи: онлайн форма за `резервация </barsy.help/210-dictionary/reservation.html>`__ която показва свободните маси в избрания час, оператор търси най-подходящото свободно място за телефонна заявка, групово събитие изисква конкретен капацитет.

**Име**: Places_searchavailable
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
   * - **$from_date**
     - *string*
     - начална дата във формат `Y-m-d` (напр. `2026-05-20`)
   * - **$to_date**
     - *string*
     - крайна дата във формат `Y-m-d` (напр. `2026-05-21`)
   * - **$persons**
     - *array*
     - диапазон за брой хора — масив с два елемента: `[min, max]`, напр. `[2, 4]`.

			Индекс `0` е минималният брой, индекс `1` е максималният. Ако `[1]` липсва, се приема равен на `[0]` (напр. `[2]` ⇒ търсене за точно 2 души).


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

     .. literalinclude:: ../../sources/places_searchavailable/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/places_searchavailable/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/places_searchavailable/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/places_searchavailable/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/places_searchavailable/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/places_searchavailable/barsy_api_client_simple.php
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

