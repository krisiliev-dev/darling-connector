.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReportsSalesByArticlesFilters
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
Lukanet\\Barsy\\Reports\\Data\\ReportsSalesByArticlesFilters


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
   * - **$time_interval**
     - *string*
     - 
     - Часови интервал на `продажбите </barsy.help/210-dictionary/sale.html>`__
   * - **$barsys_depots**
     - *string*
     - 
     - `Търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове
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
   * - **$order_pos_id**
     - *string*
     - 
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$create_pos_id**
     - *string*
     - 
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$close_pos_id**
     - *string*
     - 
     - Филтриране по `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$role_id**
     - *string*
     - 
     - Филтриране по `роля </barsy.help/210-dictionary/role.html>`__ ( виж: :doc:`../methods/roles/getlist` )
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
   * - **$paymethod_id**
     - *string*
     - 
     - Филтриране по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **0** - Без `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-5** - *Смесено*
			* **1** - *В брой*
			* **2** - *Карта*

			 пример: "0"
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
   * - **$tax_region_id**
     - *string*
     - 
     - *Тип доставка / данъчен регион*

			* **1** - *Употреба на място*
			* **2** - *Доставка до адрес*
			* **3** - *Взимане на място*
			* **4** - *Получаване от офис на куриер*
			* **5** - *За вкъщи*

			 пример: "1"
   * - **$article_type**
     - *string*
     - [-1,1,2,5,6]
     - Филтриране по вид `артикул </barsy.help/210-dictionary/article.html>`__

			* **1** - `Продажба </barsy.help/210-dictionary/sale.html>`__ на `артикул </barsy.help/210-dictionary/article.html>`__
			* **2** - `Продажба </barsy.help/210-dictionary/sale.html>`__ на пакетна карта
			* **3** - Авансово `плащане </barsy.help/210-dictionary/payment.html>`__
			* **-1** - *Ползване на пакетна карта*
			* **5** - `Зареждане </barsy.help/210-dictionary/storeload.html>`__ на кл.портфейл
			* **6** - *Бакшиш*

			 пример: "1"
   * - **$supplier_id**
     - *string*
     - 
     - Филтриране по `доставчик </barsy.help/210-dictionary/supplier.html>`__ ( виж: :doc:`../methods/suppliers/getlist` )
   * - **$details**
     - *string*
     - 
     - Филтриране по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/articledetails/gettree` )
   * - **$account_alias**
     - *string*
     - 
     - Търсене по заглавие на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$invoices**
     - *string*
     - 
     - Само `сметки </barsy.help/210-dictionary/account.html>`__ без `фактура </barsy.help/210-dictionary/invoice.html>`__
   * - **$periods_weekdays**
     - *string*
     - 
     - *По ден от седмицата*

			* **2** - *Понеделник*
			* **3** - *Вторник*
			* **4** - *Сряда*
			* **5** - *Четвъртък*
			* **6** - *Петък*
			* **7** - *Събота*
			* **1** - *Неделя*

			 пример: "2"
   * - **$invoiced_accs**
     - *string*
     - 
     - Филтърът прави връзка със `сметки </barsy.help/210-dictionary/account.html>`__ и `фактури </barsy.help/210-dictionary/invoice.html>`__, като взима предвид всички видове `фактури </barsy.help/210-dictionary/invoice.html>`__ без проформите

			* **only_invoiced** - *Само фактурираните*
			* **exclude_invoiced** - *Изключи фактурираните*

			 пример: "\"only_invoiced\""
   * - **$order_parent_id**
     - *string*
     - 
     - *Комбо Меню*

			* **1** - *участва в комбо меню*
			* **2** - *е комбо меню*
			* **3** - *не участва в комбо меню*

			 пример: "1"
   * - **$delivery_address_country**
     - *string*
     - 
     - *Държава за доставка*
   * - **$place_id**
     - *string*
     - 
     - *Място*
   * - **$parents**
     - *string*
     - 
     - Филтриране по групови `артикули </barsy.help/210-dictionary/article.html>`__

			* **P** - *+ Родители*
			* **C** - *+ Деца*
			* **PC** - *+ Родители + Деца*
			* **N** - Без групови `артикули </barsy.help/210-dictionary/article.html>`__
			* **OP** - *Само Родители*
			* **OPC** - *Само Родители и деца*

			 пример: "\"P\""
   * - **$composite**
     - *string*
     - 
     - *Рецепта*

			* **0** - *Няма*
			* **1** - Има (при `продажба </barsy.help/210-dictionary/sale.html>`__)
			* **-1** - Има (при `производство </barsy.help/210-dictionary/storeproduction.html>`__)

			 пример: "0"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reports/sales_by_articles`

