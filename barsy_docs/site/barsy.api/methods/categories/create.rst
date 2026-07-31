.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Categories_create
===========================================================
Създаване на категория

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/category </barsy.help/210-dictionary/category.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира нова `категория </barsy.help/210-dictionary/category.html>`__ в каталога/менюто — основни данни (име, описание, родителска `категория </barsy.help/210-dictionary/category.html>`__, позиция, цвят/икона за UI), флаг за публичност (видима в публичния канал), специфични настройки (`поток </barsy.help/210-dictionary/flow.html>`__ за подготовка, прикачен `артикул </barsy.help/210-dictionary/article.html>`__ за подвид). `Категориите </barsy.help/210-dictionary/category.html>`__ изграждат йерархично дърво за организиране на `артикулите </barsy.help/210-dictionary/article.html>`__ и контрол на UI на `касата </barsy.help/210-dictionary/pos.html>`__.

Типични случаи: създаване на нова продуктова група след разширение на асортимента, добавяне на сезонна `категория </barsy.help/210-dictionary/category.html>`__, изграждане на нов раздел в онлайн менюто, регулатор-задължителна категоризация (например за алкохол).

**Име**: Categories_create
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
   * - **$cat**
     - CategoryInputData_ 
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на създадената категория
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

CategoryInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CategoryInputData

   * - Параметър
     - Тип
     - Описание
   * - **$cat_name**
     - *string*
     - Име на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$cat_name_ml**
     - MultiLanguageData_ 
     - Преводи на вътрешното ime на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$cat_name_public**
     - MultiLanguageData_ 
     - Публично име на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$parent_id**
     - *int*
     - ID на родителска `категория </barsy.help/210-dictionary/category.html>`__.

			*Null ако няма родител (най-горно ниво)*
   * - **$category_icon**
     - *string*
     - Икона за `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$description**
     - MultiLanguageData_ 
     - Свободен текст описание
   * - **$code**
     - *int*
     - Код за бързо избиране
   * - **$cat_picture**
     - *string*
     - 
   * - **$slug**
     - *string*
     - Публичен URL на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$cat_public_view**
     - *int*
     - Публичен изглед на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$remote_ref_id**
     - *string*
     - ID на отдалечена система
   * - **$remote_parent_ref_id**
     - *string*
     - ID на родител отдалечена система
   * - **$preferred_article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, предпочитан за `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$category_color**
     - *string*
     - 

-----

MultiLanguageData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: MultiLanguageData

   * - Параметър
     - Тип
     - Описание
   * - **$bg_BG**
     - *string*
     - 
   * - **$en_US**
     - *string*
     - 
   * - **$de_DE**
     - *string*
     - 
   * - **$es_ES**
     - *string*
     - 
   * - **$fr_FR**
     - *string*
     - 
   * - **$it_IT**
     - *string*
     - 
   * - **$ro_RO**
     - *string*
     - 
   * - **$ru_RU**
     - *string*
     - 
   * - **$sr_RS**
     - *string*
     - 
   * - **$el_GR**
     - *string*
     - 
   * - **$tr_TR**
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

     .. literalinclude:: ../../sources/categories_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/categories_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/categories_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/categories_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/categories_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/categories_create/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Категория </barsy.help/210-dictionary/category.html>`__


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

