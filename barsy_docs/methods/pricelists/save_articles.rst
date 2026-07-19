.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Pricelists_save_articles
===========================================================
Артикули в ценово правило

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pricelist </barsy.help/210-dictionary/pricelist.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Записва изричен списък с конкретни `артикули </barsy.help/210-dictionary/article.html>`__, за които да важи дадено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__. Подаденият списък ПРЕЗАПИСВА текущите асоциации. Чрез този метод се настройва "ръчният" режим — изборът на засегнати `артикули </barsy.help/210-dictionary/article.html>`__ е експлицитен. За динамичен избор по име/характеристики виж `Pricelists_save_article_patterns`. След запис автоматично се преизграждат всички приложими цени.

Типични случаи: фиксиране на конкретни `артикули </barsy.help/210-dictionary/article.html>`__ в специална промоция, добавяне на нов VIP продукт към съществуваща ценова листа, бързо разширяване на промоция върху няколко популярни `артикула </barsy.help/210-dictionary/article.html>`__.

**Име**: Pricelists_save_articles
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
     - ID на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$rows**
     - PricelistArticleData_ []
     - Списък с ID-та на `артикули </barsy.help/210-dictionary/article.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  1
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PricelistArticleData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PricelistArticleData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$custom_price**
     - *float*
     - Предпочитана продажна цена за дадения `артикул </barsy.help/210-dictionary/article.html>`__ в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__.

			*Когато е налично, надписва изчислената цена*
   * - **$price_change_group**
     - *int*
     - ID на група, към която принадлежи `артикула </barsy.help/210-dictionary/article.html>`__.

			*Необходимо за Mix-and-match промоции. Стойности 1-10*
   * - **$req_amount**
     - *float*
     - Необходимо минимално количество, което ще трябва да присъства в `сметката </barsy.help/210-dictionary/account.html>`__ за да бъде удовлетворено правилото

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

     .. literalinclude:: ../../sources/pricelists_save_articles/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/pricelists_save_articles/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/pricelists_save_articles/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/pricelists_save_articles/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/pricelists_save_articles/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/pricelists_save_articles/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__
 * `Ценово правило </barsy.help/210-dictionary/pricelist.html>`__


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

