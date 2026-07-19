.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreLoadData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeloads\\Data\\StoreLoadData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_load_id**
     - *int*
     - 
     - ID на `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../methods/barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - 
     - Име на търговския обект
   * - **$depot_id**
     - *int*
     - 
     - ID на `склад </barsy.help/210-dictionary/store.html>`__, в който е заредено ( виж: :doc:`../methods/depots/getlist` )
   * - **$status**
     - *int*
     - 
     - Статус на `зареждането </barsy.help/210-dictionary/storeload.html>`__ [0=Отворено, 1=Приключено]
   * - **$doc_type_name**
     - *string*
     - 
     - Тип документ, по който е заредено
   * - **$doc_type_id**
     - *int*
     - 
     - ID на тип документ, по който е заредено
   * - **$doc_num**
     - *string*
     - 
     - Номер на документа
   * - **$price_mode**
     - *int*
     - 
     - Режим на единични цени (0=>без включено ДДС, 1=>с включено ДДС)
   * - **$has_tax**
     - *int*
     - 
     - Тип за `зареждането </barsy.help/210-dictionary/storeload.html>`__ (0=>без начислено ДДС, 1=>с начислено ДДС)
   * - **$date**
     - *string*
     - 
     - Дата на създаване на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$close_date**
     - *string*
     - 
     - Дата на приключване на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$doc_date**
     - *string*
     - 
     - Документална дата на операцията
   * - **$description**
     - *string*
     - 
     - Описание на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$user_name**
     - *string*
     - 
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$creator_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$supplier_id**
     - *int*
     - 
     - ID на `доставчик </barsy.help/210-dictionary/supplier.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__ ( виж: :doc:`../methods/suppliers/getlist` )
   * - **$supplier_name**
     - *string*
     - 
     - Име на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$operation_type**
     - *int*
     - 
     - Тип операция (`зареждане </barsy.help/210-dictionary/storeload.html>`__, връщане на стока към `доставчик </barsy.help/210-dictionary/supplier.html>`__)
   * - **$total_sum**
     - *float*
     - 
     - Обща сума на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$total_paid**
     - *float*
     - 
     - Общо платени по `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$paid_due_date**
     - *string*
     - 
     - Крайна дата за `плащане </barsy.help/210-dictionary/payment.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$currency_id**
     - *int*
     - 
     - ID на валутата на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$currency_rate**
     - *float*
     - 
     - Курс на валутата на `зареждането </barsy.help/210-dictionary/storeload.html>`__ към основната валута на системата
   * - **$total_costs**
     - *float*
     - 
     - Обща сума на разходите към `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$cost_mode**
     - *int*
     - 
     - Режим на изчислване на разходите спрямо общата сума (включени,изключени)
   * - **$request_id**
     - *int*
     - 
     - ID на `заявката към доставчика </barsy.help/210-dictionary/request.html>`__, по която е създадено `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$paymethod_id**
     - *int*
     - 
     - ID на реален начин `плащане </barsy.help/210-dictionary/payment.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__.

			*Формира се от плащанията към операцията* ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$preferred_paymethod_id**
     - *int*
     - 
     - ID на предпочитан начин на `плащане </barsy.help/210-dictionary/payment.html>`__ на `зареждането </barsy.help/210-dictionary/storeload.html>`__.

			*Задава се свободно. Само за информационни цели* ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$last_update**
     - *string*
     - 
     - Дата на последна редакция на `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$parent_id**
     - *int*
     - 
     - ID на родителско `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$total_costs_2**
     - *float*
     - 
     - Сума на разходите от подчинетите зареждания (свързани с PARENT_ID)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeloads/getlist`

