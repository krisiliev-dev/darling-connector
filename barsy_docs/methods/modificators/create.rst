.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Modificators_create
===========================================================
Създаване на модификатор

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/100-catalog/modifiers/index </barsy.help/110-admin/100-catalog/modifiers/index.html>`__
	 * barsy.help: `210-dictionary/modificator </barsy.help/210-dictionary/modificator.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира нов `модификатор </barsy.help/210-dictionary/modificator.html>`__ — кратко указание към поръчка, което се добавя при поръчване на `артикул </barsy.help/210-dictionary/article.html>`__, без да влияе на цената или `склада </barsy.help/210-dictionary/store.html>`__. `Модификаторите </barsy.help/210-dictionary/modificator.html>`__ носят информация за специални изисквания на `клиента </barsy.help/210-dictionary/client.html>`__ към подготовката или поднасянето: "без лук", "леко изпечено", "за вкъщи", "детска порция", "без захар". Записват се на бележките към `сметката </barsy.help/210-dictionary/account.html>`__ и излизат на дисплеите в кухнята/бара.

Типични случаи: създаване на нов `модификатор </barsy.help/210-dictionary/modificator.html>`__ след обратна връзка от персонала, добавяне на сезонен `модификатор </barsy.help/210-dictionary/modificator.html>`__, импорт на стандартни `модификатори </barsy.help/210-dictionary/modificator.html>`__ при стартиране на нов обект.

**Име**: Modificators_create
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
   * - **$data**
     - ModificatorCreateData_ 
     - Данни за `модификатор </barsy.help/210-dictionary/modificator.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ModificatorData_                                                       
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ModificatorCreateData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ModificatorCreateData

   * - Параметър
     - Тип
     - Описание
   * - **$mod_name**
     - *string*
     - Име на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$description**
     - *string*
     - 
   * - **$auto_flag**
     - *int*
     -  **По подразбиране:** 0
   * - **$mod_type**
     - *int*
     - 

			* **1** - *Липсва описание*
			* **2** - *Липсва описание* **По подразбиране:** 1

-----

ModificatorData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ModificatorData

   * - Параметър
     - Тип
     - Описание
   * - **$mod_id**
     - *int*
     - ID на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_name**
     - *string*
     - Име на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$description**
     - *string*
     - Описание на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$operation**
     - *int*
     - Вид операция ('без' `модификатора </barsy.help/210-dictionary/modificator.html>`__ или 'с' `модификатора </barsy.help/210-dictionary/modificator.html>`__) **По подразбиране:** 0
   * - **$weight**
     - *int*
     - Тежест при подреждане на мофификатори в `категория </barsy.help/210-dictionary/category.html>`__
   * - **$mod_color**
     - *string*
     - Цвят на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_type**
     - *int*
     - Тип `модификатор </barsy.help/210-dictionary/modificator.html>`__

			* **1** - *Липсва описание*
			* **2** - *Липсва описание*
   * - **$categories**
     - *array*
     - Списък с `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран този `модификатор </barsy.help/210-dictionary/modificator.html>`__ ( виж: :doc:`../categories/getlist` ) **По подразбиране:** []

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

     .. literalinclude:: ../../sources/modificators_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/modificators_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/modificators_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/modificators_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/modificators_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/modificators_create/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Модификатор </barsy.help/210-dictionary/modificator.html>`__


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

