.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articles_pricelists_save
===========================================================
Запис на артикул към ценови правила

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
Записва кои `ценови правила </barsy.help/210-dictionary/pricelist.html>`__ (pricelists) действат върху даден `артикул </barsy.help/210-dictionary/article.html>`__ и с каква специфична стойност — фиксирана цена, процент отстъпка/надценка, специален ДДС режим. Подадените редове ПРЕЗАПИСВАТ всички текущи асоциации на `артикула </barsy.help/210-dictionary/article.html>`__ с `ценови правила </barsy.help/210-dictionary/pricelist.html>`__; за добавяне без триене се ползва частично API на самите `ценови правила </barsy.help/210-dictionary/pricelist.html>`__. Действителната цена на `артикул </barsy.help/210-dictionary/article.html>`__ за конкретна `сметка </barsy.help/210-dictionary/account.html>`__ се изчислява от приложимото `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ според `клиент </barsy.help/210-dictionary/client.html>`__/обект/период.

Типични случаи: бързо включване на `артикул </barsy.help/210-dictionary/article.html>`__ в активна промоция, добавяне на VIP цена за определени `клиенти </barsy.help/210-dictionary/client.html>`__, изключване на `артикул </barsy.help/210-dictionary/article.html>`__ от групово правило с индивидуална цена. След записа активните `сметки </barsy.help/210-dictionary/account.html>`__ и кеша на цените се рекалкулират.

**Име**: Articles_pricelists_save
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
     - ID на дадения `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$rows**
     - ArticlePricelistData_ []
     - Списък от `ценови правила </barsy.help/210-dictionary/pricelist.html>`__, към който да бъде включен дадения `артикул </barsy.help/210-dictionary/article.html>`__. ( виж: :doc:`../pricelists/index_` )


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  няма
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ArticlePricelistData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticlePricelistData

   * - Параметър
     - Тип
     - Описание
   * - **$id**
     - *int*
     - ID на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ ( виж: :doc:`../pricelists/index_` )
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

     .. literalinclude:: ../../sources/articles_pricelists_save/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articles_pricelists_save/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articles_pricelists_save/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articles_pricelists_save/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articles_pricelists_save/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articles_pricelists_save/barsy_api_client_simple.php
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

