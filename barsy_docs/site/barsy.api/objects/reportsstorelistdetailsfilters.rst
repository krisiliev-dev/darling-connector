.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsStoreListDetailsFilters
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
Lukanet\\Barsy\\Reports\\Data\\ReportsStoreListDetailsFilters


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
     - *Период на движенията*
   * - **$article**
     - *string*
     - 
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../methods/articles/search` )
   * - **$cat_id**
     - *string*
     - 
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../methods/categories/gettree` )
   * - **$role_id**
     - *string*
     - 
     - Филтриране по `роля </barsy.help/210-dictionary/role.html>`__ ( виж: :doc:`../methods/roles/getlist` )
   * - **$barsys_depots**
     - *string*
     - 
     - `Търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове
   * - **$user_id**
     - *string*
     - 
     - Филтриране по `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$reason_id**
     - *string*
     - 
     - *Филтриране по причина за операцията*

			* **-21** - Авансово `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-15** - *Архивиране*
			* **-4** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__
			* **-11** - `Изписване </barsy.help/210-dictionary/storeout.html>`__
			* **-6** - *Използване на карта*
			* **-5** - *Изтегляне по рецепта*
			* **-20** - *Изтегляне по рецепта - отказ*
			* **-7** - Корекция `зареждане </barsy.help/210-dictionary/storeload.html>`__
			* **-9** - *Корекция рецепта*
			* **-2** - *Местене*
			* **-19** - *Поръчка - отказ*
			* **-1** - Поръчка в `сметка </barsy.help/210-dictionary/account.html>`__
			* **-8** - `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__
			* **-10** - `Производство </barsy.help/210-dictionary/storeproduction.html>`__
			* **-14** - `Производство </barsy.help/210-dictionary/storeproduction.html>`__ по рецепта
			* **-3** - *Ревизионна корекция*
			* **-22** - *Ревизионна корекция - отказ*
			* **-16** - Сливане на `сметки </barsy.help/210-dictionary/account.html>`__
			* **-12** - *Сторно*
			* **-17** - Сторно `зареждане </barsy.help/210-dictionary/storeload.html>`__
			* **-18** - Сторно `зареждане </barsy.help/210-dictionary/storeload.html>`__ корекция

			 пример: "-21"
   * - **$ref_id**
     - *string*
     - 
     - *Филтриране по номер на операция*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/store_list_details`

