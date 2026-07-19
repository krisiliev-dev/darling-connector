.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PricelistsIndexResultRowData
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
Lukanet\\Barsy\\Pricelists\\Data\\PricelistsIndexResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$pricelist_id**
     - *int*
     - 
     - *ID*
   * - **$pricelist_name**
     - *string*
     - 
     - *Име*
   * - **$type_title**
     - *string*
     - 
     - *Тип на ценоразписа*
   * - **$group_name**
     - *string*
     - 
     - *Група ценоразписи*
   * - **$periods_date**
     - *string*
     - 
     - *Период на действие по дати*
   * - **$periods_time**
     - *string*
     - 
     - *Период на действие по часове*
   * - **$modificator_type**
     - *string*
     - 
     - Тип ценови `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$modificator_round_type**
     - *string*
     - 
     - *Закръгляне на изчислените цени*
   * - **$articles_cnt**
     - *int*
     - 
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$clients_cnt**
     - *int*
     - 
     - Брой `клиенти </barsy.help/210-dictionary/client.html>`__ в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$client_groups_cnt**
     - *int*
     - 
     - Брой клиентски групи в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$tax_regions_cnt**
     - *int*
     - 
     - Брой типове доставка в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$countries_cnt**
     - *int*
     - 
     - Брой държави в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$subscriptions_cnt**
     - *int*
     - 
     - Брой абонаментни планове в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$price_tax_mode**
     - *string*
     - 
     - *С включено ДДС или без ДДС*
   * - **$create_date**
     - *string*
     - 
     - Дата на създаване на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$last_update**
     - *string*
     - 
     - Дата на последна актуализация на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$price_tax_id**
     - *string*
     - 
     - *ДДС група за ценоразписа*

			 пример: "2"
   * - **$weight**
     - *int*
     - 
     - *Тежест/приоритет при застъпване*
   * - **$current_status**
     - *string*
     - 
     - *Текущ статус (дали е активен в момента)*

			 пример: "0"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/pricelists/index`

