.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storeouts_getlist
===========================================================
Списък с изписвания

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/150-store/30-storeouts/index </barsy.help/110-admin/150-store/30-storeouts/index.html>`__
	 * barsy.help: `210-dictionary/storeout </barsy.help/210-dictionary/storeout.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък със складови изписвания (брак, експертиза, дегустация, личен консумация, представителен разход, рекламни проби) с богат набор от филтри — по период, `склад </barsy.help/210-dictionary/store.html>`__, тип `изписване </barsy.help/210-dictionary/storeout.html>`__, причина, статус, `потребител </barsy.help/210-dictionary/user.html>`__. Изписванията намаляват наличностите без приходен ефект и са основен инструмент за управление на загуби, маркетинг и вътрешно потребление.

*Типични случаи: одит на бракуваните количества за период, анализ на разходи за дегустации в ресторант, отчет за маркетингови подаръци, синхронизация към счетоводна система за разходи.*

**Име**: Storeouts_getlist
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
     - StoreOutsListFiltersData_ 
     - 
   * - **$extra_properties**
     - *array*
     - 

			* **all** - всички основни данни за `изписването </barsy.help/210-dictionary/storeout.html>`__
			* **details** - `Артикулите </barsy.help/210-dictionary/article.html>`__ в `изписването </barsy.help/210-dictionary/storeout.html>`__ **По подразбиране:** []
   * - **$offset**
     - *int*
     - Номер на ред от който да бъде започнат списъка.

			*Използва се при странициране, когато трябва да се прескочат Х записа* **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - StoreOutsListOrderByData_ 
     - Подреждане — обект колона⇒посока (напр. {"date":"desc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
StoreOutData_                                                          
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreOutsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreOutsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$store_out_id**
     - *int*
     - ID на `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$barsy_id**
     - *int*
     - Филтър по "`Търговски обект </barsy.help/210-dictionary/barsy.html>`__" ( виж: :doc:`../barsys/getlist` )
   * - **$depot_id**
     - *int*
     - Филтър по "`Склад </barsy.help/210-dictionary/store.html>`__" ( виж: :doc:`../depots/getlist` )
   * - **$date**
     - *datetime*
     - Филтър по дата на създаване на документа
   * - **$close_date**
     - *datetime*
     - Филтър по дата на приключване на документа
   * - **$doc_date**
     - *datetime*
     - Филтър по документална дата на документа
   * - **$user_id**
     - *int*
     - Филтър по id на създател ( виж: :doc:`../users/getlist` )
   * - **$user_name**
     - *string*
     - Филтър по име на създател ( виж: :doc:`../users/getlist` )
   * - **$status**
     - *int*
     - Филтър по статус

			* **0** - *Отворено*
			* **1** - *Приключено*
   * - **$type_id**
     - *int*
     - Филтър по тип `изписване </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../storeouts/types_getlist` )
   * - **$ref_id**
     - *int*
     - Филтър по референтен номер, свързващ анулиран с анулиращ документ
   * - **$anulate_flag**
     - *int*
     - Филтър флаг дали `изписването </barsy.help/210-dictionary/storeout.html>`__ е анулирано или анулиращо

			* **0** - *Не е анулиран*
			* **1** - *Анулиран*
			* **-1** - *Анулиращ*
   * - **$export_id**
     - *int*
     - Филтър по Export ID

-----

StoreOutsListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с изписвания (Storeouts_getlist).
		Подава се като низ ("date desc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreOutsListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - **$store_out_id**
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
   * - **$total_sum**
     - 
     - 
   * - **$status**
     - 
     - 
   * - **$type_id**
     - 
     - 
   * - **$depot_id**
     - 
     - 
   * - **$barsy_id**
     - 
     - 
   * - **$user_id**
     - 
     - 

-----

StoreOutData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreOutData

   * - Параметър
     - Тип
     - Описание
   * - **$store_out_id**
     - *int*
     - ID на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който е извършено `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - Име на търговския обект ( виж: :doc:`../barsys/getlist` )
   * - **$depot_id**
     - *int*
     - ID на `склад </barsy.help/210-dictionary/store.html>`__, от който е направено `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../depots/getlist` )
   * - **$depot_name**
     - *int*
     - Име на `склад </barsy.help/210-dictionary/store.html>`__, от който е направено `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../depots/getlist` )
   * - **$date**
     - *string*
     - Дата на създаване на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$doc_date**
     - *string*
     - Документална дата на операцията
   * - **$close_date**
     - *string*
     - Дата на приключване на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$status**
     - *int*
     - Статус на `изписването </barsy.help/210-dictionary/storeout.html>`__

			* **0** - *Отворено*
			* **1** - *Приключено*
   * - **$description**
     - *string*
     - Описание на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$type_id**
     - *int*
     - ID на типа на `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../storeouts/types_getlist` )
   * - **$type_name**
     - *string*
     - Име на типа на `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../storeouts/types_getlist` )
   * - **$ref_id**
     - *int*
     - Референтен номер, указващ ID на анулиращия или анулирания документ (ако текущият е анулиран или анулиращ - виж.anulate_flag)
   * - **$user_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$user_name**
     - *string*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$anulate_flag**
     - *int*
     - Флаг дали `изписването </barsy.help/210-dictionary/storeout.html>`__ е нормално, анулирано или анулиращо

			* **1** - *Анулиран*
			* **-1** - *Анулиращ документ*
			* **0** - *Нормален*
   * - :deprecated:`$is_anulate`
     - *bool*
     - Синоним на "anulate_flag" :deprecated_text:`Отхвърлено: */`
   * - **$export_id**
     - *string*
     - Експорт ID
   * - **$deal_id**
     - *int*
     - ID на сделката, към която е това `изписване </barsy.help/210-dictionary/storeout.html>`__
   * - **$deal_title**
     - *string*
     - Заглавие на сделката, към която е това `изписване </barsy.help/210-dictionary/storeout.html>`__
   * - **$total_sum**
     - *float*
     - Обща сума на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$details**
     - StoreOutDetailData_ []
     - Списък с редовете към `изписването </barsy.help/210-dictionary/storeout.html>`__ (ако са поискани)

-----

StoreOutDetailData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreOutDetailData

   * - Параметър
     - Тип
     - Описание
   * - **$store_out_id**
     - *int*
     - ID на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$article_id**
     - *int*
     - ID на изписания `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articles/getlist` )
   * - **$article_name**
     - *string*
     - Име на изписания `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articles/getlist` )
   * - **$amount**
     - *float*
     - Изписано количество
   * - **$current_price**
     - *float*
     - Продажна цена към момента на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$avg_delivery_price**
     - *float*
     - Средна доставна цена към момента на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$reason_id**
     - *int*
     - ID на причината за `изписване </barsy.help/210-dictionary/storeout.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../storeouts/reasons_getlist` )
   * - **$tax**
     - *int*
     - Данъчна ставка на този `артикул </barsy.help/210-dictionary/article.html>`__ към момента на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$tax_id**
     - *int*
     - ID на данъчната група на този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$notes**
     - *string*
     - Свободен текст към всеки ред/`артикул </barsy.help/210-dictionary/article.html>`__ в `изписването </barsy.help/210-dictionary/storeout.html>`__

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

     .. literalinclude:: ../../sources/storeouts_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storeouts_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storeouts_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storeouts_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storeouts_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storeouts_getlist/barsy_api_client_simple.php
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

