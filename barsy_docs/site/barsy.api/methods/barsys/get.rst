.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Barsys_get
===========================================================
Подробни данни за търговски обект

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/barsy </barsy.help/210-dictionary/barsy.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълния запис на един `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (barsy) по неговото ID — основни данни (име, тип, лого, фоново оформление), асоциирано меню, език и валута, метод на `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране, `фирма </barsy.help/210-dictionary/company.html>`__ по подразбиране, както и публичните данни за обекта (публично име, адрес, телефони, имейл, работно време, координати, описание и снимки), използвани в онлайн поръчките и `резервациите </barsy.help/210-dictionary/reservation.html>`__.

Типични случаи: `зареждане </barsy.help/210-dictionary/storeload.html>`__ на настройките на обект при редактиране в админ панела, презареждане на актуалните данни за конкретна локация в multi-site бизнес, извличане на публичните данни за обекта при показване в онлайн магазин или приложение за поръчки.

**Име**: Barsys_get
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
   * - **$barsy_id**
     - *int*
     - ID на търговския обект


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
BarsysData_                                                            
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

BarsysData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: BarsysData

   * - Параметър
     - Тип
     - Описание
   * - **$barsy_id**
     - *int*
     - 
   * - **$name**
     - 
     - 
   * - **$cat_id**
     - 
     - 
   * - **$delete_flag**
     - 
     - 
   * - **$logo**
     - 
     - 
   * - **$background_color**
     - 
     - 
   * - **$set_tab_default**
     - 
     - 
   * - **$menu_id**
     - 
     - 
   * - **$default_payment_method**
     - 
     - 
   * - **$barsy_type_id**
     - 
     - 
   * - **$delivery_article_id**
     - *int*
     - 
   * - **$default_company_id**
     - *int*
     - 
   * - **$lang_id**
     - 
     - 
   * - **$public_cat_id**
     - 
     - 
   * - **$public_pictures**
     - 
     - 
   * - **$public_description**
     - 
     - 
   * - **$public_address**
     - 
     - 
   * - **$public_phones**
     - 
     - 
   * - **$public_website**
     - 
     - 
   * - **$public_coordinates**
     - 
     - 
   * - **$export_id**
     - 
     - 
   * - **$logo_pos**
     - 
     - 
   * - **$weight**
     - 
     - 
   * - **$public_name**
     - 
     - 
   * - **$public_email**
     - 
     - 
   * - **$public_work_time**
     - 
     - 
   * - **$set_tabs_visible**
     - 
     - 
   * - **$franchise_flag**
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

     .. literalinclude:: ../../sources/barsys_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/barsys_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/barsys_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/barsys_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/barsys_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/barsys_get/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Търговски обект </barsy.help/210-dictionary/barsy.html>`__


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

