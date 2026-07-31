.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Invoices_getlist
===========================================================
Списък с документи

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/invoice </barsy.help/210-dictionary/invoice.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с издадените в системата документи — `фактури </barsy.help/210-dictionary/invoice.html>`__, проформи, кредитни известия, дебитни известия и др. — с богат набор от филтри: период, тип на документа, `клиент </barsy.help/210-dictionary/client.html>`__, статус на `плащане </barsy.help/210-dictionary/payment.html>`__, `потребител </barsy.help/210-dictionary/user.html>`__-създател, серия, диапазон на сума. Поддържа странициране и `extra_properties` за обогатяване (детайли, плащания, обвързани документи).

Типични случаи: дневник с издадени `фактури </barsy.help/210-dictionary/invoice.html>`__ за счетоводно осчетоводяване, справка за просрочени `фактури </barsy.help/210-dictionary/invoice.html>`__, експорт за данъчна декларация, преглед на издадени проформи преди потвърждение.

**Име**: Invoices_getlist
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
     - InvoicesListFiltersData_ 
     - Налични филтри за списъка
   * - **$extra_properties**
     - InvoicesListExtraPropertiesData_ 
     - Желани допълнителни колони за всяка `фактура </barsy.help/210-dictionary/invoice.html>`__ (виж класа)
   * - **$offset**
     - *int*
     - Номер на ред, от който да започне списъкът (странициране) **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 5000
   * - **$order_by**
     - InvoicesListOrderByData_ 
     - Подреждане — низ, масив или обект колона⇒посока (напр. {"create_date":"desc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
InvoiceData_                                                           Списък с документи с данни според исканите ($extra_properties)
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

InvoicesListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoicesListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$inv_id**
     - *int*
     - ID на `фактурата </barsy.help/210-dictionary/invoice.html>`__ (различно от номер на `фактурата </barsy.help/210-dictionary/invoice.html>`__)
   * - **$remote_ref_id**
     - *string* | *int*
     - Номер на `фактурата </barsy.help/210-dictionary/invoice.html>`__ спрямо отдалечената система ( виж: :doc:`../remotesystems/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, чията е `фактурата </barsy.help/210-dictionary/invoice.html>`__ ( виж: :doc:`../clients/get` , :doc:`../clients/getlist` )
   * - **$user_id**
     - *int*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `фактурата </barsy.help/210-dictionary/invoice.html>`__ ( виж: :doc:`../users/get` , :doc:`../users/getlist` )
   * - **$barsy_id**
     - *int*
     - ID на търговският обект ( виж: :doc:`../barsys/get` , :doc:`../barsys/getlist` )
   * - **$remote_id**
     - *int*
     - ID на отдалечената система. Определя обхвата на данните за обвръзка с отдалечена система —

			*ползва се от опциите за отдалечена система в extra_properties.* ( виж: :doc:`../remotesystems/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$term_date**
     - *datetime*
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$create_date**
     - *datetime*
     - Дата на създаване
   * - **$payment_date**
     - *datetime*
     - Дата на събитие
   * - **$last_update**
     - *datetime*
     - Дата на последно обновяване на `фактура </barsy.help/210-dictionary/invoice.html>`__
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$inv_num**
     - *string*
     - Номер на `фактура </barsy.help/210-dictionary/invoice.html>`__

-----

InvoicesListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към даден документ. Всяка опция включва съответната колона
		*към данните за всеки документ от списъка. Основните данни (base) се връщат винаги, а останалите се включват при стойност true.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoicesListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Основни данни`
     - 
     - 
   * - **$inv_id**
     - *bool*
     - ID на документа (различно от номера на документа) **По подразбиране:** true
   * - **$inv_num**
     - *bool*
     - Номер на документа **По подразбиране:** true
   * - **$type_id**
     - *bool*
     - ID на типа на документа (`фактура </barsy.help/210-dictionary/invoice.html>`__, проформа, кредитно/дебитно известие и др.) **По подразбиране:** true
   * - **$parent_num**
     - *bool*
     - Номер на родителския документ (документа, към който е издаден) **По подразбиране:** true
   * - **$is_anulate**
     - *bool*
     - Флаг дали документът е анулиран **По подразбиране:** true
   * - **$type_name**
     - *bool*
     - Наименование на типа на документа **По подразбиране:** false
   * - **$uuid**
     - *bool*
     - Уникален идентификатор (UUID) на документа **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
   * - **$total**
     - *bool*
     - Обща сума на документа **По подразбиране:** true
   * - **$total_neto**
     - *bool*
     - Обща сума без ДДС (нето) **По подразбиране:** true
   * - **$total_dds**
     - *bool*
     - Обща сума на начисленото ДДС **По подразбиране:** true
   * - **$total_all**
     - *bool*
     - Крайна сума за `плащане </barsy.help/210-dictionary/payment.html>`__ (с ДДС) **По подразбиране:** true
   * - **$discount**
     - *bool*
     - Отстъпка по документа **По подразбиране:** false
   * - **$payments_paid_sum**
     - *bool*
     - Платена сума по документа

			сборът от плащанията по свързаните `сметки </barsy.help/210-dictionary/account.html>`__. Сравнена с крайната сума (total_all) показва дали документът е платен, частично платен или неплатен. Връща null/0, ако няма свързани плащания **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$client_id**
     - *bool*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, за когото е издаден документът ( виж: :doc:`../clients/get` , :doc:`../clients/getlist` ) **По подразбиране:** true
   * - **$paymethod_id**
     - *bool*
     - ID на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../paymentmethods/getlist` ) **По подразбиране:** true
   * - **$receiver_id**
     - *bool*
     - ID на получателя (`фирма </barsy.help/210-dictionary/company.html>`__) на документа **По подразбиране:** true
   * - **$client_name**
     - *bool*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ по документа **По подразбиране:** false
   * - **$seller_id**
     - *bool*
     - ID на продавача **По подразбиране:** false
   * - **$bank_account_id**
     - *bool*
     - ID на банковата `сметка </barsy.help/210-dictionary/account.html>`__ на получателя **По подразбиране:** false
   * - **$receiver_name**
     - *bool*
     - Име на получателя на документа **По подразбиране:** false
   * - **$seller_bank_account_id**
     - *bool*
     - ID на банковата `сметка </barsy.help/210-dictionary/account.html>`__ на продавача **По подразбиране:** false
   * - **$barsy_id**
     - *bool*
     - ID на търговския обект, издал документа ( виж: :doc:`../barsys/get` , :doc:`../barsys/getlist` ) **По подразбиране:** false
   * - **$seller_company_id**
     - *bool*
     - ID на `фирмата </barsy.help/210-dictionary/company.html>`__-продавач ( виж: :doc:`../companies/get` , :doc:`../companies/getlist` ) **По подразбиране:** false
   * - **$user_id**
     - *bool*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа ( виж: :doc:`../users/get` , :doc:`../users/getlist` ) **По подразбиране:** false
   * - **$seller_name**
     - *bool*
     - Име на продавача **По подразбиране:** false
   * - **$seller_code**
     - *bool*
     - Код на продавача **По подразбиране:** false
   * - **$email**
     - *bool*
     - Имейл за изпращане на документа към `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
   * - **$term_date**
     - *bool*
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__ **По подразбиране:** true
   * - **$additional_text**
     - *bool*
     - Допълнителен текст към документа **По подразбиране:** true
   * - **$free_text**
     - *bool*
     - Свободен текст към документа **По подразбиране:** true
   * - **$create_date**
     - *bool*
     - Дата на създаване на документа **По подразбиране:** true
   * - **$with_tax**
     - *bool*
     - Флаг дали документът е с включено ДДС **По подразбиране:** false
   * - **$payment_date**
     - *bool*
     - Дата на `плащане </barsy.help/210-dictionary/payment.html>`__ **По подразбиране:** false
   * - **$produce_date**
     - *bool*
     - Дата на издаване (данъчно събитие) **По подразбиране:** false
   * - **$last_update**
     - *bool*
     - Дата на последна промяна на документа **По подразбиране:** false
   * - **$export_id**
     - *bool*
     - ID за експорт, свързано с начина на `плащане </barsy.help/210-dictionary/payment.html>`__ **По подразбиране:** false
   * - **$remote_system**
     - *bool*
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__, обвързана с документа в отдалечената система.

			*Изисква филтър "remote_id"* **По подразбиране:** false
   * - **$remote_accounts**
     - *bool*
     - Референция на `сметката </barsy.help/210-dictionary/account.html>`__ в отдалечената система.

			*Изисква филтър "remote_id"* **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
   * - **$payment_ids**
     - *bool*
     - Списък с ID-та на плащанията по документа **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
   * - **$is_paid**
     - *bool*
     - Дали документът е напълно платен — платената сума по свързаните `сметки </barsy.help/210-dictionary/account.html>`__ покрива крайната сума (total_all) **По подразбиране:** false
   * - **$payments_remain**
     - *bool*
     - Остатък за `плащане </barsy.help/210-dictionary/payment.html>`__ — крайната сума (total_all) минус платената сума по свързаните `сметки </barsy.help/210-dictionary/account.html>`__.

			*Стойност <= 0 означава напълно платен документ* **По подразбиране:** false
   * - **$paymethod_name**
     - *bool*
     - Име на начина на `плащане </barsy.help/210-dictionary/payment.html>`__ (с приоритет на версията на начина на `плащане </barsy.help/210-dictionary/payment.html>`__) **По подразбиране:** false
   * - **$payment_type_id**
     - *bool*
     - Тип на `плащането </barsy.help/210-dictionary/payment.html>`__ **По подразбиране:** false
   * - **$parent_inv_id**
     - *bool*
     - ID на родителския документ (документа, по който е издаден този) ( виж: :doc:`../invoices/get` ) **По подразбиране:** false
   * - **$barsy_name**
     - *bool*
     - Име на търговския обект, издал документа **По подразбиране:** false
   * - **$seller_pop_name**
     - *bool*
     - POP име на продавача (`фирмата </barsy.help/210-dictionary/company.html>`__-издател) **По подразбиране:** false
   * - **$currency_id**
     - *bool*
     - ID на валутата на документа ( виж: :doc:`../currencies/get` , :doc:`../currencies/getlist` ) **По подразбиране:** false
   * - **$currency_rate**
     - *bool*
     - Курс на валутата на документа спрямо системната валута **По подразбиране:** false
   * - **$person_id**
     - *bool*
     - ID на лицето за контакт по документа ( виж: :doc:`../persons/get` , :doc:`../persons/getlist` ) **По подразбиране:** false
   * - **$person_name**
     - *bool*
     - Име на лицето за контакт по документа **По подразбиране:** false
   * - **$deal_id**
     - *bool*
     - ID на сделката, към която е документът ( виж: :doc:`../deals/getlist` ) **По подразбиране:** false
   * - **$deal_title**
     - *bool*
     - Наименование на сделката, към която е документът ( виж: :doc:`../deals/getlist` ) **По подразбиране:** false
   * - **$linked_accounts_num**
     - *bool*
     - Брой `сметки </barsy.help/210-dictionary/account.html>`__, свързани с документа **По подразбиране:** false
   * - **$client_order_ids**
     - *bool*
     - Списък с номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__, фигуриращи в документа **По подразбиране:** false
   * - **$detailed_client_order_ids**
     - *bool*
     - Списък с номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ и датите им на издаване, фигуриращи в документа **По подразбиране:** false

-----

InvoicesListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с документи (Invoices_getlist).
		Подава се като асоциативен масив колона⇒посока (напр. ["create_date" => "desc", "inv_num" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoicesListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$inv_id**
     - *string*
     - Подреждане по ID на документа
   * - **$inv_num**
     - *string*
     - Подреждане по номер на документа
   * - **$type_id**
     - *string*
     - Подреждане по тип на документа
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$client_id**
     - *string*
     - Подреждане по `клиент </barsy.help/210-dictionary/client.html>`__
   * - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
   * - **$total**
     - *string*
     - Подреждане по обща сума
   * - **$total_all**
     - *string*
     - Подреждане по крайна сума за `плащане </barsy.help/210-dictionary/payment.html>`__ (с ДДС)
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$create_date**
     - *string*
     - Подреждане по дата на създаване
   * - **$term_date**
     - *string*
     - Подреждане по срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$payment_date**
     - *string*
     - Подреждане по дата на `плащане </barsy.help/210-dictionary/payment.html>`__ (данъчно събитие)
   * - **$last_update**
     - *string*
     - Подреждане по дата на последна промяна

-----

InvoiceData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoiceData

   * - Параметър
     - Тип
     - Описание
   * - **$inv_id**
     - *int*
     - ID на `фактурата </barsy.help/210-dictionary/invoice.html>`__ (вътрешна номенклатура)
   * - **$inv_sid**
     - *string*
     - SID на `фактурата </barsy.help/210-dictionary/invoice.html>`__ (вътрешна номенклатура кодирана)
   * - **$inv_num**
     - *string*
     - 
   * - **$linked_accounts_num**
     - 
     - 
   * - **$type_id**
     - *int*
     - Тип на документа (`фактура </barsy.help/210-dictionary/invoice.html>`__, проформа, дебитно/кредитно известие, стокова ...) **По подразбиране:** 1
   * - **$type_name**
     - *string*
     - Тип на документа
   * - **$parent_num**
     - *string*
     - Номер на документ, по който е издаден този
   * - **$produce_date**
     - *string*
     - Дата на издаване
   * - **$create_date**
     - *string*
     - Дата на създаване
   * - **$term_date**
     - *string*
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$payment_date**
     - *string*
     - Дата на събитие
   * - **$paymethod_id**
     - 
     - 
   * - **$paymethod_name**
     - 
     - 
   * - **$is_anulate**
     - *int*
     - Флаг дали `фактурата </barsy.help/210-dictionary/invoice.html>`__ е анулирана **По подразбиране:** 0
   * - **$total_all_string**
     - *string*
     - Словом на сумата на `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$total_dds_string**
     - *string*
     - Словом на сумата на ДДС
   * - **$with_tax**
     - *int*
     - Флаг дали при печат да се печатат `артикулите </barsy.help/210-dictionary/article.html>`__ с ед.цени с ДДС **По подразбиране:** 0
   * - **$seller_name**
     - *string*
     - Име на издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$receiver_name**
     - *string*
     - Име на получил `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$additional_text**
     - *string*
     - Допълнителен текст към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$free_text**
     - *string*
     - Свободен текст към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_code**
     - *int*
     - Уникален код на издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_company_id**
     - *int*
     - ID на издател на `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_bank_account_id**
     - *int*
     - ID на банкова `сметка </barsy.help/210-dictionary/account.html>`__ за която е `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ (номенклатура на Barsy)
   * - **$client**
     - ClientData_ 
     - Данни за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$barsy_id**
     - *int*
     - `Търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който е издадена `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$user_id**
     - *int*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, издал `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$accounts**
     - *array*
     - Списък с прикачените `сметки </barsy.help/210-dictionary/account.html>`__ към `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$seller_id**
     - *int*
     - 
   * - **$receiver_id**
     - *int*
     - 
   * - **$client_name**
     - 
     - 
   * - **$email**
     - 
     - 
   * - **$currency**
     - 
     - 
   * - **$seller**
     - InvoiceCompanyData_ 
     - Данни за получател
   * - **$receiver**
     - InvoiceCompanyData_ 
     - Данни за `доставчик </barsy.help/210-dictionary/supplier.html>`__
   * - **$parent**
     - 
     - 
   * - **$bank_account_id**
     - *int*
     - 
   * - **$bank_account**
     - InvoiceBankAccountData_ 
     - 
   * - **$seller_pop_name**
     - 
     - 
   * - **$paymethod_version_id**
     - 
     - 
   * - **$deal_id**
     - 
     - 
   * - **$deal_title**
     - 
     - 
   * - **$client_order_ids**
     - *string*
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ фигуриращи в `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$detailed_client_order_ids**
     - *string*
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ с дата на издаването им фигуриращи в `фактурата </barsy.help/210-dictionary/invoice.html>`__
   * - **$items**
     - InvoiceItemData_ []
     - Списък с `артикулите </barsy.help/210-dictionary/article.html>`__ към `фактурата </barsy.help/210-dictionary/invoice.html>`__ **По подразбиране:** []
   * - **$total**
     - *float*
     - Обсща сума на `фактурата </barsy.help/210-dictionary/invoice.html>`__ в системната валута **По подразбиране:** 0
   * - **$total_sum**
     - *float*
     - Обща сума с ДДС (ако се начислява) в систманата валута **По подразбиране:** 0
   * - **$total_neto**
     - *float*
     - Обща сума без ДДС в системната валута **По подразбиране:** 0
   * - **$total_dds**
     - *float*
     - Сума на ДДС в системната валута **По подразбиране:** 0
   * - **$total_all**
     - *float*
     -  **По подразбиране:** 0
   * - **$discount**
     - *float*
     -  **По подразбиране:** 0
   * - **$discount_sum**
     - 
     -  **По подразбиране:** 0
   * - **$initial_total**
     - 
     -  **По подразбиране:** 0
   * - **$tax_totals_by_tax**
     - 
     -  **По подразбиране:** []
   * - **$tax_neto_by_tax**
     - 
     -  **По подразбиране:** []
   * - **$parent_inv_id**
     - *int*
     - 
   * - **$total_remain**
     - *float*
     - 
   * - **$person_id**
     - *int*
     - 
   * - **$person_name**
     - *string*
     - 
   * - **$currency_id**
     - *int*
     - 
   * - **$currency_rate**
     - *float*
     - 

-----

ClientData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ClientData

   * - Параметър
     - Тип
     - Описание
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_name**
     - *string*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ - трябва да бъде уникално в цялата система.

			*Може да бъде физическото име или друго синтетично име*
   * - **$discount**
     - *int*
     - Процент отстъпка/надценка за всички операции на `клиента </barsy.help/210-dictionary/client.html>`__ (ако числото е отрицателно-> отстъпка; ако е положително>надценка) **По подразбиране:** 0
   * - **$tel**
     - *string*
     - Телефон за контакт
   * - **$recom**
     - *string*
     - 
   * - **$company_name**
     - *string*
     - Име на юридическото лице
   * - **$address**
     - *string*
     - Адрес по регистрация
   * - **$bulstat**
     - *string*
     - ЕИК номер (Булстат)
   * - **$vat_num**
     - *string*
     - ДДС номер
   * - **$mol**
     - *string*
     - МОЛ
   * - **$town**
     - *string*
     - Град
   * - **$zip**
     - *string*
     - Пощенски код
   * - **$delivery_address**
     - DeliveryAddressData_ 
     - Адрес за доставка
   * - **$delivery_zone_id**
     - *string*
     - ID на зона за доставка
   * - **$client_create_date**
     - *datetime*
     - Дата на създаване на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$email**
     - *string*
     - Основен email на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$email_invoices**
     - *string*
     - email за изпращане на `фактури </barsy.help/210-dictionary/invoice.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_code**
     - *string*
     - Клиентски код (на карта)
   * - **$total_balance**
     - *float*
     - Текущ баланс на клиентския портфейл **По подразбиране:** 0
   * - **$credit_limit**
     - *float*
     - Кредитен лимит на `клиента </barsy.help/210-dictionary/client.html>`__ (стойност до която може да задлъжнява)
   * - **$paid_period**
     - *int*
     - Интервал от време(в минути) за отложено `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране
   * - **$allow_client_nocard**
     - *bool*
     - Разрешено използване профила без карта **По подразбиране:** 1
   * - **$allow_credit_nocard**
     - *bool*
     - Разрешено използване на клиентски портфейл без карта **По подразбиране:** 1
   * - **$allow_discount_nocard**
     - *bool*
     - Разрешено използване на отстъпка без карта **По подразбиране:** 1
   * - **$group_id**
     - *int*
     - Клиентска група, към която принадлежи `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getgroups` ) **По подразбиране:** 1
   * - **$client_picture**
     - *string*
     - Основна снимка от наличните за този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$last_update**
     - *datetime*
     - Дата на последна актуализация на данните за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$description**
     - *string*
     - Описание - свободен текст
   * - **$user_id**
     - *int*
     - ID на потребиетля, създал `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$delete_flag**
     - *int*
     - Флаг, дали `потребителя </barsy.help/210-dictionary/user.html>`__ е маркиран като изтрит **По подразбиране:** 0
   * - **$client_auth**
     - *string*
     - Клиентско име за вход в клиентския профил
   * - **$client_pass**
     - *string*
     - Клиентска парола за вход в клиентския профил
   * - **$export_id**
     - *int*
     - ID за експорт към външни системи
   * - **$default_paymethod_id**
     - *int*
     - ID на предпочитан начин на `плащане </barsy.help/210-dictionary/payment.html>`__ за този `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: ``Paymethods`` )
   * - **$client_source_id**
     - *int*
     - ID на източника, от където е намерен този `клиент </barsy.help/210-dictionary/client.html>`__/контакт
   * - **$recruit_client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, осигурил този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$ml_subscribed**
     - *int*
     - Флаг дали `клиентът </barsy.help/210-dictionary/client.html>`__ е абониран за maillist
   * - **$delivery_data**
     - *object*
     - Обект с информация за доставката (key=>value, пр. "city"=>"London")
   * - **$receiver_name**
     - *string*
     - Име на получател
   * - **$is_guest**
     - *bool*
     - Флаг за гост **По подразбиране:** 0
   * - **$lang_id**
     - 
     - 
   * - **$session_timeout**
     - 
     -  **По подразбиране:** 30
   * - **$make_invoice_auto**
     - *int*
     - 
   * - **$send_invoice_auto**
     - *int*
     - 

