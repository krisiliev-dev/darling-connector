.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storeouts_types_getlist
===========================================================
Типове изписвания

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/storeout </barsy.help/210-dictionary/storeout.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща дефинираните в системата типове складови изписвания — общата класификация на документа (за разлика от причините, които са на ниво ред). Примерни типове: "Брак", "Дегустация", "Представителни разходи", "Маркетингови проби", "Подарък на персонал". Към всеки тип могат да са асоциирани специфични причини. Типовете контролират счетоводната класификация и достъпността пред различни `потребители </barsy.help/210-dictionary/user.html>`__.

Типични случаи: попълване на dropdown при ново `изписване </barsy.help/210-dictionary/storeout.html>`__, изграждане на справки за разходи по тип, конфигуриране на права (например само мениджъри могат да правят бракуване), синхронизация на категоризацията към счетоводна система.

**Име**: Storeouts_types_getlist
**Категория**: Store


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
StoreOutTypeData_                                                      
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

StoreOutTypeData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Тип на `изписването </barsy.help/210-dictionary/storeout.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: StoreOutTypeData

   * - Параметър
     - Тип
     - Описание
   * - **$type_id**
     - *int*
     - Id на типа
   * - **$name**
     - *string*
     - Име на типа
   * - **$color**
     - *string*
     - Цвят на тип в hex (използва се в списъците)
   * - **$delete_flag**
     - *int*
     - Флаг дали е маркиран като изтрит

			* **0** - *Активен*
			* **1** - *изтрит*

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

     .. literalinclude:: ../../sources/storeouts_types_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storeouts_types_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storeouts_types_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storeouts_types_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storeouts_types_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storeouts_types_getlist/barsy_api_client_simple.php
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

