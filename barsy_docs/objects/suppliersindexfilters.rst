.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

SuppliersIndexFilters
======================================================================================
Филтри на списъка

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Suppliers\\Data\\SuppliersIndexFilters


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$create_date**
     - *string*
     - false
     - Филтър по дата на създаване на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$supplier_name**
     - *string*
     - 
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../methods/suppliers/getlist` )
   * - **$bulstat**
     - *string*
     - 
     - *БУЛСТАТ*
   * - **$vat_num**
     - *string*
     - 
     - ДДС номер на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$group**
     - *string*
     - 
     - Филтър по група на `доставчика </barsy.help/210-dictionary/supplier.html>`__

			* **1** - *Основна*

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/suppliers/index`

