.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articles_update
===========================================================
Актуализация на съществуващ артикул

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
Презаписва данните на съществуващ `артикул </barsy.help/210-dictionary/article.html>`__ по неговото ID. Подадените полета заместват текущите стойности — име, код, баркод, цена, ДДС група, мерна единица, `поток </barsy.help/210-dictionary/flow.html>`__, `доставчици </barsy.help/210-dictionary/supplier.html>`__, `категории </barsy.help/210-dictionary/category.html>`__ и допълнителни атрибути. Полета, които не са подадени, остават непроменени. Промените влизат в сила незабавно за всички касови интерфейси, онлайн магазина и активните `сметки </barsy.help/210-dictionary/account.html>`__, които използват `артикула </barsy.help/210-dictionary/article.html>`__.

Типични случаи: ръчна корекция на цена след промоция, актуализация на баркод след преетикетиране, синхронизация на пакетни промени от външна система, корекция на ДДС група след нормативна промяна. След актуализация системата автоматично преизчислява зависими `ценови правила </barsy.help/210-dictionary/pricelist.html>`__ и емитира webhook за промяна на `артикул </barsy.help/210-dictionary/article.html>`__.

**Име**: Articles_update
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
   * - **$article_id**
     - *int*
     - 
   * - **$article**
     - ArticleInputData_ 
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*void*                                                                 
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ArticleInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Описание на възможни входни данни за `артикул </barsy.help/210-dictionary/article.html>`__ при създаване или актуализиране

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleInputData

   * - Параметър
     - Тип
     - Описание
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Уникално за текущия каталог.*
   * - **$article_name_public_ml**
     - MultiLanguageData_ 
     - Публично име на `артикул </barsy.help/210-dictionary/article.html>`__. Мултиезично.

			*Вижда се на бележките, в публичния каталог, е-магазин и т.н. Не е уникално.*
   * - **$article_name_ml**
     - MultiLanguageData_ 
     - Публично име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Мултиезично.*
   * - **$article_aliases**
     - *array* | *string* | *null*
     - Синоним/и
   * - **$article_icon**
     - *string*
     - 
   * - **$ref_num**
     - *string*
     - Референтен номер.

			*Свободен текст*
   * - **$barcode**
     - *array* | *string* | *null*
     - Баркод на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$actual_price**
     - *float*
     - Базова продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$avg_delivery_price**
     - *float*
     - Средно претеглена доставна цена/себестойност без ДДС
   * - **$amount_unit**
     - *float*
     - Единица `продажба </barsy.help/210-dictionary/sale.html>`__ **По подразбиране:** 1
   * - **$amount_prod**
     - *float*
     - Единица `производство </barsy.help/210-dictionary/storeproduction.html>`__ **По подразбиране:** 1
   * - **$part_factor**
     - *float*
     - Коефициент за корекция на количество **По подразбиране:** 0
   * - **$amount_type_id**
     - *int*
     - ID на типа количество ( виж: :doc:`../amounttypes/getlist` ) **По подразбиране:** 1
   * - **$lot_type_id**
     - *int*
     -  **По подразбиране:** 1
   * - **$stream_id**
     - *int*
     - ID на `поток </barsy.help/210-dictionary/flow.html>`__, към който е `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../streams/getlist` ) **По подразбиране:** 1
   * - **$delete_flag**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е маркиран като изтрит

			* **0** - *Активен*
			* **1** - *Блокиран* **По подразбиране:** 0
   * - **$is_for_sale**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се продава

			* **0** - *не може да се продава*
			* **1** - *може да се продава* **По подразбиране:** 0
   * - **$is_for_load**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се зарежда

			* **0** - *не може да се зарежда*
			* **1** - *може да се зарежда* **По подразбиране:** 1
   * - **$is_for_client_order**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се поръчва в `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__

			* **0** - *Не*
			* **1** - *Да* **По подразбиране:** 1
   * - **$is_for_store_move**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се прехвърля

			* **0** - *Не*
			* **1** - *Да* **По подразбиране:** 1
   * - **$is_for_irequest**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се ползва във `вътрешни заявки </barsy.help/210-dictionary/irequest.html>`__

			* **0** - *Не*
			* **1** - *Да* **По подразбиране:** 1
   * - **$is_for_store_out**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се изписва

			* **0** - *не може да се изписва*
			* **1** - *може да се изписва* **По подразбиране:** 1
   * - **$is_for_request**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се заявява към `доставчик </barsy.help/210-dictionary/supplier.html>`__

			* **0** - *Не*
			* **1** - *Да* **По подразбиране:** 1
   * - **$is_for_sale_barsys**
     - *object*
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `продажба </barsy.help/210-dictionary/sale.html>`__ ($is_for_sale)
   * - **$is_for_client_order_barsys**
     - *object*
     - 
   * - **$is_for_irequest_barsys**
     - *object*
     - 
   * - **$is_for_store_move_barsys**
     - *object*
     - 
   * - **$is_for_store_out_barsys**
     - *object*
     - 
   * - **$is_for_request_barsys**
     - *object*
     - 
   * - **$is_for_load_barsys**
     - *object*
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `зареждане </barsy.help/210-dictionary/storeload.html>`__ ($is_for_sale)
   * - **$is_service**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е услуга

			* **0** - *Не*
			* **1** - *Да* **По подразбиране:** 0
   * - **$is_public**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е публично видим (в публичен каталог, е-магазин)

			* **0** - *Не*
			* **1** - *Да* **По подразбиране:** 0
   * - **$min_amount**
     - *float*
     - Минимално количество - под него сигнализира за недостатъчна наличност
   * - **$max_amount**
     - *float*
     - Максимално количество - допълно до него при `заявки към доставчици </barsy.help/210-dictionary/request.html>`__
   * - **$min_order**
     - *float*
     - Минимално възможно количество при поръчка в `продажба </barsy.help/210-dictionary/sale.html>`__ **По подразбиране:** 0
   * - **$max_order**
     - *float*
     - Минимално възможно количество при поръчка в `продажба </barsy.help/210-dictionary/sale.html>`__ **По подразбиране:** 0
   * - **$code**
     - *string*
     - Код на `артикул </barsy.help/210-dictionary/article.html>`__ - за бързо избиране от клавиатура,везна и др.
   * - **$user_prc**
     - *float*
     - Процент комисионна за персонал при `продажба </barsy.help/210-dictionary/sale.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$recipe_description**
     - *string*
     - 
   * - **$description_ml**
     - MultiLanguageData_ 
     - Описание на `артикула </barsy.help/210-dictionary/article.html>`__ (вътрешно — етикети и служебна употреба)
   * - **$description_public_ml**
     - MultiLanguageData_ 
     - Описание-публично — показва се в публичния каталог/B2B
   * - **$form_id_co**
     - *int*
     - ID на форма за допълнителна информация за `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__ **По подразбиране:** 1
   * - **$export_id**
     - *string*
     - ID при експорт на `артикули </barsy.help/210-dictionary/article.html>`__ - например за импорт в друга система
   * - **$ref_id**
     - *int*
     - ID на `артикула </barsy.help/210-dictionary/article.html>`__ при импорт от друга система
   * - **$picture**
     - *string*
     - Основна картинка на `артикула </barsy.help/210-dictionary/article.html>`__ от наличните за него
   * - **$tax_id**
     - *int*
     - ID на данъчната ставка ( виж: :doc:`../taxgroups/getlist` ) **По подразбиране:** 2
   * - **$cat_id**
     - *array* | *int* | *null*
     - ID на `категория </barsy.help/210-dictionary/category.html>`__ (или `категории </barsy.help/210-dictionary/category.html>`__ ако е подаден масив) в които `артикула </barsy.help/210-dictionary/article.html>`__ да бъде категоризиран.

			Първата добавена `категория </barsy.help/210-dictionary/category.html>`__ става главна (ако вече няма главна) ( виж: :doc:`../categories/getlist` )
   * - **$master_cat_id**
     - *int*
     - ID на главна `категория </barsy.help/210-dictionary/category.html>`__ **По подразбиране:** -1
   * - **$details**
     - ArticleDetailInputData_ []
     - Списък от характеристики към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$default_package_id**
     - *int*
     - ID на разфасовка по подразбиране (използва се при `зареждане </barsy.help/210-dictionary/storeload.html>`__) ( виж: :doc:`../packages/index_` , :doc:`../packages/edit` )
   * - **$sale_below_zero**
     - *string*
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се продава без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се продава без наличност*
			* **NO** - *НЕ може да се продава без наличност* **По подразбиране:** 'DEF'
   * - **$storemove_below_zero**
     - *string*
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се прехвърля без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се прехвърля без наличност*
			* **NO** - *НЕ може да се прехвърля без наличност* **По подразбиране:** 'DEF'
   * - **$storeout_below_zero**
     - *string*
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се изписва без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се изписва без наличност*
			* **NO** - *НЕ може да се изписва без наличност* **По подразбиране:** 'DEF'
   * - **$storeload_return_below_zero**
     - *string*
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се връща към `доставчик </barsy.help/210-dictionary/supplier.html>`__ без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се връща без наличност*
			* **NO** - *НЕ може да се връща без наличност* **По подразбиране:** 'DEF'
   * - **$max_amount_by_depots**
     - *object*
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове, за които има зададено максимално количество. $depot_id => max
   * - **$min_amount_by_depots**
     - *object*
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове, за които има зададено минимално количество. $depot_id => min
   * - **$slug**
     - *string*
     - Публичен URL
   * - **$intrastat**
     - *string*
     - 
   * - **$min_profit_percent**
     - *float*
     - 
   * - **$group_id**
     - *int*
     - ID на група атрибути
   * - **$delivery_price**
     - *float*
     - Доставна цена
   * - **$suppliers**
     - *object*
     - Информация за `доставчиците </barsy.help/210-dictionary/supplier.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$process_time**
     - *int*
     - Време за приготвяне - В секунди.

			Ползва се за сравнение между реалното време за изработване на `артикула </barsy.help/210-dictionary/article.html>`__ и се следи дали има закъснение при поръчката. Ако не бъде зададена стойност за конкретния `артикул </barsy.help/210-dictionary/article.html>`__, то се взема тази, която е зададена за `потока </barsy.help/210-dictionary/flow.html>`__.
   * - **$article_color**
     - *string*
     - Цвят на `артикула </barsy.help/210-dictionary/article.html>`__ в модул `продажби </barsy.help/210-dictionary/sale.html>`__
   * - **$extra_data**
     - *object*
     - 
   * - **$article_type**
     - *int*
     -  **По подразбиране:** 1
   * - **$max_discount**
     - *float*
     - 
   * - **$supplements_type**
     - *string*
     - Тип комбо `артикул </barsy.help/210-dictionary/article.html>`__.

			Влияе на визуализирането на `артикула </barsy.help/210-dictionary/article.html>`__ при обслужване, ако той има комбо групи.

			* **combo** - *Липсва описание*
			* **supplements** - *Липсва описание* **По подразбиране:** 'combo'