-----

DeliveryAddressData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Съдържа всички данни за адреса на `клиент </barsy.help/210-dictionary/client.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: DeliveryAddressData

   * - Параметър
     - Тип
     - Описание
   * - **$delivery_type**
     - *string*
     - Тип на доставката

			* **no** - *Без доставка*
			* **home** - *За вкъщи*
			* **address** - *Доставка до адрес*
			* **barsy** - Получаване от `търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **office** - *Получаване от офис на куриер* **По подразбиране:** 'no'
   * - **$country_name**
     - *string*
     - Име на държава
   * - **$country_id**
     - *string*
     - ID на държава
   * - **$dest_id**
     - *int*
     - ID на населено място ( виж: :doc:`../destinations/getlist` )
   * - **$address**
     - *string*
     - Адрес за доставка (кв,бул/ул,№,бл,вх,ет)
   * - **$address_neighborhood**
     - *string*
     - Квартал на адреса за доставка
   * - **$address_number**
     - *string*
     - Номер на улица/булевард за доставка
   * - **$address_building**
     - *string*
     - Блок за доставка
   * - **$address_entry**
     - *string*
     - Вход на блок за доставка
   * - **$address_floor**
     - *string*
     - Номер на етаж за доставка
   * - **$address_ap**
     - *string*
     - Номер на апартамент за доставка
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (ако типа на доставката е "Взимане от `търговски обект </barsy.help/210-dictionary/barsy.html>`__") ( виж: :doc:`../barsys/getlist` )
   * - **$speditor_id**
     - *int*
     - ID на спедитор ( виж: :doc:`../speditors/getlist` )
   * - **$office_id**
     - *int*
     - ID на офис на куриер по номенклатурата на съответния куриер ( виж: :doc:`../speditors/getofficelist` )
   * - **$office_type**
     - *string*
     - 
   * - **$coords**
     - *string*
     - Координати на адреса
   * - **$zip**
     - *string*
     - Пощенски код
   * - **$description**
     - *string*
     - Допълнителна информация към адреса за доставка

