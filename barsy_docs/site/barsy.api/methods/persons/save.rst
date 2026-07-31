.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Persons_save
===========================================================
Запис на представител

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/person </barsy.help/210-dictionary/person.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Универсален upsert на `представител </barsy.help/210-dictionary/person.html>`__ — ако подаден `id` отсъства, създава нов `представител </barsy.help/210-dictionary/person.html>`__; ако е подаден, актуализира съществуващия. Записват се основни данни (име, тип, връзка с `клиент </barsy.help/210-dictionary/client.html>`__) и динамични атрибути според типа на `представителя </barsy.help/210-dictionary/person.html>`__ (мобилен телефон, длъжност, лична карта). Удобен endpoint за UI форми, които не правят разлика между нов и съществуващ запис.

Типични случаи: универсална форма "Запис на `представител </barsy.help/210-dictionary/person.html>`__" в админ панела, синхронизация на `представители </barsy.help/210-dictionary/person.html>`__ от външна CRM/HR система, мобилно приложение за регистрация на нов контакт от търговец на терен.

**Име**: Persons_save
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
   * - **$id**
     - *int*
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ (ако липсва - създава се нов)
   * - **$values**
     - PersonInputData_ 
     - Данни за `представителя </barsy.help/210-dictionary/person.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PersonInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PersonInputData

   * - Параметър
     - Тип
     - Описание
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
     - ID на типа на `представител </barsy.help/210-dictionary/person.html>`__ ( виж: ``*/`` ) **По подразбиране:** 1
   * - **$person_code**
     - *string*
     - Код на `представител </barsy.help/210-dictionary/person.html>`__.

			Използва се за индентификация на `представителя </barsy.help/210-dictionary/person.html>`__ чрез някакъв носител (например карта)
   * - **$delete_flag**
     - *int*
     - Флаг дали `представителя </barsy.help/210-dictionary/person.html>`__ е маркиран като изтрит **По подразбиране:** 0
   * - **$dynamic_input**
     - *object*
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

     .. literalinclude:: ../../sources/persons_save/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/persons_save/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/persons_save/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/persons_save/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/persons_save/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/persons_save/barsy_api_client_simple.php
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

