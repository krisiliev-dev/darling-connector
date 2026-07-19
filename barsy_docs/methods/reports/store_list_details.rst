.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_store_list_details
===========================================================
Подробни складови движения

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/114_Warehouse/index </barsy.help/110-admin/170-reports/114_Warehouse/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подробна справка за всички складови движения (зареждания, отписвания, прехвърляния, `ревизии </barsy.help/210-dictionary/revision.html>`__, `производства </barsy.help/210-dictionary/storeproduction.html>`__) за период, представени като плосък хронологичен списък. За всяко движение: дата, `склад </barsy.help/210-dictionary/store.html>`__, `артикул </barsy.help/210-dictionary/article.html>`__, количество, операция (приход/разход), причина, документ-основание, `потребител </barsy.help/210-dictionary/user.html>`__. Удобно за проследяване на пълната история на запас по конкретен `артикул </barsy.help/210-dictionary/article.html>`__ или `склад </barsy.help/210-dictionary/store.html>`__.

Типични случаи: одит на складовите наличности, разследване на отклонения при инвентаризация, проследяване на специфичен `артикул </barsy.help/210-dictionary/article.html>`__, експорт за счетоводно осчетоводяване.

**Име**: Reports_store_list_details
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
   * - **$filters**
     - ReportsStoreListDetailsFilters_ 
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
			* **desc** - *низходящо* **По подразбиране:** 'asc'
   * - **$columns**
     - *array* | *object*
     - Списък от колоните, които да бъдат включени в отговора (ако е празен, показва избрани по подразбиране)

			* **store_id** - *ID (Идентификатор на движението)*
			* **article_id** - ID на `артикул </barsy.help/210-dictionary/article.html>`__ (Идентификатор на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **date** - *Дата (Дата на операцията)*
			* **ref_date** - *Вальор (Вальор на операцията)*
			* **article_name** - Име на `артикул </barsy.help/210-dictionary/article.html>`__ (Име на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **user_name** - `Потребител </barsy.help/210-dictionary/user.html>`__ (`Потребител </barsy.help/210-dictionary/user.html>`__, извършил операцията)
			* **depot_name** - `Склад </barsy.help/210-dictionary/store.html>`__ (`Търговски обект </barsy.help/210-dictionary/barsy.html>`__ и `склад </barsy.help/210-dictionary/store.html>`__)
			* **reason_name** - *Операция (Вид складова операция)*
			* **amount** - *Количество (Количество по операцията)*
			* **amount_sum** - *Кол. след опер. (Количество след извършване на операцията. Показва се само ако е възможно)*
			* **avg_delivery_price** - *Себестойност (без ДДС) (Средно претеглена доставна цена без ДДС)*
			* **avg_delivery_price__sec_curr** - *Себестойност (без ДДС) (Български лев) (Средно претеглена доставна цена без ДДС)*
			* **avg_delivery_price_sum** - *Сума себест (без ДДС) (Сума по себестойност без ДДС)*
			* **avg_delivery_price_sum__sec_curr** - *Сума себест (без ДДС) (Български лев) (Сума по себестойност без ДДС)*
			* **avg_delivery_price_plus_vat_sum** - *Сума себест (+ДДС) (Сума по себестойност с ДДС)*
			* **avg_delivery_price_plus_vat_sum__sec_curr** - *Сума себест (+ДДС) (Български лев) (Сума по себестойност с ДДС)*
			* **ref_id** - *Ref ID (Референтен номер на операцията)* **По подразбиране:** ["store_id","date","ref_date","article_name","user_name","depot_name","reason_name","amount","amount_sum"]
   * - **$search**
     - *string*
     - 
   * - **$params**
     - *mixed*
     - 
   * - **$active_struct_id**
     - *string*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ReportsStoreListDetailsResultData_                                     Обект с данни за резултатите
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsStoreListDetailsFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreListDetailsFilters

   * - Параметър
     - Тип
     - Описание
   * - **$ref_date**
     - *string*
     - *Период на движенията* **По подразбиране:** ["2026-07-01"]
   * - **$article**
     - *string*
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../articles/search` )
   * - **$cat_id**
     - *string*
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../categories/gettree` )
   * - **$role_id**
     - *string*
     - Филтриране по `роля </barsy.help/210-dictionary/role.html>`__ ( виж: :doc:`../roles/getlist` )
   * - **$barsys_depots**
     - *string*
     - `Търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове
   * - **$user_id**
     - *string*
     - Филтриране по `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$reason_id**
     - *string*
     - *Филтриране по причина за операцията*

			* **-21** - Авансово `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-15** - *Архивиране*
			* **-4** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__
			* **-11** - `Изписване </barsy.help/210-dictionary/storeout.html>`__
			* **-6** - *Използване на карта*
			* **-5** - *Изтегляне по рецепта*
			* **-20** - *Изтегляне по рецепта - отказ*
			* **-7** - Корекция `зареждане </barsy.help/210-dictionary/storeload.html>`__
			* **-9** - *Корекция рецепта*
			* **-2** - *Местене*
			* **-19** - *Поръчка - отказ*
			* **-1** - Поръчка в `сметка </barsy.help/210-dictionary/account.html>`__
			* **-8** - `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__
			* **-10** - `Производство </barsy.help/210-dictionary/storeproduction.html>`__
			* **-14** - `Производство </barsy.help/210-dictionary/storeproduction.html>`__ по рецепта
			* **-3** - *Ревизионна корекция*
			* **-22** - *Ревизионна корекция - отказ*
			* **-16** - Сливане на `сметки </barsy.help/210-dictionary/account.html>`__
			* **-12** - *Сторно*
			* **-17** - Сторно `зареждане </barsy.help/210-dictionary/storeload.html>`__
			* **-18** - Сторно `зареждане </barsy.help/210-dictionary/storeload.html>`__ корекция
   * - **$ref_id**
     - *string*
     - *Филтриране по номер на операция*

-----

ReportsStoreListDetailsResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreListDetailsResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$store_id**
     - *int*
     - *Идентификатор на движението*
   * - **$article_id**
     - *string*
     - Идентификатор на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$date**
     - *string*
     - *Дата на операцията*
   * - **$ref_date**
     - *string*
     - *Вальор на операцията*
   * - **$article_name**
     - *string*
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$user_name**
     - *string*
     - `Потребител </barsy.help/210-dictionary/user.html>`__, извършил операцията
   * - **$depot_name**
     - *string*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__ и `склад </barsy.help/210-dictionary/store.html>`__
   * - **$reason_name**
     - *string*
     - *Вид складова операция*
   * - **$amount**
     - *string*
     - *Количество по операцията*
   * - **$amount_sum**
     - *string*
     - *Количество след извършване на операцията. Показва се само ако е възможно*
   * - **$avg_delivery_price**
     - *string*
     - *Средно претеглена доставна цена без ДДС*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - *Средно претеглена доставна цена без ДДС*
   * - **$avg_delivery_price_sum**
     - *string*
     - *Сума по себестойност без ДДС*
   * - **$avg_delivery_price_sum__sec_curr**
     - *string*
     - *Сума по себестойност без ДДС*
   * - **$avg_delivery_price_plus_vat_sum**
     - *string*
     - *Сума по себестойност с ДДС*
   * - **$avg_delivery_price_plus_vat_sum__sec_curr**
     - *string*
     - *Сума по себестойност с ДДС*
   * - **$ref_id**
     - *string*
     - *Референтен номер на операцията*

-----

ReportsStoreListDetailsResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreListDetailsResultData

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
     - ReportsStoreListDetailsResultRowData_ []
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

     .. literalinclude:: ../../sources/reports_store_list_details/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_store_list_details/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_store_list_details/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_store_list_details/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_store_list_details/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_store_list_details/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

