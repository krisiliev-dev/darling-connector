.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Persons_get
===========================================================
Подробни данни за представител

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/person </barsy.help/210-dictionary/person.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълен запис за един `представител </barsy.help/210-dictionary/person.html>`__ по неговото ID — основни данни (име, тип, връзка с `клиент </barsy.help/210-dictionary/client.html>`__), всички динамични полета според типа (телефон, длъжност, лични идентификатори, специални атрибути), история на промените. Параметърът `delete_check` контролира дали логически изтрити записи да се връщат. Чрез `extra_properties` могат да се изискат допълнителни секции като свързани документи или активности.

Типични случаи: визуализиране на профил на `представител </barsy.help/210-dictionary/person.html>`__ в админ панела, валидация преди операция от името на корпоративен `клиент </barsy.help/210-dictionary/client.html>`__, синхронизация на детайлни данни към външна CRM.

**Име**: Persons_get
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
   * - **$person_id**
     - *int*
     - ID на желания `представител </barsy.help/210-dictionary/person.html>`__
   * - **$delete_check**
     - *int*
     -  **По подразбиране:** 1
   * - **$extra_properties**
     - PersonsExtraPropertiesData_ 
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PersonData_                                                            Обект с основните и динамичните данни за представителя
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

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

PersonData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PersonData

   * - Параметър
     - Тип
     - Описание
   * - **$person_id**
     - *int*
     - ID на `представител </barsy.help/210-dictionary/person.html>`__
   * - **$person_name**
     - *string*
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, на който принадлежи `представителя </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../clients/getlist` )
   * - **$description**
     - *string*
     - Свободен текст
   * - **$type_id**
     - *int*
     - ID на типа на `представител </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../persons/gettypes` )
   * - **$person_code**
     - *string*
     - Флаг за наличие на записан код на `представител </barsy.help/210-dictionary/person.html>`__.

			Използва се за индентификация на `представителя </barsy.help/210-dictionary/person.html>`__ чрез някакъв носител (например карта). Не може да бъде извлечен в явен вид
   * - **$delete_flag**
     - *int*
     - Флаг дали `представителя </barsy.help/210-dictionary/person.html>`__ е маркиран като изтрит
   * - **$person_create_date**
     - *string*
     - Дата на създаване на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$last_update**
     - *string*
     - Дата на последна актуализация на данните на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$info**
     - *object*
     - Допълнителни динамични данни за `представителя </barsy.help/210-dictionary/person.html>`__ (според типа му) ( виж: :doc:`../persons/gettypes` )

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

     .. literalinclude:: ../../sources/persons_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/persons_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/persons_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/persons_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/persons_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/persons_get/barsy_api_client_simple.php
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

