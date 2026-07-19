.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsStoreAmountsByDateAndBarsysFilters
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
Lukanet\\Barsy\\Reports\\Data\\ReportsStoreAmountsByDateAndBarsysFilters


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$from_date**
     - *string*
     - '2026-07-01 00:00'
     - *Дата, към която се изчисляват наличностите*
   * - **$depot_group_id**
     - *string*
     - 
     - *Филтриране по група складове* ( виж: :doc:`../methods/depots/getgrouplist` )
   * - **$article_name**
     - *string*
     - 
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../methods/articles/search` )
   * - **$cat_id**
     - *string*
     - 
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../methods/categories/gettree` )
   * - **$supplier**
     - *string*
     - 
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../methods/suppliers/getlist` )
   * - **$stream_id**
     - *string*
     - 
     - Филтриране по `поток </barsy.help/210-dictionary/flow.html>`__

			* **4** - *Remote*
			* **2** - Втори `поток </barsy.help/210-dictionary/flow.html>`__
			* **1** - *Основен*
			* **3** - трети `поток </barsy.help/210-dictionary/flow.html>`__

			 пример: "4"
   * - **$composite**
     - *string*
     - 
     - Филтриране по тип `артикул </barsy.help/210-dictionary/article.html>`__ (рецепта)

			* **0** - *Няма*
			* **1** - Има (при `продажба </barsy.help/210-dictionary/sale.html>`__)
			* **-1** - Има (при `производство </barsy.help/210-dictionary/storeproduction.html>`__)

			 пример: "0"
   * - **$delete_flag**
     - *string*
     - 
     - Изключва изтритите `артикули </barsy.help/210-dictionary/article.html>`__
   * - **$delete_flag_b**
     - *string*
     - 
     - Изключва изтритите `търговски обекти </barsy.help/210-dictionary/barsy.html>`__
   * - **$amount**
     - *string*
     - 
     - *Филтриране по наличност*

			* **lt** - *Наличност < 0*
			* **eq** - *Наличност = 0*
			* **gt** - *Наличност > 0*

			 пример: "\"lt\""
   * - **$details**
     - *string*
     - 
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/articledetails/gettree` )

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/store_amounts_by_date_and_barsys`

