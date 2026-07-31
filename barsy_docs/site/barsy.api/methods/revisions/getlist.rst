.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Revisions_getlist
===========================================================
Списък с ревизии

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/150-store/50-revisions/index </barsy.help/110-admin/150-store/50-revisions/index.html>`__
	 * barsy.help: `210-dictionary/revision </barsy.help/210-dictionary/revision.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък със складови `ревизии </barsy.help/210-dictionary/revision.html>`__ (инвентаризации) с богат набор от филтри — по период, `склад </barsy.help/210-dictionary/store.html>`__, статус (чернова/приключена), `потребител </barsy.help/210-dictionary/user.html>`__, тип на `ревизията </barsy.help/210-dictionary/revision.html>`__ (пълна/частична). `Ревизията </barsy.help/210-dictionary/revision.html>`__ сравнява реално преброени количества с теоретичните в системата и автоматично генерира корекционни движения за откритите разлики. Поддържа странициране, сортиране и `extra_properties` за включване на редовете и общите суми на разликите.

Типични случаи: периодична годишна инвентаризация, цикличен брояч на отделни групи `артикули </barsy.help/210-dictionary/article.html>`__, специализирана `ревизия </barsy.help/210-dictionary/revision.html>`__ на скъпи/чувствителни `артикули </barsy.help/210-dictionary/article.html>`__, спор-разрешаваща `ревизия </barsy.help/210-dictionary/revision.html>`__ след откриване на разлика в обикновена операция.

**Име**: Revisions_getlist
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
     - RevisionsListFiltersData_ 
     - 
   * - **$extra_properties**
     - *array*
     - [all=>всички основни данни за `изписването </barsy.help/210-dictionary/storeout.html>`__, details=>`Артикулите </barsy.help/210-dictionary/article.html>`__ в `изписването </barsy.help/210-dictionary/storeout.html>`__] **По подразбиране:** []
   * - **$offset**
     - *int*
     -  **По подразбиране:** 0
   * - **$length**
     - *int*
     -  **По подразбиране:** 10000
   * - **$order_by**
     - RevisionsListOrderByData_ 
     - Подреждане — обект колона⇒посока (напр. {"date":"desc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
RevisionData_                                                          
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

RevisionsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: RevisionsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$rev_id**
     - *int*
     - ID на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$depot_id**
     - *int*
     - ID на `склад </barsy.help/210-dictionary/store.html>`__, в който е заредено ( виж: :doc:`../depots/getlist` )
   * - **$status**
     - *int*
     - Статус на `ревизията </barsy.help/210-dictionary/revision.html>`__ [0=Отворено, 1=Приключено]
   * - **$date**
     - *string*
     - Дата на създаване на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$close_date**
     - *string*
     - Дата на приключване на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$amount_date**
     - *string*
     - Дата на операцията (момент на засичане на наличности)
   * - **$creator_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `ревизията </barsy.help/210-dictionary/revision.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$closer_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, приключил `ревизията </barsy.help/210-dictionary/revision.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$article_name**
     - *string*
     - Филтър по име, баркод или референтен номер на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Намира и при частично съвпадение*

-----

RevisionsListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с `ревизии </barsy.help/210-dictionary/revision.html>`__ (Revisions_getlist).
		Подава се като низ ("date desc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

.. list-table::
   :header-rows: 1
   :align: center
   :name: RevisionsListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - **$rev_id**
     - 
     - 
   * - **$date**
     - 
     - 
   * - **$close_date**
     - 
     - 
   * - **$amount_date**
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

-----

RevisionData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: RevisionData

   * - Параметър
     - Тип
     - Описание
   * - **$rev_id**
     - *int*
     - ID на `ревизията </barsy.help/210-dictionary/revision.html>`__
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
     - Статус на `ревизията </barsy.help/210-dictionary/revision.html>`__ [0=Отворено, 1=Приключено]
   * - **$date**
     - *string*
     - Дата на създаване на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$close_date**
     - *string*
     - Дата на приключване на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$amount_date**
     - *string*
     - Дата на операцията (момент на засичане на наличности)
   * - **$description**
     - *string*
     - Описание на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$user_name**
     - *string*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$creator_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `ревизията </barsy.help/210-dictionary/revision.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$closer_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, приключил `ревизията </barsy.help/210-dictionary/revision.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$close_count**
     - *int*
     - Брой пъти, в които `ревизията </barsy.help/210-dictionary/revision.html>`__ е била затворена

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

     .. literalinclude:: ../../sources/revisions_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/revisions_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/revisions_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/revisions_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/revisions_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/revisions_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Ревизия </barsy.help/210-dictionary/revision.html>`__


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

