.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Clientorders_getstatuslistdata
===========================================================
Налични статуси на заявки

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/client-order </barsy.help/210-dictionary/client-order.html>`__
	 * barsy.help: `110-admin/160-pos/client-orders/index </barsy.help/110-admin/160-pos/client-orders/index.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълния списък с конфигурираните в системата статуси на `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__ — ID, име, цветово оформление, флагове за крайни статуси (приключена/отказана), статус по подразбиране за нова заявка. Списъкът отразява и custom статуси, добавени към конкретна инсталация (например "Чака потвърждение от `клиент </barsy.help/210-dictionary/client.html>`__", "Изпратена с куриер X"). Не отчита персонални права — допустимостта на конкретен преход за дадена заявка/`роля </barsy.help/210-dictionary/role.html>`__ се проверява при `Clientorders_setstatus`.

*Типични случаи: попълване на dropdown за смяна на статус, конфигуриране на филтри в листинг екран, изграждане на kanban-табло със статусни колони, легенда в куриерско приложение.*

**Име**: Clientorders_getstatuslistdata
**Категория**: Cashdesk


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ClientOrderStatus_                                                     
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ClientOrderStatus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientOrderStatus

   * - Параметър
     - Тип
     - Описание
   * - **$status_id**
     - *int*
     - ID на статус
   * - **$status_name**
     - *string*
     - Име на статус
   * - **$delete_flag**
     - *int*
     - Флаг за изтрит статус
   * - **$color**
     - *string*
     - Настройка за цвят на статус в списъци
   * - **$ask_for_barsy**
     - *int*
     - Настройка за питане за обработващ `търговски обект </barsy.help/210-dictionary/barsy.html>`__ при назначаване на статус

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

     .. literalinclude:: ../../sources/clientorders_getstatuslistdata/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/clientorders_getstatuslistdata/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/clientorders_getstatuslistdata/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/clientorders_getstatuslistdata/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/clientorders_getstatuslistdata/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/clientorders_getstatuslistdata/barsy_api_client_simple.php
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

