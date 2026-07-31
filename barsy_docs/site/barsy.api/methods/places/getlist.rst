.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Places_getlist
===========================================================
Списък с всички места

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с конфигурираните в системата места — маси, бар столове, стаи, корти, билярдни маси, кабинети, всякакви физически обекти, които могат да бъдат заети или резервирани. За всяко място — основни данни (име, капацитет, тип, обект-локация, прикачен `артикул </barsy.help/210-dictionary/article.html>`__ за почасово таксуване), позиция в плана на залата. Чрез `extra_properties` могат да се поискат текущ брой отворени `сметки </barsy.help/210-dictionary/account.html>`__, брой `резервации </barsy.help/210-dictionary/reservation.html>`__, прикачени файлове.

Типични случаи: визуализиране на план на зала в касовия интерфейс, попълване на dropdown при отваряне на `сметка </barsy.help/210-dictionary/account.html>`__, конфигуриране на резервационна система, проверка на капацитет на залата.

**Име**: Places_getlist
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
   * - **$filters**
     - PlacesListFiltersData_ 
     - Филтриране на списъка **По подразбиране:** []
   * - **$extra_properties**
     - *array*
     - Допълнителни данни за всяка маса

			* **accounts_count** - Брой `сметки </barsy.help/210-dictionary/account.html>`__
			* **article** - Информация за `артикула </barsy.help/210-dictionary/article.html>`__
			* **reservations_count** - Брой `резервации </barsy.help/210-dictionary/reservation.html>`__
			* **files** - *Прикачени файлове* **По подразбиране:** []
   * - **$offset**
     - *int*
     - Начална стойност **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати записи **По подразбиране:** 10000
   * - **$order_by**
     - *string*
     - Сортиране по


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PlaceData_                                                             списък от обекти
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PlacesListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PlacesListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$salon_id**
     - *int*
     - Филтър по ID на салон.
   * - **$place_id**
     - *int*
     - Филтър по ID на място.
   * - **$place_type**
     - *int*
     - Филтър по ID на място.
   * - **$salon_delete_flag**
     - *int*
     - Филтър по флаг за изтрит Салон
   * - **$place_code**
     - *string*
     - 
   * - **$place_sid**
     - *string*
     - 
   * - **$is_public**
     - *int*
     - 

-----

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

     .. literalinclude:: ../../sources/places_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/places_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/places_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/places_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/places_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/places_getlist/barsy_api_client_simple.php
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

