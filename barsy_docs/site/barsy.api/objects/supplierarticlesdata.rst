.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

SupplierArticlesData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Suppliers\\Data\\SupplierArticlesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$article_id**
     - *int*
     - 
     - Article_id
   * - **$default_delivery_price**
     - *float*
     - 
     - Договорена доставна цена
   * - **$remote_ref_id**
     - *string*
     - 
     - ID на `артикула </barsy.help/210-dictionary/article.html>`__ в номенклатирата на `доставчика </barsy.help/210-dictionary/supplier.html>`__
   * - **$remote_article_name**
     - *string*
     - 
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__ в номенклатирата на `доставчика </barsy.help/210-dictionary/supplier.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/suppliers/save_articles`

