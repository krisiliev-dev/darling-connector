.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Depots_getlistcurrent
===========================================================
Складове за текущия обект

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/store </barsy.help/210-dictionary/store.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък със складовете, асоциирани конкретно с текущия активен `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (barsy). За разлика от `Depots_getlist`, който връща всички системни складове, тук резултатът е ограничен до релевантните за текущия контекст — удобно за касов или мобилен интерфейс, който не трябва да показва складове на други обекти.

Типични случаи: попълване на dropdown "`Склад </barsy.help/210-dictionary/store.html>`__" в складова операция от `каса </barsy.help/210-dictionary/pos.html>`__, проверка кои складове са достъпни от мобилно приложение на сервитьор, конфигуриране на отговорност за конкретен обект.

**Име**: Depots_getlistcurrent
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
     - DepotsListFiltersData_ 
     -  **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
DepotType_                                                             
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

DepotsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Възможни филтри при изтегляне на списък складове

.. list-table::
   :header-rows: 1
   :align: center
   :name: DepotsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$barsy_id**
     - *int*
     - 
   * - **$depot_group_id**
     - *int*
     - 
   * - **$depot_id**
     - *int*
     - 
   * - **$depot_delete_flag**
     - *int*
     -  **По подразбиране:** 0
   * - **$barsy_delete_flag**
     - *int*
     - 
   * - **$can_load**
     - *int*
     - 
   * - **$is_virtual**
     - *int*
     - 
   * - **$user_id**
     - *int*
     - 
   * - **$accept_canceled_storemoves**
     - *int*
     - 

-----

DepotType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: DepotType

   * - Параметър
     - Тип
     - Описание
   * - **$depot_id**
     - *int*
     - ID на `склада </barsy.help/210-dictionary/store.html>`__
   * - **$depot_name**
     - *string*
     - Име на `склада </barsy.help/210-dictionary/store.html>`__
   * - **$barsy_id**
     - *int*
     - ID на търговския обект ( виж: :doc:`../barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - Име на търговския обект
   * - **$depot_group_id**
     - *int*
     - ID на групата, към която принадлежи `склада </barsy.help/210-dictionary/store.html>`__
   * - **$group_name**
     - *string*
     - Име на складовата група, към която принадлежи `склада </barsy.help/210-dictionary/store.html>`__
   * - **$description**
     - *string*
     - Описание на `склада </barsy.help/210-dictionary/store.html>`__
   * - **$delete_flag**
     - *bool*
     - Флаг дали `склада </barsy.help/210-dictionary/store.html>`__ е маркиран като изтрит
   * - **$can_load**
     - *bool*
     - Флаг дали `склада </barsy.help/210-dictionary/store.html>`__ може да се зарежда чрез операция "`Зареждане </barsy.help/210-dictionary/storeload.html>`__"
   * - **$can_move_outside**
     - *bool*
     - Флаг дали от `склада </barsy.help/210-dictionary/store.html>`__ може да бъде извършено `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ от и към външни складове (в други `търговски обекти </barsy.help/210-dictionary/barsy.html>`__)

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

     .. literalinclude:: ../../sources/depots_getlistcurrent/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/depots_getlistcurrent/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/depots_getlistcurrent/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/depots_getlistcurrent/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/depots_getlistcurrent/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/depots_getlistcurrent/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

