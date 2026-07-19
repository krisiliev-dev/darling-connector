.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Persons_getlist
===========================================================
Списък с представители

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/person </barsy.help/210-dictionary/person.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с `представители </barsy.help/210-dictionary/person.html>`__ на `клиенти </barsy.help/210-dictionary/client.html>`__ с филтри — по `клиент </barsy.help/210-dictionary/client.html>`__, тип `представител </barsy.help/210-dictionary/person.html>`__, име, статус. Поддържа странициране и допълнителни секции. По подразбиране се връща съкратена ("short") форма с ключови полета за бърз листинг — пълните детайли се извличат поименно през `Persons_get`.

Типични случаи: dropdown за избор на `представител </barsy.help/210-dictionary/person.html>`__ при отваряне на `сметка </barsy.help/210-dictionary/account.html>`__ на корпоративен `клиент </barsy.help/210-dictionary/client.html>`__, експорт на всички контактни лица на VIP `клиенти </barsy.help/210-dictionary/client.html>`__, синхронизация към външна CRM, преглед на упълномощените лица за конкретен B2B `клиент </barsy.help/210-dictionary/client.html>`__.

**Име**: Persons_getlist
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
     - PersonsListFiltersData_ 
     - 
   * - **$extra_properties**
     - PersonsExtraPropertiesData_ 
     - 
   * - **$offset**
     - *int*
     -  **По подразбиране:** 0
   * - **$length**
     - *int*
     -  **По подразбиране:** 100


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PersonsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PersonsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$client_id**
     - *int*
     - Филтър по ID на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$person_id**
     - *int*
     - Филтър по ID на представиртел
   * - **$person_name**
     - *string*
     - Филтър по име на `представител </barsy.help/210-dictionary/person.html>`__
   * - **$type_id**
     - *int*
     - Филтър по ID на тип на представиртел
   * - **$info_value**
     - *string*
     - Филтър по допълнителни данни на `представител </barsy.help/210-dictionary/person.html>`__
   * - **$delete_flag**
     - *int*
     - Филтър по флаг за изтрит на `представител </barsy.help/210-dictionary/person.html>`__ **По подразбиране:** 0
   * - **$last_update**
     - *string*
     - Филтър по последна актуализация

-----

PersonsExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PersonsExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$has_person_code**
     - *bool*
     - Ако е подадено, се връща флаг, който е 1 или 0 и показва дали ИМА или НЯМА код на карта **По подразбиране:** false
   * - **$person_code**
     - *bool*
     - Ако е подадено, се връща самия код на картата, ако `потребителя </barsy.help/210-dictionary/user.html>`__ има право да редактира `представители </barsy.help/210-dictionary/person.html>`__ **По подразбиране:** false
   * - **$person_create_date**
     - *bool*
     - Ако е подадено, се връща датата на създаване на `представителя </barsy.help/210-dictionary/person.html>`__ **По подразбиране:** false
   * - **$short_info**
     - *bool*
     - Казва дали да върне само ключа и стойноста на допълнителните данни към `представител </barsy.help/210-dictionary/person.html>`__ **По подразбиране:** false
   * - **$detailed_info**
     - *bool*
     - Казва дали да върне подробна информация за допълнителните данни към типът `представител </barsy.help/210-dictionary/person.html>`__ **По подразбиране:** false

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

     .. literalinclude:: ../../sources/persons_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/persons_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/persons_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/persons_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/persons_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/persons_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Представител </barsy.help/210-dictionary/person.html>`__


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

