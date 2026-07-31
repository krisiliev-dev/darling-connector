.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storeloads_getlist
===========================================================
Списък със зареждания

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/150-store/10-storeloads/index </barsy.help/110-admin/150-store/10-storeloads/index.html>`__
	 * barsy.help: `210-dictionary/storeload </barsy.help/210-dictionary/storeload.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с регистрираните складови зареждания (доставки) с богат набор от филтри — по период (документална дата), `склад </barsy.help/210-dictionary/store.html>`__, `доставчик </barsy.help/210-dictionary/supplier.html>`__, статус (чернова/приключена), `потребител </barsy.help/210-dictionary/user.html>`__, документ-основание, диапазон на сума. Поддържа странициране, сортиране и `extra_properties` за обогатяване с редовете на документа.

Типични случаи: справка за доставки от конкретен `доставчик </barsy.help/210-dictionary/supplier.html>`__ за период, `ревизия </barsy.help/210-dictionary/revision.html>`__ на приключени зареждания преди счетоводно осчетоводяване, експорт към счетоводна система, проверка на черновите за приключване в края на деня.

**Име**: Storeloads_getlist
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
     - StoreLoadsListFiltersData_ 
     - Филтри на списъка със складови зареждания
   * - **$extra_properties**
     - *array*
     - 

			* **all** - всички основни данни за `зареждането </barsy.help/210-dictionary/storeload.html>`__
			* **details** - `Артикулите </barsy.help/210-dictionary/article.html>`__ в `зареждането </barsy.help/210-dictionary/storeload.html>`__ **По подразбиране:** []
   * - **$offset**
     - *int*
     -  **По подразбиране:** 0
   * - **$length**
     - *int*
     -  **По подразбиране:** 10000
   * - **$order_by**
     - StoreLoadsListOrderByData_ 
     - Подреждане — обект колона⇒посока (напр. {"date":"desc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
StoreLoadData_                                                         
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreLoadsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreLoadsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$store_load_id**
     - *int*
     - ID на `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$barsy_id**
     - *int*
     - Филтър по "`Търговски обект </barsy.help/210-dictionary/barsy.html>`__" в който е направено `зареждането </barsy.help/210-dictionary/storeload.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$depot_id**
     - *int*
     - Филтър по "`Склад </barsy.help/210-dictionary/store.html>`__" в който е направено `зареждането </barsy.help/210-dictionary/storeload.html>`__ ( виж: :doc:`../depots/getlist` )
   * - **$date**
     - *datetime*
     - Филтър по дата на създаване на документа
   * - **$doc_date**
     - *datetime*
     - Филтър по дата на документа, по които е направена операцията
   * - **$creator_id**
     - *int*
     - Филтър по ID на създател на операцията ( виж: :doc:`../users/getlist` )
   * - **$user_name**
     - *string*
     - Филтър по име на създател на операцията ( виж: :doc:`../users/getlist` )
   * - **$status**
     - *int*
     - Филтър по статус

			* **0** - *Отворено*
			* **1** - *Приключено*
   * - **$last_update**
     - *datetime*
     - Дата на последно обновяване на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$operation_type**
     - *int*
     - Операция на `зареждането </barsy.help/210-dictionary/storeload.html>`__ (1: `Зареждане </barsy.help/210-dictionary/storeload.html>`__ на стока, 2: Връщане на стока)
   * - **$doc_type_id**
     - *int*
     - Тип на документа ( виж: :doc:`../storeloads/getdocumenttypes` )
   * - **$remote_id**
     - *int*
     - Номер на отдалечената система ( виж: :doc:`../remotesystems/getlist` )

-----

StoreLoadsListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка със зареждания (Storeloads_getlist).
		Подава се като низ ("date desc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreLoadsListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - **$store_load_id**
     - 
     - 
   * - **$date**
     - 
     - 
   * - **$close_date**
     - 
     - 
   * - **$doc_date**
     - 
     - 
   * - **$doc_num**
     - 
     - 
   * - **$total_sum**
     - 
     - 
   * - **$status**
     - 
     - 
   * - **$depot_id**
     - 
     - 
   * - **$barsy_id**
     - 
     - 
   * - **$creator_id**
     - 
     - 

-----

StoreLoadData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreLoadData

   * - Параметър
     - Тип
     - Описание
   * - **$store_load_id**
     - *int*
     - ID на `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - Име на търговския обект
   * - **$depot_id**
     - *int*
     - ID на `склад </barsy.help/210-dictionary/store.html>`__, в който е заредено ( виж: :doc:`../depots/getlist` )
   * - **$status**
     - *int*
     - Статус на `зареждането </barsy.help/210-dictionary/storeload.html>`__ [0=Отворено, 1=Приключено]
   * - **$doc_type_name**
     - *string*
     - Тип документ, по който е заредено
   * - **$doc_type_id**
     - *int*
     - ID на тип документ, по който е заредено
   * - **$doc_num**
     - *string*
     - Номер на документа
   * - **$price_mode**
     - *int*
     - Режим на единични цени (0=>без включено ДДС, 1=>с включено ДДС)
   * - **$has_tax**
     - *int*
     - Тип за `зареждането </barsy.help/210-dictionary/storeload.html>`__ (0=>без начислено ДДС, 1=>с начислено ДДС)
   * - **$date**
     - *string*
     - Дата на създаване на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$close_date**
     - *string*
     - Дата на приключване на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$doc_date**
     - *string*
     - Документална дата на операцията
   * - **$description**
     - *string*
     - Описание на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$user_name**
     - *string*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$creator_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$supplier_id**
     - *int*
     - ID на `доставчик </barsy.help/210-dictionary/supplier.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__ ( виж: :doc:`../suppliers/getlist` )
   * - **$supplier_name**
     - *string*
     - Име на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$operation_type**
     - *int*
     - Тип операция (`зареждане </barsy.help/210-dictionary/storeload.html>`__, връщане на стока към `доставчик </barsy.help/210-dictionary/supplier.html>`__)
   * - **$total_sum**
     - *float*
     - Обща сума на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$total_paid**
     - *float*
     - Общо платени по `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$paid_due_date**
     - *string*
     - Крайна дата за `плащане </barsy.help/210-dictionary/payment.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$currency_id**
     - *int*
     - ID на валутата на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$currency_rate**
     - *float*
     - Курс на валутата на `зареждането </barsy.help/210-dictionary/storeload.html>`__ към основната валута на системата
   * - **$total_costs**
     - *float*
     - Обща сума на разходите към `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$cost_mode**
     - *int*
     - Режим на изчислване на разходите спрямо общата сума (включени,изключени)
   * - **$request_id**
     - *int*
     - ID на `заявката към доставчика </barsy.help/210-dictionary/request.html>`__, по която е създадено `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$paymethod_id**
     - *int*
     - ID на реален начин `плащане </barsy.help/210-dictionary/payment.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__.

			*Формира се от плащанията към операцията* ( виж: :doc:`../paymentmethods/getlist` )
   * - **$preferred_paymethod_id**
     - *int*
     - ID на предпочитан начин на `плащане </barsy.help/210-dictionary/payment.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__.

			*Задава се свободно. Само за информационни цели* ( виж: :doc:`../paymentmethods/getlist` )
   * - **$last_update**
     - *string*
     - Дата на последна редакция на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$parent_id**
     - *int*
     - ID на родителско `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$total_costs_2**
     - *float*
     - Сума на разходите от подчинетите зареждания (свързани с PARENT_ID)

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

     .. literalinclude:: ../../sources/storeloads_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storeloads_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storeloads_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storeloads_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storeloads_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storeloads_getlist/barsy_api_client_simple.php
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

