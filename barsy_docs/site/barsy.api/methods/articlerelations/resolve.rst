.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articlerelations_resolve
===========================================================
Предложени артикули по артикулна връзка

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Резолва връзките между `артикули </barsy.help/210-dictionary/article.html>`__ до конкретен списък с предложения: за Upsell — алтернативите на даден `артикул </barsy.help/210-dictionary/article.html>`__ при добавянето му в кошницата, за Cross-sell — препоръчаните допълващи `артикули </barsy.help/210-dictionary/article.html>`__ според съдържанието на кошницата. Връщат се само активни, публично видими и налични `артикули </barsy.help/210-dictionary/article.html>`__, без тези, които вече са в кошницата, с публично име, картинка и текуща цена според контекста.

Типични случаи: поп-ъп с предложения за замяна при добавяне на `артикул </barsy.help/210-dictionary/article.html>`__ в киоск или публичен каталог, поп-ъп с препоръчани продукти при преминаване към преглед на поръчката.

**Име**: Articlerelations_resolve
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
   * - **$type**
     - *string*
     - Тип на резолюцията — upsell (надграждане), addon (допълнение) или cross_sell (препоръчани)
   * - **$article_id**
     - *int*
     - ID на добавяния `артикул </barsy.help/210-dictionary/article.html>`__ (задължителен при upsell и addon)
   * - **$cart**
     - *array*
     - Съдържание на кошницата: {article_id, amount, added_index} **По подразбиране:** []
   * - **$limit**
     - *int*
     - Максимален брой предложения
   * - **$strategy**
     - *string*
     - Cross-sell стратегия — mix, most_expensive или last_added


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
RecommendationData_                                                    
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

RecommendationData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: RecommendationData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - ID на предложения `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name_public**
     - *string*
     - Публично име на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_name_public_ml**
     - *object*
     - Публично име на `артикула </barsy.help/210-dictionary/article.html>`__ по езици
   * - **$picture**
     - *string*
     - URL на основната картинка на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_price**
     - *float*
     - Текуща продажна цена според контекста
   * - **$current_price_curr**
     - *float*
     - Текуща продажна цена във втора валута

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

     .. literalinclude:: ../../sources/articlerelations_resolve/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articlerelations_resolve/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articlerelations_resolve/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articlerelations_resolve/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articlerelations_resolve/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articlerelations_resolve/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__


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

