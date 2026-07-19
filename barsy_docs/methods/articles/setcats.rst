.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articles_setcats
===========================================================
Категоризиране на артикул

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
Асоциира `артикул </barsy.help/210-dictionary/article.html>`__ с една или повече `категории </barsy.help/210-dictionary/category.html>`__ от менюто. Едната от тях се отбелязва като "главна" (`master_cat_id`) — тя определя позицията на `артикула </barsy.help/210-dictionary/article.html>`__ в основната йерархия (например за справки и breadcrumbs), останалите са допълнителни (cross-listings). Чрез `remove_currents` се избира дали подаденият списък да замени напълно текущите `категории </barsy.help/210-dictionary/category.html>`__, или да се добави към тях. След промяната автоматично се преоценяват приложимите `ценови правила </barsy.help/210-dictionary/pricelist.html>`__ базирани на `категория </barsy.help/210-dictionary/category.html>`__.

Типични случаи: разместване на `артикул </barsy.help/210-dictionary/article.html>`__ между `категории </barsy.help/210-dictionary/category.html>`__ след реорганизация на менюто, добавяне на сезонен `артикул </barsy.help/210-dictionary/article.html>`__ в "Нови" и "Промоции" едновременно, миграция от плоска към йерархична категоризация, синхронизация на `категории </barsy.help/210-dictionary/category.html>`__ от външна PIM система.

**Име**: Articles_setcats
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
     - ID на желания `артикул </barsy.help/210-dictionary/article.html>`__, който се категоризира
   * - **$cats**
     - *array*
     - Списък от ID-та на `категории </barsy.help/210-dictionary/category.html>`__, в които се категоризира `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$master_cat_id**
     - *int*
     - ID на `категория </barsy.help/210-dictionary/category.html>`__ (от подадения списък), която да бъде маркирана като главна
   * - **$remove_currents**
     - *bool*
     - При подадена стойност=1, текущите `категории </barsy.help/210-dictionary/category.html>`__ ще бъдат подменени с подадените.

			*При стойност=0 - подадените ще бъдат добавени към текущите* **По подразбиране:** true


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  1
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

     .. literalinclude:: ../../sources/articles_setcats/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articles_setcats/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articles_setcats/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articles_setcats/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articles_setcats/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articles_setcats/barsy_api_client_simple.php
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

