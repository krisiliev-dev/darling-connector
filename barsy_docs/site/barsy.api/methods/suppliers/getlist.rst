.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Suppliers_getlist
===========================================================
Списък с доставчици

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/supplier </barsy.help/210-dictionary/supplier.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с регистрираните в системата `доставчици </barsy.help/210-dictionary/supplier.html>`__ с филтри по име, ЕИК, ДДС номер, група. Чрез `extra_properties` могат да се поискат допълнителни секции — бележки, статус (активен/изтрит), фирмени идентификатори, МОЛ, адрес, контактни лица, email. Резултатът се ползва за избор при ново складово `зареждане </barsy.help/210-dictionary/storeload.html>`__, за асоцииране с `артикули </barsy.help/210-dictionary/article.html>`__, за справки и експорти.

Типични случаи: попълване на dropdown "`Доставчик </barsy.help/210-dictionary/supplier.html>`__" при ново `зареждане </barsy.help/210-dictionary/storeload.html>`__, експорт за счетоводно осчетоводяване, идентификация по ЕИК при автоматичен импорт на `фактура </barsy.help/210-dictionary/invoice.html>`__, проверка дали даден `доставчик </barsy.help/210-dictionary/supplier.html>`__ вече съществува.

**Име**: Suppliers_getlist
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
   * - **$extra_properties**
     - *array*
     - Допълнителни данни към `доставчик </barsy.help/210-dictionary/supplier.html>`__

			* **min** - *Базова информация*
			* **notes** - *Белецка*
			* **delete_flag** - *Флаг за изтрит (0 - акривен, 1 - изтрит)*
			* **bulstat** - *Булстат*
			* **vat_num** - *Данъчен номер*
			* **mol** - *МОЛ*
			* **address** - *Адрес*
			* **contact_persons** - *Лице за контакт*
			* **email** - *Имейл* **По подразбиране:** []
   * - **$filters**
     - *array*
     -  **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                
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

     .. literalinclude:: ../../sources/suppliers_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/suppliers_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/suppliers_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/suppliers_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/suppliers_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/suppliers_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Доставчик </barsy.help/210-dictionary/supplier.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

