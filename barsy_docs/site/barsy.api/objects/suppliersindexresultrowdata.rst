.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

SuppliersIndexResultRowData
======================================================================================
Данни за резултата

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Suppliers\\Data\\SuppliersIndexResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$supplier_id**
     - *int*
     - 
     - Идентификатор на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$supplier_name**
     - *string*
     - 
     - Име на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$group_name**
     - *string*
     - 
     - Група на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$create_date**
     - *string*
     - 
     - *Дата на създаване на записа*
   * - **$bulstat**
     - *string*
     - 
     - *БУЛСТАТ*
   * - **$vat_num**
     - *string*
     - 
     - ДДС номер на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$has_tax**
     - *string*
     - 
     - Дали `доставчикът </barsy.help/210-dictionary/supplier.html>`__ е регистриран по ДДС

			 пример: "0"
   * - **$default_price_mode**
     - *string*
     - 
     - Режим на цени при зареждания от `доставчика </barsy.help/210-dictionary/supplier.html>`__

			 пример: "0"
   * - **$notes**
     - *string*
     - 
     - Допълнителни бележки за `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$mol**
     - *string*
     - 
     - *Материално отговорно лице*
   * - **$address**
     - *string*
     - 
     - Адрес на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$contact_person**
     - *string*
     - 
     - *Лице за контакт и телефон*
   * - **$email**
     - *string*
     - 
     - *Имейл адреси за контакт*
   * - **$export_id**
     - *string*
     - 
     - *Идентификатор за експорт към външни системи*
   * - **$remote_id**
     - *string*
     - 
     - *Свързана отдалечена система*

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/suppliers/index`

