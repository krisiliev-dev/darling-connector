.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Categories_get
===========================================================
Подробни данни за категория

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/category </barsy.help/210-dictionary/category.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълни данни за конкретна `категория </barsy.help/210-dictionary/category.html>`__ по нейното ID — основни полета (име, описание, родителска `категория </barsy.help/210-dictionary/category.html>`__, позиция, цвят/икона), флаг за публичност, асоцииран `поток </barsy.help/210-dictionary/flow.html>`__ за подготовка, статус. За цяло йерархично дърво (с подкатегории, `артикули </barsy.help/210-dictionary/article.html>`__ и `модификатори </barsy.help/210-dictionary/modificator.html>`__) виж `Categories_getalltree`.

Типични случаи: визуализиране на детайли в админ панела, презареждане на актуални данни при отваряне на форма за редакция, синхронизация на една `категория </barsy.help/210-dictionary/category.html>`__ към външна PIM система.

**Име**: Categories_get
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
   * - **$cat_id**
     - *int*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
CategoryData_                                                          
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

CategoryData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CategoryData

   * - Параметър
     - Тип
     - Описание
   * - **$cat_id**
     - *int*
     - ID на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$parent_id**
     - *int*
     - ID на родителска `категория </barsy.help/210-dictionary/category.html>`__ (null за главна `категория </barsy.help/210-dictionary/category.html>`__)
   * - **$cat_name**
     - *string*
     - Име на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_name_ml**
     - *object*
     - Всички преводи на вътрешното ime на `категорията </barsy.help/210-dictionary/category.html>`__ (за активните езици)
   * - **$cat_name_public**
     - *string*
     - Публично има на `категорията </barsy.help/210-dictionary/category.html>`__ (за текущия език)
   * - **$cat_name_public_ml**
     - *string*
     - Всички преводи на публично има на `категорията </barsy.help/210-dictionary/category.html>`__ (за активните езици)
   * - **$cat_type**
     - *int*
     - Тип на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_path**
     - *string*
     - Пълен път на `категория </barsy.help/210-dictionary/category.html>`__ от основна
   * - **$description**
     - *string*
     - Описание на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$description_ml**
     - *string*
     - Всички преводи на описание на `категория </barsy.help/210-dictionary/category.html>`__ (на активните езици)
   * - **$child_articles_cnt**
     - *int*
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в `категорията </barsy.help/210-dictionary/category.html>`__ и нейните под `категории </barsy.help/210-dictionary/category.html>`__
   * - **$cat_picture**
     - *string*
     - Основна картинка на `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$code**
     - *string*
     - код за бързо избиране на `категория </barsy.help/210-dictionary/category.html>`__
   * - **$slug**
     - *string*
     - Публично URL на `категорията </barsy.help/210-dictionary/category.html>`__ (за електронен магазин)
   * - **$category_icon**
     - *string*
     - Икона за `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$cat_public_view**
     - *int*
     - Режим на визуализиране на `категорията </barsy.help/210-dictionary/category.html>`__ в публично меню
   * - **$cat_path_ids**
     - *string*
     - Път до `категорията </barsy.help/210-dictionary/category.html>`__ от основна, описан с id-та на родителските `категории </barsy.help/210-dictionary/category.html>`__
   * - **$remote_id**
     - *int*
     - ID на отдалечена система
   * - **$remote_ref_id**
     - *int*
     - ID на `категорията </barsy.help/210-dictionary/category.html>`__ в отдалечена система
   * - **$preferred_article_id**
     - *int*
     - ID на предпочитан `артикул </barsy.help/210-dictionary/article.html>`__ за `категорията </barsy.help/210-dictionary/category.html>`__
   * - **$category_color**
     - *string*
     - Цвят на `категорията </barsy.help/210-dictionary/category.html>`__

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

     .. literalinclude:: ../../sources/categories_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/categories_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/categories_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/categories_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/categories_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/categories_get/barsy_api_client_simple.php
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

