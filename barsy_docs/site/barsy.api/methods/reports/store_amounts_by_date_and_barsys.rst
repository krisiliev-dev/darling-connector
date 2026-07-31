.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_store_amounts_by_date_and_barsys
===========================================================
Наличности по обекти и дата

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/114_Warehouse/index </barsy.help/110-admin/170-reports/114_Warehouse/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Историческа справка за складовите наличности към конкретна дата, разбита по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__. За всеки `артикул </barsy.help/210-dictionary/article.html>`__ се връща наличността в всеки обект отделно — удобно за централно управление на multi-site бизнес. Реконструира моментно състояние от хронологичните движения.

*Типични случаи: централна управителска справка "Кой обект има колко от какво към 31.12", разпределителна логистика преди голяма доставка, годишен счетоводен баланс на запасите по обекти.*

**Име**: Reports_store_amounts_by_date_and_barsys
**Категория**: Reports


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$action_type**
     - *string*
     - Тип на върнатите данни

			* **content** - *структура на списъка*
			* **values** - *стойности на списъка* **По подразбиране:** 'content'
   * - **$id**
     - *string*
     - ID на обекта, който се обработва

			*Складови наличности към дата*
   * - **$filters**
     - ReportsStoreAmountsByDateAndBarsysFilters_ 
     - масив от налични филтри за този списък.

			*Всички са опционални* **По подразбиране:** []
   * - **$page_num**
     - *int*
     - Номер на желана страница **По подразбиране:** 1
   * - **$rows**
     - *int*
     - Брой реда на страница **По подразбиране:** 50
   * - **$order_by**
     - *string*
     - Сортиране по (името на колоната като елемент)
   * - **$order_dir**
     - *string*
     - Посока на сортиране

			* **asc** - *възходящо*
			* **desc** - *низходящо*
   * - **$columns**
     - *array*
     - Списък от колоните, които да бъдат включени в отговора (ако е празен, показва избрани по подразбиране)

			* **article_id** - `Артикул </barsy.help/210-dictionary/article.html>`__ ID (Номер на `артикул </barsy.help/210-dictionary/article.html>`__)
			* **picture** - Снимка (Снимка на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **article_name** - Име на `артикул </barsy.help/210-dictionary/article.html>`__
			* **barcode** - Баркод (Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **master_cat_id** - `Категория </barsy.help/210-dictionary/category.html>`__ път (Пълен път на главна `категория </barsy.help/210-dictionary/category.html>`__)
			* **actual_price** - Продажна цена към дата (Продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ към избраната дата)
			* **actual_price__sec_curr** - Продажна цена към дата (Български лев) (Продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ към избраната дата)
			* **amount_unit** - Единица `продажба </barsy.help/210-dictionary/sale.html>`__ (Количество, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при единична `продажба </barsy.help/210-dictionary/sale.html>`__)
			* **ref_num** - Референтен номер (Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **stream_name** - `Поток </barsy.help/210-dictionary/flow.html>`__ (`Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **store_amount_2** - Втори търговски (Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__)
			* **store_amount_1** - Незнайно (Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__)
			* **store_amount_3** - Трети обект (Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__)
			* **amount** - *Общо кол (Общо налично количество към избраната дата)*
			* **avg_delivery_price** - *Себестойност (без ДДС) (Средно претеглена себестойност без ДДС към датата)*
			* **avg_delivery_price__sec_curr** - *Себестойност (без ДДС) (Български лев) (Средно претеглена себестойност без ДДС към датата)*
			* **avg_delivery_price_sum** - *Сума себест (без ДДС) (Обща сума по себестойност без ДДС за наличното количество)*
			* **avg_delivery_price_sum__sec_curr** - *Сума себест (без ДДС) (Български лев) (Обща сума по себестойност без ДДС за наличното количество)* **По подразбиране:** ["article_id","article_name","barcode","master_cat_id","stream_name","store_amount_2","store_amount_1","store_amount_3","amount","avg_delivery_price","avg_delivery_price_sum"]
   * - **$values**
     - *bool*
     - Масив от стойности на обекта (при запис)
   * - **$search**
     - *string*
     - 
   * - **$params**
     - *bool*
     - 
   * - **$extra_elements**
     - *bool*
     - 
   * - **$image_col_size**
     - *string*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ReportsStoreAmountsByDateAndBarsysResultData_                          
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsStoreAmountsByDateAndBarsysFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreAmountsByDateAndBarsysFilters

   * - Параметър
     - Тип
     - Описание
   * - **$from_date**
     - *string*
     - *Дата, към която се изчисляват наличностите* **По подразбиране:** '2026-07-01 00:00'
   * - **$depot_group_id**
     - *string*
     - *Филтриране по група складове* ( виж: :doc:`../depots/getgrouplist` )
   * - **$article_name**
     - *string*
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../articles/search` )
   * - **$cat_id**
     - *string*
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../categories/gettree` )
   * - **$supplier**
     - *string*
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../suppliers/getlist` )
   * - **$stream_id**
     - *string*
     - Филтриране по `поток </barsy.help/210-dictionary/flow.html>`__

			* **4** - *Remote*
			* **2** - Втори `поток </barsy.help/210-dictionary/flow.html>`__
			* **1** - *Основен*
			* **3** - трети `поток </barsy.help/210-dictionary/flow.html>`__
   * - **$composite**
     - *string*
     - Филтриране по тип `артикул </barsy.help/210-dictionary/article.html>`__ (рецепта)

			* **0** - *Няма*
			* **1** - Има (при `продажба </barsy.help/210-dictionary/sale.html>`__)
			* **-1** - Има (при `производство </barsy.help/210-dictionary/storeproduction.html>`__)
   * - **$delete_flag**
     - *string*
     - Изключва изтритите `артикули </barsy.help/210-dictionary/article.html>`__
   * - **$delete_flag_b**
     - *string*
     - Изключва изтритите `търговски обекти </barsy.help/210-dictionary/barsy.html>`__
   * - **$amount**
     - *string*
     - *Филтриране по наличност*

			* **lt** - *Наличност < 0*
			* **eq** - *Наличност = 0*
			* **gt** - *Наличност > 0*
   * - **$details**
     - *string*
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articledetails/gettree` )

-----

ReportsStoreAmountsByDateAndBarsysResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreAmountsByDateAndBarsysResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - Номер на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$picture**
     - *string*
     - Снимка на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$barcode**
     - *string*
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$master_cat_id**
     - *string*
     - Пълен път на главна `категория </barsy.help/210-dictionary/category.html>`__
   * - **$detail_0**
     - *string*
     - *Алергени234*
   * - **$detail_1**
     - *string*
     - *Главен*
   * - **$detail_2**
     - *string*
     - *Друго*
   * - **$detail_3**
     - *string*
     - *Друго2*
   * - **$detail_4**
     - *string*
     - *Размер*
   * - **$actual_price**
     - *string*
     - Продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ към избраната дата
   * - **$actual_price__sec_curr**
     - *string*
     - Продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__ към избраната дата
   * - **$amount_unit**
     - *string*
     - Количество, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при единична `продажба </barsy.help/210-dictionary/sale.html>`__ **По подразбиране:** 1.000000000
   * - **$ref_num**
     - *string*
     - Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$stream_name**
     - *string*
     - `Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$store_amount_2**
     - *string*
     - Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$store_amount_1**
     - *string*
     - Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$store_amount_3**
     - *string*
     - Наличност по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$amount**
     - *string*
     - *Общо налично количество към избраната дата*
   * - **$avg_delivery_price**
     - *string*
     - *Средно претеглена себестойност без ДДС към датата*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - *Средно претеглена себестойност без ДДС към датата*
   * - **$avg_delivery_price_sum**
     - *string*
     - *Обща сума по себестойност без ДДС за наличното количество*
   * - **$avg_delivery_price_sum__sec_curr**
     - *string*
     - *Обща сума по себестойност без ДДС за наличното количество*

-----

ReportsStoreAmountsByDateAndBarsysResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreAmountsByDateAndBarsysResultData

   * - Параметър
     - Тип
     - Описание
   * - **$page_num**
     - *int*
     - Номер на текуща страница
   * - **$total**
     - *int*
     - Общ брой страници
   * - **$records**
     - *int*
     - Общ брой записи
   * - **$rows**
     - ReportsStoreAmountsByDateAndBarsysResultRowData_ []
     - Полета на всеки ред от списъка
   * - **$totals**
     - 
     - 
   * - **$filters_resume**
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

     .. literalinclude:: ../../sources/reports_store_amounts_by_date_and_barsys/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_store_amounts_by_date_and_barsys/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_store_amounts_by_date_and_barsys/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_store_amounts_by_date_and_barsys/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_store_amounts_by_date_and_barsys/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_store_amounts_by_date_and_barsys/barsy_api_client_simple.php
     .. code-block:: bash


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

