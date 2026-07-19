.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Persons_gettype
===========================================================
Данни за тип представител

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/person </barsy.help/210-dictionary/person.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща данни за конкретен тип `представител </barsy.help/210-dictionary/person.html>`__ — основни параметри (име, описание, дали е активен) и опционално (`extra_properties=["lines"]`) списък с дефинираните динамични полета за този тип (име, тип данни, задължителност, валидации). Различните типове `представители </barsy.help/210-dictionary/person.html>`__ имат различни набори от полета — например "Шофьор" има поле "`Категория </barsy.help/210-dictionary/category.html>`__ книжка", докато "Управител" има "ЕГН".

Типични случаи: динамично изграждане на форма за нов `представител </barsy.help/210-dictionary/person.html>`__ според избрания тип, валидация на входни данни в интеграция, синхронизация на структурата на типовете към външна система.

**Име**: Persons_gettype
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
   * - **$type_id**
     - *int*
     - 
   * - **$extra_properties**
     - *array*
     - @value=["lines":"наличните полета за дадения тип"] **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*object* | *bool*                                                      
====================================================================== ======================================================================

----
 
Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/persons_gettype/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/persons_gettype/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/persons_gettype/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/persons_gettype/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/persons_gettype/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/persons_gettype/barsy_api_client_simple.php
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

