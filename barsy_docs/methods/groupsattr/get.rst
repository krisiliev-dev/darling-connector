.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Groupsattr_get
===========================================================
Подробни данни за група атрибути

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/100-catalog/articles/attribute-groups </barsy.help/110-admin/100-catalog/articles/attribute-groups.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълни данни за конкретна група атрибути (groupsattr) — механизмът, чрез който в Barsy се изграждат вариации на `артикул </barsy.help/210-dictionary/article.html>`__. Група атрибути дефинира измерения (например за дрехи: "Размер", "Цвят") със списък от възможни стойности (S/M/L/XL, червено/синьо/зелено). Един "основен" `артикул </barsy.help/210-dictionary/article.html>`__ свързан с такава група автоматично получава вариации, всяка с уникална комбинация от стойности (тениска S червена, тениска S синя, ...).

*Типични случаи: визуализиране на dropdown в продуктова страница "Изберете размер/цвят", редакция на стойностите на група атрибути (добавяне на нов цвят), синхронизация към PIM система.*

**Име**: Groupsattr_get
**Категория**: Catalog


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$group_id**
     - *int*
     - ID на желаната група атрибути
   * - **$extra_properties**
     - GroupsattrExtraPropertiesData_ 
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
GroupsattrData_                                                        Обект с основните и динамичните данни за групата атрибути
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

GroupsattrExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: GroupsattrExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$attributes**
     - *bool*
     - Ако е подадено, се връща информация за атрибутите на групата **По подразбиране:** false
   * - **$description**
     - *bool*
     - Ако е подадено, се връща информация за описанието на групата **По подразбиране:** false
   * - **$weight**
     - *bool*
     - Ако е подадено, се връща информация за теглото (WEIGHT) на групата **По подразбиране:** false
   * - **$create_date**
     - *bool*
     - Ако е подадено, се връща информация за датата на създаване на групата **По подразбиране:** false
   * - **$last_update**
     - *bool*
     - Ако е подадено, се връща информация за датата на последна промяна **По подразбиране:** false
   * - **$own_group**
     - *bool*
     - Ако е подадено, се връща информация за флага OWN_GROUP **По подразбиране:** false
   * - **$article_id**
     - *int*
     - Ако е подадено, се връща и информация за възможните атрибути за посочения `артикул </barsy.help/210-dictionary/article.html>`__

-----

GroupsattrData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за група атрибути

.. list-table::
   :header-rows: 1
   :align: center
   :name: GroupsattrData

   * - Параметър
     - Тип
     - Описание
   * - **$group_id**
     - *int*
     - ID на групата атрибути
   * - **$group_name**
     - *string*
     - Име на групата атрибути
   * - **$description**
     - *string*
     - Описание на групата атрибути
   * - **$weight**
     - *int*
     - Тегло на групата атрибути
   * - **$create_date**
     - *string*
     - Дата на създаване на групата атрибути
   * - **$last_update**
     - *string*
     - Дата на последна промяна на групата атрибути
   * - **$own_group**
     - *int*
     - Флаг за собствена група атрибути
   * - **$attributes**
     - *array*
     - Атрибути на групата атрибути

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

     .. literalinclude:: ../../sources/groupsattr_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/groupsattr_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/groupsattr_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/groupsattr_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/groupsattr_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/groupsattr_get/barsy_api_client_simple.php
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

