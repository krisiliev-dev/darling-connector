.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storemoves_get
===========================================================
Преглед на прехвърляне

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/storemove </barsy.help/210-dictionary/storemove.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълни данни за конкретно `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ между складове по ID — основни полета (източник, дестинация, дата, статус, `потребители </barsy.help/210-dictionary/user.html>`__-създател и приемник, документ-основание, бележки), общи суми и евентуални разлики между изпратени и получени количества. Чрез `extra_properties` могат да се поискат допълнителни секции като редовете с `артикули </barsy.help/210-dictionary/article.html>`__, история на статусите, прикачени файлове.

Типични случаи: детайлен изглед в админ панела на едно `прехвърляне </barsy.help/210-dictionary/storemove.html>`__, проверка на разлики при инспекция в приемащ `склад </barsy.help/210-dictionary/store.html>`__, печат на товарителен лист, синхронизация към счетоводна система.

**Име**: Storemoves_get
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
   * - **$store_move_id**
     - *int*
     - ID на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$extra_properties**
     - StoreMoveExtraProperties_ 
     - Допълнителни данни за `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
StoreMoveData_                                                         
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreMoveExtraProperties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMoveExtraProperties

   * - Параметър
     - Тип
     - Описание
   * - **$details**
     - *bool*
     - Данни за `артикулите </barsy.help/210-dictionary/article.html>`__ в `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ **По подразбиране:** false

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

     .. literalinclude:: ../../sources/storemoves_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storemoves_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storemoves_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storemoves_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storemoves_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storemoves_get/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__


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

