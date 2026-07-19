.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storeproductions_movements
===========================================================
Движения за производство

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/storeproduction </barsy.help/210-dictionary/storeproduction.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща две таблици с детайлни складови движения, свързани с конкретно `производство </barsy.help/210-dictionary/storeproduction.html>`__ — изтеглените компоненти (съставките по рецептата с реални количества и себестойност) и заредените готови продукти (произведената стока, заведена като нова наличност). Полезно за проверка на материален баланс — сравнение между теоретичната рецептурна норма и реалното отписване.

*Типични случаи: контрол на загубите в цех (теория vs реалност), одит на коректността на рецептите, изчисляване на действителна себестойност на готовия продукт, разследване на отклонение в произведено/доставено количество.*

**Име**: Storeproductions_movements
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
   * - **$action_type**
     - *string*
     - Тип на върнатите данни

			* **content** - *структура на списъка*
			* **values** - *стойности на списъка* **По подразбиране:** 'content'
   * - **$id**
     - *string*
     - ID на обекта, който се обработва

			Складови движения - изтеглени `артикули </barsy.help/210-dictionary/article.html>`__
   * - **$filters**
     - StoreproductionsMovementsFilters_ 
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

			* **store_id** - *ID (ID на складово движение)*
			* **row_id** - *Row ID (ID на запис в документа)*
			* **article_name_prod** - Произведен `артикул </barsy.help/210-dictionary/article.html>`__
			* **article_name** - Изтеглен `артикул </barsy.help/210-dictionary/article.html>`__
			* **amount** - *Количество*
			* **avg_delivery_price** - *Себестойност (без ДДС)*
			* **avg_delivery_price__sec_curr** - *Себестойност (без ДДС) (Български лев)*
			* **dds_avg_delivery_price** - *Себестойност (+ДДС)*
			* **dds_avg_delivery_price__sec_curr** - *Себестойност (+ДДС) (Български лев)*
			* **avg_delivery_price_sum** - *Сума себест (без ДДС)*
			* **avg_delivery_price_sum__sec_curr** - *Сума себест (без ДДС) (Български лев)*
			* **dds_avg_delivery_price_sum** - *Сума себест (+ДДС)*
			* **dds_avg_delivery_price_sum__sec_curr** - *Сума себест (+ДДС) (Български лев)* **По подразбиране:** ["store_id","article_name_prod","article_name","amount","avg_delivery_price","avg_delivery_price_sum"]
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
StoreproductionsMovementsResultData_                                   
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreproductionsMovementsFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

-----

StoreproductionsMovementsResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreproductionsMovementsResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$store_id**
     - *int*
     - *ID на складово движение*
   * - **$row_id**
     - *string*
     - *ID на запис в документа*
   * - **$article_name_prod**
     - *string*
     - Произведен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name**
     - *string*
     - Изтеглен `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *string*
     - *Количество*
   * - **$avg_delivery_price**
     - *string*
     - *Себестойност (без ДДС)*
   * - **$avg_delivery_price__sec_curr**
     - *string*
     - *Себестойност (без ДДС) (Български лев)*
   * - **$dds_avg_delivery_price**
     - *string*
     - *Себестойност (+ДДС)*
   * - **$dds_avg_delivery_price__sec_curr**
     - *string*
     - *Себестойност (+ДДС) (Български лев)*
   * - **$avg_delivery_price_sum**
     - *string*
     - *Сума себест (без ДДС)*
   * - **$avg_delivery_price_sum__sec_curr**
     - *string*
     - *Сума себест (без ДДС) (Български лев)*
   * - **$dds_avg_delivery_price_sum**
     - *string*
     - *Сума себест (+ДДС)*
   * - **$dds_avg_delivery_price_sum__sec_curr**
     - *string*
     - *Сума себест (+ДДС) (Български лев)*

-----

StoreproductionsMovementsResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreproductionsMovementsResultData

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
     - StoreproductionsMovementsResultRowData_ []
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

     .. literalinclude:: ../../sources/storeproductions_movements/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storeproductions_movements/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storeproductions_movements/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storeproductions_movements/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storeproductions_movements/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storeproductions_movements/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Производство </barsy.help/210-dictionary/storeproduction.html>`__


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

