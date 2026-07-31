.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Packages_get
===========================================================
Подробни данни за разфасовка

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълен запис за една разфасовка по нейното ID — име, количество `артикул </barsy.help/210-dictionary/article.html>`__ в разфасовката, тежест за подреждане, описание, тип закръгляне при изчисляване и флаг за изтрита разфасовка. Изтрити разфасовки не се връщат — при опит за достъп се връща грешка.

Типични случаи: `зареждане </barsy.help/210-dictionary/storeload.html>`__ на разфасовка при редакция на `артикул </barsy.help/210-dictionary/article.html>`__, проверка на количество при складово `зареждане </barsy.help/210-dictionary/storeload.html>`__, синхронизация на каталог с разфасовки към външна система.

**Име**: Packages_get
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
   * - **$package_id**
     - *int*
     - ID на разфасовката


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PackageData_                                                           
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PackageData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PackageData

   * - Параметър
     - Тип
     - Описание
   * - **$package_id**
     - *int*
     - ID на разфасовката ( виж: :doc:`../packages/get` )
   * - **$package_name**
     - *string*
     - Име на разфасовката
   * - **$package_name_title**
     - *string*
     - Име на разфасовката с количество (напр. „`Каса </barsy.help/210-dictionary/pos.html>`__ (x12)“)
   * - **$package_ratio**
     - *string*
     - Количество `артикул </barsy.help/210-dictionary/article.html>`__ в една разфасовка
   * - **$package_weight**
     - *int*
     - Тежест за подреждане в списъци
   * - **$description**
     - *string*
     - Описание на разфасовката
   * - **$delete_flag**
     - *int*
     - Флаг за изтрита разфасовка
   * - **$round_amount**
     - *int*
     - Тип закръгляне при изчисляване на количество (0 — няма, 1 — до цяла разфасовка и др.)

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

     .. literalinclude:: ../../sources/packages_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/packages_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/packages_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/packages_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/packages_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/packages_get/barsy_api_client_simple.php
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

