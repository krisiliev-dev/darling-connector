.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storeloads_create
===========================================================
Създаване на нова операция Зареждане от доставчик

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/150-store/10-storeloads/index </barsy.help/110-admin/150-store/10-storeloads/index.html>`__
	 * barsy.help: `210-dictionary/storeload </barsy.help/210-dictionary/storeload.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира нов складов документ от тип "`Зареждане </barsy.help/210-dictionary/storeload.html>`__" — постъпление на стока в избран `склад </barsy.help/210-dictionary/store.html>`__ с конкретен `доставчик </barsy.help/210-dictionary/supplier.html>`__, дата, валута, документ-основание и редове по `артикули </barsy.help/210-dictionary/article.html>`__ с количество, единична цена, отстъпки и партиди. Документът може да бъде запазен в чернова (`save`) за по-късно дописване, или приключен веднага (`save_and_close`), при което количествата официално влизат в наличностите и се отразяват в себестойността чрез метода, конфигуриран за `склада </barsy.help/210-dictionary/store.html>`__ (средно претеглена или партидна).

Типични случаи: ежедневно осчетоводяване на доставки от търговски `представител </barsy.help/210-dictionary/person.html>`__, импорт на електронни `фактури </barsy.help/210-dictionary/invoice.html>`__ от `доставчик </barsy.help/210-dictionary/supplier.html>`__, начално `зареждане </barsy.help/210-dictionary/storeload.html>`__ на `склад </barsy.help/210-dictionary/store.html>`__ при стартиране на нов обект. При приключване автоматично се регенерират партиди и се изпращат webhook събития за интеграции.

**Име**: Storeloads_create
**Категория**: Store


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$store_load**
     - StoreLoadInputData_ 
     - Инфорамция за `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$articles**
     - StoreLoadInputRowData_ []
     - Информация за `артикулите </barsy.help/210-dictionary/article.html>`__ в `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$action_type**
     - *string*
     - [save=Запис без приключване, save_and_close=Запис с приключване] **По подразбиране:** 'save'


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на създаденото зареждане
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreLoadInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за опреция `зареждане </barsy.help/210-dictionary/storeload.html>`__ от `доставчик </barsy.help/210-dictionary/supplier.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreLoadInputData

   * - Параметър
     - Тип
     - Описание
   * - **$depot_id**
     - *int*
     - Id на `склад </barsy.help/210-dictionary/store.html>`__, който ще се зарежда ( виж: :doc:`../depots/getlist` )
   * - **$supplier_id**
     - *int*
     - ID на `доставчик </barsy.help/210-dictionary/supplier.html>`__ по `зареждането </barsy.help/210-dictionary/storeload.html>`__ ( виж: :doc:`../suppliers/getlist` ) **По подразбиране:** 1
   * - **$doc_date**
     - *string*
     - Дата на документа (дата на завеждане на стоката в `склада </barsy.help/210-dictionary/store.html>`__)
   * - **$doc_num**
     - *string*
     - Номер на документа.

			*Трябва да е уникален за търговския обект*
   * - **$doc_type_id**
     - *int*
     - Тип на подадения документ ( виж: :doc:`../storeloads/getdocumenttypes` ) **По подразбиране:** 1
   * - **$price_mode**
     - *int*
     - Флаг дали подадените единични цени на `артикули </barsy.help/210-dictionary/article.html>`__ са с ДДС или без **По подразбиране:** 0
   * - **$has_tax**
     - *int*
     - Флаг дали документът е с начислен ДДС **По подразбиране:** 1
   * - **$description**
     - *string*
     - Свободен текст
   * - **$operation_type**
     - *int*
     - Фалг дали документа е за `зареждане </barsy.help/210-dictionary/storeload.html>`__ на стока (1) или за връщане на стока (2) **По подразбиране:** 1
   * - **$paid_due_date**
     - *string*
     - Крайна дата за `плащане </barsy.help/210-dictionary/payment.html>`__ към `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$currency_id**
     - *int*
     - ID на валута, в която са подадени единичните цени на `артикулите </barsy.help/210-dictionary/article.html>`__.

			*Ако е оставена непопълнена, ще се вземе системната валута*
   * - **$currency_rate**
     - *float*
     - Курс на подадената валута към базовата валута на системата (BGN) към момента на сделката
   * - **$paymethod_id**
     - *int*
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ към `доставчика </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../paymentmethods/getlist` )
   * - **$request_id**
     - *int*
     - ID на `заявката към доставчик </barsy.help/210-dictionary/request.html>`__, от която се прави `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$store_load_cat_id**
     - *int*
     - ID на `категорията </barsy.help/210-dictionary/category.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__ **По подразбиране:** 1
   * - **$extra_doc_num**
     - *string*
     - Допълнителен номер на документа
   * - **$discount**
     - *float*
     -  **По подразбиране:** 0
   * - **$preferred_paymethod_id**
     - *int*
     - Предпочитан начин за `плащане </barsy.help/210-dictionary/payment.html>`__

-----

StoreLoadInputRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreLoadInputRowData

   * - Параметър
     - Тип
     - Описание
   * - **$store_load_row_id**
     - *int*
     - ID на ред в `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$original_article_name**
     - *string*
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, който се зарежда ( виж: :doc:`../articles/getlist` )
   * - **$amount**
     - *float*
     - Количество, което се зарежда в `склада </barsy.help/210-dictionary/store.html>`__ (в основна единици: бр, кг, л,...)
   * - **$current_price**
     - *float*
     - Единична доставна цена, на която се зарежда `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$actual_price**
     - *float*
     - Единична продажна цена
   * - **$delivery_tax_id**
     - *int*
     - ID на ДДС за доставка
   * - **$notes**
     - *string*
     - Свободен текст към реда на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$package_name**
     - *string*
     - Име на опаковката (при използване на опаковки)
   * - **$package_ratio**
     - *float*
     - Количеството в една опаковка (при използване на опаковки)
   * - **$attributes**
     - *array*
     - Атрибути
   * - **$return_from_store_load_row_id**
     - *int*
     - Id на ред в `зареждане </barsy.help/210-dictionary/storeload.html>`__, връзка при връщане на стока
   * - **$deal_id**
     - *int*
     - Id на сделка
   * - **$lot_value**
     - *string*
     - Партида номер
   * - **$lot_exp_date**
     - *string*
     - Партида дата - срок на годност
   * - **$lot_detail_id**
     - *int*
     - Id на партидата в операцията
   * - **$manufacturer**
     - *string*
     - Производител
   * - **$add_data**
     - *array*
     - Допълнителни данни/колони - конфигурируеми
   * - **$discount**
     - *float*
     -  **По подразбиране:** 0

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

     .. literalinclude:: ../../sources/storeloads_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storeloads_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storeloads_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storeloads_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storeloads_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storeloads_create/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Доставчик </barsy.help/210-dictionary/supplier.html>`__
 * `Зареждане </barsy.help/210-dictionary/storeload.html>`__


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

