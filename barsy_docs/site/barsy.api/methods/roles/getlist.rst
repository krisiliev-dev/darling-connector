.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Roles_getlist
===========================================================
Списък с роли

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/role </barsy.help/210-dictionary/role.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с конфигурираните в системата потребителски `роли </barsy.help/210-dictionary/role.html>`__ (например "Касиер", "Сервитьор", "Управител", "Складов работник", "Куриер"). Всяка `роля </barsy.help/210-dictionary/role.html>`__ носи асоциирани права и определя какво `потребителят </barsy.help/210-dictionary/user.html>`__ може да прави в системата. Поддържа филтри за активност, тип, конкретен обект.

Типични случаи: попълване на dropdown "`Роля </barsy.help/210-dictionary/role.html>`__" при създаване/редакция на `потребител </barsy.help/210-dictionary/user.html>`__, изграждане на справки за `продажби </barsy.help/210-dictionary/sale.html>`__ по `роля </barsy.help/210-dictionary/role.html>`__, конфигуриране на нова `роля </barsy.help/210-dictionary/role.html>`__ със специфични права.

**Име**: Roles_getlist
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
   * - **$filters**
     - RolesListFiltersData_ 
     -  **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

RolesListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: RolesListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$role_id**
     - *int*
     - Филтър по ID на `роля </barsy.help/210-dictionary/role.html>`__
   * - **$role_name**
     - *string*
     - Филтър по име на `роля </barsy.help/210-dictionary/role.html>`__.
   * - **$role_weight**
     - *int*
     - Филтър по тежест на `роля </barsy.help/210-dictionary/role.html>`__
   * - **$delete_flag**
     - *int*
     - Филтър по флаг за изтрит
   * - **$parent_id**
     - *int*
     - Филтър по родител
   * - **$role_path**
     - *string*
     - Филтър по път на `роля </barsy.help/210-dictionary/role.html>`__.
   * - **$role_id_path**
     - *string*
     - Филтър по път на `роля </barsy.help/210-dictionary/role.html>`__.

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

     .. literalinclude:: ../../sources/roles_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/roles_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/roles_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/roles_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/roles_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/roles_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Роля </barsy.help/210-dictionary/role.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

