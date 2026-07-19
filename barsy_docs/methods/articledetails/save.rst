.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articledetails_save
===========================================================
Запис на характеристики

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/article </barsy.help/210-dictionary/article.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Записва пълен списък с характеристики (ключ-стойност двойки) към даден `артикул </barsy.help/210-dictionary/article.html>`__. Подаденият списък ПРЕЗАПИСВА текущите характеристики. Ако подадените ключове или стойности още не съществуват в системата, те автоматично се създават — позволявайки бързо разширение на номенклатурата чрез използване.

*Типични случаи: масов импорт на спецификации от Excel, обновяване на сезонни характеристики, синхронизация от външна PIM (Product Information Management) система, ръчно дописване от продуктов мениджър.*

**Име**: Articledetails_save
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
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, за който се отнасят характеристиките
   * - **$rows**
     - ArticleDetailInputData_ []
     - Списък с характеристиките


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  1
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ArticleDetailInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за създаване създаване/редактиране на детайл към `артикул </barsy.help/210-dictionary/article.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailInputData

   * - Параметър
     - Тип
     - Описание
   * - **$detail_id**
     - *int*
     - ID на детайл (празно за нов)
   * - **$detail_name**
     - *string*
     - Име на детайл (подава се за създаване на нов)
   * - **$detail_value**
     - *string*
     - Стойност на детайл
   * - **$key_id**
     - *int*
     - ID на стойност на детайл (празно за нова)

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

     .. literalinclude:: ../../sources/articledetails_save/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articledetails_save/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articledetails_save/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articledetails_save/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articledetails_save/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articledetails_save/barsy_api_client_simple.php
     .. code-block:: bash


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

