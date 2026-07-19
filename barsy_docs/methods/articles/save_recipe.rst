.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articles_save_recipe
===========================================================
Запис на рецепта към артикул

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/100-catalog/articles/index </barsy.help/110-admin/100-catalog/articles/index.html>`__
	 * barsy.help: `210-dictionary/article </barsy.help/210-dictionary/article.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Записва (или презаписва) рецептата на даден `артикул </barsy.help/210-dictionary/article.html>`__ — списък от съставки с количества и допълнителни параметри (загуба при обработка, отпадък, фиксирано/пропорционално количество). Рецептата дефинира как при `продажба </barsy.help/210-dictionary/sale.html>`__ или `производство </barsy.help/210-dictionary/storeproduction.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__ се отписват количествата от съставките му от `склада </barsy.help/210-dictionary/store.html>`__. Допуска многонивови рецепти — съставка също може да е композитен `артикул </barsy.help/210-dictionary/article.html>`__ със собствена рецепта.

Типични случаи: дефиниране на ястия в ресторант (например `Шопска салата` = 200г домати + 50г сирене + ...), производствени калкулации в малък цех, комплекти и асортиментни кутии в магазин. След запис автоматично се преизчислява себестойността на `артикула </barsy.help/210-dictionary/article.html>`__ спрямо настоящите доставни цени на съставките.

**Име**: Articles_save_recipe
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
   * - **$id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, на който се задава рецепта
   * - **$rows**
     - ArticleRecipeRowData_ []
     - Масив от `артикули </barsy.help/210-dictionary/article.html>`__, участващи в рецептата
   * - **$values**
     - ArticleRecipeData_ 
     - Допълнителни данни за рецептата


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ArticleRecipeRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleRecipeRowData

   * - Параметър
     - Тип
     - Описание
   * - **$sub_article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__-съставка
   * - **$part**
     - *float*
     - Количество, с което участва `артикула </barsy.help/210-dictionary/article.html>`__ в рецептата и се изтегля от `склад </barsy.help/210-dictionary/store.html>`__ при изпълнение на рецептата
   * - **$part_after**
     - *float*
     - Количество, се влага реално в крайния продукт при изпълнение на рецептата (за справки)

-----

ArticleRecipeData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за рецепта към `артикул </barsy.help/210-dictionary/article.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleRecipeData

   * - Параметър
     - Тип
     - Описание
   * - **$composite**
     - *int*
     - Тип на рецептата [1=При приключване на `сметка </barsy.help/210-dictionary/account.html>`__; -1=При `производство </barsy.help/210-dictionary/storeproduction.html>`__] **По подразбиране:** 1
   * - **$amount_prod**
     - *float*
     - Получено количество от `производството </barsy.help/210-dictionary/storeproduction.html>`__ на тази рецепта **По подразбиране:** 1
   * - **$recipe_description**
     - *string*
     - Описание на рецептата (свободен текст)

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

     .. literalinclude:: ../../sources/articles_save_recipe/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articles_save_recipe/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articles_save_recipe/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articles_save_recipe/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articles_save_recipe/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articles_save_recipe/barsy_api_client_simple.php
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

