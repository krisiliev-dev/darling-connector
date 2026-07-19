.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Packages_edit
===========================================================
Запис на разфасовка

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Създава или редактира разфасовка (package) — предефинирано количество на `артикул </barsy.help/210-dictionary/article.html>`__ за по-бързо въвеждане при зареждания и `продажби </barsy.help/210-dictionary/sale.html>`__. Например за бутилки бира: разфасовка "`Каса </barsy.help/210-dictionary/pos.html>`__ 24бр" = 24, "Стек 6бр" = 6. Разфасовката съдържа име, количество, тежест за подреждане в UI, описание и тип на закръгление при изчисляване (нагоре/надолу/няма). `Артикулите </barsy.help/210-dictionary/article.html>`__ могат да имат разфасовка по подразбиране.

*Типични случаи: дефиниране на стандартни търговски единици в магазин на едро, конфигуриране на палетни разфасовки за складова работа, добавяне на сезонна разфасовка (напр. "Великденски пакет 4бр").*

**Име**: Packages_edit
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
   * - **$action_type**
     - *string*
     - Тип на върнатите данни [content=структура,values=стойности,save=запис,delete=изтриване] **По подразбиране:** 'content'
   * - **$id**
     - *int*
     - ID на обекта, който се обработва
   * - **$values**
     - *array*
     - Стойности за запис (при $action_type=save)
   * - **$active_struct_id**
     - *int*
     - ID на активната структура


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PackagesEditResultData_                                                
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PackagesEditFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

-----

PackagesEditResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: PackagesEditResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$package_id**
     - *int*
     - *ID*
   * - **$package_name**
     - *string*
     - *Име на разфасовката*
   * - **$package_ratio**
     - *string*
     - Какво количество от `артикула </barsy.help/210-dictionary/article.html>`__ съдържа разфасовката
   * - **$description**
     - *string*
     - *Описание на разфасовката*
   * - **$package_weight**
     - *int*
     - *Тежест за подреждане на разфасовките*
   * - **$round_amount**
     - *string*
     - *Закръгляне на количеството до цяла разфасовка*
   * - **$delete_flag**
     - *string*
     - *Блокира записа за използване в системата*

-----

PackagesEditResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PackagesEditResultData

   * - Параметър
     - Тип
     - Описание
   * - **$page_num**
     - *int*
     - Номер на текуща страница
   * - **$total**
     - *int*
     - Общ брой страници
   * - **$records**
     - *int*
     - Общ брой записи
   * - **$rows**
     - PackagesEditResultRowData_ []
     - Полета на всеки ред от списъка
   * - **$totals**
     - 
     - 
   * - **$filters_resume**
     - *array*
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

     .. literalinclude:: ../../sources/packages_edit/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/packages_edit/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/packages_edit/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/packages_edit/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/packages_edit/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/packages_edit/barsy_api_client_simple.php
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

