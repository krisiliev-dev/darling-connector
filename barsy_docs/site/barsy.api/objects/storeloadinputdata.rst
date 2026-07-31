.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreLoadInputData
======================================================================================
Данни за опреция зареждане от доставчик

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeloads\\Data\\StoreLoadInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$depot_id**
     - *int*
     - 
     - Id на `склад </barsy.help/210-dictionary/store.html>`__, който ще се зарежда ( виж: :doc:`../methods/depots/getlist` )
   * - **$supplier_id**
     - *int*
     - 1
     - ID на `доставчик </barsy.help/210-dictionary/supplier.html>`__ по `зареждането </barsy.help/210-dictionary/storeload.html>`__ ( виж: :doc:`../methods/suppliers/getlist` )
   * - **$doc_date**
     - *string*
     - 
     - Дата на документа (дата на завеждане на стоката в `склада </barsy.help/210-dictionary/store.html>`__)

			 пример: "\"2019-01-20\""
   * - **$doc_num**
     - *string*
     - 
     - Номер на документа.

			*Трябва да е уникален за търговския обект*

			 пример: "\"XR1231\""
   * - **$doc_type_id**
     - *int*
     - 1
     - Тип на подадения документ

			 пример: "1" ( виж: :doc:`../methods/storeloads/getdocumenttypes` )
   * - **$price_mode**
     - *int*
     - 0
     - Флаг дали подадените единични цени на `артикули </barsy.help/210-dictionary/article.html>`__ са с ДДС или без

			 пример: "0"
   * - **$has_tax**
     - *int*
     - 1
     - Флаг дали документът е с начислен ДДС
   * - **$description**
     - *string*
     - 
     - Свободен текст

			 пример: "\"\\u0421\\u0432\\u043e\\u0431\\u043e\\u0434\\u0435\\u043d \\u0442\\u0435\\u043a\\u0441\\u0442 \\u0437\\u0430 \\u0431\\u0435\\u043b\\u0435\\u0436\\u043a\\u0438 \\u043a\\u044a\\u043c \\u0437\\u0430\\u0440\\u0435\\u0436\\u0434\\u0430\\u043d\\u0435\\u0442\\u043e\""
   * - **$operation_type**
     - *int*
     - 1
     - Фалг дали документа е за `зареждане </barsy.help/210-dictionary/storeload.html>`__ на стока (1) или за връщане на стока (2)
   * - **$paid_due_date**
     - *string*
     - 
     - Крайна дата за `плащане </barsy.help/210-dictionary/payment.html>`__ към `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$currency_id**
     - *int*
     - 
     - ID на валута, в която са подадени единичните цени на `артикулите </barsy.help/210-dictionary/article.html>`__.

			*Ако е оставена непопълнена, ще се вземе системната валута*
   * - **$currency_rate**
     - *float*
     - 
     - Курс на подадената валута към базовата валута на системата (BGN) към момента на сделката
   * - **$paymethod_id**
     - *int*
     - 
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ към `доставчика </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$request_id**
     - *int*
     - 
     - ID на `заявката към доставчик </barsy.help/210-dictionary/request.html>`__, от която се прави `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$store_load_cat_id**
     - *int*
     - 1
     - ID на `категорията </barsy.help/210-dictionary/category.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$extra_doc_num**
     - *string*
     - 
     - Допълнителен номер на документа
   * - **$discount**
     - *float*
     - 0
     - 
   * - **$preferred_paymethod_id**
     - *int*
     - 
     - Предпочитан начин за `плащане </barsy.help/210-dictionary/payment.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeloads/create`
	 * :doc:`../methods/storeloads/update`

Виж също
--------

 * `Доставчик </barsy.help/210-dictionary/supplier.html>`__
 * `Зареждане </barsy.help/210-dictionary/storeload.html>`__

