.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Pricelists_set_status
===========================================================
Активиране/деактивиране на правило

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pricelist </barsy.help/210-dictionary/pricelist.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Активира (`status=1`) или деактивира (`status=0`) дадено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__. Активирането прави правилото ефективно в системата според неговите времеви рамки и критерии — то ще започне да влияе върху `сметките </barsy.help/210-dictionary/account.html>`__ веднага щом съответства на контекста. Деактивирането спира действието без да изтрива конфигурацията — удобно за временно спиране и последващо реактивиране.

*Типични случаи: ръчно включване на сезонна промоция в определен ден, аварийно изключване на грешно конфигурирано правило, стартиране на промоция след нейната подготовка, временно спиране при ребрандиране.*

**Име**: Pricelists_set_status
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
   * - **$pricelist_id**
     - *int*
     - 
   * - **$status**
     - *int*
     - ID на желан сатус (1=активиране,0=деактивиране)


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PricelistStatusData_                                                   Информация за статуса на ценотовото правило
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PricelistStatusData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PricelistStatusData

   * - Параметър
     - Тип
     - Описание
   * - **$status_id**
     - *int*
     - ID на статус на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$status_name**
     - *string*
     - Име на статус на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__

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

     .. literalinclude:: ../../sources/pricelists_set_status/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/pricelists_set_status/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/pricelists_set_status/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/pricelists_set_status/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/pricelists_set_status/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/pricelists_set_status/barsy_api_client_simple.php
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

