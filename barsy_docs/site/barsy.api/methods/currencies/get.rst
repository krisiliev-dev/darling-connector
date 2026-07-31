.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Currencies_get
===========================================================
Подробни данни за валута

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*Връща пълен запис за една валута по нейното ID — код (BGN, EUR, USD и др.), име, знак/символ, текущ обменен курс към системната валута, точност на десетичните знаци, стратегия за закръгляване, флаг за активност и дали е вторична/текуща валута. Изтрити валути не се връщат — при опит за достъп се връща грешка.*

Типични случаи: `зареждане </barsy.help/210-dictionary/storeload.html>`__ на валутни настройки при отваряне на `сметка </barsy.help/210-dictionary/account.html>`__ в чужда валута, проверка на актуален обменен курс преди `плащане </barsy.help/210-dictionary/payment.html>`__, синхронизация на валутен каталог към външна система.

**Име**: Currencies_get
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
   * - **$currency_id**
     - *int*
     - ID на валутата


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
CurrencyData_                                                          
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

CurrencyData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CurrencyData

   * - Параметър
     - Тип
     - Описание
   * - **$currency_id**
     - *int*
     - 
   * - **$currency_name**
     - *string*
     - 
   * - **$currency_code**
     - *string*
     - 
   * - **$currency_rate**
     - *float*
     - 
   * - **$currency_code_num**
     - *int*
     - 
   * - **$currency_suffix**
     - *string*
     - 
   * - **$currency_suffix_display**
     - *string*
     - 
   * - **$currency_prefix**
     - *string*
     - 
   * - **$delete_flag**
     - *int*
     -  **По подразбиране:** 0
   * - **$weight**
     - *int*
     -  **По подразбиране:** 1
   * - **$rounding_strategy**
     - *string*
     - 
   * - **$is_secondary**
     - *int*
     - 
   * - **$currency_settings**
     - *object*
     - 
   * - **$is_current**
     - *int*
     -  **По подразбиране:** 0

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

     .. literalinclude:: ../../sources/currencies_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/currencies_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/currencies_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/currencies_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/currencies_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/currencies_get/barsy_api_client_simple.php
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

