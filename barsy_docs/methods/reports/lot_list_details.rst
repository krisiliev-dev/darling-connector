.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Reports_lot_list_details
===========================================================
Партидни движения

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/170-reports/114_Warehouse/index </barsy.help/110-admin/170-reports/114_Warehouse/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Детайлна справка за складови движения, разбити по партиди (lots). За всяко движение се проследява конкретната партида (серия, дата на доставка, `доставчик </barsy.help/210-dictionary/supplier.html>`__), което позволява точно FIFO/LIFO проследяване. Незаменима за регулирани сектори (хранителни стоки, медикаменти, алкохол) и за контрол на сроковете на годност.

*Типични случаи: проследяване на партида при отзоваване от пазара, контрол на FIFO коректност, проверка на изпълнение на гаранции по серийни номера, анализ на свежостта на стоковия фонд.*

**Име**: Reports_lot_list_details
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
     - ReportsLotListDetailsFilters_ 
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

			* **lot_detail_id** - *ID (Идентификатор на партидно движение)*
			* **article_id** - Код на `артикула </barsy.help/210-dictionary/article.html>`__ (Идентификатор на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **create_date** - *Дата (Дата на движението)*
			* **operation_doc_date** - *Вальор (Дата-вальор на операцията)*
			* **article_name** - Име на `артикул </barsy.help/210-dictionary/article.html>`__ (Име на `артикула </barsy.help/210-dictionary/article.html>`__)
			* **user_name** - `Потребител </barsy.help/210-dictionary/user.html>`__ (`Потребител </barsy.help/210-dictionary/user.html>`__, извършил операцията)
			* **depot_name** - `Склад </barsy.help/210-dictionary/store.html>`__ (`Търговски обект </barsy.help/210-dictionary/barsy.html>`__ и `склад </barsy.help/210-dictionary/store.html>`__)
			* **operation_ref_type** - *Операция (Тип складова операция)*
			* **lot_value** - *Партида (Номер/стойност на партида)*
			* **lot_exp_date** - *Годно до (Срок на годност на партидата)*
			* **amount** - *Количество (Количество на движението)*
			* **amount_sum** - *Кол. след опер. (Количество след извършване на операцията. Показва се само ако е възможно)*
			* **ref_id** - * (Номер на операция-основание)* **По подразбиране:** ["lot_detail_id","create_date","operation_doc_date","article_name","user_name","depot_name","operation_ref_type","lot_value","lot_exp_date","amount","amount_sum"]
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
ReportsLotListDetailsResultData_                                       Обект с данни за резултатите
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ReportsLotListDetailsFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsLotListDetailsFilters

   * - Параметър
     - Тип
     - Описание
   * - **$ref_date**
     - *string*
     - *Период на движенията* **По подразбиране:** ["2026-07-01"]
   * - **$article**
     - *string*
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../articles/search` )
   * - **$lot_value**
     - *string*
     - *Филтриране по партида*
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
   * - **$operation_ref_type**
     - *string*
     - *Филтриране по тип складова операция*

			* **AC** - Приключване на `сметка </barsy.help/210-dictionary/account.html>`__
			* **ST** - *Сторно*
			* **LD** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__
			* **LC** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__ корекция
			* **MV** - `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__
			* **SO** - `Изписване </barsy.help/210-dictionary/storeout.html>`__
			* **OT** - `Изписване </barsy.help/210-dictionary/storeout.html>`__ - анулирано
			* **AP** - `Производство </barsy.help/210-dictionary/storeproduction.html>`__
			* **RC** - `Ревизия </barsy.help/210-dictionary/revision.html>`__
			* **CR** - *Корекция на рецепта*
			* **AR** - *Архивиране*
   * - **$ref_id**
     - *string*
     - *Филтриране по номер на операция*

-----

ReportsLotListDetailsResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsLotListDetailsResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$lot_detail_id**
     - *int*
     - *Идентификатор на партидно движение*
   * - **$article_id**
     - *string*
     - Идентификатор на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$create_date**
     - *string*
     - *Дата на движението*
   * - **$operation_doc_date**
     - *string*
     - *Дата-вальор на операцията*
   * - **$article_name**
     - *string*
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$user_name**
     - *string*
     - `Потребител </barsy.help/210-dictionary/user.html>`__, извършил операцията
   * - **$depot_name**
     - *string*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__ и `склад </barsy.help/210-dictionary/store.html>`__
   * - **$operation_ref_type**
     - *string*
     - *Тип складова операция*
   * - **$lot_value**
     - *string*
     - *Номер/стойност на партида*
   * - **$lot_exp_date**
     - *string*
     - *Срок на годност на партидата*
   * - **$amount**
     - *string*
     - *Количество на движението*
   * - **$amount_sum**
     - *string*
     - *Количество след извършване на операцията. Показва се само ако е възможно*
   * - **$ref_id**
     - *string*
     - *Номер на операция-основание*

-----

ReportsLotListDetailsResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ReportsLotListDetailsResultData

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
     - ReportsLotListDetailsResultRowData_ []
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

     .. literalinclude:: ../../sources/reports_lot_list_details/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/reports_lot_list_details/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/reports_lot_list_details/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/reports_lot_list_details/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/reports_lot_list_details/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/reports_lot_list_details/barsy_api_client_simple.php
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

