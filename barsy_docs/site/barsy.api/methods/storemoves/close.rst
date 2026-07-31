.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Storemoves_close
===========================================================
Приключване на прехвърляне

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/150-store/20-storemoves/index </barsy.help/110-admin/150-store/20-storemoves/index.html>`__
	 * barsy.help: `210-dictionary/storemove </barsy.help/210-dictionary/storemove.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Финализира `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ между складове — количествата официално се отписват от източника и се завеждат в дестинацията, преизчислява се средно претеглена себестойност в приемащия `склад </barsy.help/210-dictionary/store.html>`__, регенерират се партиди (при партиден режим). След приключване документът става read-only. За двуетапни прехвърляния с инспекция приключването е възможно само след `confirm_move` от приемащия `склад </barsy.help/210-dictionary/store.html>`__.

Типични случаи: финализиране на ежедневно `зареждане </barsy.help/210-dictionary/storeload.html>`__ на обект, batch-приключване на одобрени междускладови движения, автоматично приключване от ERP интеграция след одобрение от двамата отговорни складови ръководители.

**Име**: Storemoves_close
**Категория**: Store


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
     - ID на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__


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

     .. literalinclude:: ../../sources/storemoves_close/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/storemoves_close/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/storemoves_close/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/storemoves_close/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/storemoves_close/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/storemoves_close/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__


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

