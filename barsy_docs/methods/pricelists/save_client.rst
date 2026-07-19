.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Pricelists_save_client
===========================================================
Добавяне на клиент към правило

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pricelist </barsy.help/210-dictionary/pricelist.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Бързо добавя един `клиент </barsy.help/210-dictionary/client.html>`__ към обхвата на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ — удобен endpoint за инкрементално включване от UI без необходимост от презаписване на пълния списък. След добавянето `клиентът </barsy.help/210-dictionary/client.html>`__ получава специалните цени, дефинирани от правилото, при следващите си покупки. За масово добавяне на много `клиенти </barsy.help/210-dictionary/client.html>`__ наведнъж виж `Pricelists_save_clients`.

Типични случаи: добавяне на нов VIP `клиент </barsy.help/210-dictionary/client.html>`__ към съществуваща B2B ценова листа, ad-hoc включване на корпоративен партньор в специална промоция, бързо разширяване от CRM workflow.

**Име**: Pricelists_save_client
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
     - ID на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$client_id**
     - *int*
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*void*                                                                 
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

     .. literalinclude:: ../../sources/pricelists_save_client/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/pricelists_save_client/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/pricelists_save_client/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/pricelists_save_client/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/pricelists_save_client/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/pricelists_save_client/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Клиент </barsy.help/210-dictionary/client.html>`__


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

