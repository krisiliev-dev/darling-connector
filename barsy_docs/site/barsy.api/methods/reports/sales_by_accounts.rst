.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_sales_by_accounts
===========================================================
Продажби по сметки

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/112_by_Sales/index </barsy.help/110-admin/170-reports/112_by_Sales/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Справка за реализирани `продажби </barsy.help/210-dictionary/sale.html>`__, групирана по `сметки </barsy.help/210-dictionary/account.html>`__ за избран период. За всяка `сметка </barsy.help/210-dictionary/account.html>`__ връща ключови данни — `клиент </barsy.help/210-dictionary/client.html>`__, обект, обслужващ `потребител </barsy.help/210-dictionary/user.html>`__, дата на отваряне/затваряне, обща сума, ДДС, отстъпки, направени плащания и метод на `плащане </barsy.help/210-dictionary/payment.html>`__. Поддържа богат набор от филтри (период, обект, `клиент </barsy.help/210-dictionary/client.html>`__, `потребител </barsy.help/210-dictionary/user.html>`__, статус, метод на `плащане </barsy.help/210-dictionary/payment.html>`__, диапазон на сума).

Типични случаи: справка за големи `сметки </barsy.help/210-dictionary/account.html>`__ за периода, идентификация на VIP `клиенти </barsy.help/210-dictionary/client.html>`__ по обем, експорт за reconciliation с фискални документи, проследяване на `сметки </barsy.help/210-dictionary/account.html>`__ на конкретен сервитьор.

