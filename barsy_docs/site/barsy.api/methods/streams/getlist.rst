.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Streams_getlist
===========================================================
Списък с потоци

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с конфигурираните в системата `потоци </barsy.help/210-dictionary/flow.html>`__ (streams) — логически разделения за обработка на поръчките към различни точки на изпълнение (например "Кухня", "Бар", "Гриль", "За вкъщи"). Всеки `артикул </barsy.help/210-dictionary/article.html>`__ се асоциира с `поток </barsy.help/210-dictionary/flow.html>`__, който определя на кой кухненски/складов дисплей се появява, кой служител го обработва и каква бележка се отпечатва. Поддържа сортиране (по подразбиране азбучно).

Типични случаи: попълване на dropdown "`Поток </barsy.help/210-dictionary/flow.html>`__" при редакция на `артикул </barsy.help/210-dictionary/article.html>`__, конфигуриране на KDS системите по работни места, изграждане на справка за натовареност по `поток </barsy.help/210-dictionary/flow.html>`__.

**Име**: Streams_getlist
**Категория**: Settings


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
     - StreamsListFiltersData_ 
     - Налични филтри за списъка с `потоци </barsy.help/210-dictionary/flow.html>`__
   * - **$offset**
     - *int*
     - Номер на ред, от който да започне списъкът (странициране) **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - StreamsListOrderByData_ 
     - Подреждане — низ, масив или обект колона⇒посока (напр. {"name":"asc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
StreamData_                                                            Списък с потоци според филтрите
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StreamsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StreamsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$scales_update**
     - *int*
     - Филтър по флаг за "Подаване към везна"
   * - **$name**
     - *string*
     - Филтър по име на `поток </barsy.help/210-dictionary/flow.html>`__.

			*Намира и при частично съвпадение*
   * - **$for_service**
     - *int*
     - Само `потоци </barsy.help/210-dictionary/flow.html>`__, обслужими от текущата `каса </barsy.help/210-dictionary/pos.html>`__ (подай 1 за активиране)
   * - **$delete_flag**
     - *int*
     - Филтър по delete_flag (0 — активни, 1 — изтрити).

			Ако не е подаден — връщат се всички `потоци </barsy.help/210-dictionary/flow.html>`__

-----

StreamsListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с `потоци </barsy.help/210-dictionary/flow.html>`__ (Streams_getlist).
		Подава се като асоциативен масив колона⇒посока (напр. ["name" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

.. list-table::
   :header-rows: 1
   :align: center
   :name: StreamsListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - **$name**
     - *string*
     - Подреждане по име на `потока </barsy.help/210-dictionary/flow.html>`__
   * - **$order_in_receipt**
     - *string*
     - Подреждане по тежест в бележките
   * - **$stream_id**
     - *string*
     - Подреждане по ID на `потока </barsy.help/210-dictionary/flow.html>`__

-----

StreamData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StreamData

   * - Параметър
     - Тип
     - Описание
   * - **$stream_id**
     - *int*
     - 
   * - **$stream_name**
     - *string*
     - 
   * - **$description**
     - *string*
     - 
   * - **$label_id**
     - *int*
     - 
   * - **$order_in_receipt**
     - *int*
     - 
   * - **$scales_update**
     - *int*
     - 
   * - **$process_time_expired**
     - *int*
     - 
   * - **$delete_flag**
     - 
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

     .. literalinclude:: ../../sources/streams_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/streams_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/streams_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/streams_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/streams_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/streams_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Поток </barsy.help/210-dictionary/flow.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

