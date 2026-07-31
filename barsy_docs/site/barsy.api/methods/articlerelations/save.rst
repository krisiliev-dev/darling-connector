.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articlerelations_save
===========================================================
Запис на артикулна връзка

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Създава или презаписва връзка между `артикули </barsy.help/210-dictionary/article.html>`__ (Upsell, Cross-sell или Консумативи) за даден източник, заедно с редовете-цели. Целите могат да са конкретни `артикули </barsy.help/210-dictionary/article.html>`__, `категории </barsy.help/210-dictionary/category.html>`__, характеристики или шаблони за име; ред с exclude_flag=1 изключва `артикулите </barsy.help/210-dictionary/article.html>`__ си от предложенията.

**Име**: Articlerelations_save
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
   * - **$relation_type**
     - *int*
     - Тип на връзката — 1=Upsell, 2=Cross-sell, 3=Консумативи
   * - **$source_type**
     - *int*
     - Тип на източника — 1=`артикул </barsy.help/210-dictionary/article.html>`__, 2=`категория </barsy.help/210-dictionary/category.html>`__, 3=публичен интерфейс
   * - **$source_id**
     - *int*
     - ID на източника според типа
   * - **$targets**
     - *array*
     - Редове-цели: {target_type, target_ref_id, target_pattern, exclude_flag, sort} **По подразбиране:** []
   * - **$active_flag**
     - *int*
     - 1 = връзката е активна **По подразбиране:** 1


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на връзката
====================================================================== ======================================================================

----
 
Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articlerelations_save/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articlerelations_save/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articlerelations_save/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articlerelations_save/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articlerelations_save/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articlerelations_save/barsy_api_client_simple.php
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

