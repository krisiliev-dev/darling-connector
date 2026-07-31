.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Documents_getlist
===========================================================
Списък с документи

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с документи от системата (`оферти </barsy.help/210-dictionary/offer.html>`__, договори, протоколи, гаранции и др.) с филтри по тип, статус, `клиент </barsy.help/210-dictionary/client.html>`__, период, `търговски обект </barsy.help/210-dictionary/barsy.html>`__ и др. Поддържа странициране, сортиране и `extra_properties` за обогатяване с допълнителни колони (`клиент </barsy.help/210-dictionary/client.html>`__, отговорник, сделка, шаблон и т.н.).

Типични случаи: интеграция за извличане на `оферти </barsy.help/210-dictionary/offer.html>`__ по `клиент </barsy.help/210-dictionary/client.html>`__ и период, попълване на dropdown с шаблони, синхронизация на документи към външна система, справки по статус и тип документ.

**Име**: Documents_getlist
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
   * - **$filters**
     - DocumentsListFiltersData_ 
     - Налични филтри за списъка с документи
   * - **$extra_properties**
     - DocumentsListExtraPropertiesData_ 
     - Искане на допълнителни данни за всеки документ
   * - **$offset**
     - *int*
     - Номер на ред, от който да започне списъкът (странициране) **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - DocumentsListOrderByData_ 
     - Подреждане — низ, масив или обект колона⇒посока (напр. {"update_date":"desc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
DocumentData_                                                          Списък с документи с данни според исканите ($extra_properties)
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

DocumentsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: DocumentsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$document_id**
     - *int*
     - Филтър по ID на документ ( виж: :doc:`../documents/get` )
   * - **$doc_type_id**
     - *int*
     - Филтър по тип документ ( виж: :doc:`../documents/gettypes` )
   * - **$deal_id**
     - *int*
     - Филтър по сделка ( виж: :doc:`../deals/getlist` )
   * - **$parent_id**
     - *int*
     - Филтър по родителски документ (версия/клон) ( виж: :doc:`../documents/get` )
   * - **$template_ref_id**
     - *int*
     - Филтър по шаблон, от който е създаден документът ( виж: :doc:`../documents/get` )
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$barsy_id**
     - *int*
     - Филтър по `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/get` , :doc:`../barsys/getlist` )
   * - **$user_id**
     - *int*
     - Филтър по `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа ( виж: :doc:`../users/get` , :doc:`../users/getlist` )
   * - **$owner_id**
     - *int*
     - Филтър по отговорник на документа ( виж: :doc:`../users/get` , :doc:`../users/getlist` )
   * - **$client_id**
     - *int*
     - Филтър по `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/get` , :doc:`../clients/getlist` )
   * - **$client_group_id**
     - *int* | *int*
     - Филтър по група на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clientgroups/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$doc_type_name**
     - *string*
     - Филтър по системно име на типа документ.

			*Намира и при частично съвпадение*
   * - **$article_name**
     - *string*
     - Филтър по име на `артикул </barsy.help/210-dictionary/article.html>`__ в редовете на документа
   * - **$document_name**
     - *string*
     - Филтър по име на документа.

			*Намира и при частично съвпадение*
   * - **$doc_num**
     - *string*
     - Филтър по номер на документ.

			*Намира и при частично съвпадение*
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$status_id**
     - *int* | *int*
     - Филтър по статус на документ (единична стойност или масив за IN)
   * - **$resolution_status**
     - *int* | *int*
     - Филтър по резултат на `оферта </barsy.help/210-dictionary/offer.html>`__ (0=няма, 1=приета, 2=отхвърлена, 3=преработена)
   * - **$is_template**
     - *int*
     - Филтър по флаг за шаблон
   * - **$delete_flag**
     - *int*
     - Филтър по флаг за изтрит **По подразбиране:** 0
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$send_date**
     - *datetime*
     - Филтър по дата на изпращане на `оферта </barsy.help/210-dictionary/offer.html>`__
   * - **$call_date**
     - *datetime*
     - Филтър по дата на прозвъняване на `оферта </barsy.help/210-dictionary/offer.html>`__
   * - **$create_date**
     - *datetime*
     - Филтър по дата на създаване
   * - **$update_date**
     - *datetime*
     - Филтър по дата на последна промяна
   * - **$ref_date**
     - *datetime*
     - Филтър по вальор (дата на документа)

-----

DocumentsListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към документ. Всяка опция включва съответната колона към данните за
		*всеки запис. Основните данни (base) се връщат винаги, останалите при стойност true.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: DocumentsListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Основни данни`
     - 
     - 
   * - **$document_id**
     - *bool*
     - ID на документа **По подразбиране:** true
   * - **$doc_type_id**
     - *bool*
     - ID на типа документ ( виж: :doc:`../documents/gettypes` ) **По подразбиране:** true
   * - **$doc_type_name**
     - *bool*
     - Системно име на типа документ **По подразбиране:** true
   * - **$create_date**
     - *bool*
     - Дата на създаване **По подразбиране:** true
   * - **$update_date**
     - *bool*
     - Дата на последна промяна **По подразбиране:** true
   * - **$ref_date**
     - *bool*
     - Вальор (дата на документа) **По подразбиране:** true
   * - **$status_id**
     - *bool*
     - ID на статуса на документа **По подразбиране:** true
   * - **$status_name**
     - *bool*
     - Име на статуса на документа **По подразбиране:** true
   * - **$is_template**
     - *bool*
     - Флаг дали записът е шаблон **По подразбиране:** true
   * - **$document_name**
     - *bool*
     - Име на документа **По подразбиране:** true
   * - **$document_sid**
     - *bool*
     - SID на документа **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$barsy_id**
     - *bool*
     - ID на търговския обект ( виж: :doc:`../barsys/get` , :doc:`../barsys/getlist` ) **По подразбиране:** false
   * - **$user_id**
     - *bool*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа ( виж: :doc:`../users/get` , :doc:`../users/getlist` ) **По подразбиране:** true
   * - **$user_name**
     - *bool*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа **По подразбиране:** true
   * - **$client_id**
     - *bool*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/get` , :doc:`../clients/getlist` ) **По подразбиране:** false
   * - **$client_name**
     - *bool*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$email**
     - *bool*
     - Имейл на `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$parent_id**
     - *bool*
     - ID на родителски документ ( виж: :doc:`../documents/get` ) **По подразбиране:** false
   * - **$owner_id**
     - *bool*
     - ID на отговорника ( виж: :doc:`../users/get` , :doc:`../users/getlist` ) **По подразбиране:** false
   * - **$owner_name**
     - *bool*
     - Име на отговорника **По подразбиране:** false
   * - **$deal_id**
     - *bool*
     - ID на сделка ( виж: :doc:`../deals/getlist` ) **По подразбиране:** false
   * - **$deal_title**
     - *bool*
     - Заглавие на сделката **По подразбиране:** false
   * - **$currency_id**
     - *bool*
     - ID на валутата на документа ( виж: :doc:`../currencies/getlist` ) **По подразбиране:** false
   * - **$currency_rate**
     - *bool*
     - Курс на валутата на документа **По подразбиране:** false
   * - **$template_ref_id**
     - *bool*
     - ID на шаблона, от който е създаден документът ( виж: :doc:`../documents/get` ) **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
   * - **$text**
     - *bool*
     - Текст/шаблон на документа **По подразбиране:** false
   * - **$description**
     - *bool*
     - Бележки към документа **По подразбиране:** false
   * - **$document_options**
     - *bool*
     - Допълнителни опции на документа

			*Връща структурираните данни с допълнителни опции на документа.* **По подразбиране:** false
   * - **$delete_flag**
     - *bool*
     - Флаг дали документът е изтрит **По подразбиране:** true
   * - **$doc_num**
     - *bool*
     - Номер на документа **По подразбиране:** false
   * - **$lines_count**
     - *bool*
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в документа **По подразбиране:** false
   * - **$resolution_status**
     - *bool*
     - Резултат на `оферта </barsy.help/210-dictionary/offer.html>`__

			*Възможни стойности: 0=няма, 1=приета, 2=отхвърлена, 3=преработена.* **По подразбиране:** false
   * - **$send_date**
     - *bool*
     - Дата на изпращане на `оферта </barsy.help/210-dictionary/offer.html>`__ **По подразбиране:** false
   * - **$call_date**
     - *bool*
     - Дата на прозвъняване на `оферта </barsy.help/210-dictionary/offer.html>`__ **По подразбиране:** false
   * - **$parse_document_options**
     - *bool*
     - Разпада опциите на документа в отделни полета

			Връща опциите на документа (отстъпка, капаро, дати на `оферта </barsy.help/210-dictionary/offer.html>`__ и др.) като отделни полета в отговора. **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
   * - **$total_amount**
     - *bool*
     - Обща сума на редовете (без документна отстъпка) **По подразбиране:** false
   * - **$total_with_discount**
     - *bool*
     - Обща сума след документна отстъпка/надценка **По подразбиране:** false
   * - **$discount**
     - *bool*
     - Отстъпка или надценка на документа в % **По подразбиране:** false
   * - **$caparo**
     - *bool*
     - Предплащане в % **По подразбиране:** false
   * - **$caparo_fixed**
     - *bool*
     - Капаро във валута **По подразбиране:** false

-----

DocumentsListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с документи (Documents_getlist).
		Подава се като асоциативен масив колона⇒посока (напр. ["update_date" => "desc", "document_id" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

.. list-table::
   :header-rows: 1
   :align: center
   :name: DocumentsListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$document_id**
     - *string*
     - Подреждане по ID на документ
   * - **$doc_type_id**
     - *string*
     - Подреждане по тип документ
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$document_name**
     - *string*
     - Подреждане по име на документ
   * - **$doc_num**
     - *string*
     - Подреждане по номер на документ
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$create_date**
     - *string*
     - Подреждане по дата на създаване
   * - **$update_date**
     - *string*
     - Подреждане по дата на последна промяна
   * - **$ref_date**
     - *string*
     - Подреждане по вальор
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$status_id**
     - *string*
     - Подреждане по статус
   * - **$delete_flag**
     - *string*
     - Подреждане по флаг за изтрит
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$client_id**
     - *string*
     - Подреждане по `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$user_id**
     - *string*
     - Подреждане по `потребител </barsy.help/210-dictionary/user.html>`__-създател
   * - **$owner_id**
     - *string*
     - Подреждане по отговорник

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

     .. literalinclude:: ../../sources/documents_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/documents_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/documents_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/documents_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/documents_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/documents_getlist/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 
 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

