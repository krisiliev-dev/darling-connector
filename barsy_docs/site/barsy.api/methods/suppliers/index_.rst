.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Suppliers_index
===========================================================
UI списък с доставчици

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/supplier </barsy.help/210-dictionary/supplier.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Структуриран изглед (eStructList) на `доставчиците </barsy.help/210-dictionary/supplier.html>`__ за административния UI с пълен набор от колони (име, група, ЕИК/ДДС номер, регистрация по ДДС, МОЛ, адрес, контакти, email, отдалечена система), вградени действия (преглед, нов, импорт, контакти, изтриване) и многобройни филтри (име, ЕИК, ДДС номер, дата на създаване, група). За програмно извличане на данни виж `Suppliers_getlist`, който е плосък JSON endpoint.

Типични случаи: основен изглед на администраторския панел "`Доставчици </barsy.help/210-dictionary/supplier.html>`__", изграждане на филтрирани справки, ad-hoc експорти от UI.

**Име**: Suppliers_index
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
   * - **$action_type**
     - *string*
     - Тип на върнатите данни

			* **content** - *структура на списъка*
			* **values** - *стойности на списъка* **По подразбиране:** 'content'
   * - **$id**
     - *string*
     - ID на обекта, който се обработва

			Списък с `доставчици </barsy.help/210-dictionary/supplier.html>`__
   * - **$filters**
     - SuppliersIndexFilters_ 
     - масив от налични филтри за този списък.

			*Всички са опционални* **По подразбиране:** []
   * - **$page_num**
     - *int*
     - Номер на желана страница **По подразбиране:** 1
   * - **$rows**
     - *int*
     - Брой реда на страница **По подразбиране:** 50
   * - **$order_by**
     - *string*
     - Сортиране по (името на колоната като елемент)
   * - **$order_dir**
     - *string*
     - Посока на сортиране

			* **asc** - *възходящо*
			* **desc** - *низходящо*
   * - **$columns**
     - *array*
     - Списък от колоните, които да бъдат включени в отговора (ако е празен, показва избрани по подразбиране)

			* **supplier_id** - ID (Идентификатор на `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **supplier_name** - Име (Име на `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **group_name** - Група (Група на `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **create_date** - *Създаден на (Дата на създаване на записа)*
			* **bulstat** - *ЕИК (БУЛСТАТ)*
			* **vat_num** - ДДС № (ДДС номер на `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **has_tax** - Регистриран по ДДС (Дали `доставчикът </barsy.help/210-dictionary/supplier.html>`__ е регистриран по ДДС)
			* **default_price_mode** - Цени по подразбиране (Режим на цени при зареждания от `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **notes** - Бележки (Допълнителни бележки за `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **mol** - *МОЛ (Материално отговорно лице)*
			* **address** - Адрес (Адрес на `доставчика </barsy.help/210-dictionary/supplier.html>`__)
			* **contact_person** - *Контакт - телефон (Лице за контакт и телефон)*
			* **email** - *Еmail (Имейл адреси за контакт)*
			* **export_id** - *Export ID (Идентификатор за експорт към външни системи)*
			* **remote_id** - *Отдалечена система (Свързана отдалечена система)* **По подразбиране:** ["supplier_id","supplier_name","group_name","bulstat","vat_num","has_tax","remote_id"]
   * - **$values**
     - *bool*
     - Масив от стойности на обекта (при запис)
   * - **$search**
     - *string*
     - 
   * - **$params**
     - *bool*
     - 
   * - **$extra_elements**
     - *bool*
     - 
   * - **$image_col_size**
     - *string*
     - 


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
SuppliersIndexResultData_                                              
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

SuppliersIndexFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

.. list-table::
   :header-rows: 1
   :align: center
   :name: SuppliersIndexFilters

   * - Параметър
     - Тип
     - Описание
   * - **$create_date**
     - *string*
     - Филтър по дата на създаване на `доставчика </barsy.help/210-dictionary/supplier.html>`__ **По подразбиране:** false
   * - **$supplier_name**
     - *string*
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../suppliers/getlist` )
   * - **$bulstat**
     - *string*
     - *БУЛСТАТ*
   * - **$vat_num**
     - *string*
     - ДДС номер на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$group**
     - *string*
     - Филтър по група на `доставчика </barsy.help/210-dictionary/supplier.html>`__

			* **1** - *Основна*

-----

SuppliersIndexResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: SuppliersIndexResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$supplier_id**
     - *int*
     - Идентификатор на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$supplier_name**
     - *string*
     - Име на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$group_name**
     - *string*
     - Група на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$create_date**
     - *string*
     - *Дата на създаване на записа*
   * - **$bulstat**
     - *string*
     - *БУЛСТАТ*
   * - **$vat_num**
     - *string*
     - ДДС номер на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$has_tax**
     - *string*
     - Дали `доставчикът </barsy.help/210-dictionary/supplier.html>`__ е регистриран по ДДС
   * - **$default_price_mode**
     - *string*
     - Режим на цени при зареждания от `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$notes**
     - *string*
     - Допълнителни бележки за `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$mol**
     - *string*
     - *Материално отговорно лице*
   * - **$address**
     - *string*
     - Адрес на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$contact_person**
     - *string*
     - *Лице за контакт и телефон*
   * - **$email**
     - *string*
     - *Имейл адреси за контакт*
   * - **$export_id**
     - *string*
     - *Идентификатор за експорт към външни системи*
   * - **$remote_id**
     - *string*
     - *Свързана отдалечена система*

-----

SuppliersIndexResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: SuppliersIndexResultData

   * - Параметър
     - Тип
     - Описание
   * - **$page_num**
     - *int*
     - Номер на текуща страница
   * - **$total**
     - *int*
     - Общ брой страници
   * - **$records**
     - *int*
     - Общ брой записи
   * - **$rows**
     - SuppliersIndexResultRowData_ []
     - Полета на всеки ред от списъка
   * - **$totals**
     - 
     - 
   * - **$filters_resume**
     - *array*
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

     .. literalinclude:: ../../sources/suppliers_index/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/suppliers_index/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/suppliers_index/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/suppliers_index/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/suppliers_index/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/suppliers_index/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Доставчик </barsy.help/210-dictionary/supplier.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

