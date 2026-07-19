.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticlesListFiltersData
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
Lukanet\\Barsy\\Articles\\Data\\ArticlesListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - 
     - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
     - 
   * - **$article_id**
     - *int*
     - 
     - Филтър по ID на `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$code**
     - *string*
     - 
     - Филтър по код на `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$ref_id**
     - *int*
     - 
     - Филтър по референтен идентификатор

			 пример: "123"
   * - **$ref_num**
     - *string*
     - 
     - Филтър по референтен номер

			 пример: "123"
   * - **$ref_num_eq**
     - *string*
     - 
     - Филтрира по точен референтен номер
   * - **$barcode**
     - *string*
     - 
     - Филтър по баркод - може да търси по част от баркода

			 пример: "1234567890123"
   * - **$barcode_eq**
     - *string*
     - 
     - Филтър по баркод - точна стойност

			 пример: "1234567890123"
   * - **$export_id**
     - *string*
     - 
     - Филтър по идентификатор за експорт

			 пример: "999"
   * - **$ref_num_group_main**
     - *string*
     - 
     - Филтър по главен обединяващ `артикул </barsy.help/210-dictionary/article.html>`__ (чрез характеристика) при `артикули </barsy.help/210-dictionary/article.html>`__ с ref_num
   * - **$search_article_ids**
     - *int*
     - 
     - Филтър по ID-та на `артикули </barsy.help/210-dictionary/article.html>`__.

			*Подреждане на резултатите по подадените id-та*

			 пример: "1"
   * - **$remote_ref_id**
     - *int*
     - 
     - Филтър по ID на продукта в отдалечена система

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$article_name**
     - *string*
     - 
     - Филтър по име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Намира и при частично съвпадение*

			 пример: "\"Beer\""
   * - **$article_name_eq**
     - *string*
     - 
     - Филтрира по точно име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$alias_name**
     - *string*
     - 
     - Филтър по синоним на `артикул </barsy.help/210-dictionary/article.html>`__ (включва и имената)

			 пример: "\"Beer Alias\""
   * - **$description**
     - *string*
     - 
     - Филтър по описание на `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "\"Very Good beer\""
   * - **$recipe_description**
     - *string*
     - 
     - Филтър по описание на рецептата

			 пример: "\"Milk\""
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$create_date**
     - *datetime*
     - 
     - Филтър по дата на създаване на `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$last_update**
     - *datetime*
     - 
     - Филтър по последна промяна в данните за `артикула </barsy.help/210-dictionary/article.html>`__

			Обхваща основни данни, характеристики, категоризирания, `ценови правила </barsy.help/210-dictionary/pricelist.html>`__ и др.

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$amount_last_update**
     - *datetime*
     - 
     - Филтър по последна промяна в складовите наличности за `артикула </barsy.help/210-dictionary/article.html>`__.

			*Актуализира за при всяка складова операция*

			 пример: "\"2018-01-01 00:00:00\""
   * - **$all_last_update**
     - *datetime*
     - 
     - Филтър по последна промяна спрямо датата на складовите наличности за `артикула </barsy.help/210-dictionary/article.html>`__ ИЛИ последната промяна на основните данни на `артикула </barsy.help/210-dictionary/article.html>`__ ИЛИ последна промяна в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност

			*Комбинира филтрите last_update и amount_last_update*

			 пример: "\"2018-12-31 23:59:00\""
   * - **$orders_amount_period**
     - *datetime*
     - 
     - Филтър по период на количество поръчки за `артикули </barsy.help/210-dictionary/article.html>`__.

			*Изисква extra_element "orders_amount"*

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - 
     - 
     - 
     - 
   * - :category_header:`Цени и количества`
     - 
     - 
     - 
   * - **$min_amount**
     - *float*
     - 
     - Филтър по минимално складово количество

			 пример: "0.1"
   * - **$actual_price**
     - *float*
     - 
     - Филтър по базова цена

			 пример: "1.2"
   * - **$amount_unit**
     - *float*
     - 
     - Филтър по единица `продажба </barsy.help/210-dictionary/sale.html>`__

			 пример: "0.5"
   * - **$user_prc**
     - *float*
     - 
     - Филтър по процент за персонала

			 пример: "10"
   * - **$max_amount**
     - *float*
     - 
     - Филтър по максимално количество

			 пример: "15"
   * - **$amount_prod**
     - 
     - 
     - Филтър по количество `производство </barsy.help/210-dictionary/storeproduction.html>`__

			 пример: "1.5"
   * - **$delivery_price**
     - *float*
     - 
     - Филтър по последна доставна цена (без ДДС)

			 пример: "2.3"
   * - **$avg_delivery_price**
     - *float*
     - 
     - Филтър по средно претеглена доставна цена (без ДДС)

			 пример: "2.24"
   * - **$current_price_diff**
     - *string*
     - 
     - Филтър за разлика между текуща и базова цена

			* **> или 'gt'** - *текуща > базова*
			* **< или 'lt'** - *текуща < базова*
			* **= или 'eq'** - *текуща равна на базова*
   * - **$discount_percent**
     - *string*
     - 
     - Филтър по интервали за процент отстъпка.

			*Процент отстъпка се формира от текуща и базова цена*
   * - **$has_amount**
     - *bool*
     - 
     - Филтър по наличност - връща само `артикулите </barsy.help/210-dictionary/article.html>`__ с положителна наличност
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$composite**
     - *int*
     - 
     - Филтър по тип `артикул </barsy.help/210-dictionary/article.html>`__

			Възможни стойности: обикновен, съставен при приключване, съставен при `производство </barsy.help/210-dictionary/storeproduction.html>`__.

			 пример: "1"
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по признак за изтрит `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$article_type**
     - *int*
     - 
     - Филтър по тип на `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$is_for_sale**
     - *int* | *array*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ е в `продажба </barsy.help/210-dictionary/sale.html>`__

			 пример: "1"
   * - **$is_for_client_order**
     - *int* | *array*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ може да участва в `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__

			 пример: "1"
   * - **$is_for_load**
     - *int* | *array*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ може да се зарежда

			 пример: "1"
   * - **$is_for_store_move**
     - *int* | *array*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ може да се прехвърля

			 пример: "1"
   * - **$is_for_store_out**
     - *int* | *array*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ може да се изписва

			 пример: "1"
   * - **$is_for_request**
     - *int* | *array*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ може да се заявява към `доставчик </barsy.help/210-dictionary/supplier.html>`__

			 пример: "1"
   * - **$is_for_irequest**
     - *int* | *array*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ може да се използва за `вътрешна заявка </barsy.help/210-dictionary/irequest.html>`__

			 пример: "1"
   * - **$is_for_sale_barsys**
     - *int* | *array*
     - 
     - 

			 пример: "1"
   * - **$is_for_load_barsys**
     - *int* | *array*
     - 
     - 

			 пример: "1"
   * - **$is_for_store_out_barsys**
     - *int* | *array*
     - 
     - 

			 пример: "1"
   * - **$is_for_irequest_barsys**
     - *int* | *array*
     - 
     - 

			 пример: "1"
   * - **$is_for_request_barsys**
     - *int* | *array*
     - 
     - 

			 пример: "1"
   * - **$is_service**
     - *int*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ е услуга

			 пример: "1"
   * - **$is_public**
     - *int*
     - 
     - Филтър дали `артикулът </barsy.help/210-dictionary/article.html>`__ е публичен

			 пример: "1"
   * - **$recipe_component**
     - *array*
     - 
     - Филтър по участие в рецепта ['Ne'=>'Не участва в рецепта', 'R1'=>'Участва в рецепта', 'R2'=>'Участва в `производство </barsy.help/210-dictionary/storeproduction.html>`__']

			 пример: "\"R1\""
   * - **$use_lots**
     - *int*
     - 
     - Филтър флаг за партидност на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$for_remote_update**
     - *int*
     - 
     - Филтър по това, дали продукта е обновяван в Барси

			 пример: "1"
   * - **$for_remote_update_child**
     - *int*
     - 
     - Филтър по това, дали дъщерният `артикул </barsy.help/210-dictionary/article.html>`__ е обновяван в Барси

			 пример: "1"
   * - **$parent_delete_flag**
     - *int*
     - 
     - Прилага се при вземане на дъщерни `артикули </barsy.help/210-dictionary/article.html>`__ (вариации) и искаме вземем само вариации, чиито родител не е с вдигнат delete_flag

			 пример: "1"
   * - **$add_parent_groups**
     - *int*
     - 
     - 
   * - **$no_parent**
     - *int*
     - 
     - 
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$amount_type_id**
     - *int*
     - 
     - Филтър по тип на количеството

			 пример: "1" ( виж: :doc:`../methods/amounttypes/getlist` )
   * - **$stream_id**
     - *int*
     - 
     - Филтър по `поток </barsy.help/210-dictionary/flow.html>`__

			 пример: "1" ( виж: :doc:`../methods/streams/getlist` )
   * - **$group_id**
     - *int*
     - 
     - Филтър по група

			 пример: "1"
   * - **$parent_id**
     - *int*
     - 
     - Филтър по родител

			 пример: "1"
   * - **$user_id**
     - *int*
     - 
     - Филтър по `потребител </barsy.help/210-dictionary/user.html>`__, създал `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$form_id_co**
     - *int*
     - 
     - Филтър по ID на форма за допълнителна информация в `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__

			 пример: "1"
   * - **$cat_id**
     - *int*
     - 
     - Филтър по `категория </barsy.help/210-dictionary/category.html>`__

			 пример: "1"
   * - **$parent_cat_id**
     - *int*
     - 
     - Филтър по родителска `категория </barsy.help/210-dictionary/category.html>`__

			Връща всички `артикули </barsy.help/210-dictionary/article.html>`__ от тази `категория </barsy.help/210-dictionary/category.html>`__ или нейните подкатегории. С опция mode=exclude изборът се обръща (изключва вместо включва).
   * - **$single_cat_id**
     - *int*
     - 
     - Филтър по единична `категория </barsy.help/210-dictionary/category.html>`__

			 пример: "1"
   * - **$master_cat_id**
     - *int*
     - 
     - Филтър по главна `категория </barsy.help/210-dictionary/category.html>`__

			 пример: "1"
   * - **$cat_id_deep**
     - *int*
     - 
     - Филтър по `категория </barsy.help/210-dictionary/category.html>`__ и всички вложени в нея

			Филтрирането се извършва пряко по `категориите </barsy.help/210-dictionary/category.html>`__, а не по `артикулите </barsy.help/210-dictionary/article.html>`__.

			 пример: "1"
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
   * - **$menu_id**
     - *int*
     - 
     - Филтър по ID на каталог

			 пример: "1"
   * - **$lot_type_id**
     - *int*
     - 
     - Филтър по тип партидност
   * - **$remote_id**
     - *int*
     - 
     - Филтърът по ID на отдалечена системи, за която да бъде върната remote информацията за `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$card_type_id**
     - 
     - 
     - 
   * - 
     - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
     - 
   * - **$picture**
     - *string*
     - 
     - Филтър по основна картинка

			 пример: "\"Pic.jpg\""
   * - **$article_details**
     - *object*
     - 
     - Филтър по характеристики на `артикула </barsy.help/210-dictionary/article.html>`__.

			*Подава се като масив от ключове и стойности, където ключът е името (или id) на характеристиката,a стойност - желаната стойността (или id й). {ключ1=>стойност1,ключ2=>стойност2,ключ3=>{стойност3,стойност4}, ...}*

			 пример: "{\"\\u0426\\u0432\\u044f\\u0442\":\"\\u0437\\u0435\\u043b\\u0435\\u043d\"}"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articles/getlist`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

