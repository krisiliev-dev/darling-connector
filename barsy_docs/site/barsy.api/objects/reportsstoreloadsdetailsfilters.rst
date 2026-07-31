.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsStoreloadsDetailsFilters
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
Lukanet\\Barsy\\Reports\\Data\\ReportsStoreloadsDetailsFilters


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$ref_date**
     - *string*
     - ["2026-07-01"]
     - Период на `зареждане </barsy.help/210-dictionary/storeload.html>`__
   * - **$article_name**
     - *string*
     - 
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../methods/articles/search` )
   * - **$cat_id**
     - *string*
     - 
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../methods/categories/gettree` )
   * - **$barsys_depots**
     - *string*
     - 
     - `Търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове
   * - **$doc_type_id**
     - *string*
     - 
     - *Филтриране по тип документ*

			* **1** - `Фактура </barsy.help/210-dictionary/invoice.html>`__
			* **11** - `Фактура </barsy.help/210-dictionary/invoice.html>`__ ЧВ
			* **2** - *Стокова р/ка*
			* **5** - *Дебитно известие*
			* **4** - *Кредитно известие*
			* **6** - *Митническа декларация*
			* **3** - *Друго*
			* **-1** - *Неизвестен*

			 пример: "1"
   * - **$status**
     - *string*
     - 1
     - Статус на `зареждането </barsy.help/210-dictionary/storeload.html>`__ (отворено/затворено)

			* **0** - *Отворени*
			* **1** - *Затворени*

			 пример: "0"
   * - **$supplier_name**
     - *string*
     - 
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../methods/suppliers/getlist` )
   * - **$supplier_group**
     - *string*
     - 
     - Филтриране по група `доставчици </barsy.help/210-dictionary/supplier.html>`__

			* **1** - *Основна*

			 пример: "1"
   * - **$user_name**
     - *string*
     - 
     - Филтриране по `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$operation_type**
     - *string*
     - 
     - *Филтриране по тип операция*

			* **1** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__ на стока
			* **2** - *Връщане на стока*

			 пример: "1"
   * - **$details**
     - *string*
     - 
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/articledetails/gettree` )
   * - **$store_load_cat**
     - *string*
     - 
     - Филтриране по `категория </barsy.help/210-dictionary/category.html>`__ `зареждане </barsy.help/210-dictionary/storeload.html>`__

			* **1** - *Обща*
			* **2** - *Зумба*

			 пример: "1"
   * - **$paymethod_id**
     - *string*
     - 
     - Филтриране по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **1** - *В брой*
			* **2** - *Карта*

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/storeloads_details`

