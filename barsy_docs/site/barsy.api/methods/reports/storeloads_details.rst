.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_storeloads_details
===========================================================
Подробни складови зареждания

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/114_Warehouse/index </barsy.help/110-admin/170-reports/114_Warehouse/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подробна справка за всички складови зареждания за период с раздропируване по редове — за всеки `артикул </barsy.help/210-dictionary/article.html>`__ в всяко `зареждане </barsy.help/210-dictionary/storeload.html>`__ се връща `доставчик </barsy.help/210-dictionary/supplier.html>`__, `склад </barsy.help/210-dictionary/store.html>`__, дата, количество, единична доставна цена, ДДС, документ-основание, тип на документа. Поддържа богат набор от филтри (период, `доставчик </barsy.help/210-dictionary/supplier.html>`__, обект, `склад </barsy.help/210-dictionary/store.html>`__, `артикул </barsy.help/210-dictionary/article.html>`__, тип документ, статус).

Типични случаи: детайлен експорт за счетоводно осчетоводяване на доставки, одит на доставни цени за период, `ревизия </barsy.help/210-dictionary/revision.html>`__ преди тримесечно отчитане, анализ на цените на `доставчиците </barsy.help/210-dictionary/supplier.html>`__.

**Име**: Reports_storeloads_details
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

			*Списък на доставките*
   * - **$filters**
     - ReportsStoreloadsDetailsFilters_ 
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

			* **store_load_id** - *ID*
			* **article_name** - Име на `артикул </barsy.help/210-dictionary/article.html>`__ (Име на `артикул </barsy.help/210-dictionary/article.html>`__)
			* **cat_name** - `Категория </barsy.help/210-dictionary/category.html>`__ (главна) (Име на главна `категория </barsy.help/210-dictionary/category.html>`__)
			* **cat_path** - `Категория </barsy.help/210-dictionary/category.html>`__ път(главна) (Пълен път на главна `категория </barsy.help/210-dictionary/category.html>`__)
			* **cat_names** - `Категории </barsy.help/210-dictionary/category.html>`__ (Имена на `категории </barsy.help/210-dictionary/category.html>`__)
			* **cat_paths** - `Категории </barsy.help/210-dictionary/category.html>`__ пътища (Пътища на `категории </barsy.help/210-dictionary/category.html>`__)
			* **barsy_name** - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__ (`Търговски обект </barsy.help/210-dictionary/barsy.html>`__ на доставката)
			* **date** - Дата (Дата на `зареждане </barsy.help/210-dictionary/storeload.html>`__)
			* **doc_num** - *Док. номер (Номер на документ-основание)*
			* **barcode** - Баркод (Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **doc_date** - *Док. дата (Дата на документ-основание)*
			* **doc_type_name** - *Тип документ (Тип на документа-основание)*
			* **store_load_cat** - `Категория </barsy.help/210-dictionary/category.html>`__ `зареждане </barsy.help/210-dictionary/storeload.html>`__ (`Категория </barsy.help/210-dictionary/category.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__)
			* **supplier_name** - `Доставчик </barsy.help/210-dictionary/supplier.html>`__ (`Доставчик </barsy.help/210-dictionary/supplier.html>`__ по `зареждането </barsy.help/210-dictionary/storeload.html>`__)
			* **bulstat** - ЕИК (ЕИК на `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **vat_num** - ДДС Номер (ДДС номер на `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **group_name** - Група (Група `доставчик </barsy.help/210-dictionary/supplier.html>`__)
			* **user_name** - `Потребител </barsy.help/210-dictionary/user.html>`__ (`Потребител </barsy.help/210-dictionary/user.html>`__, въвел `зареждането </barsy.help/210-dictionary/storeload.html>`__)
			* **amount** - *Количество (Заредено количество)*
			* **current_price** - *Доставна цена без ДДС (Доставна цена без ДДС)*
			* **current_price__sec_curr** - *Доставна цена без ДДС (Български лев) (Доставна цена без ДДС)*
			* **current_price_total** - *Общо без ДДС (Доставната цена без ДДС умножена по количеството)*
			* **current_price_total__sec_curr** - *Общо без ДДС (Български лев) (Доставната цена без ДДС умножена по количеството)*
			* **current_price_tax** - *Доставна цена с ДДС (Доставна цена с ДДС)*
			* **current_price_tax__sec_curr** - *Доставна цена с ДДС (Български лев) (Доставна цена с ДДС)*
			* **current_price_tax_total** - *Общо с ДДС (Доставната цена с ДДС умножена по количеството)*
			* **current_price_tax_total__sec_curr** - *Общо с ДДС (Български лев) (Доставната цена с ДДС умножена по количеството)*
			* **operation_type** - *Операция (Тип складова операция)*
			* **article_id** - ID на `артикул </barsy.help/210-dictionary/article.html>`__
			* **supplier_id** - ID на `доставчик </barsy.help/210-dictionary/supplier.html>`__
			* **ref_num** - Референтен номер (Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **export_id** - *export_id (Идентификатор за експорт към външни системи)*
			* **notes** - Бележки `артикул </barsy.help/210-dictionary/article.html>`__ (Бележки към реда на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **description** - Бележки `зареждане </barsy.help/210-dictionary/storeload.html>`__ (Бележки към `зареждането </barsy.help/210-dictionary/storeload.html>`__)
			* **lot_value** - *Партида (Номер/стойност на партида)*
			* **lot_exp_date** - *Годно до (Срок на годност на партидата)*
			* **discount_row** - Отстъпка за `артикул </barsy.help/210-dictionary/article.html>`__ (Отстъпка на ниво `артикул </barsy.help/210-dictionary/article.html>`__)
			* **discount_store_load** - Отстъпка за `зареждане </barsy.help/210-dictionary/storeload.html>`__ (Отстъпка на ниво `зареждане </barsy.help/210-dictionary/storeload.html>`__)
			* **discount_sum** - *Отстъпка (обща сума) (Обща сума на отстъпката)*
			* **discount_sum__sec_curr** - *Отстъпка (обща сума) (Български лев) (Обща сума на отстъпката)* **По подразбиране:** ["store_load_id","article_name","barsy_name","date","doc_date","supplier_name","bulstat","vat_num","user_name","amount","current_price","current_price_tax"]
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
ReportsStoreloadsDetailsResultData_                                    
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsStoreloadsDetailsFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreloadsDetailsFilters

   * - Параметър
     - Тип
     - Описание
   * - **$ref_date**
     - *string*
     - Период на `зареждане </barsy.help/210-dictionary/storeload.html>`__ **По подразбиране:** ["2026-07-01"]
   * - **$article_name**
     - *string*
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../articles/search` )
   * - **$cat_id**
     - *string*
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../categories/gettree` )
   * - **$barsys_depots**
     - *string*
     - `Търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове
   * - **$doc_type_id**
     - *string*
     - *Филтриране по тип документ*

			* **1** - `Фактура </barsy.help/210-dictionary/invoice.html>`__
			* **11** - `Фактура </barsy.help/210-dictionary/invoice.html>`__ ЧВ
			* **2** - *Стокова р/ка*
			* **5** - *Дебитно известие*
			* **4** - *Кредитно известие*
			* **6** - *Митническа декларация*
			* **3** - *Друго*
			* **-1** - *Неизвестен*
   * - **$status**
     - *string*
     - Статус на `зареждането </barsy.help/210-dictionary/storeload.html>`__ (отворено/затворено)

			* **0** - *Отворени*
			* **1** - *Затворени* **По подразбиране:** 1
   * - **$supplier_name**
     - *string*
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../suppliers/getlist` )
   * - **$supplier_group**
     - *string*
     - Филтриране по група `доставчици </barsy.help/210-dictionary/supplier.html>`__

			* **1** - *Основна*
   * - **$user_name**
     - *string*
     - Филтриране по `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$operation_type**
     - *string*
     - *Филтриране по тип операция*

			* **1** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__ на стока
			* **2** - *Връщане на стока*
   * - **$details**
     - *string*
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articledetails/gettree` )
   * - **$store_load_cat**
     - *string*
     - Филтриране по `категория </barsy.help/210-dictionary/category.html>`__ `зареждане </barsy.help/210-dictionary/storeload.html>`__

			* **1** - *Обща*
			* **2** - *Зумба*
   * - **$paymethod_id**
     - *string*
     - Филтриране по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **1** - *В брой*
			* **2** - *Карта*

-----

ReportsStoreloadsDetailsResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreloadsDetailsResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$store_load_id**
     - *int*
     - *ID*
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$cat_name**
     - *string*
     - Име на главна `категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_path**
     - *string*
     - Пълен път на главна `категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_names**
     - *string*
     - Имена на `категории </barsy.help/210-dictionary/category.html>`__
   * - **$cat_paths**
     - *string*
     - Пътища на `категории </barsy.help/210-dictionary/category.html>`__
   * - **$barsy_name**
     - *string*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__ на доставката
   * - **$date**
     - *string*
     - Дата на `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$doc_num**
     - *string*
     - *Номер на документ-основание*
   * - **$barcode**
     - *string*
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$doc_date**
     - *string*
     - *Дата на документ-основание*
   * - **$doc_type_name**
     - *string*
     - *Тип на документа-основание*
   * - **$store_load_cat**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$supplier_name**
     - *string*
     - `Доставчик </barsy.help/210-dictionary/supplier.html>`__ по `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$bulstat**
     - *string*
     - ЕИК на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$vat_num**
     - *string*
     - ДДС номер на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$group_name**
     - *string*
     - Група `доставчик </barsy.help/210-dictionary/supplier.html>`__
   * - **$user_name**
     - *string*
     - `Потребител </barsy.help/210-dictionary/user.html>`__, въвел `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$amount**
     - *string*
     - *Заредено количество*
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
   * - **$current_price**
     - *string*
     - *Доставна цена без ДДС*
   * - **$current_price__sec_curr**
     - *string*
     - *Доставна цена без ДДС*
   * - **$current_price_total**
     - *string*
     - *Доставната цена без ДДС умножена по количеството*
   * - **$current_price_total__sec_curr**
     - *string*
     - *Доставната цена без ДДС умножена по количеството*
   * - **$current_price_tax**
     - *string*
     - *Доставна цена с ДДС*
   * - **$current_price_tax__sec_curr**
     - *string*
     - *Доставна цена с ДДС*
   * - **$current_price_tax_total**
     - *string*
     - *Доставната цена с ДДС умножена по количеството*
   * - **$current_price_tax_total__sec_curr**
     - *string*
     - *Доставната цена с ДДС умножена по количеството*
   * - **$operation_type**
     - *string*
     - *Тип складова операция*
   * - **$article_id**
     - *string*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$supplier_id**
     - *string*
     - ID на `доставчик </barsy.help/210-dictionary/supplier.html>`__
   * - **$ref_num**
     - *string*
     - Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$export_id**
     - *string*
     - *Идентификатор за експорт към външни системи*
   * - **$notes**
     - *string*
     - Бележки към реда на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$description**
     - *string*
     - Бележки към `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$lot_value**
     - *string*
     - *Номер/стойност на партида*
   * - **$lot_exp_date**
     - *string*
     - *Срок на годност на партидата*
   * - **$discount_row**
     - *string*
     - Отстъпка на ниво `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$discount_store_load**
     - *string*
     - Отстъпка на ниво `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$discount_sum**
     - *string*
     - *Обща сума на отстъпката*
   * - **$discount_sum__sec_curr**
     - *string*
     - *Обща сума на отстъпката*

-----

ReportsStoreloadsDetailsResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsStoreloadsDetailsResultData

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
     - ReportsStoreloadsDetailsResultRowData_ []
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

     .. literalinclude:: ../../sources/reports_storeloads_details/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_storeloads_details/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_storeloads_details/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_storeloads_details/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_storeloads_details/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_storeloads_details/barsy_api_client_simple.php
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

