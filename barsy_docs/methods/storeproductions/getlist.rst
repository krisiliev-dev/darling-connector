.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storeproductions_getlist
===========================================================
Списък с производства

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/150-store/40-storeproductions/index </barsy.help/110-admin/150-store/40-storeproductions/index.html>`__
	 * barsy.help: `210-dictionary/storeproduction </barsy.help/210-dictionary/storeproduction.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък със складови `производства </barsy.help/210-dictionary/storeproduction.html>`__ (операции, при които съставки се преобразуват в готов продукт по рецепта) с филтри — по период, `склад </barsy.help/210-dictionary/store.html>`__, производител, готов `артикул </barsy.help/210-dictionary/article.html>`__, статус. `Производството </barsy.help/210-dictionary/storeproduction.html>`__ отписва съставките и зарежда готовия продукт като нова наличност. Поддържа странициране, сортиране и `extra_properties` за включване на детайлите по компоненти.

Типични случаи: ежедневен отчет на цех за `производство </barsy.help/210-dictionary/storeproduction.html>`__, `ревизия </barsy.help/210-dictionary/revision.html>`__ на коректност на рецептите спрямо реалното отписване, отчет за производителност на оператори, синхронизация към ERP за разходни норми.

**Име**: Storeproductions_getlist
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
   * - **$filters**
     - StoreProductionsListFiltersData_ 
     - Филтриране по подадени критерии
   * - **$extra_properties**
     - *array*
     - Включване на допълнителни данни [all=>всички основни данни за `производството </barsy.help/210-dictionary/storeproduction.html>`__, details=>`Артикулите </barsy.help/210-dictionary/article.html>`__ в `производството </barsy.help/210-dictionary/storeproduction.html>`__] **По подразбиране:** []
   * - **$offset**
     - *int*
     - Начален запис **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати записи **По подразбиране:** 1000
   * - **$order_by**
     - *string*
     - Подреждане по [store_production_id, barsy_id, depot_id, user_id, user_name, request_id, close_date, doc_date, anulate_flag, ref_id, total_rows]


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
StoreProductionData_                                                   
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreProductionsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreProductionsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$store_production_id**
     - *int*
     - Филтър по ID на `производство </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$barsy_id**
     - *int*
     - Филтър по "`Търговски обект </barsy.help/210-dictionary/barsy.html>`__" ( виж: :doc:`../barsys/getlist` )
   * - **$depot_id**
     - *int*
     - Филтър по "`Склад </barsy.help/210-dictionary/store.html>`__" ( виж: :doc:`../depots/getlist` )
   * - **$date**
     - *datetime*
     - Филтър по дата на създаване на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$user_id**
     - *int*
     - Филтър по id на създател ( виж: :doc:`../users/getlist` )
   * - **$user_name**
     - *string*
     - Филтър по име на създател ( виж: :doc:`../users/getlist` )
   * - **$status**
     - *int*
     - Филтър по статус [0=Отворено, 1=Приключено]
   * - **$close_date**
     - *datetime*
     - Филтър по дата на приключване на `производството </barsy.help/210-dictionary/storeproduction.html>`__

-----

StoreProductionData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreProductionData

   * - Параметър
     - Тип
     - Описание
   * - **$store_production_id**
     - *int*
     - ID на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - Име на търговския обект
   * - **$depot_id**
     - *int*
     - ID на `склад </barsy.help/210-dictionary/store.html>`__, в който е произведено ( виж: :doc:`../depots/getlist` )
   * - **$status**
     - *int*
     - Статус на `производството </barsy.help/210-dictionary/storeproduction.html>`__ [0=Отворено, 1=Приключено]
   * - **$date**
     - *string*
     - Дата на създаване на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$close_date**
     - *string*
     - Дата на приключване на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$doc_date**
     - *string*
     - Документална дата на операцията
   * - **$description**
     - *string*
     - Описание на `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$user_name**
     - *string*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$user_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$total_rows**
     - *float*
     - Брой редове в `производството </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$anulate_flag**
     - *bool*
     - Флаг дали е анулирано
   * - **$details**
     - *array*
     - Списък с редовете към `производството </barsy.help/210-dictionary/storeproduction.html>`__ (ако са поискани)

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

     .. literalinclude:: ../../sources/storeproductions_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storeproductions_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storeproductions_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storeproductions_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storeproductions_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storeproductions_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Производство </barsy.help/210-dictionary/storeproduction.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

