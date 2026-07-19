.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsLotListDetailsFilters
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
Lukanet\\Barsy\\Reports\\Data\\ReportsLotListDetailsFilters


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
   * - **$lot_value**
     - *string*
     - 
     - *Филтриране по партида*
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
   * - **$operation_ref_type**
     - *string*
     - 
     - *Филтриране по тип складова операция*

			* **AC** - Приключване на `сметка </barsy.help/210-dictionary/account.html>`__
			* **ST** - *Сторно*
			* **LD** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__
			* **LC** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__ корекция
			* **MV** - `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__
			* **SO** - `Изписване </barsy.help/210-dictionary/storeout.html>`__
			* **OT** - `Изписване </barsy.help/210-dictionary/storeout.html>`__ - анулирано
			* **AP** - `Производство </barsy.help/210-dictionary/storeproduction.html>`__
			* **RC** - `Ревизия </barsy.help/210-dictionary/revision.html>`__
			* **CR** - *Корекция на рецепта*
			* **AR** - *Архивиране*

			 пример: "\"AC\""
   * - **$ref_id**
     - *string*
     - 
     - *Филтриране по номер на операция*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/lot_list_details`

