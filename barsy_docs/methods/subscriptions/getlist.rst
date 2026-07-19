.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Subscriptions_getlist
===========================================================
Списък с абонаменти

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/subscription </barsy.help/210-dictionary/subscription.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с дефинираните в системата абонаментни планове — типове периодични услуги, които `клиенти </barsy.help/210-dictionary/client.html>`__ могат да закупят за фиксиран срок (месечно, годишно, etc) и да получат продължително право или преференциални условия. Всеки `абонамент </barsy.help/210-dictionary/subscription.html>`__ включва период, цена, асоциирани `артикули </barsy.help/210-dictionary/article.html>`__/услуги, отстъпки, политика за подновяване.

Типични случаи: каталог "Абонаментни планове" в онлайн магазин, конфигуриране на лоялна програма, корпоративни B2B `абонаменти </barsy.help/210-dictionary/subscription.html>`__ за пакетни услуги, попълване на dropdown при `ценови правила </barsy.help/210-dictionary/pricelist.html>`__ обвързани с `абонамент </barsy.help/210-dictionary/subscription.html>`__.

**Име**: Subscriptions_getlist
**Категория**: Catalog


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
SubscriptionData_                                                      
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

SubscriptionData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: SubscriptionData

   * - Параметър
     - Тип
     - Описание
   * - **$subscription_id**
     - *int*
     - 
   * - **$barsy_id**
     - *int*
     - 
   * - **$subscription_name**
     - *string*
     - 
   * - **$description**
     - *string*
     - 
   * - **$delete_flag**
     - *int*
     - 
   * - **$user_id**
     - *int*
     - 
   * - **$inv_item_template**
     - *string*
     - 
   * - **$inv_item_type**
     - *int*
     - 
   * - **$last_run**
     - *string*
     - 
   * - **$user_name**
     - *string*
     - 
   * - **$paid_period**
     - *int*
     - 
   * - **$paid_due_date**
     - *string*
     - 
   * - **$resources**
     - *array*
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

     .. literalinclude:: ../../sources/subscriptions_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/subscriptions_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/subscriptions_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/subscriptions_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/subscriptions_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/subscriptions_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Абонамент </barsy.help/210-dictionary/subscription.html>`__


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

