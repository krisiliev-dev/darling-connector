.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_sales_by_tax_groups
===========================================================
Продажби по ДДС групи

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/112_by_Sales/index </barsy.help/110-admin/170-reports/112_by_Sales/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Агрегирана справка за реализирани `продажби </barsy.help/210-dictionary/sale.html>`__, групирана по ДДС група (например 20% стандартна, 9% намалена, 0% освободени). За всяка ДДС група връща обща нетна сума, ДДС сума, брутна сума, брой поръчки. Основен инструмент за месечно/тримесечно ДДС отчитане и подготовка на справки-декларации към НАП.

Типични случаи: месечно изчисляване на дължимо ДДС, експорт за счетоводна справка по ставки, контрол на коректност на ДДС класификацията на `артикулите </barsy.help/210-dictionary/article.html>`__, подготовка на справка-декларация.

**Име**: Reports_sales_by_tax_groups
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

			`Продажби </barsy.help/210-dictionary/sale.html>`__ по ДДС групи
   * - **$filters**
     - ReportsSalesByTaxGroupsFilters_ 
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

			* **tax_id** - *ID*
			* **tax_name** - *ДДС група*
			* **tax** - *ДДС*
			* **amount** - *Продадено количество*
			* **store_amount** - *Складови бройки*
			* **discounts** - *Отстъпки сума*
			* **discounts__sec_curr** - *Отстъпки сума (Български лев)*
			* **total** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума
			* **total__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
			* **total_no_dds** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС
			* **total_no_dds__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС (Български лев)
			* **dds_total** - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума
			* **dds_total__sec_curr** - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
			* **delivery_total** - *Сума себест (без ДДС)*
			* **delivery_total__sec_curr** - *Сума себест (без ДДС) (Български лев)*
			* **comision** - *Комисионни сума*
			* **comision__sec_curr** - *Комисионни сума (Български лев)*
			* **grand_total_dds_exc** - Печалба (Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС)
			* **grand_total_dds_exc__sec_curr** - Печалба (Български лев) (Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС)
			* **actual_price_base** - Базова цена (Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
			* **actual_price_base__sec_curr** - Базова цена (Български лев) (Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
			* **total_actual_price_base** - *Сума баз. цена (Сума по базова цена с извадени отстъпки)*
			* **total_actual_price_base__sec_curr** - *Сума баз. цена (Български лев) (Сума по базова цена с извадени отстъпки)*
			* **current_pricelist_id** - `Ценови правила </barsy.help/210-dictionary/pricelist.html>`__ (Списък от `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, въздействали на продажната цена)
			* **base_discount** - *Базова отстъпка (Процентно отношение между базовата продажна цена и реалната такава)*
			* **total_discount** - *Пълна отстъпка*
			* **total_discount__sec_curr** - *Пълна отстъпка (Български лев)*
			* **client_id**
			* **article_id** **По подразбиране:** ["tax_id","tax_name","amount","discounts","total","total_no_dds","dds_total","delivery_total","comision","grand_total_dds_exc","actual_price_base","total_actual_price_base","base_discount","total_discount"]
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
ReportsSalesByTaxGroupsResultData_                                     
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsSalesByTaxGroupsFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByTaxGroupsFilters

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
   * - **$fx**
     - *string*
     - Вид `плащане </barsy.help/210-dictionary/payment.html>`__

			* **0** - *Нефискални*
			* **1** - *Фискални*
   * - **$account_alias**
     - *string*
     - Търсене по заглавие на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$served_by**
     - *string*
     - *Филтриране по обслужил* ( виж: :doc:`../users/getlist` )

-----

ReportsSalesByTaxGroupsResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByTaxGroupsResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$tax_id**
     - *int*
     - *ID*
   * - **$tax_name**
     - *string*
     - *ДДС група*
   * - **$tax**
     - *string*
     - *ДДС*
   * - **$amount**
     - *string*
     - *Продадено количество*
   * - **$store_amount**
     - *string*
     - *Складови бройки*
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
   * - **$total_no_dds**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС
   * - **$total_no_dds__sec_curr**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ сума без ДДС (Български лев)
   * - **$dds_total**
     - *string*
     - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума
   * - **$dds_total__sec_curr**
     - *string*
     - ДДС `продажби </barsy.help/210-dictionary/sale.html>`__ сума (Български лев)
   * - **$delivery_total**
     - *string*
     - *Сума себест (без ДДС)*
   * - **$delivery_total__sec_curr**
     - *string*
     - *Сума себест (без ДДС) (Български лев)*
   * - **$comision**
     - *string*
     - *Комисионни сума*
   * - **$comision__sec_curr**
     - *string*
     - *Комисионни сума (Български лев)*
   * - **$grand_total_dds_exc**
     - *string*
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$grand_total_dds_exc__sec_curr**
     - *string*
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
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
   * - **$current_pricelist_id**
     - *string*
     - Списък от `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, въздействали на продажната цена
   * - **$base_discount**
     - *int*
     - *Процентно отношение между базовата продажна цена и реалната такава*
   * - **$total_discount**
     - *string*
     - *Пълна отстъпка*
   * - **$total_discount__sec_curr**
     - *string*
     - *Пълна отстъпка (Български лев)*
   * - **$client_id**
     - *string*
     - 
   * - **$article_id**
     - *string*
     - 

-----

ReportsSalesByTaxGroupsResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByTaxGroupsResultData

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
     - ReportsSalesByTaxGroupsResultRowData_ []
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

     .. literalinclude:: ../../sources/reports_sales_by_tax_groups/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_sales_by_tax_groups/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_sales_by_tax_groups/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_sales_by_tax_groups/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_sales_by_tax_groups/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_sales_by_tax_groups/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Продажба </barsy.help/210-dictionary/sale.html>`__


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

