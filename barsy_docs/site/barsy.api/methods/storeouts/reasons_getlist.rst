.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storeouts_reasons_getlist
===========================================================
Причини за изписване

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/storeout </barsy.help/210-dictionary/storeout.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща дефинираните в системата причини за `изписване </barsy.help/210-dictionary/storeout.html>`__ на конкретен ред (`артикул </barsy.help/210-dictionary/article.html>`__) в складово `изписване </barsy.help/210-dictionary/storeout.html>`__ — например "Изтекъл срок", "Повреден", "Дегустация", "Кражба", "Представителни разходи". Причините се ползват за аналитични справки и счетоводна категоризация. Всяка причина може да е глобална (валидна за всички типове изписвания) или да принадлежи към конкретен тип. Списъкът е custom за конкретна инсталация.

Типични случаи: попълване на dropdown "Причина" при ред в `изписване </barsy.help/210-dictionary/storeout.html>`__, изграждане на справки за загуби по причини, конфигуриране на UI workflow при бракуване, обучение на персонала за коректна категоризация.

**Име**: Storeouts_reasons_getlist
**Категория**: Store


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
StoreOutReasonData_                                                    
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreOutReasonData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Причина за `изписване </barsy.help/210-dictionary/storeout.html>`__ на `артикул </barsy.help/210-dictionary/article.html>`__ в операция `изписване </barsy.help/210-dictionary/storeout.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreOutReasonData

   * - Параметър
     - Тип
     - Описание
   * - **$reason_id**
     - *int*
     - Id на причината
   * - **$type_id**
     - *int*
     - ID на типа `изписване </barsy.help/210-dictionary/storeout.html>`__, към който принадлежи причината.

			*Ако е празно - причината е глобална (видима във всички типове изписвания)*
   * - **$name**
     - *int*
     - Име на причината
   * - **$color**
     - *int*
     - Цвят на причината (в списъците)
   * - **$delete_flag**
     - *int*
     - Флаг дали е маркиран като изтрит

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

     .. literalinclude:: ../../sources/storeouts_reasons_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storeouts_reasons_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storeouts_reasons_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storeouts_reasons_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storeouts_reasons_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storeouts_reasons_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Изписване </barsy.help/210-dictionary/storeout.html>`__


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

