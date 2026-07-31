.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Edocs_get_by_sid
===========================================================
eDoc по SID

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*Връща данни за електронен документ, намерен по неговия публичен SID (signed ID). Изисква специално ниво на достъп (SU — система-към-система). Удобно за достъп от външни системи, които пазят само публичните идентификатори на документите без вътрешни ID-та.*

*Типични случаи: synchronization layer между две Barsy инсталации, fetch на документ от counter-party системно ниво, audit log в централизирана reporting платформа.*

**Име**: Edocs_get_by_sid
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
   * - **$doc_sid**
     - *string*
     - SID на документа


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
eDocData_                                                              Обект от данни за документ
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

eDocData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: eDocData

   * - Параметър
     - Тип
     - Описание
   * - **$discount**
     - *float*
     - Обща отстъпка за `сметка </barsy.help/210-dictionary/account.html>`__ в проценти (отрицателна стойност -> отстъпка, положителна -> надценка)
   * - **$paymethod_id**
     - *int*
     - ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$client_name**
     - *string*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__, асоциран с документа
   * - **$description**
     - *string*
     - Описание на документа - свободен текст
   * - **$orders**
     - eDocOrderData_ 
     - Списък от `поръчки към сметка </barsy.help/210-dictionary/account-order.html>`__
   * - **$status**
     - *string*
     - Текущ статус на документа
   * - **$type**
     - *string*
     - Тип на документа
   * - **$doc_id**
     - *int*
     - ID на документ
   * - **$date**
     - *datetime*
     - Датата на която е създаден документа
   * - **$total**
     - *float*
     - Обща сума за `сметка </barsy.help/210-dictionary/account.html>`__

-----

eDocOrderData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: eDocOrderData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *string*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$current_price**
     - *float*
     - Цена, на която се извършена операцията
   * - **$amount_type_name_short**
     - *string*
     - Кратко име на тип количество ( виж: :doc:`../amounttypes/getlist` )
   * - **$amount**
     - *float*
     - Количество, което е включено в операцията
   * - **$lot_value**
     - *string*
     - Партида на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$lot_exp_date**
     - *string*
     - Партида дата - срок на годност
   * - **$rs_tax_id**
     - *int*
     - ID на ДДС-то на отдалечената система, от която получаваме данните

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

     .. literalinclude:: ../../sources/edocs_get_by_sid/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/edocs_get_by_sid/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/edocs_get_by_sid/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/edocs_get_by_sid/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/edocs_get_by_sid/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/edocs_get_by_sid/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

