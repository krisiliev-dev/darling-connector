.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Taxgroups_getlist
===========================================================
Списък с ДДС групи

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с конфигурираните в системата данъчни групи (ДДС групи) — например "20% стандартна ставка", "9% намалена ставка", "0% освободени", "Експорт". За всяка група: ID, име, процент, флаг за активност, евентуален лимит на валидност. ДДС групите се асоциират с `артикули </barsy.help/210-dictionary/article.html>`__ и определят как се изчислява и отчита данъкът във фискалните бележки и `фактурите </barsy.help/210-dictionary/invoice.html>`__.

Типични случаи: попълване на dropdown "ДДС група" при създаване/редакция на `артикул </barsy.help/210-dictionary/article.html>`__, конфигуриране на `ценови правила </barsy.help/210-dictionary/pricelist.html>`__ с данъчна диференциация, синхронизация към счетоводна система.

**Име**: Taxgroups_getlist
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
   * - **$filters**
     - TaxGroupsListFiltersData_ 
     - 
   * - **$list_options**
     - TaxGroupsListOptions_ 
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

TaxGroupsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: TaxGroupsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$tax_id**
     - *int*
     - ID на ДДС група
   * - **$tax**
     - *int*
     - Процент на ДДС група
   * - **$tax_name**
     - *string*
     - Име на ДДС група
   * - **$is_default**
     - *int*
     - Дали се ползва по подразбиране
   * - **$tax_code**
     - *string*
     - Код на ДДС група
   * - **$country_id**
     - *array* | *string* | *null*
     - Държава на ДДС група

-----

TaxGroupsListOptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: TaxGroupsListOptions

   * - Параметър
     - Тип
     - Описание
   * - **$row_key**
     - *string*
     - 

			* **tax_id** - *Липсва описание*

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

     .. literalinclude:: ../../sources/taxgroups_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/taxgroups_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/taxgroups_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/taxgroups_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/taxgroups_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/taxgroups_getlist/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

