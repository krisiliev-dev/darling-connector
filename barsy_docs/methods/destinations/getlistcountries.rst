.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Destinations_getlistcountries
===========================================================
Списък с държави

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*Връща списък с поддържаните в системата държави — ID, ISO код (BG, DE, GB, ...), име на държавата, флаг за членство в ЕС, валута по подразбиране, телефонен код. Държавите се ползват за конфигуриране на адреси за доставка, регулаторни различия в данъчните регионни, дефиниране на територии за маркетинг.*

Типични случаи: попълване на dropdown "Държава" при адрес за доставка, конфигуриране на държави в `ценови правила </barsy.help/210-dictionary/pricelist.html>`__ за международна търговия, синхронизация на ISO кодове към външни системи.

**Име**: Destinations_getlistcountries
**Категория**: Misc


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
     - CountriesFiltersData_ 
     - Налични филтри


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
CountryData_                                                           
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

CountriesFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CountriesFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$country_name**
     - *string*
     - Филтър по име на страна
   * - **$country_id**
     - *string*
     - Филтър по двубуквен код на страна
   * - **$country_code_3**
     - *string*
     - Филтър по трибуквен код на страна
   * - **$has_delivery**
     - *int*
     - Доставя се до тази страна
   * - **$with_tax_groups_only**
     - *int*
     - Филтър по страни с познати за нас ДДС групи

-----

CountryData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CountryData

   * - Параметър
     - Тип
     - Описание
   * - **$country_id**
     - *int*
     - ID на държавата
   * - **$country_name**
     - *string*
     - Име на държавата
   * - **$country_code_3**
     - *string*
     - Кратък код на държавата (3 букви)

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

     .. literalinclude:: ../../sources/destinations_getlistcountries/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/destinations_getlistcountries/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/destinations_getlistcountries/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/destinations_getlistcountries/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/destinations_getlistcountries/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/destinations_getlistcountries/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

