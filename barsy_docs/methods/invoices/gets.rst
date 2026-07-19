.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Invoices_gets
===========================================================
Преглед на множество фактури

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/invoice </barsy.help/210-dictionary/invoice.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Batch версия на `Invoices_get` — приема масив от ID-та на `фактури </barsy.help/210-dictionary/invoice.html>`__ и връща обект, в който за всеки ID е разположен пълният запис на съответната `фактура </barsy.help/210-dictionary/invoice.html>`__. Удобно за интеграции, при които трябва да се изтеглят данните за няколко документа едновременно, без N+1 заявки.

Типични случаи: експорт на пакет от `фактури </barsy.help/210-dictionary/invoice.html>`__ към счетоводен софтуер с една заявка, печат на дневник с `фактури </barsy.help/210-dictionary/invoice.html>`__ за период, синхронизация на множество документи към ERP.

**Име**: Invoices_gets
**Категория**: Documents


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$inv_ids**
     - *array*
     - Списък от ID-та на `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$copy**
     - *int*
     - Казва дали ще покажем Оригинал(0), Копие(1) или Оригинал+Копие(-1), ползва се вътрешно **По подразбиране:** 0


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                Подробни данни за всяка фактура
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

     .. literalinclude:: ../../sources/invoices_gets/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/invoices_gets/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/invoices_gets/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/invoices_gets/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/invoices_gets/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/invoices_gets/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Фактура </barsy.help/210-dictionary/invoice.html>`__


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

