.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_sales_by_orders
===========================================================
Продажби по поръчки

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/112_by_Sales/index </barsy.help/110-admin/170-reports/112_by_Sales/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Агрегирана справка за реализирани `продажби </barsy.help/210-dictionary/sale.html>`__, групирана по поръчки (`сметки </barsy.help/210-dictionary/account.html>`__) за избран период. За всяка поръчка връща обща сума, ДДС, отстъпки, краен платена сума, метод на `плащане </barsy.help/210-dictionary/payment.html>`__, обслужващ `потребител </barsy.help/210-dictionary/user.html>`__, продължителност на обслужването. Поддържа богат набор от филтри: период, `каса </barsy.help/210-dictionary/pos.html>`__, `потребител </barsy.help/210-dictionary/user.html>`__, `клиент </barsy.help/210-dictionary/client.html>`__, `артикул </barsy.help/210-dictionary/article.html>`__, ДДС група, статус (платена/неплатена/частично платена).

*Типични случаи: дневен оборот на касиер за смяна, седмичен/месечен мениджърски отчет, експорт за счетоводна отчетност, анализ на средна стойност на поръчка.*

**Име**: Reports_sales_by_orders
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
     - ReportsSalesByOrdersFilters_ 
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

			* **order_id** - *ID*
			* **date** - *Дата*
			* **ref_date** - *Вальор*
			* **barsy** - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **user_name** - `Потребител </barsy.help/210-dictionary/user.html>`__
			* **salon_name** - *Салон*
			* **place_name** - *Място*
			* **stream_name** - `Поток </barsy.help/210-dictionary/flow.html>`__ (`Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **client_name** - `Клиент </barsy.help/210-dictionary/client.html>`__
			* **client_email** - *Имейл*
			* **article_name** - `Артикул </barsy.help/210-dictionary/article.html>`__
			* **barcode** - Баркод (Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **export_id** - *Експортен идентификатор (Идентификатор за експорт към външни системи)*
			* **ref_num** - Референтен номер (Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **cat_name** - `Категория </barsy.help/210-dictionary/category.html>`__
			* **cat_path** - `Категория </barsy.help/210-dictionary/category.html>`__ път
			* **current_price** - *Ед. цена*
			* **current_price__sec_curr** - *Ед. цена (Български лев)*
			* **amount** - *Количество*
			* **discounts** - *Отстъпки сума*
			* **discounts__sec_curr** - *Отстъпки сума (Български лев)*
			* **total** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума
			* **total__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
			* **delivery_total** - *Себестойност сума (без ДДС)*
			* **delivery_total__sec_curr** - *Себестойност сума (без ДДС) (Български лев)*
			* **delivery_total_dds** - *Себестойност сума (+ДДС) (Себестойност с ДДС)*
			* **delivery_total_dds__sec_curr** - *Себестойност сума (+ДДС) (Български лев) (Себестойност с ДДС)*
			* **comision** - *Комисионни сума*
			* **comision__sec_curr** - *Комисионни сума (Български лев)*
			* **grand_total** - *Печалба (Печалба при себестойност без ДДС)*
			* **grand_total__sec_curr** - *Печалба (Български лев) (Печалба при себестойност без ДДС)*
			* **actual_price_base** - Базова цена (Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
			* **actual_price_base__sec_curr** - Базова цена (Български лев) (Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
			* **total_actual_price_base** - *Сума баз. цена (Сума по базова цена с извадени отстъпки)*
			* **total_actual_price_base__sec_curr** - *Сума баз. цена (Български лев) (Сума по базова цена с извадени отстъпки)*
			* **base_discount** - *Базова отстъпка (Процентно отношение между базовата продажна цена и реалната такава)*
			* **paymethod_name** - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__
			* **account_id** - `Сметка </barsy.help/210-dictionary/account.html>`__ №
			* **account_close_date** - *Закрита*
			* **inv_num** - Номера на `фактури </barsy.help/210-dictionary/invoice.html>`__ **По подразбиране:** ["order_id","date","ref_date","barsy","user_name","client_name","article_name","current_price","amount","discounts","total","delivery_total","delivery_total_dds","comision","grand_total","actual_price_base","total_actual_price_base","base_discount","paymethod_name","account_id","account_close_date"]
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
ReportsSalesByOrdersResultData_                                        Обект с данни за резултатите
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsSalesByOrdersFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByOrdersFilters

   * - Параметър
     - Тип
     - Описание
   * - **$ref_date**
     - *string*
     - *Филтриране на редовете за избран период* **По подразбиране:** ["2026-07-01"]
   * - **$barsys**
     - *string*
     - Филтриране по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$article_name**
     - *string*
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../articles/search` )
   * - **$cat_id**
     - *string*
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../categories/gettree` )
   * - **$stream_id**
     - *string*
     - Филтриране по `поток </barsy.help/210-dictionary/flow.html>`__

			* **4** - *Remote*
			* **2** - Втори `поток </barsy.help/210-dictionary/flow.html>`__
			* **1** - *Основен*
			* **3** - трети `поток </barsy.help/210-dictionary/flow.html>`__
   * - **$pos_id**
     - *string*
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$client**
     - *string*
     - Търсене по `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getlistsmart` )
   * - **$person**
     - *string*
     - Филтриране по `представител </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../persons/getlist` )
   * - **$client_group_id**
     - *string*
     - *Филтриране по клиентска група* ( виж: :doc:`../clients/getgroups` )
   * - **$user_id**
     - *string*
     - Филтриране по `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$role_id**
     - *string*
     - Филтриране по `роля </barsy.help/210-dictionary/role.html>`__ ( виж: :doc:`../roles/getlist` )
   * - **$paymethod_id**
     - *string*
     - Филтриране по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **-5** - *Смесено*
			* **1** - *В брой*
			* **2** - *Карта*
   * - **$tax_id**
     - *string*
     - *Филтриране по ДДС група*

			* **2** - *20% (Б)*
			* **1** - *0% (А)*
			* **3** - *20% (В)*
			* **4** - *9% (Г)*
			* **12** - *7%*
			* **100** - *0% (Без ДДС)*
   * - **$status**
     - *string*
     - `Сметки </barsy.help/210-dictionary/account.html>`__

			* **0** - *Отворени*
			* **1** - *Затворени* **По подразбиране:** 1
   * - **$cprice_less_cprice**
     - *string*
     - *Продажна цена < от себестойност (+ДДС)*
   * - **$card_num**
     - *string*
     - *Карта №*
   * - **$details**
     - *string*
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articledetails/gettree` )
   * - **$account_alias**
     - *string*
     - Търсене по заглавие на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$order_parent_id**
     - *string*
     - *Комбо Меню*

			* **1** - *участва в комбо меню*
			* **2** - *е комбо меню*
			* **3** - *не участва в комбо меню*

-----

ReportsSalesByOrdersResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByOrdersResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$order_id**
     - *int*
     - *ID*
   * - **$date**
     - *string*
     - *Дата*
   * - **$ref_date**
     - *string*
     - *Вальор*
   * - **$barsy**
     - *string*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$user_name**
     - *string*
     - `Потребител </barsy.help/210-dictionary/user.html>`__
   * - **$salon_name**
     - *string*
     - *Салон*
   * - **$place_name**
     - *string*
     - *Място*
   * - **$stream_name**
     - *string*
     - `Поток </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$client_name**
     - *string*
     - `Клиент </barsy.help/210-dictionary/client.html>`__
   * - **$client_email**
     - *string*
     - *Имейл*
   * - **$article_name**
     - *string*
     - `Артикул </barsy.help/210-dictionary/article.html>`__
   * - **$barcode**
     - *string*
     - Баркодове на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$export_id**
     - *string*
     - *Идентификатор за експорт към външни системи*
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
   * - **$ref_num**
     - *string*
     - Референтен номер на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$cat_name**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__
   * - **$cat_path**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__ път
   * - **$current_price**
     - *string*
     - *Ед. цена*
   * - **$current_price__sec_curr**
     - *string*
     - *Ед. цена (Български лев)*
   * - **$amount**
     - *string*
     - *Количество*
   * - **$discounts**
     - *string*
     - *Отстъпки сума*
   * - **$discounts__sec_curr**
     - *string*
     - *Отстъпки сума (Български лев)*
   * - **$total**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума
   * - **$total__sec_curr**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
   * - **$delivery_total**
     - *string*
     - *Себестойност сума (без ДДС)*
   * - **$delivery_total__sec_curr**
     - *string*
     - *Себестойност сума (без ДДС) (Български лев)*
   * - **$delivery_total_dds**
     - *string*
     - *Себестойност с ДДС*
   * - **$delivery_total_dds__sec_curr**
     - *string*
     - *Себестойност с ДДС*
   * - **$comision**
     - *string*
     - *Комисионни сума*
   * - **$comision__sec_curr**
     - *string*
     - *Комисионни сума (Български лев)*
   * - **$grand_total**
     - *string*
     - *Печалба при себестойност без ДДС*
   * - **$grand_total__sec_curr**
     - *string*
     - *Печалба при себестойност без ДДС*
   * - **$actual_price_base**
     - *string*
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$actual_price_base__sec_curr**
     - *string*
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__
   * - **$total_actual_price_base**
     - *string*
     - *Сума по базова цена с извадени отстъпки*
   * - **$total_actual_price_base__sec_curr**
     - *string*
     - *Сума по базова цена с извадени отстъпки*
   * - **$base_discount**
     - *int*
     - *Процентно отношение между базовата продажна цена и реалната такава*
   * - **$paymethod_name**
     - *string*
     - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$account_id**
     - *int*
     - `Сметка </barsy.help/210-dictionary/account.html>`__ №
   * - **$account_close_date**
     - *string*
     - *Закрита*
   * - **$inv_num**
     - *string*
     - Номера на `фактури </barsy.help/210-dictionary/invoice.html>`__

-----

ReportsSalesByOrdersResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByOrdersResultData

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
     - ReportsSalesByOrdersResultRowData_ []
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

     .. literalinclude:: ../../sources/reports_sales_by_orders/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_sales_by_orders/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_sales_by_orders/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_sales_by_orders/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_sales_by_orders/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_sales_by_orders/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Продажба </barsy.help/210-dictionary/sale.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

