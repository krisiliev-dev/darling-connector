.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Accounts_divide
===========================================================
Разделяне на сметка

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/account </barsy.help/210-dictionary/account.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Разделя отворена `сметка </barsy.help/210-dictionary/account.html>`__ на две — създава нова `сметка </barsy.help/210-dictionary/account.html>`__ и прехвърля в нея избраните `артикули </barsy.help/210-dictionary/article.html>`__ с конкретни количества; от оригиналната `сметка </barsy.help/210-dictionary/account.html>`__ количествата се отписват. Може да се прехвърли и определен брой посетители (`persons`) за коректно изчисление на средна `сметка </barsy.help/210-dictionary/account.html>`__. По избор новата `сметка </barsy.help/210-dictionary/account.html>`__ се асоциира с конкретен `клиент </barsy.help/210-dictionary/client.html>`__ (`client_id`), което позволява раздяла "по `клиент </barsy.help/210-dictionary/client.html>`__" в ресторант.

Типични случаи: на масата всеки иска да плати своите си `артикули </barsy.help/210-dictionary/article.html>`__ поотделно, разделяне на корпоративна `сметка </barsy.help/210-dictionary/account.html>`__ на персонална/представителна част, отделяне на върнати `артикули </barsy.help/210-dictionary/article.html>`__ в собствена `сметка </barsy.help/210-dictionary/account.html>`__ преди сторно. За пълно копие виж `Accounts_clone`, за обединяване обратно — `Accounts_merge`.

**Име**: Accounts_divide
**Категория**: Cashdesk


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$old_account_id**
     - *int*
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__ за разделяне
   * - **$orders**
     - OrderMakeData_ []
     - списък на желаните `артикули </barsy.help/210-dictionary/article.html>`__ с техните количества
   * - **$persons**
     - *int*
     - Колко посетители да бъдат прехвърлени към новата `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$client_id**
     - *int*
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__ за новата `сметка </barsy.help/210-dictionary/account.html>`__.

			*Ако не е подаден, ще бъде сложен Анонимен* **По подразбиране:** 1


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на новата сметка
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

OrderMakeData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: OrderMakeData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *float*
     - Количество
   * - :deprecated:`$current_price`
     - *float*
     - Продажна цена (ако се пропусне - ще се използва текущата) :deprecated_text:`Отхвърлено: Използваме original_current_price вместо това поле`
   * - **$original_current_price**
     - *float*
     - Продажна цена (ако се пропусне - ще се използва текущата)
   * - **$discount**
     - *float*
     - Отстъпка/надценка в проценти на продажната цена на `артикул </barsy.help/210-dictionary/article.html>`__ в `сметка </barsy.help/210-dictionary/account.html>`__ (различно от отстъпка на цялата `сметка </barsy.help/210-dictionary/account.html>`__)
   * - **$tax_id**
     - *int*
     - ДДС
   * - **$modificators**
     - ModificatorInputData_ []
     - 
   * - **$article_attributes**
     - ArticleAttributesSimpleData_ 
     - 
   * - **$supplements**
     - ArticleSupplementData_ []
     - Комбинирани `артикули </barsy.help/210-dictionary/article.html>`__
   * - **$storno_of_account_id**
     - *int*
     - Номер на `сметка </barsy.help/210-dictionary/account.html>`__ по което се сторнира тази поръчка (само при отрицателно количество)
   * - **$tax_region_id**
     - *int*
     - ID на данъчен регион

-----

ModificatorInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ModificatorInputData

   * - Параметър
     - Тип
     - Описание
   * - **$mod_name**
     - *string*
     - Име на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$description**
     - *string*
     - Описание на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_type**
     - *int*
     - Тип `модификатор </barsy.help/210-dictionary/modificator.html>`__

			* **1** - *Липсва описание*
			* **2** - *Липсва описание*

-----

ArticleAttributesSimpleData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleAttributesSimpleData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - 
   * - **$amount**
     - *float*
     - 
   * - **$attributes**
     - 
     - 

-----

ArticleSupplementData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleSupplementData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, в участва в комбо `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *float*
     - Количество на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо
   * - **$supplement_price**
     - *float*
     - цена на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо (ако не се подаде, се ползва зададената или изчислената)
   * - **$supplement_group_id**
     - *int*
     - ID на група на комбото, в която участва `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$discount**
     - *float*
     - Отстъпка на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо
   * - **$tax_id**
     - *int*
     - ДДС id на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$tax_region_id**
     - *int*
     - ID на тип доставка
   * - **$article_attributes**
     - *array*
     - Атрибути на `артикула </barsy.help/210-dictionary/article.html>`__ (при `артикули </barsy.help/210-dictionary/article.html>`__ с дефинирани атрибути — цвят, размер и т.н.).

			*Структура: [{article_id, amount, attributes: [{key, value}, ...]}]*
   * - **$lot_value**
     - *string*
     - Партида на supplement-а (за `артикули </barsy.help/210-dictionary/article.html>`__ с LOT_TYPE_ID > 1).
   * - **$supplement_article**
     - 
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

     .. literalinclude:: ../../sources/accounts_divide/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/accounts_divide/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/accounts_divide/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/accounts_divide/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/accounts_divide/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/accounts_divide/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