-----

MultiLanguageData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: MultiLanguageData

   * - Параметър
     - Тип
     - Описание
   * - **$bg_BG**
     - *string*
     - 
   * - **$en_US**
     - *string*
     - 
   * - **$de_DE**
     - *string*
     - 
   * - **$es_ES**
     - *string*
     - 
   * - **$fr_FR**
     - *string*
     - 
   * - **$it_IT**
     - *string*
     - 
   * - **$ro_RO**
     - *string*
     - 
   * - **$ru_RU**
     - *string*
     - 
   * - **$sr_RS**
     - *string*
     - 
   * - **$el_GR**
     - *string*
     - 
   * - **$tr_TR**
     - *string*
     - 

-----

ArticleDetailInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за създаване създаване/редактиране на детайл към `артикул </barsy.help/210-dictionary/article.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailInputData

   * - Параметър
     - Тип
     - Описание
   * - **$detail_id**
     - *int*
     - ID на детайл (празно за нов)
   * - **$detail_name**
     - *string*
     - Име на детайл (подава се за създаване на нов)
   * - **$detail_value**
     - *string*
     - Стойност на детайл
   * - **$key_id**
     - *int*
     - ID на стойност на детайл (празно за нова)

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

     .. literalinclude:: ../../sources/articles_update/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articles_update/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articles_update/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articles_update/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articles_update/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articles_update/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__


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

