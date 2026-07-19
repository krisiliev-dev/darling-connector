.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articles_get
===========================================================
Подробни данни за конкретен артикул

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/100-catalog/articles/index </barsy.help/110-admin/100-catalog/articles/index.html>`__
	 * barsy.help: `210-dictionary/article </barsy.help/210-dictionary/article.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълния запис на един `артикул </barsy.help/210-dictionary/article.html>`__ по неговото ID — основни данни (име, код, баркод, цена, ДДС група, мерна единица), `категории </barsy.help/210-dictionary/category.html>`__, атрибути, връзка с `поток </barsy.help/210-dictionary/flow.html>`__ и `доставчици </barsy.help/210-dictionary/supplier.html>`__. Чрез параметъра `extra_properties` могат да се поискат допълнителни секции като наличности по складове, рецепта, `ценови правила </barsy.help/210-dictionary/pricelist.html>`__, изображения, мета-данни. Филтрите позволяват изчисляване на цена и наличност в контекст на конкретна `каса </barsy.help/210-dictionary/pos.html>`__, `склад </barsy.help/210-dictionary/store.html>`__, дата или `клиент </barsy.help/210-dictionary/client.html>`__ — така един и същ `артикул </barsy.help/210-dictionary/article.html>`__ може да върне различна продажна цена в зависимост от `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, които действат към момента на заявката.

Типични случаи: показване на карта на `артикул </barsy.help/210-dictionary/article.html>`__ в кошницата на онлайн магазин, презареждане на актуални данни в POS интерфейса, проверка на наличност преди добавяне към поръчка, синхронизация на каталог към външна система.

**Име**: Articles_get
**Категория**: Catalog


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - ID на желания `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$filters**
     - ArticlesGetFiltersData_ 
     - Допълнителни параметри за изчислване на цена, наличност и други **По подразбиране:** []
   * - **$extra_properties**
     - ArticlesListExtraPropertiesData_ 
     -  **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ArticleData_                                                           Данни за тях според исканите ($extra_properties)
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ArticlesGetFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Списък с наличните филтри, които могат да се подават при изтегляне на списък с `артикули </barsy.help/210-dictionary/article.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticlesGetFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$client_id**
     - *int*
     - Филтър по `клиент </barsy.help/210-dictionary/client.html>`__.

			*Използва е за изчислване на текуща цена*
   * - **$client_group_id**
     - *int*
     - Филтър по клиентска група.

			*Използва се за изчислване на текуща цена* ( виж: :doc:`../clientgroups/getlist` )
   * - **$country_id**
     - *string*
     - Филтър по държава.

			*Използва се за изчислване на текуща цена* ( виж: :doc:`../destinations/getlistcountries` )
   * - **$delivery_type_id**
     - *string*
     - Филтър по тип доставка.

			*Използва се за изчислване на текуща цена*

			* **no** - *Без доставка*
			* **home** - *За вкъщи*
			* **address** - *Доставка до адрес*
			* **barsy** - Получаване от `търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **office** - *Получаване от офис на куриер*
   * - **$currency_id**
     - *int*
     - Филтър по валута.

			*Използва се за изчислване на текуща цена* ( виж: :doc:`../currencies/getlist` )
   * - **$pos_id**
     - *int*
     - Филтър по `каса </barsy.help/210-dictionary/pos.html>`__.

			*Използва е за изчислване на текуща цена* ( виж: :doc:`../poses/getlist` )
   * - **$depot_id**
     - *int*
     - Филтър по `склад </barsy.help/210-dictionary/store.html>`__.

			Валиден ако са поискани складовите количества за `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../depots/getlist` )
   * - **$depot_group_id**
     - *int*
     - Филтър по група складове.

			Валиден ако са поискани складовите количества за `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../depots/getgrouplist` )
   * - **$orders_amount_period**
     - *datetime*
     - Филтър по период на количество поръчки за `артикули </barsy.help/210-dictionary/article.html>`__.

			*Изисква extra_element "orders_amount"*

-----

ArticlesListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към даден `артикул </barsy.help/210-dictionary/article.html>`__.
		Могат да се подадат повече от един като масив. Добавят се към основните данните за всеки `артикул </barsy.help/210-dictionary/article.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticlesListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Основни данни`
     - 
     - 
   * - **$common**
     - *string*
     - Обем на върнатите основни данни

			*Определя кои основни данни да се върнат. Възможни стойности: min, common, all, public.* **По подразбиране:** 'common'
   * - **$code**
     - *bool*
     - Код на `артикула </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - **$article_name_ml**
     - MultiLanguageData_ 
     - Обект с името на `артикул </barsy.help/210-dictionary/article.html>`__ в различните езици **По подразбиране:** false
   * - **$article_icon**
     - *bool*
     - Икона на `артикула </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - **$article_color**
     - *bool*
     - Цвят на `артикула </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - **$picture**
     - *bool*
     - Име на изображениеето на `артикула </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - **$article_type**
     - *bool*
     - Тип на `артикула </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Категории и класификация`
     - 
     - 
   * - **$master_cat**
     - *bool*
     - име на основната `категория </barsy.help/210-dictionary/category.html>`__
   * - **$categories**
     - *bool*
     - данни за всички `категории </barsy.help/210-dictionary/category.html>`__,
   * - **$categories_names**
     - *bool*
     - имена за другите `категории </barsy.help/210-dictionary/category.html>`__
   * - **$categories_paths**
     - *bool*
     - пътища на всички `категории </barsy.help/210-dictionary/category.html>`__
   * - **$categories_details**
     - *bool*
     - Подробности за всички `категории </barsy.help/210-dictionary/category.html>`__ **По подразбиране:** false
   * - **$group_id**
     - *bool*
     - ID на група на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$categories_remote_details**
     - *bool*
     - Подробности за `категориите </barsy.help/210-dictionary/category.html>`__ в отдалечени системи **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$suppliers_details**
     - *bool*
     - данни за `доставчиците </barsy.help/210-dictionary/supplier.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_delivery_data**
     - *bool*
     - Текуща доставна цена и ДДС група

			Връща текущата доставна цена и текущата ДДС група след прилагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__.
   * - **$files**
     - *string*
     - Информация за всички прикачени файлове към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$supplements**
     - *bool*
     - Списък на комбо групите, включени в `артикула </barsy.help/210-dictionary/article.html>`__ (ако има такива)
   * - **$remote_ref_id**
     - *int*
     - Референтно ID използвано от отдалечена система
   * - **$parent_remote_ref_id**
     - *bool*
     - ID на родителския `артикул </barsy.help/210-dictionary/article.html>`__ в отдалечена система(Използва се при груповите атрибути) **По подразбиране:** false
   * - **$client_ref_num**
     - *bool*
     - Показва референтент номер на `артикула </barsy.help/210-dictionary/article.html>`__, специфично за подадения `клиент </barsy.help/210-dictionary/client.html>`__ (като филтър) **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Цени и количества`
     - 
     - 
   * - **$has_amount**
     - *bool*
     - Кратки данни (има/няма) за складова наличност
   * - **$store_amount**
     - *bool*
     - Складова наличност за текущия обект

			Общи данни (сума) за складовата наличност в текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__.
   * - **$store_amount_all**
     - *bool*
     - Складова наличност за цялата система

			*Общи данни (сума) за складовата наличност в цялата система.*
   * - **$total_store_amount**
     - *bool*
     - Обща складова наличност за обекта

			Връща складовата наличност за целия `търговски обект </barsy.help/210-dictionary/barsy.html>`__, независимо от избрания `склад </barsy.help/210-dictionary/store.html>`__. **По подразбиране:** false
   * - **$store_amount_details**
     - *bool*
     - Разширени данни (по складове) за складова наличност
   * - **$has_amount_recipe**
     - *bool*
     - Виртуална наличност (има/няма)

			Кратки данни дали има виртуална наличност за `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта.
   * - **$store_amount_recipe**
     - *bool*
     - Виртуална наличност за текущия обект

			Общи данни (сума) за виртуалната наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта в текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__.
   * - **$store_amount_all_recipe**
     - *bool*
     - Виртуална наличност за цялата система

			Общи данни (сума) за виртуалната наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта в цялата система.
   * - **$store_amount_details_recipe**
     - *bool*
     - Виртуална наличност по складове

			Разширени данни (по складове) за виртуалната наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта.
   * - **$client_orders_reserved_amount**
     - *bool*
     - Резервирано количество по заявки

			Количеството в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност.
   * - **$open_orders_amount**
     - *bool*
     - Количество поръчки за `артикула </barsy.help/210-dictionary/article.html>`__ в отворени `сметки </barsy.help/210-dictionary/account.html>`__.
   * - **$orders_amount**
     - *bool*
     - Количество поръчки за `артикула </barsy.help/210-dictionary/article.html>`__ за зададен период.

			*Изисква филтър "orders_amount_period"*
   * - **$pricelist_id**
     - *bool*
     - Информация по кое `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ е изчислена текущата цена
   * - **$client_orders_amount**
     - *bool*
     - Информация за количество, което е в "отворени" `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__ (според настройка на статусите на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__)
   * - **$show_min_max_inventory**
     - *bool*
     - Показва информация за минимално/максимално количество на наличност.

			Ако е подаден depot_id - показва за избрания `склад </barsy.help/210-dictionary/store.html>`__, ако не е - включва глобална стойност за цялата система **По подразбиране:** false
   * - **$current_price**
     - *bool*
     - Текуща продажна цена **По подразбиране:** false
   * - **$amount_type_id**
     - *bool*
     - ID на мерната единица **По подразбиране:** false
   * - **$actual_price**
     - *bool*
     - Базова цена **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
   * - **$client_orders_reserved_last_update**
     - *bool*
     - Последна промяна на `резервациите </barsy.help/210-dictionary/reservation.html>`__

			Дата на последната промяна в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност.
   * - **$store_load_last_date**
     - *bool*
     - Дата на последно `зареждане </barsy.help/210-dictionary/storeload.html>`__

			Дата на последното `зареждане </barsy.help/210-dictionary/storeload.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__. Ако е избран `склад </barsy.help/210-dictionary/store.html>`__, се отчита само за него.
   * - **$remote_last_update**
     - *string*
     - Дата на последна актуализация на `артикула </barsy.help/210-dictionary/article.html>`__ в отдалечена система
   * - **$process_time**
     - *bool*
     -  **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
   * - **$article_details**
     - *string*
     - Всички характеристики за `артикула </barsy.help/210-dictionary/article.html>`__ [1=JSON списък,flat=отделни стойности]
   * - **$picture_content**
     - *int*
     - Съдържание (base64) на основната картинка

			*(Внимание: натоварва изключително изтеглянето. Да се ползва в подходящи ситуации)*
   * - **$picture_url**
     - *string*
     - URL адрес за изтегляне на основната картинка
   * - **$has_attributes**
     - *bool*
     - Флаг дали `артикула </barsy.help/210-dictionary/article.html>`__ има атрибути (вариции)
   * - **$has_supplements**
     - *bool*
     - Флаг дали `артикула </barsy.help/210-dictionary/article.html>`__ има комбо групи
   * - **$limits_by_barsys**
     - *bool*
     - Информация за ограничения за `продажби </barsy.help/210-dictionary/sale.html>`__, зареждания, прехвърляния, `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, `вътрешни заявки </barsy.help/210-dictionary/irequest.html>`__ по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__
   * - **$ml_data**
     - *bool*
     - Включва всички мултиезични данни към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$composite**
     - *bool*
     - Съставен `артикул </barsy.help/210-dictionary/article.html>`__ (обикновен,съставен при приключване,съставен при `производство </barsy.help/210-dictionary/storeproduction.html>`__)
   * - **$group_attributes_options**
     - *bool*
     - Опциите на атрибутите за `артикул </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - **$group_attributes**
     - *bool*
     - Информация за групоте атрибути, техните опции и id в отдалечена система **По подразбиране:** false
   * - **$slug**
     - *string*
     - Slug на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$form_data**
     - *bool*
     -  **По подразбиране:** false
   * - **$form_data_public**
     - *bool*
     - 
   * - **$package_details**
     - *bool*
     -  **По подразбиране:** false
   * - **$extra_data**
     - *bool*
     -  **По подразбиране:** false
   * - **$eshop_router**
     - *bool*
     -  **По подразбиране:** true
   * - **$supplements_type**
     - *bool*
     -  **По подразбиране:** false
   * - **$list_count**
     - *bool*
     - Определя, дали да се върне $count в ArticlesListData **По подразбиране:** false
   * - **$stream_name**
     - *bool*
     - Име на `поток </barsy.help/210-dictionary/flow.html>`__ **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
   * - **$tax_id**
     - *bool*
     - ID на данъчната група на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../taxgroups/getlist` )
   * - **$inv_ref_num**
     - 
     - Показва референтент номер на `артикула </barsy.help/210-dictionary/article.html>`__, използван за `фактури </barsy.help/210-dictionary/invoice.html>`__ (според настройките на системата)
   * - **$discount**
     - *bool*
     - Отстъпка на `артикула </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
   * - **$has_upsell**
     - *bool*
     - Флаг дали `артикулът </barsy.help/210-dictionary/article.html>`__ има връзка "Надграждане" с предложения за замяна
   * - **$has_addon**
     - *bool*
     - Флаг дали `артикулът </barsy.help/210-dictionary/article.html>`__ има връзка "Допълнение" с предложения за добавяне
   * - **$client_package_id**
     - *bool*
     - Показва разфасовката по подразбиране за подадения `клиент </barsy.help/210-dictionary/client.html>`__ (като филтър) — конфигурация `артикул </barsy.help/210-dictionary/article.html>`__-`клиент </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false

-----

MultiLanguageData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: MultiLanguageData

   * - Параметър
     - Тип
     - Описание
   * - **$bg_BG**
     - *string*
     - 
   * - **$en_US**
     - *string*
     - 
   * - **$de_DE**
     - *string*
     - 
   * - **$es_ES**
     - *string*
     - 
   * - **$fr_FR**
     - *string*
     - 
   * - **$it_IT**
     - *string*
     - 
   * - **$ro_RO**
     - *string*
     - 
   * - **$ru_RU**
     - *string*
     - 
   * - **$sr_RS**
     - *string*
     - 
   * - **$el_GR**
     - *string*
     - 
   * - **$tr_TR**
     - *string*
     - 

-----

ArticleData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Описание на основните данни за `артикул </barsy.help/210-dictionary/article.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Основни данни`
     - 
     - 
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$parent_id**
     - *int*
     - ID на родител
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Уникално за текущия каталог.*
   * - **$article_name_ml**
     - MultiLanguageData_ 
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__.

			*Мултиезично. Не включва системното име article_name*
   * - **$article_name_cl**
     - *string*
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__ - спрямо текущият език
   * - **$article_name_public**
     - *string*
     - Публично име на `артикула </barsy.help/210-dictionary/article.html>`__

			*Вижда се на бележките, в публичния каталог, е-магазин и т.н. Не е уникално.*

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→ml_data <#ArticlesListExtraPropertiesData>`_
   * - **$article_name_public_ml**
     - MultiLanguageData_ 
     - Публично име на `артикул </barsy.help/210-dictionary/article.html>`__.

			*Мултиезично.*

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→ml_data <#ArticlesListExtraPropertiesData>`_
   * - **$article_icon**
     - *string*
     - Икона за `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_color**
     - *string*
     - Цвят за `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$ref_num**
     - *string*
     - Референтен номер.

			*Свободен текст*
   * - **$barcode**
     - *string*
     - Баркод на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$is_service**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е услуга

			* **0** - *Стока*
			* **1** - *Услуга*
   * - **$is_public**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е публично видим (в публичен каталог, е-магазин)
   * - **$code**
     - *string*
     - Код на `артикул </barsy.help/210-dictionary/article.html>`__ - за бързо избиране от клавиатура,везна и др.
   * - **$description**
     - *string*
     - Описание на `артикула </barsy.help/210-dictionary/article.html>`__ - свободен текст
   * - **$description_ml**
     - MultiLanguageData_ 
     - Описание на `артикула </barsy.help/210-dictionary/article.html>`__ - свободен текст.

			*Мултиезично.*
   * - **$menu_id**
     - *int*
     - Каталог, към който принадлежи `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$picture**
     - *string*
     - Основна картинка на `артикула </barsy.help/210-dictionary/article.html>`__ от наличните за него
   * - **$picture_url**
     - *string*
     - Пълен URL адрес за изтегляне на основната картинка

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→picture_url <#ArticlesListExtraPropertiesData>`_
   * - **$slug**
     - *string*
     - Публичен URL
   * - 
     - 
     - 
   * - :category_header:`Цени и количества`
     - 
     - 
   * - **$delivery_price**
     - *float*
     - Доставна цена
   * - **$actual_price**
     - *float*
     - Базова продажна цена на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_price**
     - *float*
     - Текъща `продажба </barsy.help/210-dictionary/sale.html>`__ цена (след прилагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
   * - **$original_price**
     - *float*
     - Текъща `продажба </barsy.help/210-dictionary/sale.html>`__ цена (след прилагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__) във валута
   * - **$avg_delivery_price**
     - *float*
     - Средно претеглена доставна цена/себестойност без ДДС
   * - **$current_delivery_price**
     - *float*
     - Показване на текуща доставна цена (след `ценови правила </barsy.help/210-dictionary/pricelist.html>`__)

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→current_delivery_data <#ArticlesListExtraPropertiesData>`_
   * - **$current_delivery_tax_id**
     - *int*
     - Показване на текуща ДДС група за `зареждане </barsy.help/210-dictionary/storeload.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__ (след `ценови правила </barsy.help/210-dictionary/pricelist.html>`__)

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→current_delivery_data <#ArticlesListExtraPropertiesData>`_
   * - **$amount_unit**
     - *float*
     - Единица `продажба </barsy.help/210-dictionary/sale.html>`__

			Указва коичеството, което се изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при `продажба </barsy.help/210-dictionary/sale.html>`__ на 1.
   * - **$amount_prod**
     - *float*
     - Единица `производство </barsy.help/210-dictionary/storeproduction.html>`__
   * - **$amount_type_id**
     - *int*
     - ID на типа количество ( виж: ``Amounttypes::getList()`` )
   * - **$min_amount**
     - *float*
     - Минимално количество

			Под него системата сигнализира за недостатъчна наличност. Ако е подаден depot_id - показва за избрания `склад </barsy.help/210-dictionary/store.html>`__, ако не е - включва глобална стойност за цялата система.

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→show_min_max_inventory <#ArticlesListExtraPropertiesData>`_
   * - **$max_amount**
     - *float*
     - Максимално количество

			Допълва се до него при `заявки към доставчици </barsy.help/210-dictionary/request.html>`__. Ако е подаден depot_id - показва за избрания `склад </barsy.help/210-dictionary/store.html>`__, ако не е - включва глобална стойност за цялата система.

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→show_min_max_inventory <#ArticlesListExtraPropertiesData>`_
   * - **$min_order**
     - *float*
     - Минимално възможно количество при поръчка в `продажба </barsy.help/210-dictionary/sale.html>`__
   * - **$max_order**
     - *float*
     - Максимално възможно количество при поръчка в `продажба </barsy.help/210-dictionary/sale.html>`__
   * - **$max_amount_by_depots**
     - *array*
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове, за които има зададено максимално количество.
   * - **$min_amount_by_depots**
     - *array*
     - Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ и складове, за които има зададено минимално количество.
   * - **$has_amount**
     - *bool*
     - Кратки данни (има/няма) за складова наличност за този `артикул </barsy.help/210-dictionary/article.html>`__ в цялата система

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→has_amount <#ArticlesListExtraPropertiesData>`_
   * - **$store_amount**
     - *float*
     - Общи данни (сума за текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__) за складова наличност

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→store_amount <#ArticlesListExtraPropertiesData>`_
   * - **$store_amount_all**
     - *float*
     - Общи данни (сума за цялата система) за складова наличност

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→store_amount_all <#ArticlesListExtraPropertiesData>`_
   * - **$store_amount_details**
     - *array*
     - Разширени данни (по складове) за складова наличност

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→store_amount_details <#ArticlesListExtraPropertiesData>`_
   * - **$has_amount_recipe**
     - *bool*
     - Кратки данни (има/няма) за виртуална наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта

			*За да има достатъчно наличност, трябва да има наличност за всички продукти в рецептата.*

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→has_amount_recipe <#ArticlesListExtraPropertiesData>`_
   * - **$store_amount_recipe**
     - *float*
     - Общи данни (сума за текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__) за виртуална наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта

			*За да има достатъчно наличност, трябва да има наличност за всички продукти в рецептата.*

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→store_amount_recipe <#ArticlesListExtraPropertiesData>`_
   * - **$store_amount_all_recipe**
     - *float*
     - Общи данни (сума за цялата система) за виртуална наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→store_amount_all_recipe <#ArticlesListExtraPropertiesData>`_
   * - **$store_amount_details_recipe**
     - *array*
     - Разширени данни (по складове) за виртуална наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→store_amount_details_recipe <#ArticlesListExtraPropertiesData>`_
   * - **$client_orders_reserved_amount**
     - *float*
     - Количество в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→client_orders_reserved_amount <#ArticlesListExtraPropertiesData>`_
   * - **$open_orders_amount**
     - *float*
     - Количество поръчки за `артикула </barsy.help/210-dictionary/article.html>`__ в отворени `сметки </barsy.help/210-dictionary/account.html>`__.

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→open_orders_amount <#ArticlesListExtraPropertiesData>`_
   * - **$orders_amount**
     - *float*
     - Количество поръчки за `артикула </barsy.help/210-dictionary/article.html>`__ за зададен период

			*Изисква филтър "orders_amount_period".* ( виж: :doc:`ArticlesListFiltersData→$orders_amount_period </objects/articleslistfiltersdata>` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→orders_amount <#ArticlesListExtraPropertiesData>`_
   * - **$pricelist_id**
     - *int*
     - Информация по кое `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ е изчислена текущата цена

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→pricelist_id <#ArticlesListExtraPropertiesData>`_
   * - **$depot_id**
     - *int*
     - `Склад </barsy.help/210-dictionary/store.html>`__ за изтегляне по подразбиране за `потока </barsy.help/210-dictionary/flow.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__ и текущата (или подадена) `каса </barsy.help/210-dictionary/pos.html>`__

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→depot_id <#ArticlesListExtraPropertiesData>`_
   * - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
   * - **$process_time**
     - *int*
     - Време за приготвяне в секунди

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→process_time <#ArticlesListExtraPropertiesData>`_
   * - **$create_date**
     - *string*
     - Дата на създаване
   * - **$client_orders_reserved_last_update**
     - *string*
     - Последна промяна в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→client_orders_reserved_last_update <#ArticlesListExtraPropertiesData>`_
   * - **$store_load_last_date**
     - *string*
     - Дата на последно `зареждане </barsy.help/210-dictionary/storeload.html>`__ на дадения `артикул </barsy.help/210-dictionary/article.html>`__

			Ако има подаден филтър по `склад </barsy.help/210-dictionary/store.html>`__ - взима се под внимание.

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→store_load_last_date <#ArticlesListExtraPropertiesData>`_
   * - **$remote_ref_id**
     - *int*
     - Референтно ID използвано от отдалечена система

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→remote_ref_id <#ArticlesListExtraPropertiesData>`_
   * - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
   * - **$stream_id**
     - *int*
     - ID на `поток </barsy.help/210-dictionary/flow.html>`__, към който е `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$delete_flag**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е маркиран като изтрит
   * - **$is_for_sale**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се продава

			* **0** - *не може да се продава*
			* **1** - *може да се продава*
   * - **$is_for_sale_barsys**
     - *array*
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `продажба </barsy.help/210-dictionary/sale.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `продажба </barsy.help/210-dictionary/sale.html>`__ ($is_for_sale).

			* **0** - *не може да се продава*
			* **1** - *може да се продава* ( виж: :doc:`../barsys/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→limits_by_barsys <#ArticlesListExtraPropertiesData>`_
   * - **$is_for_client_order**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да участва в `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__

			* **0** - *не може да участва*
			* **1** - *може да участва*
   * - **$is_for_client_order_barsys**
     - *array*
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ ($is_for_client_order).

			* **0** - *не може да участва*
			* **1** - *може да участва* ( виж: :doc:`../barsys/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→limits_by_barsys <#ArticlesListExtraPropertiesData>`_
   * - **$is_for_load**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е в `продажба </barsy.help/210-dictionary/sale.html>`__

			* **0** - *не може да се зарежда*
			* **1** - *може да се зарежда*
   * - **$is_for_load_barsys**
     - *array*
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `зареждане </barsy.help/210-dictionary/storeload.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `зареждане </barsy.help/210-dictionary/storeload.html>`__ ($is_for_load).

			* **0** - *не може да се зарежда*
			* **1** - *може да се зарежда* ( виж: :doc:`../barsys/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→limits_by_barsys <#ArticlesListExtraPropertiesData>`_
   * - **$is_for_store_move**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ може да се прехвърля

			* **0** - *не може да се прехвърля*
			* **1** - *може да се прехвърля*
   * - **$is_for_store_move_barsys**
     - *array*
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ ($is_for_store_move).

			* **0** - *не може да се прехвърля*
			* **1** - *може да се прехвърля* ( виж: :doc:`../barsys/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→limits_by_barsys <#ArticlesListExtraPropertiesData>`_
   * - **$is_for_irequest**
     - *int*
     - Флаг, дали `артикула </barsy.help/210-dictionary/article.html>`__ е може да участва във `вътрешна заявка </barsy.help/210-dictionary/irequest.html>`__

			* **0** - *не може*
			* **1** - *може*
   * - **$is_for_irequest_barsys**
     - *array*
     - Изключения по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__ за `вътрешна заявка </barsy.help/210-dictionary/irequest.html>`__

			Списък от `търговски обекти </barsy.help/210-dictionary/barsy.html>`__, за които има изключение от основната стойност на флага за `вътрешна заявка </barsy.help/210-dictionary/irequest.html>`__ ($is_for_irequest).

			* **0** - *не може да участва*
			* **1** - *може да участва* ( виж: :doc:`../barsys/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→limits_by_barsys <#ArticlesListExtraPropertiesData>`_
   * - **$export_id**
     - *string*
     - ID при експорт на `артикули </barsy.help/210-dictionary/article.html>`__ - например за импорт в друга система
   * - **$ref_id**
     - *int*
     - ID на `артикула </barsy.help/210-dictionary/article.html>`__ при импорт от друга система
   * - **$sale_below_zero**
     - *string*
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се продава без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се продава без наличност*
			* **NO** - *НЕ може да се продава без наличност*
   * - **$storemove_below_zero**
     - *string*
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се прехвърля без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се прехвърля без наличност*
			* **NO** - *НЕ може да се прехвърля без наличност*
   * - **$storeload_return_below_zero**
     - *string*
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се връща към `доставчик </barsy.help/210-dictionary/supplier.html>`__ без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се връща без наличност*
			* **NO** - *НЕ може да се връща без наличност*
   * - **$storeout_below_zero**
     - *string*
     - Флаг за `артикул </barsy.help/210-dictionary/article.html>`__ (може ли да се изписва без складова наличност)

			* **DEF** - Според правата на `потребителя </barsy.help/210-dictionary/user.html>`__
			* **YES** - *Може да се изписва без наличност*
			* **NO** - *НЕ може да се изписва без наличност*
   * - **$intrastat**
     - *string*
     - Intrastat код
   * - **$lot_type_id**
     - *int*
     - Партиди - тип употреба
   * - **$article_details**
     - *array*
     - Всички характеристики за `артикула </barsy.help/210-dictionary/article.html>`__

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→article_details <#ArticlesListExtraPropertiesData>`_
   * - **$has_attributes**
     - *bool*
     - Флаг дали `артикула </barsy.help/210-dictionary/article.html>`__ има атрибути (вариции)

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→has_attributes <#ArticlesListExtraPropertiesData>`_
   * - **$has_supplements**
     - *bool*
     - Флаг дали `артикула </barsy.help/210-dictionary/article.html>`__ има комбо групи (пакетно предложение)

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→has_supplements <#ArticlesListExtraPropertiesData>`_
   * - **$supplements_type**
     - *string*
     - Тип комбо `артикул </barsy.help/210-dictionary/article.html>`__ (Комбо меню или `Артикул </barsy.help/210-dictionary/article.html>`__ със съставки)

			* **0** - *combo*
			* **1** - *supplements*

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→supplements_type <#ArticlesListExtraPropertiesData>`_
   * - **$ml_data**
     - *array*
     - Включва всички мултиезични данни към `артикула </barsy.help/210-dictionary/article.html>`__

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→ml_data <#ArticlesListExtraPropertiesData>`_
   * - **$composite**
     - *int*
     - Съставен `артикул </barsy.help/210-dictionary/article.html>`__ (обикновен,съставен при приключване,съставен при `производство </barsy.help/210-dictionary/storeproduction.html>`__)

			* **0** - *Без рецепта*
			* **1** - *Рецепта при приключване*
			* **-1** - Рецепта при `производство </barsy.help/210-dictionary/storeproduction.html>`__

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→composite <#ArticlesListExtraPropertiesData>`_
   * - **$group_attributes_options**
     - *array*
     - Опциите на атрибутите за `артикул </barsy.help/210-dictionary/article.html>`__

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→group_attributes_options <#ArticlesListExtraPropertiesData>`_
   * - **$group_attributes**
     - *array*
     - Информация за групоте атрибути, техните опции и id в отдалечена система

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→group_attributes <#ArticlesListExtraPropertiesData>`_
   * - **$form_data**
     - *array*
     - Структура на формуляра за допълнителни полета към този `артикул </barsy.help/210-dictionary/article.html>`__ при взимане на поръчка

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→form_data <#ArticlesListExtraPropertiesData>`_
   * - **$form_data_public**
     - *array*
     - Структура на формуляра за допълнителни публични полета към този `артикул </barsy.help/210-dictionary/article.html>`__ при взимане на поръчка

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→form_data_public <#ArticlesListExtraPropertiesData>`_
   * - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
   * - **$has_upsell**
     - *int*
     - Флаг, дали `артикулът </barsy.help/210-dictionary/article.html>`__ има връзка "Надграждане" с предложения за замяна
   * - **$has_addon**
     - *int*
     - Флаг, дали `артикулът </barsy.help/210-dictionary/article.html>`__ има връзка "Допълнение" с предложения за добавяне
   * - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
   * - **$user_prc**
     - *float*
     - Процент комисионна за персонал при `продажба </barsy.help/210-dictionary/sale.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_id**
     - *int*
     - ID на данъчната ставка
   * - **$actual_tax_id**
     - *int*
     - ID на базовата данъчна ставка (преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__)
   * - **$min_profit_percent**
     - *float*
     - Минимален процент печалба
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$form_id_co**
     - *int*
     - ID на форма за допълнителна информация за `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__
   * - **$files**
     - *string*
     - Списък за всички прикачени файлове към `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../files/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→files <#ArticlesListExtraPropertiesData>`_
   * - **$default_package_id**
     - *int*
     - ID на разфасовка по подразбиране (използва се при `зареждане </barsy.help/210-dictionary/storeload.html>`__) ( виж: :doc:`../packages/getlist` )
   * - **$package_details**
     - *array*
     - Информация за пакетната единица по подразбиране за този `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../packages/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→package_details <#ArticlesListExtraPropertiesData>`_
   * - **$suppliers_details**
     - *array*
     - Данни за `доставчиците </barsy.help/210-dictionary/supplier.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→suppliers_details <#ArticlesListExtraPropertiesData>`_
   * - **$supplements**
     - *array*
     - Списък на комбо групите, включени в `артикула </barsy.help/210-dictionary/article.html>`__ (ако има такива)

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→supplements <#ArticlesListExtraPropertiesData>`_
   * - **$inv_ref_num**
     - *string*
     - Показва референтент номер на `артикула </barsy.help/210-dictionary/article.html>`__, използван за `фактури </barsy.help/210-dictionary/invoice.html>`__ (според настройките на системата)

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→inv_ref_num <#ArticlesListExtraPropertiesData>`_
   * - **$client_ref_num**
     - *string*
     - Показва референтент номер на `артикула </barsy.help/210-dictionary/article.html>`__, специфично за подадения `клиент </barsy.help/210-dictionary/client.html>`__ (като филтър)

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→client_ref_num <#ArticlesListExtraPropertiesData>`_
   * - 
     - 
     - 
   * - :category_header:`Категории и класификация`
     - 
     - 
   * - **$master_cat_id**
     - *int*
     - ID на основната `категория </barsy.help/210-dictionary/category.html>`__ ( виж: :doc:`../categories/getlist` )
   * - **$master_cat**
     - *string*
     - Име на основната `категория </barsy.help/210-dictionary/category.html>`__ ( виж: :doc:`../categories/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→master_cat <#ArticlesListExtraPropertiesData>`_
   * - **$categories**
     - *string*
     - Списък от ID на всички `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../categories/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→categories <#ArticlesListExtraPropertiesData>`_
   * - **$categories_names**
     - *string*
     - Списък от имена на всички `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../categories/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→categories_names <#ArticlesListExtraPropertiesData>`_
   * - **$categories_paths**
     - *string*
     - Списък от пътища на всички `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../categories/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→categories_paths <#ArticlesListExtraPropertiesData>`_
   * - **$categories_details**
     - *array*
     - Подробности за всички `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../categories/getlist` )

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→categories_details <#ArticlesListExtraPropertiesData>`_
   * - **$group_id**
     - *int*
     - ID на група на `артикула </barsy.help/210-dictionary/article.html>`__

			 **Изисква флаг:** `ArticlesListExtraPropertiesData→group_id <#ArticlesListExtraPropertiesData>`_

-----

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articles_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articles_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articles_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articles_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articles_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articles_get/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

