.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleData
======================================================================================
Описание на основните данни за артикул

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticleData


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
   * - :category_header:`Основни данни`
     - 
     - 
     - 
   * - **$article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$parent_id**
     - *int*
     - 
     - ID на родител
   * - **$article_name**
     - *string*
     - 
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Уникално за текущия каталог.*
   * - **$article_name_ml**
     - *MultiLanguageData*
     - 
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__.

			*Мултиезично. Не включва системното име article_name*
   * - **$article_name_cl**
     - *string*
     - 
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__ - спрямо текущият език
   * - **$article_name_public**
     - *string*
     - 
     - Публично име на `артикула </barsy.help/210-dictionary/article.html>`__

			*Вижда се на бележките, в публичния каталог, е-магазин и т.н. Не е уникално.*
   * - **$article_name_public_ml**
     - *MultiLanguageData*
     - 
     - Публично име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Мултиезично.*
   * - **$article_icon**
     - *string*
     - 
     - Икона за `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_color**
     - *string*
     - 
     - Цвят за `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$ref_num**
     - *string*
     - 
     - Референтен номер.

			*Свободен текст*
   * - **$barcode**
     - *string*
     - 
     - Баркод на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$is_service**
     - *int*
     - 
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е услуга

			* **0** - *Стока*
			* **1** - *Услуга*
   * - **$is_public**
     - *int*
     - 
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е публично видим (в публичен каталог, е-магазин)
   * - **$code**
     - *string*
     - 
     - Код на `артикул </barsy.help/210-dictionary/article.html>`__ - за бързо избиране от клавиатура,везна и др.
   * - **$description**
     - *string*
     - 
     - Описание на `артикула </barsy.help/210-dictionary/article.html>`__ - свободен текст
   * - **$description_ml**
     - *MultiLanguageData*
     - 
     - Описание на `артикула </barsy.help/210-dictionary/article.html>`__ - свободен текст.

			*Мултиезично.*
   * - **$menu_id**
     - *int*
     - 
     - Каталог, към който принадлежи `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$picture**
     - *string*
     - 
     - Основна картинка на `артикула </barsy.help/210-dictionary/article.html>`__ от наличните за него
   * - **$picture_url**
     - *string*
     - 
     - Пълен URL адрес за изтегляне на основната картинка
   * - **$slug**
     - *string*
     - 
     - Публичен URL
   * - 
     - 
     - 
     - 
   * - :category_header:`Цени и количества`
     - 
     - 
     - 
   * - **$delivery_price**
     - *float*
     - 
     - Доставна цена
   * - **$actual_price**
     - *float*
     - 
     - Базова продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_price**
     - *float*
     - 
     - Текъща `продажба </barsy.help/210-dictionary/sale.html>`__ цена (след прилагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
   * - **$original_price**
     - *float*
     - 
     - Текъща `продажба </barsy.help/210-dictionary/sale.html>`__ цена (след прилагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__) във валута
   * - **$avg_delivery_price**
     - *float*
     - 
     - Средно претеглена доставна цена/себестойност без ДДС
   * - **$current_delivery_price**
     - *float*
     - 
     - Показване на текуща доставна цена (след `ценови правила </barsy.help/210-dictionary/pricelist.html>`__)
   * - **$current_delivery_tax_id**
     - *int*
     - 
     - Показване на текуща ДДС група за `зареждане </barsy.help/210-dictionary/storeload.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__ (след `ценови правила </barsy.help/210-dictionary/pricelist.html>`__)
   * - **$amount_unit**
     - *float*
     - 
     - Единица `продажба </barsy.help/210-dictionary/sale.html>`__

			Указва коичеството, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при `продажба </barsy.help/210-dictionary/sale.html>`__ на 1.
   * - **$amount_prod**
     - *float*
     - 
     - Единица `производство </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$amount_type_id**
     - *int*
     - 
     - ID на типа количество ( виж: ``Amounttypes::getList()`` )
   * - **$min_amount**
     - *float*
     - 
     - Минимално количество

			Под него системата сигнализира за недостатъчна наличност. Ако е подаден depot_id - показва за избрания `склад </barsy.help/210-dictionary/store.html>`__, ако не е - включва глобална стойност за цялата система.
   * - **$max_amount**
     - *float*
     - 
     - Максимално количество

			Допълва се до него при `заявки към доставчици </barsy.help/210-dictionary/request.html>`__. Ако е подаден depot_id - показва за избрания `склад </barsy.help/210-dictionary/store.html>`__, ако не е - включва глобална стойност за цялата система.
   * - **$min_order**
     - *float*
     - 
     - Минимално възможно количество при поръчка в `продажба </barsy.help/210-dictionary/sale.html>`__
   * - **$max_order**
     - *float*
     - 
     - Максимално възможно количество при поръчка в `продажба </barsy.help/210-dictionary/sale.html>`__
   * - **$max_amount_by_depots**
     - *array*
     - 
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове, за които има зададено максимално количество.
   * - **$min_amount_by_depots**
     - *array*
     - 
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове, за които има зададено минимално количество.
   * - **$has_amount**
     - *bool*
     - 
     - Кратки данни (има/няма) за складова наличност за този `артикул </barsy.help/210-dictionary/article.html>`__ в цялата система
   * - **$store_amount**
     - *float*
     - 
     - Общи данни (сума за текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__) за складова наличност
   * - **$store_amount_all**
     - *float*
     - 
     - Общи данни (сума за цялата система) за складова наличност
   * - **$store_amount_details**
     - *array*
     - 
     - Разширени данни (по складове) за складова наличност
   * - **$has_amount_recipe**
     - *bool*
     - 
     - Кратки данни (има/няма) за виртуална наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта

			*За да има достатъчно наличност, трябва да има наличност за всички продукти в рецептата.*
   * - **$store_amount_recipe**
     - *float*
     - 
     - Общи данни (сума за текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__) за виртуална наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта

			*За да има достатъчно наличност, трябва да има наличност за всички продукти в рецептата.*
   * - **$store_amount_all_recipe**
     - *float*
     - 
     - Общи данни (сума за цялата система) за виртуална наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта
   * - **$store_amount_details_recipe**
     - *array*
     - 
     - Разширени данни (по складове) за виртуална наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта
   * - **$client_orders_reserved_amount**
     - *float*
     - 
     - Количество в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност
   * - **$open_orders_amount**
     - *float*
     - 
     - Количество поръчки за `артикула </barsy.help/210-dictionary/article.html>`__ в отворени `сметки </barsy.help/210-dictionary/account.html>`__.
   * - **$orders_amount**
     - *float*
     - 
     - Количество поръчки за `артикула </barsy.help/210-dictionary/article.html>`__ за зададен период

			*Изисква филтър "orders_amount_period".* ( виж: :doc:`ArticlesListFiltersData→$orders_amount_period </objects/articleslistfiltersdata>` )
   * - **$pricelist_id**
     - *int*
     - 
     - Информация по кое `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ е изчислена текущата цена
   * - **$depot_id**
     - *int*
     - 
     - `Склад </barsy.help/210-dictionary/store.html>`__ за изтегляне по подразбиране за `потока </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__ и текущата (или подадена) `каса </barsy.help/210-dictionary/pos.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
     - 
   * - **$process_time**
     - *int*
     - 
     - Време за приготвяне в секунди
   * - **$create_date**
     - *string*
     - 
     - Дата на създаване
   * - **$client_orders_reserved_last_update**
     - *string*
     - 
     - Последна промяна в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност
   * - **$store_load_last_date**
     - *string*
     - 
     - Дата на последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ на дадения `артикул </barsy.help/210-dictionary/article.html>`__

			Ако има подаден филтър по `склад </barsy.help/210-dictionary/store.html>`__ - взима се под внимание.
   * - **$remote_ref_id**
     - *int*
     - 
     - Референтно ID използвано от отдалечена система
   * - 
     - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
     - 
   * - **$stream_id**
     - *int*
     - 
     - ID на `поток </barsy.help/210-dictionary/flow.html>`__, към който е `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$delete_flag**
     - *int*
     - 
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е маркиран като изтрит
   * - **$is_for_sale**
     - *int*
     - 
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се продава

			* **0** - *не може да се продава*
			* **1** - *може да се продава*
   * - **$is_for_sale_barsys**
     - *array*
     - 
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `продажба </barsy.help/210-dictionary/sale.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `продажба </barsy.help/210-dictionary/sale.html>`__ ($is_for_sale).

			* **0** - *не може да се продава*
			* **1** - *може да се продава* ( виж: :doc:`../methods/barsys/getlist` )
   * - **$is_for_client_order**
     - *int*
     - 
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да участва в `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__

			* **0** - *не може да участва*
			* **1** - *може да участва*
   * - **$is_for_client_order_barsys**
     - *array*
     - 
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ ($is_for_client_order).

			* **0** - *не може да участва*
			* **1** - *може да участва* ( виж: :doc:`../methods/barsys/getlist` )
   * - **$is_for_load**
     - *int*
     - 
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е в `продажба </barsy.help/210-dictionary/sale.html>`__

			* **0** - *не може да се зарежда*
			* **1** - *може да се зарежда*
   * - **$is_for_load_barsys**
     - *array*
     - 
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `зареждане </barsy.help/210-dictionary/storeload.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `зареждане </barsy.help/210-dictionary/storeload.html>`__ ($is_for_load).

			* **0** - *не може да се зарежда*
			* **1** - *може да се зарежда* ( виж: :doc:`../methods/barsys/getlist` )
   * - **$is_for_store_move**
     - *int*
     - 
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се прехвърля

			* **0** - *не може да се прехвърля*
			* **1** - *може да се прехвърля*
   * - **$is_for_store_move_barsys**
     - *array*
     - 
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ ($is_for_store_move).

			* **0** - *не може да се прехвърля*
			* **1** - *може да се прехвърля* ( виж: :doc:`../methods/barsys/getlist` )
   * - **$is_for_irequest**
     - *int*
     - 
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е може да участва във `вътрешна заявка </barsy.help/210-dictionary/irequest.html>`__

			* **0** - *не може*
			* **1** - *може*
   * - **$is_for_irequest_barsys**
     - *array*
     - 
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `вътрешна заявка </barsy.help/210-dictionary/irequest.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `вътрешна заявка </barsy.help/210-dictionary/irequest.html>`__ ($is_for_irequest).

			* **0** - *не може да участва*
			* **1** - *може да участва* ( виж: :doc:`../methods/barsys/getlist` )
   * - **$export_id**
     - *string*
     - 
     - ID при експорт на `артикули </barsy.help/210-dictionary/article.html>`__ - например за импорт в друга система
   * - **$ref_id**
     - *int*
     - 
     - ID на `артикула </barsy.help/210-dictionary/article.html>`__ при импорт от друга система
   * - **$sale_below_zero**
     - *string*
     - 
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се продава без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се продава без наличност*
			* **NO** - *НЕ може да се продава без наличност*
   * - **$storemove_below_zero**
     - *string*
     - 
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се прехвърля без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се прехвърля без наличност*
			* **NO** - *НЕ може да се прехвърля без наличност*
   * - **$storeload_return_below_zero**
     - *string*
     - 
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се връща към `доставчик </barsy.help/210-dictionary/supplier.html>`__ без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се връща без наличност*
			* **NO** - *НЕ може да се връща без наличност*
   * - **$storeout_below_zero**
     - *string*
     - 
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се изписва без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се изписва без наличност*
			* **NO** - *НЕ може да се изписва без наличност*
   * - **$intrastat**
     - *string*
     - 
     - Intrastat код
   * - **$lot_type_id**
     - *int*
     - 
     - Партиди - тип употреба
   * - **$article_details**
     - *array*
     - 
     - Всички характеристики за `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$has_attributes**
     - *bool*
     - 
     - Флаг дали `артикула </barsy.help/210-dictionary/article.html>`__ има атрибути (вариции)
   * - **$has_supplements**
     - *bool*
     - 
     - Флаг дали `артикула </barsy.help/210-dictionary/article.html>`__ има комбо групи (пакетно предложение)
   * - **$supplements_type**
     - *string*
     - 
     - Тип комбо `артикул </barsy.help/210-dictionary/article.html>`__ (Комбо меню или `Артикул </barsy.help/210-dictionary/article.html>`__ със съставки)

			* **0** - *combo*
			* **1** - *supplements*
   * - **$ml_data**
     - *array*
     - 
     - Включва всички мултиезични данни към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$composite**
     - *int*
     - 
     - Съставен `артикул </barsy.help/210-dictionary/article.html>`__ (обикновен,съставен при приключване,съставен при `производство </barsy.help/210-dictionary/storeproduction.html>`__)

			* **0** - *Без рецепта*
			* **1** - *Рецепта при приключване*
			* **-1** - Рецепта при `производство </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$group_attributes_options**
     - *array*
     - 
     - Опциите на атрибутите за `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$group_attributes**
     - *array*
     - 
     - Информация за групоте атрибути, техните опции и id в отдалечена система
   * - **$form_data**
     - *array*
     - 
     - Структура на формуляра за допълнителни полета към този `артикул </barsy.help/210-dictionary/article.html>`__ при взимане на поръчка
   * - **$form_data_public**
     - *array*
     - 
     - Структура на формуляра за допълнителни публични полета към този `артикул </barsy.help/210-dictionary/article.html>`__ при взимане на поръчка
   * - 
     - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
     - 
   * - **$has_upsell**
     - *int*
     - 
     - Флаг, дали `артикулът </barsy.help/210-dictionary/article.html>`__ има връзка "Надграждане" с предложения за замяна
   * - **$has_addon**
     - *int*
     - 
     - Флаг, дали `артикулът </barsy.help/210-dictionary/article.html>`__ има връзка "Допълнение" с предложения за добавяне
   * - 
     - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
     - 
   * - **$user_prc**
     - *float*
     - 
     - Процент комисионна за персонал при `продажба </barsy.help/210-dictionary/sale.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_id**
     - *int*
     - 
     - ID на данъчната ставка
   * - **$actual_tax_id**
     - *int*
     - 
     - ID на базовата данъчна ставка (преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
   * - **$min_profit_percent**
     - *float*
     - 
     - Минимален процент печалба
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$form_id_co**
     - *int*
     - 
     - ID на форма за допълнителна информация за `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__
   * - **$files**
     - *string*
     - 
     - Списък за всички прикачени файлове към `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/files/getlist` )
   * - **$default_package_id**
     - *int*
     - 
     - ID на разфасовка по подразбиране (използва се при `зареждане </barsy.help/210-dictionary/storeload.html>`__) ( виж: :doc:`../methods/packages/getlist` )
   * - **$package_details**
     - *array*
     - 
     - Информация за пакетната единица по подразбиране за този `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/packages/getlist` )
   * - **$suppliers_details**
     - *array*
     - 
     - Данни за `доставчиците </barsy.help/210-dictionary/supplier.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$supplements**
     - *array*
     - 
     - Списък на комбо групите, включени в `артикула </barsy.help/210-dictionary/article.html>`__ (ако има такива)
   * - **$inv_ref_num**
     - *string*
     - 
     - Показва референтент номер на `артикула </barsy.help/210-dictionary/article.html>`__, използван за `фактури </barsy.help/210-dictionary/invoice.html>`__ (според настройките на системата)
   * - **$client_ref_num**
     - *string*
     - 
     - Показва референтент номер на `артикула </barsy.help/210-dictionary/article.html>`__, специфично за подадения `клиент </barsy.help/210-dictionary/client.html>`__ (като филтър)
   * - 
     - 
     - 
     - 
   * - :category_header:`Категории и класификация`
     - 
     - 
     - 
   * - **$master_cat_id**
     - *int*
     - 
     - ID на основната `категория </barsy.help/210-dictionary/category.html>`__ ( виж: :doc:`../methods/categories/getlist` )
   * - **$master_cat**
     - *string*
     - 
     - Име на основната `категория </barsy.help/210-dictionary/category.html>`__ ( виж: :doc:`../methods/categories/getlist` )
   * - **$categories**
     - *string*
     - 
     - Списък от ID на всички `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/categories/getlist` )
   * - **$categories_names**
     - *string*
     - 
     - Списък от имена на всички `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/categories/getlist` )
   * - **$categories_paths**
     - *string*
     - 
     - Списък от пътища на всички `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/categories/getlist` )
   * - **$categories_details**
     - *array*
     - 
     - Подробности за всички `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/categories/getlist` )
   * - **$group_id**
     - *int*
     - 
     - ID на група на `артикула </barsy.help/210-dictionary/article.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articles/getlistobject`
	 * :doc:`../methods/articles/getlist`
	 * :doc:`../methods/articles/get`
	 * :doc:`../methods/articles/search`
	 * :doc:`../methods/categories/getalltree`
	 * :doc:`../methods/categories/gettree`
	 * :doc:`../methods/categories/print`
	 * :doc:`../methods/edocs/get_catalog`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

