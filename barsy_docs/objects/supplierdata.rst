.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

SupplierData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Suppliers\\Data\\SupplierData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$supplier_name**
     - *string*
     - 
     - Име на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$bulstat**
     - *int*
     - 
     - ЕИК на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$vat_num**
     - *string*
     - 
     - ДДС номер
   * - **$mol**
     - *string*
     - 
     - МОЛ
   * - **$address**
     - *string*
     - 
     - Адрес за кореспонденция
   * - **$has_tax**
     - *int*
     - 
     - Регистриран по ДДС
   * - **$group_id**
     - *int*
     - 1
     - ID на група
   * - **$default_paid_period**
     - *int*
     - 
     - Интервал от време(в минути) за отложено `плащане </barsy.help/210-dictionary/payment.html>`__ от дата на доставка
   * - **$notes**
     - *string*
     - 
     - Бележки
   * - **$delete_flag**
     - *int*
     - 0
     - Флаг, дали `потребителя </barsy.help/210-dictionary/user.html>`__ е маркиран като изтрит
   * - **$export_id**
     - *string*
     - 
     - ID за експорт към външна система
   * - **$bank_statement_regex**
     - *string*
     - 
     - Регулярен израз (MariaDB REGEXP формат), който се прилага върху описанието на банковото извлечение за автоматично мапване към този `доставчик </barsy.help/210-dictionary/supplier.html>`__
   * - **$default_price_mode**
     - *int*
     - 0
     - Цени по подразбиране (без или със ДДС)
   * - **$default_currency_id**
     - *int*
     - 
     - Валута по подразбиране.

			*Ако е оставена непопълнена, ще се вземе системната валута*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/suppliers/create`
	 * :doc:`../methods/suppliers/update`

