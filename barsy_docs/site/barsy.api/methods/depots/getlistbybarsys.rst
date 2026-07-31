.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Depots_getlistbybarsys
===========================================================
Складове по обекти

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/store </barsy.help/210-dictionary/store.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък със складове, групирани по асоциирания `търговски обект </barsy.help/210-dictionary/barsy.html>`__. Резултатът е удобен за многоравнен UI компонент (например navtree), който показва обектите като родителски възли и техните складове като деца. Поддържа филтри за ограничаване по конкретни обекти.

*Типични случаи: визуализиране на йерархичен treeView в админ панела, конфигуриране на маршрути за прехвърляния между обекти, експорт за справка "Складове в мрежата по обекти".*

**Име**: Depots_getlistbybarsys
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
*array*                                                                
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

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/depots_getlistbybarsys/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/depots_getlistbybarsys/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/depots_getlistbybarsys/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/depots_getlistbybarsys/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/depots_getlistbybarsys/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/depots_getlistbybarsys/barsy_api_client_simple.php
     .. code-block:: bash


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

