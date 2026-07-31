.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storemoves_getlist
===========================================================
Списък с прехвърляния

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/storemove </barsy.help/210-dictionary/storemove.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с операции за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ между складове с богат набор от филтри — по период, изходен/приемащ `склад </barsy.help/210-dictionary/store.html>`__, статус (чернова, изпратено, инспектирано, приключено, отказано), `потребител </barsy.help/210-dictionary/user.html>`__-създател, документ-основание. Поддържа странициране, сортиране и `extra_properties` за обогатяване с редове и междинна история на статусите.

Типични случаи: одиторска справка за движения между обекти, оперативен преглед на чакащи за приемане прехвърляния, експорт за периодична логистична отчетност, проверка на текущ baseline между централен `склад </barsy.help/210-dictionary/store.html>`__ и обекти.

**Име**: Storemoves_getlist
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
   * - **$filters**
     - StoreMovesListFiltersData_ 
     - 
   * - **$extra_properties**
     - StoreMovesListExtraProperties_ 
     - 
   * - **$offset**
     - *int*
     -  **По подразбиране:** 0
   * - **$length**
     - *int*
     -  **По подразбиране:** 1000
   * - **$order_by**
     - StoreMovesListOrderByData_ 
     - Подреждане — обект колона⇒посока (напр. {"date":"desc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
StoreMoveData_                                                         
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreMovesListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMovesListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$from_barsy_id**
     - *int*
     - Филтър по "от ТО"
   * - **$from_depot_id**
     - *int*
     - Филтър по "от `Склад </barsy.help/210-dictionary/store.html>`__"
   * - **$to_barsy_id**
     - *int*
     - Филтър по "до ТО"
   * - **$to_depot_id**
     - *int*
     - Филтър по "до `Склад </barsy.help/210-dictionary/store.html>`__"
   * - **$date**
     - *datetime*
     - Филтър по дата на създаване на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$creator_id**
     - *int*
     - Филтър по id на създател
   * - **$creator_name**
     - *string*
     - Филтър по име на създател
   * - **$inspector_id**
     - *int*
     - Филтър по id на приел
   * - **$inspector_name**
     - *string*
     - Филтър по име на приел
   * - **$status**
     - *int*
     - Филтър по статус

-----

StoreMovesListExtraProperties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMovesListExtraProperties

   * - Параметър
     - Тип
     - Описание
   * - **$common**
     - *bool*
     - Основни данни за `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ **По подразбиране:** true
   * - **$user**
     - *bool*
     - `Потребител </barsy.help/210-dictionary/user.html>`__, създал `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ ( виж: :doc:`../users/getlist` ) **По подразбиране:** true
   * - **$from**
     - *bool*
     - Показва данни за `склада </barsy.help/210-dictionary/store.html>`__ и търговския обект, от които се изтегля стоката **По подразбиране:** true
   * - **$to**
     - *bool*
     - Показва данни за `склада </barsy.help/210-dictionary/store.html>`__ и търговския обект, към които се изпраща стоката **По подразбиране:** true
   * - **$doc_date**
     - *bool*
     - Документална дата на операцията **По подразбиране:** false
   * - **$inspector_user_name**
     - *bool*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, проверил `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ ( виж: :doc:`../users/getlist` ) **По подразбиране:** false
   * - **$description**
     - *bool*
     - Описание на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ **По подразбиране:** false
   * - **$inspector_description**
     - *bool*
     - Описание, въведено от `потребителя </barsy.help/210-dictionary/user.html>`__, проверил `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ **По подразбиране:** false
   * - **$status**
     - *bool*
     - ID статус на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ **По подразбиране:** false
   * - **$status_title**
     - *bool*
     - 

			* **0** - *Отворено*
			* **1** - *Приключено*
			* **2** - *На път*
			* **3** - *Отказано*
			* **10** - *За получаване*
			* **11** - *Изпратено* **По подразбиране:** false
   * - **$close_date**
     - *bool*
     - Дата на затваряне на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ **По подразбиране:** false
   * - **$details**
     - *bool*
     - Данни за `артикулите </barsy.help/210-dictionary/article.html>`__ в `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ **По подразбиране:** false

-----

StoreMovesListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с прехвърляния (Storemoves_getlist).
		Подава се като низ ("date desc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMovesListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - **$store_move_id**
     - 
     - 
   * - **$date**
     - 
     - 
   * - **$doc_date**
     - 
     - 
   * - **$close_date**
     - 
     - 
   * - **$status**
     - 
     - 
   * - **$from_depot_id**
     - 
     - 
   * - **$to_depot_id**
     - 
     - 

-----

StoreMoveData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMoveData

   * - Параметър
     - Тип
     - Описание
   * - **$store_move_id**
     - 
     - 
   * - **$depot_id_left**
     - *int*
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, от който се изтелгя количество
   * - **$depot_id_right**
     - *int*
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, в кой се прехвърля количество
   * - **$doc_date**
     - *string*
     - 
   * - **$description**
     - *string*
     - 
   * - **$user_name**
     - *string*
     - `Потребител </barsy.help/210-dictionary/user.html>`__, създал `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$user_id**
     - *int*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$inspector_user_name**
     - *string*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, проверил `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$date**
     - *string*
     - Дата на създаване на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$inspector_description**
     - *string*
     - Description of the inspector
   * - **$status**
     - *string*
     - Статус на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$user_status**
     - *string*
     - Заглавие на статус
   * - **$close_date**
     - *string*
     - Дата за затваряне на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$from_barsy_id**
     - *int*
     - ID на изходящия `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$to_barsy_id**
     - *int*
     - ID на входящия `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$from_depot_name**
     - 
     - 
   * - **$to_depot_name**
     - 
     - 
   * - **$from_barsy_name**
     - 
     - 
   * - **$to_barsy_name**
     - 
     - 
   * - **$details**
     - StoreMoveDetailData_ []
     - Детайли за `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__

-----

StoreMoveDetailData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за един ред от `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMoveDetailData

   * - Параметър
     - Тип
     - Описание
   * - **$row_id**
     - *int*
     - ID на реда
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articles/getlist` )
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *float*
     - Количество за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__
   * - **$avg_delivery_price**
     - *float*
     - Средна доставна цена
   * - **$inspection_amount**
     - *float*
     - Проверено/получено количество
   * - **$notes**
     - *string*
     - Бележки към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_price**
     - *float*
     - Текуща цена на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$tax**
     - *float*
     - Данъчна ставка в проценти
   * - **$tax_id**
     - *int*
     - ID на данъчната ставка ( виж: :doc:`../taxgroups/getlist` )

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

     .. literalinclude:: ../../sources/storemoves_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storemoves_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storemoves_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storemoves_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storemoves_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storemoves_getlist/barsy_api_client_simple.php
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

