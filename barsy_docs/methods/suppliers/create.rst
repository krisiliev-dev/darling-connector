.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Suppliers_create
===========================================================
Създаване на доставчик

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/supplier </barsy.help/210-dictionary/supplier.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира нов `доставчик </barsy.help/210-dictionary/supplier.html>`__ в системата с данни за фирмена идентификация (име, ЕИК/БУЛСТАТ, ДДС номер, МОЛ, регистрация по ДДС), адрес, контактни лица, банкови `сметки </barsy.help/210-dictionary/account.html>`__, група и режим на цените по подразбиране (с/без ДДС). `Доставчиците </barsy.help/210-dictionary/supplier.html>`__ се ползват за регистрация на постъпления (складови зареждания) и за асоциация с `артикули </barsy.help/210-dictionary/article.html>`__, които те доставят, заедно с тяхната доставна цена.

Типични случаи: добавяне на нов `доставчик </barsy.help/210-dictionary/supplier.html>`__ след подписан рамков договор, импорт от външна ERP/CRM, регистрация на `доставчик </barsy.help/210-dictionary/supplier.html>`__ от служител при първа доставка. Уникалността по ЕИК се проверява за избягване на дубликати.

**Име**: Suppliers_create
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
   * - **$supplier**
     - SupplierData_ 
     - Данни за `доставчика </barsy.help/210-dictionary/supplier.html>`__.

			*Записват се само подадените*


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

SupplierData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: SupplierData

   * - Параметър
     - Тип
     - Описание
   * - **$supplier_name**
     - *string*
     - Име на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$bulstat**
     - *int*
     - ЕИК на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$vat_num**
     - *string*
     - ДДС номер
   * - **$mol**
     - *string*
     - МОЛ
   * - **$address**
     - *string*
     - Адрес за кореспонденция
   * - **$has_tax**
     - *int*
     - Регистриран по ДДС
   * - **$group_id**
     - *int*
     - ID на група **По подразбиране:** 1
   * - **$default_paid_period**
     - *int*
     - Интервал от време(в минути) за отложено `плащане </barsy.help/210-dictionary/payment.html>`__ от дата на доставка
   * - **$notes**
     - *string*
     - Бележки
   * - **$delete_flag**
     - *int*
     - Флаг, дали `потребителя </barsy.help/210-dictionary/user.html>`__ е маркиран като изтрит **По подразбиране:** 0
   * - **$export_id**
     - *string*
     - ID за експорт към външна система
   * - **$bank_statement_regex**
     - *string*
     - Регулярен израз (MariaDB REGEXP формат), който се прилага върху описанието на банковото извлечение за автоматично мапване към този `доставчик </barsy.help/210-dictionary/supplier.html>`__
   * - **$default_price_mode**
     - *int*
     - Цени по подразбиране (без или със ДДС) **По подразбиране:** 0
   * - **$default_currency_id**
     - *int*
     - Валута по подразбиране.

			*Ако е оставена непопълнена, ще се вземе системната валута*

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

     .. literalinclude:: ../../sources/suppliers_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/suppliers_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/suppliers_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/suppliers_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/suppliers_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/suppliers_create/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Доставчик </barsy.help/210-dictionary/supplier.html>`__


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

