.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Amounttypes_getlist
===========================================================
Списък с мерни единици

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с конфигурираните в системата мерни единици (брой, килограми, литри, метри, часове, нощувки, ...) — за всяка единица: ID, име, кратко означение (kg, l, бр.), точност на десетичните знаци, флаг за активност. Мерните единици се асоциират с `артикули </barsy.help/210-dictionary/article.html>`__ и определят как се записват количествата в `склад </barsy.help/210-dictionary/store.html>`__ и при `продажба </barsy.help/210-dictionary/sale.html>`__ (с/без знак за десетичен или цяло).

Типични случаи: попълване на dropdown "Мерна единица" при създаване на `артикул </barsy.help/210-dictionary/article.html>`__, конфигуриране на UI за количествени полета (везна, тегло), валидация на формата на количеството при импорт от външна система.

**Име**: Amounttypes_getlist
**Категория**: Catalog


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
AmountTypeData_                                                        
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

AmountTypeData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: AmountTypeData

   * - Параметър
     - Тип
     - Описание
   * - **$amount_type_id**
     - *int*
     - ID на типа ( виж: :doc:`../amounttypes/getlist` )
   * - **$amount_type_name**
     - *string*
     - Име на типа ( виж: :doc:`../amounttypes/getlist` )
   * - **$amount_type_name_short**
     - *string*
     - Кратко име на типа
   * - **$time_interval**
     - *int*
     - 
   * - **$value_precision**
     - *float*
     - Точност след десетичния знак
   * - **$export_id**
     - *string*
     - ID при експорт на тип - например за импорт в друга система

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

     .. literalinclude:: ../../sources/amounttypes_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/amounttypes_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/amounttypes_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/amounttypes_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/amounttypes_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/amounttypes_getlist/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

