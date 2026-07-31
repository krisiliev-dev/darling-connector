.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Documents_get
===========================================================
Подробни данни за документ

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълния запис на един документ по неговото ID — основни полета (тип, статус, `клиент </barsy.help/210-dictionary/client.html>`__, дати, текст, отговорник, номер, сделка). Допълнителните опции, специфични за типа документ (`оферта </barsy.help/210-dictionary/offer.html>`__, договор и др.), се включват като отделни полета в отговора. С `extra_properties` може да се поискат групи, артикулни редове и агрегирани суми. Достъпът се проверява според типа на документа (`document_{type}_view`).

Типични случаи: `зареждане </barsy.help/210-dictionary/storeload.html>`__ на текст на шаблон в редактор, интеграция за преглед на `оферта </barsy.help/210-dictionary/offer.html>`__/договор, извличане на редове и суми за външна система.

**Име**: Documents_get
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
   * - **$document_id**
     - *int*
     - ID на документа @test_value 1
   * - **$extra_properties**
     - DocumentsGetExtraPropertiesData_ 
     - Допълнителни данни (групи, редове, суми)


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
DocumentData_ | *object*                                               Данни за документа; може да съдържа и полета от document_options
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

DocumentsGetExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Допълнителни данни към Documents_get (групи, редове, суми).

.. list-table::
   :header-rows: 1
   :align: center
   :name: DocumentsGetExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$groups**
     - *bool*
     - Групи на документа **По подразбиране:** false
   * - **$details**
     - *bool*
     - Редове (`артикули </barsy.help/210-dictionary/article.html>`__) на документа **По подразбиране:** false
   * - **$totals**
     - *bool*
     - Агрегирани суми за документа **По подразбиране:** false

-----

DocumentData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за един документ (`оферта </barsy.help/210-dictionary/offer.html>`__, договор, протокол, гаранция и др.)

.. list-table::
   :header-rows: 1
   :align: center
   :name: DocumentData

   * - Параметър
     - Тип
     - Описание
   * - **$document_id**
     - *int*
     - ID на документа
   * - **$doc_type_id**
     - *int*
     - ID на типа документ ( виж: :doc:`../documents/gettypes` )
   * - **$doc_type_name**
     - *string*
     - Системно име на типа документ
   * - **$barsy_id**
     - *int*
     - ID на търговския обект.

			При `extra_properties.barsy_id` ( виж: :doc:`../barsys/getlist` )
   * - **$user_id**
     - *int*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа ( виж: :doc:`../users/getlist` )
   * - **$user_name**
     - *string*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа
   * - **$create_date**
     - *string*
     - Дата на създаване
   * - **$ref_date**
     - *string*
     - Вальор (дата на документа)
   * - **$update_date**
     - *string*
     - Дата на последна промяна
   * - **$text**
     - *string*
     - Текст или шаблон на документа.

			При `extra_properties.text`
   * - **$status_id**
     - *int*
     - ID на статуса на документа
   * - **$status_name**
     - *string*
     - Име на статуса на документа
   * - **$is_template**
     - *int*
     - Флаг дали записът е шаблон (0 или 1)
   * - **$document_name**
     - *string*
     - Име на документа
   * - **$document_sid**
     - *string*
     - SID на документа.

			При `extra_properties.document_sid`
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__.

			При `extra_properties.client_id` ( виж: :doc:`../clients/getlist` )
   * - **$client_name**
     - *string*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__.

			При `extra_properties.client_name`
   * - **$description**
     - *string*
     - Бележки към документа.

			При `extra_properties.description`
   * - **$parent_id**
     - *int*
     - ID на родителски документ.

			При `extra_properties.parent_id` ( виж: :doc:`../documents/get` )
   * - **$document_options**
     - *string*
     - Допълнителни опции на документа.

			При `extra_properties.document_options`
   * - **$owner_id**
     - *int*
     - ID на отговорника.

			При `extra_properties.owner_id` ( виж: :doc:`../users/getlist` )
   * - **$owner_name**
     - *string*
     - Име на отговорника.

			При `extra_properties.owner_name`
   * - **$delete_flag**
     - *int*
     - Флаг дали документът е изтрит (0 или 1)
   * - **$doc_num**
     - *string*
     - Номер на документа.

			При `extra_properties.doc_num`
   * - **$deal_id**
     - *int*
     - ID на сделка.

			При `extra_properties.deal_id` ( виж: :doc:`../deals/getlist` )
   * - **$deal_title**
     - *string*
     - Заглавие на сделката.

			При `extra_properties.deal_title`
   * - **$email**
     - *string*
     - Имейл на `клиента </barsy.help/210-dictionary/client.html>`__.

			При `extra_properties.email`
   * - **$currency_id**
     - *int*
     - ID на валутата на документа.

			При `extra_properties.currency_id`
   * - **$currency_rate**
     - *float*
     - Курс на валутата на документа.

			При `extra_properties.currency_rate`
   * - **$template_ref_id**
     - *int*
     - ID на шаблона, от който е създаден документът.

			При `extra_properties.template_ref_id` ( виж: :doc:`../documents/get` )
   * - **$lines_count**
     - *int*
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в документа.

			При `extra_properties.lines_count`
   * - **$total_amount**
     - *float*
     - Обща сума на редовете без документна отстъпка.

			При `extra_properties.total_amount`
   * - **$total_with_discount**
     - *float*
     - Обща сума след документна отстъпка или надценка.

			При `extra_properties.total_with_discount`
   * - **$resolution_status**
     - *int*
     - Резултат на `оферта </barsy.help/210-dictionary/offer.html>`__: 0=няма, 1=приета, 2=отхвърлена, 3=преработена.

			При `extra_properties.resolution_status`
   * - **$send_date**
     - *string*
     - Дата на изпращане на `оферта </barsy.help/210-dictionary/offer.html>`__.

			При `extra_properties.send_date`
   * - **$call_date**
     - *string*
     - Дата на прозвъняване на `оферта </barsy.help/210-dictionary/offer.html>`__.

			При `extra_properties.call_date`
   * - **$discount**
     - *float*
     - Отстъпка или надценка на документа в %.

			При `extra_properties.discount` или при преглед на един документ
   * - **$caparo**
     - *float*
     - Предплащане в %.

			При `extra_properties.caparo` или при преглед на един документ
   * - **$caparo_fixed**
     - *float*
     - Капаро във валута.

			При `extra_properties.caparo_fixed` или при преглед на един документ

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

     .. literalinclude:: ../../sources/documents_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/documents_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/documents_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/documents_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/documents_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/documents_get/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

