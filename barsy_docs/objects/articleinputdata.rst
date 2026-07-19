.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleInputData
======================================================================================
Описание на възможни входни данни за артикул при създаване или актуализиране

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticleInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$article_name**
     - *string*
     - 
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Уникално за текущия каталог.*

			 пример: "\"\\u041a\\u0430\\u043f\\u0443\\u0447\\u0438\\u043d\\u043e\""
   * - **$article_name_public_ml**
     - *MultiLanguageData*
     - 
     - Публично име на `артикул </barsy.help/210-dictionary/article.html>`__. Мултиезично.

			*Вижда се на бележките, в публичния каталог, е-магазин и т.н. Не е уникално.*
   * - **$article_name_ml**
     - *MultiLanguageData*
     - 
     - Публично име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Мултиезично.*
   * - **$article_aliases**
     - *array* | *string* | *null*
     - 
     - Синоним/и
   * - **$article_icon**
     - *string*
     - 
     - 
   * - **$ref_num**
     - *string*
     - 
     - Референтен номер.

			*Свободен текст*

			 пример: "\"CP01\""
   * - **$barcode**
     - *array* | *string* | *null*
     - 
     - Баркод на `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "3890000000011"
   * - **$actual_price**
     - *float*
     - 
     - Базова продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "1.5"
   * - **$avg_delivery_price**
     - *float*
     - 
     - Средно претеглена доставна цена/себестойност без ДДС

			 пример: "1"
   * - **$amount_unit**
     - *float*
     - 1
     - Единица `продажба </barsy.help/210-dictionary/sale.html>`__

			 пример: "1"
   * - **$amount_prod**
     - *float*
     - 1
     - Единица `производство </barsy.help/210-dictionary/storeproduction.html>`__

			 пример: "1"
   * - **$part_factor**
     - *float*
     - 0
     - Коефициент за корекция на количество

			 пример: "10"
   * - **$amount_type_id**
     - *int*
     - 1
     - ID на типа количество

			 пример: "1" ( виж: :doc:`../methods/amounttypes/getlist` )
   * - **$lot_type_id**
     - *int*
     - 1
     - 
   * - **$stream_id**
     - *int*
     - 1
     - ID на `поток </barsy.help/210-dictionary/flow.html>`__, към който е `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/streams/getlist` )
   * - **$delete_flag**
     - *int*
     - 0
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е маркиран като изтрит

			* **0** - *Активен*
			* **1** - *Блокиран*
   * - **$is_for_sale**
     - *int*
     - 0
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се продава

			* **0** - *не може да се продава*
			* **1** - *може да се продава*
   * - **$is_for_load**
     - *int*
     - 1
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се зарежда

			* **0** - *не може да се зарежда*
			* **1** - *може да се зарежда*
   * - **$is_for_client_order**
     - *int*
     - 1
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се поръчва в `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__

			* **0** - *Не*
			* **1** - *Да*
   * - **$is_for_store_move**
     - *int*
     - 1
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се прехвърля

			* **0** - *Не*
			* **1** - *Да*
   * - **$is_for_irequest**
     - *int*
     - 1
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се ползва във `вътрешни заявки </barsy.help/210-dictionary/irequest.html>`__

			* **0** - *Не*
			* **1** - *Да*
   * - **$is_for_store_out**
     - *int*
     - 1
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се изписва

			* **0** - *не може да се изписва*
			* **1** - *може да се изписва*
   * - **$is_for_request**
     - *int*
     - 1
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се заявява към `доставчик </barsy.help/210-dictionary/supplier.html>`__

			* **0** - *Не*
			* **1** - *Да*
   * - **$is_for_sale_barsys**
     - *object*
     - 
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `продажба </barsy.help/210-dictionary/sale.html>`__ ($is_for_sale)
   * - **$is_for_client_order_barsys**
     - *object*
     - 
     - 
   * - **$is_for_irequest_barsys**
     - *object*
     - 
     - 
   * - **$is_for_store_move_barsys**
     - *object*
     - 
     - 
   * - **$is_for_store_out_barsys**
     - *object*
     - 
     - 
   * - **$is_for_request_barsys**
     - *object*
     - 
     - 
   * - **$is_for_load_barsys**
     - *object*
     - 
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `зареждане </barsy.help/210-dictionary/storeload.html>`__ ($is_for_sale)
   * - **$is_service**
     - *int*
     - 0
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е услуга

			* **0** - *Не*
			* **1** - *Да*
   * - **$is_public**
     - *int*
     - 0
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е публично видим (в публичен каталог, е-магазин)

			* **0** - *Не*
			* **1** - *Да*
   * - **$min_amount**
     - *float*
     - 
     - Минимално количество - под него сигнализира за недостатъчна наличност
   * - **$max_amount**
     - *float*
     - 
     - Максимално количество - допълно до него при `заявки към доставчици </barsy.help/210-dictionary/request.html>`__
   * - **$min_order**
     - *float*
     - 0
     - Минимално възможно количество при поръчка в `продажба </barsy.help/210-dictionary/sale.html>`__
   * - **$max_order**
     - *float*
     - 0
     - Минимално възможно количество при поръчка в `продажба </barsy.help/210-dictionary/sale.html>`__
   * - **$code**
     - *string*
     - 
     - Код на `артикул </barsy.help/210-dictionary/article.html>`__ - за бързо избиране от клавиатура,везна и др.
   * - **$user_prc**
     - *float*
     - 
     - Процент комисионна за персонал при `продажба </barsy.help/210-dictionary/sale.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$recipe_description**
     - *string*
     - 
     - 
   * - **$description_ml**
     - *MultiLanguageData*
     - 
     - Описание на `артикула </barsy.help/210-dictionary/article.html>`__ (вътрешно — етикети и служебна употреба)
   * - **$description_public_ml**
     - *MultiLanguageData*
     - 
     - Описание-публично — показва се в публичния каталог/B2B
   * - **$form_id_co**
     - *int*
     - 1
     - ID на форма за допълнителна информация за `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__
   * - **$export_id**
     - *string*
     - 
     - ID при експорт на `артикули </barsy.help/210-dictionary/article.html>`__ - например за импорт в друга система
   * - **$ref_id**
     - *int*
     - 
     - ID на `артикула </barsy.help/210-dictionary/article.html>`__ при импорт от друга система
   * - **$picture**
     - *string*
     - 
     - Основна картинка на `артикула </barsy.help/210-dictionary/article.html>`__ от наличните за него
   * - **$tax_id**
     - *int*
     - 2
     - ID на данъчната ставка ( виж: :doc:`../methods/taxgroups/getlist` )
   * - **$cat_id**
     - *array* | *int* | *null*
     - 
     - ID на `категория </barsy.help/210-dictionary/category.html>`__ (или `категории </barsy.help/210-dictionary/category.html>`__ ако е подаден масив) в които `артикула </barsy.help/210-dictionary/article.html>`__ да бъде категоризиран.

			Първата добавена `категория </barsy.help/210-dictionary/category.html>`__ става главна (ако вече няма главна) ( виж: :doc:`../methods/categories/getlist` )
   * - **$master_cat_id**
     - *int*
     - -1
     - ID на главна `категория </barsy.help/210-dictionary/category.html>`__
   * - **$details**
     - *ArticleDetailInputData*
     - 
     - Списък от характеристики към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$default_package_id**
     - *int*
     - 
     - ID на разфасовка по подразбиране (използва се при `зареждане </barsy.help/210-dictionary/storeload.html>`__) ( виж: :doc:`../methods/packages/index_` , :doc:`../methods/packages/edit` )
   * - **$sale_below_zero**
     - *string*
     - 'DEF'
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се продава без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се продава без наличност*
			* **NO** - *НЕ може да се продава без наличност*
   * - **$storemove_below_zero**
     - *string*
     - 'DEF'
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се прехвърля без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се прехвърля без наличност*
			* **NO** - *НЕ може да се прехвърля без наличност*
   * - **$storeout_below_zero**
     - *string*
     - 'DEF'
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се изписва без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се изписва без наличност*
			* **NO** - *НЕ може да се изписва без наличност*
   * - **$storeload_return_below_zero**
     - *string*
     - 'DEF'
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се връща към `доставчик </barsy.help/210-dictionary/supplier.html>`__ без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се връща без наличност*
			* **NO** - *НЕ може да се връща без наличност*
   * - **$max_amount_by_depots**
     - *object*
     - 
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове, за които има зададено максимално количество. $depot_id => max
   * - **$min_amount_by_depots**
     - *object*
     - 
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове, за които има зададено минимално количество. $depot_id => min
   * - **$slug**
     - *string*
     - 
     - Публичен URL
   * - **$intrastat**
     - *string*
     - 
     - 
   * - **$min_profit_percent**
     - *float*
     - 
     - 
   * - **$group_id**
     - *int*
     - 
     - ID на група атрибути
   * - **$delivery_price**
     - *float*
     - 
     - Доставна цена
   * - **$suppliers**
     - *object*
     - 
     - Информация за `доставчиците </barsy.help/210-dictionary/supplier.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$process_time**
     - *int*
     - 
     - Време за приготвяне - В секунди.

			Ползва се за сравнение между реалното време за изработване на `артикула </barsy.help/210-dictionary/article.html>`__ и се следи дали има закъснение при поръчката. Ако не бъде зададена стойност за конкретния `артикул </barsy.help/210-dictionary/article.html>`__, то се взема тази, която е зададена за `потока </barsy.help/210-dictionary/flow.html>`__.

			 пример: "15"
   * - **$article_color**
     - *string*
     - 
     - Цвят на `артикула </barsy.help/210-dictionary/article.html>`__ в модул `продажби </barsy.help/210-dictionary/sale.html>`__

			 пример: "\"FFFFFF\""
   * - **$extra_data**
     - *object*
     - 
     - 
   * - **$article_type**
     - *int*
     - 1
     - 
   * - **$max_discount**
     - *float*
     - 
     - 
   * - **$supplements_type**
     - *string*
     - 'combo'
     - Тип комбо `артикул </barsy.help/210-dictionary/article.html>`__.

			Влияе на визуализирането на `артикула </barsy.help/210-dictionary/article.html>`__ при обслужване, ако той има комбо групи.

			* **combo** - *Липсва описание*
			* **supplements** - *Липсва описание*

			 пример: "\"combo\""

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articles/create`
	 * :doc:`../methods/articles/update`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

