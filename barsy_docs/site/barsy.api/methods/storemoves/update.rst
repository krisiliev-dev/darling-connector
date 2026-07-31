.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storemoves_update
===========================================================
Редактиране на прехвърляне

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/150-store/20-storemoves/index </barsy.help/110-admin/150-store/20-storemoves/index.html>`__
	 * barsy.help: `210-dictionary/storemove </barsy.help/210-dictionary/storemove.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Презаписва данните на съществуващо `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ между складове — основни полета и редовете с `артикули </barsy.help/210-dictionary/article.html>`__. Подаденият списък `rows` ИЗЦЯЛО заменя текущите редове. Чрез `action_type` се избира преходът към следващ статус (`save`, `save_and_close`, `save_and_send`, `save_inspection`, `confirm_move`, `cancel_move`). Допустимостта на конкретен преход зависи от текущия статус и правата на `потребителя </barsy.help/210-dictionary/user.html>`__.

Типични случаи: корекция на количества преди изпращане, добавяне на пропуснат `артикул </barsy.help/210-dictionary/article.html>`__, отбелязване на инспектирани количества от приемащия `склад </barsy.help/210-dictionary/store.html>`__ (разлики между изпратено и получено).

**Име**: Storemoves_update
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
   * - **$id**
     - *int*
     - ID на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__.

			*При null, създава ново*
   * - **$storemove**
     - StoreMoveCreateData_ 
     - Обект, съдържаш информация за `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$rows**
     - StoreMoveCreateRowData_ []
     - Масив от обекти, съдържащи информация за `артикулите </barsy.help/210-dictionary/article.html>`__
   * - **$action_type**
     - *string*
     - [save=Запис без приключване, save_and_close=Запис с приключване, save_and_send=Запис с изпращане,save_inspection=Запис на инспектиране,confirm_move=Потвърждаване на `прехвърляне </barsy.help/210-dictionary/storemove.html>`__,cancel_move=Отхвърняне на `прехвърляне </barsy.help/210-dictionary/storemove.html>`__] **По подразбиране:** 'save'


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на прехвърлянето
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreMoveCreateData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMoveCreateData

   * - Параметър
     - Тип
     - Описание
   * - **$depot_id_left**
     - *int*
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, от който се изтелгя количество ( виж: :doc:`../depots/getlist` )
   * - **$depot_id_right**
     - *int*
     - ID на `склада </barsy.help/210-dictionary/store.html>`__, в кой се прехвърля количество ( виж: :doc:`../depots/getlist` )
   * - **$doc_date**
     - *string*
     - 
   * - **$description**
     - *string*
     - 
   * - **$deal_id**
     - *string*
     -  ( виж: :doc:`../deals/getlist` )
   * - **$inspector_description**
     - *string*
     - 
   * - **$redirect_depot_id**
     - *int*
     - 

-----

StoreMoveCreateRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreMoveCreateRowData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *float*
     - Количество, което ще се прехвърля от единия `склад </barsy.help/210-dictionary/store.html>`__ в другия
   * - **$notes**
     - *string*
     - Свободни бележки за реда
   * - **$received**
     - 
     - 
   * - **$row_id**
     - 
     - 
   * - **$lot_value**
     - *string*
     - Партида

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

     .. literalinclude:: ../../sources/storemoves_update/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storemoves_update/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storemoves_update/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storemoves_update/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storemoves_update/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storemoves_update/barsy_api_client_simple.php
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

