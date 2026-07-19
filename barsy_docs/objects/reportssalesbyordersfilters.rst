.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsSalesByOrdersFilters
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
Lukanet\\Barsy\\Reports\\Data\\ReportsSalesByOrdersFilters


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
     - *Филтриране на редовете за избран период*
   * - **$barsys**
     - *string*
     - 
     - Филтриране по `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$article_name**
     - *string*
     - 
     - Филтриране по име на `артикул </barsy.help/210-dictionary/article.html>`__ (основно и публично). Търси се по цяло или част от името ( виж: :doc:`../methods/articles/search` )
   * - **$cat_id**
     - *string*
     - 
     - Филтрира по `категория </barsy.help/210-dictionary/category.html>`__. Подава се ID. По подразбиране търси в избраната `категория </barsy.help/210-dictionary/category.html>`__ и всички нейни подкатегории ( виж: :doc:`../methods/categories/gettree` )
   * - **$stream_id**
     - *string*
     - 
     - Филтриране по `поток </barsy.help/210-dictionary/flow.html>`__

			* **4** - *Remote*
			* **2** - Втори `поток </barsy.help/210-dictionary/flow.html>`__
			* **1** - *Основен*
			* **3** - трети `поток </barsy.help/210-dictionary/flow.html>`__

			 пример: "4"
   * - **$pos_id**
     - *string*
     - 
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$client**
     - *string*
     - 
     - Търсене по `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/clients/getlistsmart` )
   * - **$person**
     - *string*
     - 
     - Филтриране по `представител </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../methods/persons/getlist` )
   * - **$client_group_id**
     - *string*
     - 
     - *Филтриране по клиентска група* ( виж: :doc:`../methods/clients/getgroups` )
   * - **$user_id**
     - *string*
     - 
     - Филтриране по `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$role_id**
     - *string*
     - 
     - Филтриране по `роля </barsy.help/210-dictionary/role.html>`__ ( виж: :doc:`../methods/roles/getlist` )
   * - **$paymethod_id**
     - *string*
     - 
     - Филтриране по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **-5** - *Смесено*
			* **1** - *В брой*
			* **2** - *Карта*

			 пример: "-5"
   * - **$tax_id**
     - *string*
     - 
     - *Филтриране по ДДС група*

			* **2** - *20% (Б)*
			* **1** - *0% (А)*
			* **3** - *20% (В)*
			* **4** - *9% (Г)*
			* **12** - *7%*
			* **100** - *0% (Без ДДС)*

			 пример: "2"
   * - **$status**
     - *string*
     - 1
     - `Сметки </barsy.help/210-dictionary/account.html>`__

			* **0** - *Отворени*
			* **1** - *Затворени*

			 пример: "0"
   * - **$cprice_less_cprice**
     - *string*
     - 
     - *Продажна цена < от себестойност (+ДДС)*
   * - **$card_num**
     - *string*
     - 
     - *Карта №*
   * - **$details**
     - *string*
     - 
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/articledetails/gettree` )
   * - **$account_alias**
     - *string*
     - 
     - Търсене по заглавие на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$order_parent_id**
     - *string*
     - 
     - *Комбо Меню*

			* **1** - *участва в комбо меню*
			* **2** - *е комбо меню*
			* **3** - *не участва в комбо меню*

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/sales_by_orders`

