.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Barsys_getcurrent
===========================================================
Текущ търговски обект

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/barsy </barsy.help/210-dictionary/barsy.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълни данни за търговския обект (barsy), в чийто контекст работи текущата сесия — основни данни (име, адрес, идентификатори), асоциирано меню, валута, езици, работно време, специфични настройки. Допълнително връща версията на приложението (`app_version`) и timestamp на последна промяна в менюто (`info_last_update`) — за инкрементални обновления в клиентски кеш.

*Типични случаи: bootstrap на касов/онлайн интерфейс с информация за обекта, проверка дали менюто е обновено (cache invalidation), показване на адрес и работно време в публична страница.*

**Име**: Barsys_getcurrent
**Категория**: Catalog


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
BarsyCurrentData_                                                      информация за текущия търговски обект
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

BarsyCurrentData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Описание на текущ `търговски обект </barsy.help/210-dictionary/barsy.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: BarsyCurrentData

   * - Параметър
     - Тип
     - Описание
   * - **$menu_id**
     - *int*
     - ID на каталог
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$name**
     - *string*
     - Име на търговския обект
   * - **$logo**
     - *string*
     - Име на файлът, отговарящ за логото
   * - **$background_color**
     - *string*
     - Основен цвят за този `търговски обект </barsy.help/210-dictionary/barsy.html>`__.

			*Използва се за условно визуално отличаване на текущия обект*
   * - **$default_payment_method**
     - *int*
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране
   * - **$app_version**
     - *string*
     - Текуща версия на инсталацията
   * - **$info_last_update**
     - *int*
     - timestamp на последната промяна на каталога, използван от този `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$method**
     - *string*
     - 

			* **IP** - *Липсва описание*
			* **POS_KEY** - *Липсва описание*
			* **PUBLIC** - *Липсва описание*
			* **ID** - *Липсва описание*
			* **AUTO** - *Липсва описание*
			* **REMOTE_SYSTEM** - *Липсва описание*
   * - **$user_pos_id**
     - *int*
     - 
   * - **$cat_id**
     - 
     - 
   * - **$delete_flag**
     - 
     - 
   * - **$set_tab_default**
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

     .. literalinclude:: ../../sources/barsys_getcurrent/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/barsys_getcurrent/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/barsys_getcurrent/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/barsys_getcurrent/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/barsys_getcurrent/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/barsys_getcurrent/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Търговски обект </barsy.help/210-dictionary/barsy.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

