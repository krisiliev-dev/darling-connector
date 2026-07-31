.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Pricelists_save_subscriptions
===========================================================
Абонаменти в ценово правило

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pricelist </barsy.help/210-dictionary/pricelist.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Записва списък с абонаментни планове, за които да важи дадено `ценово правило </barsy.help/210-dictionary/pricelist.html>`__. `Клиенти </barsy.help/210-dictionary/client.html>`__ с активен `абонамент </barsy.help/210-dictionary/subscription.html>`__ от избран план автоматично получават специалните цени за периода на `абонамента </barsy.help/210-dictionary/subscription.html>`__. Удобно за изграждане на стратегия "Subscribe & Save" — `клиентите </barsy.help/210-dictionary/client.html>`__ получават преференциални цени докато техния `абонамент </barsy.help/210-dictionary/subscription.html>`__ е валиден.

Типични случаи: 15% отстъпка за всички с активен Premium `абонамент </barsy.help/210-dictionary/subscription.html>`__, безплатна доставка за членове на лоялна програма, специални цени на ястия в ресторант за месечни `абонаменти </barsy.help/210-dictionary/subscription.html>`__.

**Име**: Pricelists_save_subscriptions
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
   * - **$rows**
     - PricelistSubscriptionData_ []
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  1
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PricelistSubscriptionData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PricelistSubscriptionData

   * - Параметър
     - Тип
     - Описание
   * - **$subscription_id**
     - *int*
     - ID на абонаментен план ( виж: :doc:`../subscriptions/getlist` )
   * - **$checked**
     - *int*
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

     .. literalinclude:: ../../sources/pricelists_save_subscriptions/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/pricelists_save_subscriptions/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/pricelists_save_subscriptions/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/pricelists_save_subscriptions/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/pricelists_save_subscriptions/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/pricelists_save_subscriptions/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Абонамент </barsy.help/210-dictionary/subscription.html>`__
 * `Ценово правило </barsy.help/210-dictionary/pricelist.html>`__


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

