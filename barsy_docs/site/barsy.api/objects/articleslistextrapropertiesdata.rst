.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticlesListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към даден артикул.

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Могат да се подадат повече от един като масив. Добавят се към основните данните за всеки `артикул </barsy.help/210-dictionary/article.html>`__

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticlesListExtraPropertiesData


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
   * - **$common**
     - *string*
     - 'common'
     - Обем на върнатите основни данни

			*Определя кои основни данни да се върнат. Възможни стойности: min, common, all, public.*

			 пример: "1"
   * - **$code**
     - *bool*
     - false
     - Код на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_name_ml**
     - *MultiLanguageData*
     - false
     - Обект с името на `артикул </barsy.help/210-dictionary/article.html>`__ в различните езици
   * - **$article_icon**
     - *bool*
     - false
     - Икона на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_color**
     - *bool*
     - false
     - Цвят на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$picture**
     - *bool*
     - false
     - Име на изображениеето на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_type**
     - *bool*
     - false
     - Тип на `артикула </barsy.help/210-dictionary/article.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`Категории и класификация`
     - 
     - 
     - 
   * - **$master_cat**
     - *bool*
     - 
     - име на основната `категория </barsy.help/210-dictionary/category.html>`__

			 пример: "1"
   * - **$categories**
     - *bool*
     - 
     - данни за всички `категории </barsy.help/210-dictionary/category.html>`__,

			 пример: "1"
   * - **$categories_names**
     - *bool*
     - 
     - имена за другите `категории </barsy.help/210-dictionary/category.html>`__

			 пример: "1"
   * - **$categories_paths**
     - *bool*
     - 
     - пътища на всички `категории </barsy.help/210-dictionary/category.html>`__

			 пример: "1"
   * - **$categories_details**
     - *bool*
     - false
     - Подробности за всички `категории </barsy.help/210-dictionary/category.html>`__

			 пример: "1"
   * - **$group_id**
     - *bool*
     - 
     - ID на група на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$categories_remote_details**
     - *bool*
     - false
     - Подробности за `категориите </barsy.help/210-dictionary/category.html>`__ в отдалечени системи
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$suppliers_details**
     - *bool*
     - 
     - данни за `доставчиците </barsy.help/210-dictionary/supplier.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$current_delivery_data**
     - *bool*
     - 
     - Текуща доставна цена и ДДС група

			Връща текущата доставна цена и текущата ДДС група след прилагане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__.
   * - **$files**
     - *string*
     - 
     - Информация за всички прикачени файлове към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$supplements**
     - *bool*
     - 
     - Списък на комбо групите, включени в `артикула </barsy.help/210-dictionary/article.html>`__ (ако има такива)
   * - **$remote_ref_id**
     - *int*
     - 
     - Референтно ID използвано от отдалечена система
   * - **$parent_remote_ref_id**
     - *bool*
     - false
     - ID на родителския `артикул </barsy.help/210-dictionary/article.html>`__ в отдалечена система(Използва се при груповите атрибути)
   * - **$client_ref_num**
     - *bool*
     - false
     - Показва референтент номер на `артикула </barsy.help/210-dictionary/article.html>`__, специфично за подадения `клиент </barsy.help/210-dictionary/client.html>`__ (като филтър)
   * - 
     - 
     - 
     - 
   * - :category_header:`Цени и количества`
     - 
     - 
     - 
   * - **$has_amount**
     - *bool*
     - 
     - Кратки данни (има/няма) за складова наличност

			 пример: "1"
   * - **$store_amount**
     - *bool*
     - 
     - Складова наличност за текущия обект

			Общи данни (сума) за складовата наличност в текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__.

			 пример: "1"
   * - **$store_amount_all**
     - *bool*
     - 
     - Складова наличност за цялата система

			*Общи данни (сума) за складовата наличност в цялата система.*

			 пример: "1"
   * - **$total_store_amount**
     - *bool*
     - false
     - Обща складова наличност за обекта

			Връща складовата наличност за целия `търговски обект </barsy.help/210-dictionary/barsy.html>`__, независимо от избрания `склад </barsy.help/210-dictionary/store.html>`__.

			 пример: "1"
   * - **$store_amount_details**
     - *bool*
     - 
     - Разширени данни (по складове) за складова наличност

			 пример: "1"
   * - **$has_amount_recipe**
     - *bool*
     - 
     - Виртуална наличност (има/няма)

			Кратки данни дали има виртуална наличност за `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта.

			 пример: "1"
   * - **$store_amount_recipe**
     - *bool*
     - 
     - Виртуална наличност за текущия обект

			Общи данни (сума) за виртуалната наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта в текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__.

			 пример: "1"
   * - **$store_amount_all_recipe**
     - *bool*
     - 
     - Виртуална наличност за цялата система

			Общи данни (сума) за виртуалната наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта в цялата система.

			 пример: "1"
   * - **$store_amount_details_recipe**
     - *bool*
     - 
     - Виртуална наличност по складове

			Разширени данни (по складове) за виртуалната наличност на `артикул </barsy.help/210-dictionary/article.html>`__ с рецепта.

			 пример: "1"
   * - **$client_orders_reserved_amount**
     - *bool*
     - 
     - Резервирано количество по заявки

			Количеството в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност.

			 пример: "1"
   * - **$open_orders_amount**
     - *bool*
     - 
     - Количество поръчки за `артикула </barsy.help/210-dictionary/article.html>`__ в отворени `сметки </barsy.help/210-dictionary/account.html>`__.
   * - **$orders_amount**
     - *bool*
     - 
     - Количество поръчки за `артикула </barsy.help/210-dictionary/article.html>`__ за зададен период.

			*Изисква филтър "orders_amount_period"*
   * - **$pricelist_id**
     - *bool*
     - 
     - Информация по кое `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ е изчислена текущата цена
   * - **$client_orders_amount**
     - *bool*
     - 
     - Информация за количество, което е в "отворени" `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__ (според настройка на статусите на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__)
   * - **$show_min_max_inventory**
     - *bool*
     - false
     - Показва информация за минимално/максимално количество на наличност.

			Ако е подаден depot_id - показва за избрания `склад </barsy.help/210-dictionary/store.html>`__, ако не е - включва глобална стойност за цялата система
   * - **$current_price**
     - *bool*
     - false
     - Текуща продажна цена
   * - **$amount_type_id**
     - *bool*
     - false
     - ID на мерната единица
   * - **$actual_price**
     - *bool*
     - false
     - Базова цена
   * - 
     - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
     - 
   * - **$client_orders_reserved_last_update**
     - *bool*
     - 
     - Последна промяна на `резервациите </barsy.help/210-dictionary/reservation.html>`__

			Дата на последната промяна в отворени `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, които резервират наличност.
   * - **$store_load_last_date**
     - *bool*
     - 
     - Дата на последно `зареждане </barsy.help/210-dictionary/storeload.html>`__

			Дата на последното `зареждане </barsy.help/210-dictionary/storeload.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__. Ако е избран `склад </barsy.help/210-dictionary/store.html>`__, се отчита само за него.
   * - **$remote_last_update**
     - *string*
     - 
     - Дата на последна актуализация на `артикула </barsy.help/210-dictionary/article.html>`__ в отдалечена система
   * - **$process_time**
     - *bool*
     - false
     - 
   * - 
     - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
     - 
   * - **$article_details**
     - *string*
     - 
     - Всички характеристики за `артикула </barsy.help/210-dictionary/article.html>`__ [1=JSON списък,flat=отделни стойности]

			 пример: "1"
   * - **$picture_content**
     - *int*
     - 
     - Съдържание (base64) на основната картинка

			*(Внимание: натоварва изключително изтеглянето. Да се ползва в подходящи ситуации)*
   * - **$picture_url**
     - *string*
     - 
     - URL адрес за изтегляне на основната картинка
   * - **$has_attributes**
     - *bool*
     - 
     - Флаг дали `артикула </barsy.help/210-dictionary/article.html>`__ има атрибути (вариции)
   * - **$has_supplements**
     - *bool*
     - 
     - Флаг дали `артикула </barsy.help/210-dictionary/article.html>`__ има комбо групи
   * - **$limits_by_barsys**
     - *bool*
     - 
     - Информация за ограничения за `продажби </barsy.help/210-dictionary/sale.html>`__, зареждания, прехвърляния, `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__, `вътрешни заявки </barsy.help/210-dictionary/irequest.html>`__ по `търговски обекти </barsy.help/210-dictionary/barsy.html>`__
   * - **$ml_data**
     - *bool*
     - 
     - Включва всички мултиезични данни към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$composite**
     - *bool*
     - 
     - Съставен `артикул </barsy.help/210-dictionary/article.html>`__ (обикновен,съставен при приключване,съставен при `производство </barsy.help/210-dictionary/storeproduction.html>`__)
   * - **$group_attributes_options**
     - *bool*
     - false
     - Опциите на атрибутите за `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$group_attributes**
     - *bool*
     - false
     - Информация за групоте атрибути, техните опции и id в отдалечена система
   * - **$slug**
     - *string*
     - 
     - Slug на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$form_data**
     - *bool*
     - false
     - 
   * - **$form_data_public**
     - *bool*
     - 
     - 
   * - **$package_details**
     - *bool*
     - false
     - 
   * - **$extra_data**
     - *bool*
     - false
     - 
   * - **$eshop_router**
     - *bool*
     - true
     - 
   * - **$supplements_type**
     - *bool*
     - false
     - 
   * - **$list_count**
     - *bool*
     - false
     - Определя, дали да се върне $count в ArticlesListData
   * - **$stream_name**
     - *bool*
     - false
     - Име на `поток </barsy.help/210-dictionary/flow.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
     - 
   * - **$tax_id**
     - *bool*
     - 
     - ID на данъчната група на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/taxgroups/getlist` )
   * - **$inv_ref_num**
     - 
     - 
     - Показва референтент номер на `артикула </barsy.help/210-dictionary/article.html>`__, използван за `фактури </barsy.help/210-dictionary/invoice.html>`__ (според настройките на системата)
   * - **$discount**
     - *bool*
     - false
     - Отстъпка на `артикула </barsy.help/210-dictionary/article.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
     - 
   * - **$has_upsell**
     - *bool*
     - 
     - Флаг дали `артикулът </barsy.help/210-dictionary/article.html>`__ има връзка "Надграждане" с предложения за замяна
   * - **$has_addon**
     - *bool*
     - 
     - Флаг дали `артикулът </barsy.help/210-dictionary/article.html>`__ има връзка "Допълнение" с предложения за добавяне
   * - **$client_package_id**
     - *bool*
     - false
     - Показва разфасовката по подразбиране за подадения `клиент </barsy.help/210-dictionary/client.html>`__ (като филтър) — конфигурация `артикул </barsy.help/210-dictionary/article.html>`__-`клиент </barsy.help/210-dictionary/client.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articles/getlist`
	 * :doc:`../methods/articles/get`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

