.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Packages_getlist
===========================================================
Списък с разфасовки

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с дефинираните разфасовки в системата — предефинирани количества (например „`Каса </barsy.help/210-dictionary/pos.html>`__ 24бр“, „Стек 6бр“), използвани за бързо въвеждане при складови зареждания и продажби. За всяка разфасовка се връща име, количество, тежест за подреждане, описание и флаг за изтрита. По подразбиране връща само активни разфасовки. Поддържа филтри, странициране и подреждане.

Типични случаи: попълване на dropdown „Разфасовка“ при продажба или `зареждане </barsy.help/210-dictionary/storeload.html>`__, синхронизация на стандартни търговски единици към външна система, листинг на разфасовките в админ панела.

**Име**: Packages_getlist
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
     - PackagesListFiltersData_ 
     - Налични филтри за списъка с разфасовки
   * - **$extra_properties**
     - PackagesListExtraPropertiesData_ 
     - Искане на допълнителни данни за всяка разфасовка
   * - **$offset**
     - *int*
     - Номер на ред, от който да започне списъкът (странициране) **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - *array*
     - Подреждане — асоциативен масив колона⇒посока (напр. {"package_name":"asc"}) **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PackageData_                                                           Списък с разфасовки с данни според исканите ($extra_properties)
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PackagesListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PackagesListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$package_id**
     - *int*
     - Филтър по ID на разфасовка ( виж: :doc:`../packages/get` )
   * - **$package_name**
     - *string*
     - Филтър по име на разфасовка.

			*Намира и при частично съвпадение*
   * - **$delete_flag**
     - *int*
     - Филтър по флаг за изтрита разфасовка.

			*Стойност -1 премахва филтъра* **По подразбиране:** 0

-----

PackagesListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към разфасовка от списъка. Всяка опция включва съответната колона към
		*данните за всеки запис. Основните данни се връщат винаги, останалите при стойност true.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: PackagesListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$package_id**
     - *bool*
     - ID на разфасовката ( виж: :doc:`../packages/get` ) **По подразбиране:** true
   * - **$package_name**
     - *bool*
     - Име на разфасовката **По подразбиране:** true
   * - **$package_name_title**
     - *bool*
     - Име на разфасовката с количество (напр. „`Каса </barsy.help/210-dictionary/pos.html>`__ (x12)“) **По подразбиране:** true
   * - **$package_ratio**
     - *bool*
     - Количество `артикул </barsy.help/210-dictionary/article.html>`__ в една разфасовка **По подразбиране:** true
   * - **$package_weight**
     - *bool*
     - Тежест за подреждане в списъци **По подразбиране:** true
   * - **$description**
     - *bool*
     - Описание на разфасовката **По подразбиране:** false
   * - **$delete_flag**
     - *bool*
     - Флаг за изтрита разфасовка **По подразбиране:** true
   * - **$round_amount**
     - *bool*
     - Тип закръгляне при изчисляване на количество **По подразбиране:** true

-----

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

     .. literalinclude:: ../../sources/packages_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/packages_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/packages_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/packages_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/packages_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/packages_getlist/barsy_api_client_simple.php
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