-----

InvoiceCompanyData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoiceCompanyData

   * - Параметър
     - Тип
     - Описание
   * - **$company_id**
     - *int*
     - 
   * - **$company_name**
     - *string*
     - 
   * - **$identity_num**
     - *string*
     - 
   * - **$vat_num**
     - *string*
     - 
   * - **$mol**
     - *string*
     - 
   * - **$town**
     - *string*
     - 
   * - **$address**
     - *string*
     - 
   * - **$country_id**
     - *string*
     - 

-----

InvoiceBankAccountData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoiceBankAccountData

   * - Параметър
     - Тип
     - Описание
   * - **$account_id**
     - *int*
     - 
   * - **$company_id**
     - *int*
     - 
   * - **$account_name**
     - *string*
     - 
   * - **$bank_name**
     - *string*
     - 
   * - **$bic**
     - *string*
     - 
   * - **$iban**
     - *string*
     - 
   * - **$currency**
     - *string*
     - 

-----

InvoiceItemData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InvoiceItemData

   * - Параметър
     - Тип
     - Описание
   * - **$item_id**
     - *int*
     - 
   * - **$item_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - :deprecated:`$single_price`
     - *float*
     - Служебна стойност за единична цена без ДДС.

			*Изполвайте original_single_price* :deprecated_text:`Отхвърлено: */`
   * - **$original_single_price**
     - *float*
     - Единична цена без ДДС
   * - :deprecated:`$single_price_with_tax`
     - *float*
     - Служебна стойност за единична цена с ДДС.

			*Изполвайте original_single_price_with_tax* :deprecated_text:`Отхвърлено: */`
   * - **$original_single_price_with_tax**
     - *float*
     - Единична цена с ДДС
   * - **$quantity**
     - *float*
     - Колиество на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$line_total**
     - *float*
     - Тотал на цената спрямо това дали са поискани тотали в оригинална или системна валута и дали са с ДДС или без ДДС
   * - **$measure**
     - *string*
     - Мерна единица на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_id**
     - *int*
     - ДДС група на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax**
     - *int*
     - ДДС на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$inv_ref_num**
     - *string*
     - Референтен номер на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_reason**
     - *string*
     - 
   * - **$discount**
     - *float*
     -  **По подразбиране:** 0
   * - **$remote_ref_id**
     - *int*
     - Номер на `артикула </barsy.help/210-dictionary/article.html>`__ спрямо отдалечената система
   * - **$uuid**
     - *string*
     - Уникален номер на редър
   * - **$lot_value**
     - *string*
     - Номер на партида

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

     .. literalinclude:: ../../sources/invoices_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/invoices_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/invoices_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/invoices_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/invoices_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/invoices_getlist/barsy_api_client_simple.php
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

