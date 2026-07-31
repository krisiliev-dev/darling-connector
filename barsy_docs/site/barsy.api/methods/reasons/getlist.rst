.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reasons_getlist
===========================================================
Причини за отказ на поръчка

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с причините, които могат да се избират при отказване на поръчка в отворена `сметка </barsy.help/210-dictionary/account.html>`__. Всяка причина има ключова бизнес характеристика — флаг "отписва от `склад </barsy.help/210-dictionary/store.html>`__" — който определя дали отказаната поръчка все пак ще предизвика складово движение или ще се счита за никога не консумирана. Например ако `клиентът </barsy.help/210-dictionary/client.html>`__ отказва вече приготвено капучино, продуктите са вече използвани и трябва да се отпишат, но не и да се таксуват.

Типични случаи: dropdown в диалога "Откажи поръчка" в POS `касата </barsy.help/210-dictionary/pos.html>`__, конфигуриране на бизнес правила за управление на загуби, изграждане на справка "Откази по причини".

**Име**: Reasons_getlist
**Категория**: Settings


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ReasonData_                                                            
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReasonData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReasonData

   * - Параметър
     - Тип
     - Описание
   * - **$reason_id**
     - *int*
     - ID на причината
   * - **$name**
     - *string*
     - Име на причината
   * - **$upd_store**
     - *int*
     - Флаг дали тази причина изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при финализиране на `сметката </barsy.help/210-dictionary/account.html>`__

			* **0** - Изтегля от `склада </barsy.help/210-dictionary/store.html>`__
			* **1** - Не изтегля от `склада </barsy.help/210-dictionary/store.html>`__

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

     .. literalinclude:: ../../sources/reasons_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reasons_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reasons_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reasons_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reasons_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reasons_getlist/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