**Име**: Reports_sales_by_accounts
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
     - ReportsSalesByAccountsFilters_ 
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

			* **account_id** - `Сметка </barsy.help/210-dictionary/account.html>`__
			* **account_alias** - *Заглавие*
			* **create_date** - *Отворена*
			* **close_date** - *Закрита на*
			* **ref_date** - *Документ дата*
			* **barsy** - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **user_name** - `Потребител </barsy.help/210-dictionary/user.html>`__
			* **place_name** - *Място*
			* **persons** - *Хора*
			* **client_name** - `Клиент </barsy.help/210-dictionary/client.html>`__
			* **discount** - *Отстъпка*
			* **cnt** - *Продадени бройки*
			* **store_amount** - *Складови бройки*
			* **oborot** - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот
			* **oborot__sec_curr** - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот (Български лев)
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
			* **delivery_total_dds** - *Сума себест (+ДДС) (Себестойност с ДДС)*
			* **delivery_total_dds__sec_curr** - *Сума себест (+ДДС) (Български лев) (Себестойност с ДДС)*
			* **delivery_price_dds** - Себестойност (+ДДС) (Себестойност с ДДС за единичен `артикул </barsy.help/210-dictionary/article.html>`__)
			* **delivery_price_dds__sec_curr** - Себестойност (+ДДС) (Български лев) (Себестойност с ДДС за единичен `артикул </barsy.help/210-dictionary/article.html>`__)
			* **comision** - *Комисионни*
			* **comision__sec_curr** - *Комисионни (Български лев)*
			* **grand_total** - Печалба (Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС)
			* **grand_total__sec_curr** - Печалба (Български лев) (Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС)
			* **procent** - Надценка (Процент надценка между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС)
			* **total_actual_price_base** - *Сума баз. цена (Сума по базова цена с извадени отстъпки)*
			* **total_actual_price_base__sec_curr** - *Сума баз. цена (Български лев) (Сума по базова цена с извадени отстъпки)*
			* **actual_base_total_diff** - *Разлика € (Разлика в € между реалната продажна цена и базовата такава умножени по количеството)*
			* **actual_base_total_diff__sec_curr** - *Разлика € (Български лев) (Разлика в € между реалната продажна цена и базовата такава умножени по количеството)* **По подразбиране:** ["account_id","create_date","close_date","user_name","place_name","persons","client_name","discount","cnt","oborot","discounts","total","total_no_dds","delivery_total_dds","grand_total"]
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
ReportsSalesByAccountsResultData_                                      Обект с данни за резултатите
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsSalesByAccountsFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByAccountsFilters

   * - Параметър
     - Тип
     - Описание
   * - **$ref_date**
     - *string*
     - *Филтриране на редовете за избран период* **По подразбиране:** ["2026-07-01"]
   * - **$barsys_depots**
     - *string*
     - `Търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове
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
   * - **$role_id**
     - *string*
     - Филтриране по `роля </barsy.help/210-dictionary/role.html>`__ ( виж: :doc:`../roles/getlist` )
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
   * - **$paymethod_id**
     - *string*
     - Филтриране по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **0** - Без `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-5** - *Смесено*
			* **1** - *В брой*
			* **2** - *Карта*
   * - **$article_type**
     - *string*
     - Филтриране по вид `артикул </barsy.help/210-dictionary/article.html>`__

			* **1** - `Продажба </barsy.help/210-dictionary/sale.html>`__ на `артикул </barsy.help/210-dictionary/article.html>`__
			* **2** - `Продажба </barsy.help/210-dictionary/sale.html>`__ на пакетна карта
			* **3** - Авансово `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-1** - *Ползване на пакетна карта*
			* **5** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__ на кл.портфейл
			* **6** - *Бакшиш* **По подразбиране:** [-1,1,2,5,6]
   * - **$supplier_id**
     - *string*
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../suppliers/getlist` )
   * - **$details**
     - *string*
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articledetails/gettree` )
   * - **$account_alias**
     - *string*
     - Търсене по заглавие на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$invoices**
     - *string*
     - Само `сметки </barsy.help/210-dictionary/account.html>`__ без `фактура </barsy.help/210-dictionary/invoice.html>`__

-----

ReportsSalesByAccountsResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByAccountsResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$account_id**
     - *int*
     - `Сметка </barsy.help/210-dictionary/account.html>`__
   * - **$account_alias**
     - *string*
     - *Заглавие*
   * - **$create_date**
     - *string*
     - *Отворена*
   * - **$close_date**
     - *string*
     - *Закрита на*
   * - **$ref_date**
     - *string*
     - *Документ дата*
   * - **$barsy**
     - *string*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$user_name**
     - *string*
     - `Потребител </barsy.help/210-dictionary/user.html>`__
   * - **$place_name**
     - *string*
     - *Място*
   * - **$persons**
     - *string*
     - *Хора*
   * - **$client_name**
     - *string*
     - `Клиент </barsy.help/210-dictionary/client.html>`__
   * - **$discount**
     - *int*
     - *Отстъпка*
   * - **$cnt**
     - *string*
     - *Продадени бройки*
   * - **$store_amount**
     - *string*
     - *Складови бройки*
   * - **$oborot**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот
   * - **$oborot__sec_curr**
     - *string*
     - `Продажби </barsy.help/210-dictionary/sale.html>`__ оборот (Български лев)
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
   * - **$delivery_total_dds**
     - *string*
     - *Себестойност с ДДС*
   * - **$delivery_total_dds__sec_curr**
     - *string*
     - *Себестойност с ДДС*
   * - **$delivery_price_dds**
     - *string*
     - Себестойност с ДДС за единичен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$delivery_price_dds__sec_curr**
     - *string*
     - Себестойност с ДДС за единичен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$comision**
     - *string*
     - *Комисионни*
   * - **$comision__sec_curr**
     - *string*
     - *Комисионни (Български лев)*
   * - **$grand_total**
     - *string*
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$grand_total__sec_curr**
     - *string*
     - Разлика между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$procent**
     - *string*
     - Процент надценка между сума `продажби </barsy.help/210-dictionary/sale.html>`__ без ДДС и себестойност без ДДС
   * - **$total_actual_price_base**
     - *string*
     - *Сума по базова цена с извадени отстъпки*
   * - **$total_actual_price_base__sec_curr**
     - *string*
     - *Сума по базова цена с извадени отстъпки*
   * - **$actual_base_total_diff**
     - *string*
     - *Разлика в € между реалната продажна цена и базовата такава умножени по количеството*
   * - **$actual_base_total_diff__sec_curr**
     - *string*
     - *Разлика в € между реалната продажна цена и базовата такава умножени по количеството*

-----

ReportsSalesByAccountsResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsSalesByAccountsResultData

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
     - ReportsSalesByAccountsResultRowData_ []
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

     .. literalinclude:: ../../sources/reports_sales_by_accounts/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_sales_by_accounts/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_sales_by_accounts/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_sales_by_accounts/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_sales_by_accounts/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_sales_by_accounts/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Продажба </barsy.help/210-dictionary/sale.html>`__
 * `Сметка </barsy.help/210-dictionary/account.html>`__


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

