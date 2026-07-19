.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Clientorders_getdetails
===========================================================
Артикули в клиентска заявка

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/client-order </barsy.help/210-dictionary/client-order.html>`__
	 * barsy.help: `110-admin/160-pos/client-orders/index </barsy.help/110-admin/160-pos/client-orders/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с поръчаните редове (`артикули </barsy.help/210-dictionary/article.html>`__) в дадена `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__. За всеки ред — `артикул </barsy.help/210-dictionary/article.html>`__, количество, мерна единица, единична цена, отстъпка, крайна сума, приложени `модификатори </barsy.help/210-dictionary/modificator.html>`__/опции, бележка от `клиента </barsy.help/210-dictionary/client.html>`__ и евентуален пълен снапшот на `артикула </barsy.help/210-dictionary/article.html>`__ към момента на поръчката (име, код), за да остане заявката четима дори ако `артикулът </barsy.help/210-dictionary/article.html>`__ се промени или изтрие в каталога.

Типични случаи: изпращане на работна бона към `склад </barsy.help/210-dictionary/store.html>`__/кухня за подготовка, изграждане на товарителен лист за куриер, изчисление на нужни материали по рецепти преди `производство </barsy.help/210-dictionary/storeproduction.html>`__, печат на пред-разписка.

**Име**: Clientorders_getdetails
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
   * - **$client_order_id**
     - *int*
     - ID на `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ClientOrderRowData_                                                    Списък с артикули в заявката
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ClientOrderRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientOrderRowData

   * - Параметър
     - Тип
     - Описание
   * - **$client_order_row**
     - *integer*
     - ID на реда
   * - **$article_id**
     - *integer*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ по номенклатура на barsy
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__ по номенклатура на barsy
   * - **$amount**
     - *float*
     - Желано количество - може да бъде дробно число до 9-ти знак
   * - **$current_price**
     - *float*
     - Единична цена на поръчката - ако не е подадена, ще бъде ползвана текущата цена за този `търговски обект </barsy.help/210-dictionary/barsy.html>`__/`клиент </barsy.help/210-dictionary/client.html>`__/`артикул </barsy.help/210-dictionary/article.html>`__
   * - **$detail_notes**
     - *string*
     - Свободен текст - Може да съдържа някакви допълнително описание към конкретния `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$details**
     - *object*
     - Детайли към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$detail_status**
     - *int*
     - 
   * - **$user_id**
     - *int*
     - Id на `потребител </barsy.help/210-dictionary/user.html>`__, въвел `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$last_update**
     - *string*
     - Последна промяна на `артикула </barsy.help/210-dictionary/article.html>`__ в заявката
   * - **$details_checksum**
     - *string*
     - Чексума на данните на реда
   * - **$amount_type_name_short**
     - *string*
     - Тип количество - кратко име
   * - **$package_name**
     - *string*
     - Име на разфасовката (при използване на разфасовки)
   * - **$package_ratio**
     - *float*
     - Количеството в една разфасовка (при използване на разфасовки)

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

     .. literalinclude:: ../../sources/clientorders_getdetails/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/clientorders_getdetails/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/clientorders_getdetails/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/clientorders_getdetails/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/clientorders_getdetails/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clientorders_getdetails/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__
 * `Клиентска заявка </barsy.help/210-dictionary/client-order.html>`__


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

