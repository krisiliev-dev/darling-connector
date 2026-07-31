.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articles_getmodificators
===========================================================
Модификатори, закачени към артикул

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

**Име**: Articles_getmodificators
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
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ @test_value 1


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ModificatorData_                                                       
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

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

     .. literalinclude:: ../../sources/articles_getmodificators/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articles_getmodificators/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articles_getmodificators/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articles_getmodificators/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articles_getmodificators/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articles_getmodificators/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__
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

