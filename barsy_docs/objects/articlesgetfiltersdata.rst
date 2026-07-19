.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticlesGetFiltersData
======================================================================================
Списък с наличните филтри, които могат да се подават при изтегляне на списък с артикули

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticlesGetFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_id**
     - *int*
     - 
     - Филтър по `клиент </barsy.help/210-dictionary/client.html>`__.

			*Използва е за изчислване на текуща цена*

			 пример: "1"
   * - **$client_group_id**
     - *int*
     - 
     - Филтър по клиентска група.

			*Използва се за изчислване на текуща цена*

			 пример: "1" ( виж: :doc:`../methods/clientgroups/getlist` )
   * - **$country_id**
     - *string*
     - 
     - Филтър по държава.

			*Използва се за изчислване на текуща цена*

			 пример: "\"GR\"" ( виж: :doc:`../methods/destinations/getlistcountries` )
   * - **$delivery_type_id**
     - *string*
     - 
     - Филтър по тип доставка.

			*Използва се за изчислване на текуща цена*

			* **no** - *Без доставка*
			* **home** - *За вкъщи*
			* **address** - *Доставка до адрес*
			* **barsy** - Получаване от `търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **office** - *Получаване от офис на куриер*

			 пример: "\"address\""
   * - **$currency_id**
     - *int*
     - 
     - Филтър по валута.

			*Използва се за изчислване на текуща цена*

			 пример: "-1" ( виж: :doc:`../methods/currencies/getlist` )
   * - **$pos_id**
     - *int*
     - 
     - Филтър по `каса </barsy.help/210-dictionary/pos.html>`__.

			*Използва е за изчислване на текуща цена*

			 пример: "1" ( виж: :doc:`../methods/poses/getlist` )
   * - **$depot_id**
     - *int*
     - 
     - Филтър по `склад </barsy.help/210-dictionary/store.html>`__.

			Валиден ако са поискани складовите количества за `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "1" ( виж: :doc:`../methods/depots/getlist` )
   * - **$depot_group_id**
     - *int*
     - 
     - Филтър по група складове.

			Валиден ако са поискани складовите количества за `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "1" ( виж: :doc:`../methods/depots/getgrouplist` )
   * - **$orders_amount_period**
     - *datetime*
     - 
     - Филтър по период на количество поръчки за `артикули </barsy.help/210-dictionary/article.html>`__.

			*Изисква extra_element "orders_amount"*

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articles/get`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

