.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Orders_getlist
===========================================================
Списък с поръчки

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с поръчките (orders — редове в `сметки </barsy.help/210-dictionary/account.html>`__, не `сметките </barsy.help/210-dictionary/account.html>`__ сами по себе си). Поръчката е атомарната единица на `продажба </barsy.help/210-dictionary/sale.html>`__ — една `сметка </barsy.help/210-dictionary/account.html>`__ съдържа множество поръчки за конкретни `артикули </barsy.help/210-dictionary/article.html>`__ с количества. Богат набор от филтри за анализ на `продажби </barsy.help/210-dictionary/sale.html>`__: период/дата, `артикул </barsy.help/210-dictionary/article.html>`__, `категория </barsy.help/210-dictionary/category.html>`__, `потребител </barsy.help/210-dictionary/user.html>`__ (продавач), обслужил, обект, `каса </barsy.help/210-dictionary/pos.html>`__, `поток </barsy.help/210-dictionary/flow.html>`__, начин на `плащане </barsy.help/210-dictionary/payment.html>`__, ДДС група, `клиент </barsy.help/210-dictionary/client.html>`__, статус. Чрез `extra_properties` се добавят финансови показатели (отстъпка, ДДС, сума на реда, базова/първоначална цена, ценоразпис, сторно, `категория </barsy.help/210-dictionary/category.html>`__) и детайли (`модификатори </barsy.help/210-dictionary/modificator.html>`__, групови атрибути, данни за `сметка </barsy.help/210-dictionary/account.html>`__/`клиент </barsy.help/210-dictionary/client.html>`__).

Типични случаи: анализ на `продажби </barsy.help/210-dictionary/sale.html>`__ (по `артикул </barsy.help/210-dictionary/article.html>`__/`категория </barsy.help/210-dictionary/category.html>`__/период/`потребител </barsy.help/210-dictionary/user.html>`__/`каса </barsy.help/210-dictionary/pos.html>`__), дневен оборот на касиер, KDS дисплей за подготовка, експорт на детайли на `продажбите </barsy.help/210-dictionary/sale.html>`__, синхронизация към bar/grill дисплеи.

**Име**: Orders_getlist
**Категория**: Cashdesk


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$filters**
     - OrdersListFiltersData_ 
     - Филтриране на поръчки
   * - **$extra_properties**
     - OrdersListExtraPropertiesData_ 
     - Искане на допълнително данни за поръчките
   * - **$offset**
     - *int*
     - Номер на ред от който да бъде започнат списъка.

			*Използва се при странициране, когато трябва да се прескочат Х записа* **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - OrdersListOrderByData_ 
     - Подреждане — низ, масив или обект колона⇒посока (напр. {"date":"desc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
OrderData_                                                             
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

OrdersListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: OrdersListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$account_id**
     - *int*
     - Филтър по ID на `сметка </barsy.help/210-dictionary/account.html>`__ ( виж: :doc:`../accounts/getlist` )
   * - **$order_id**
     - *int*
     - Филтър по ID на поръчката
   * - **$order_barsy_id**
     - *int*
     - Филтър по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ на поръчката ( виж: :doc:`../barsys/getlist` )
   * - **$order_account_id**
     - *int*
     - Филтър по ID на `сметка </barsy.help/210-dictionary/account.html>`__ на поръчката ( виж: :doc:`../accounts/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$barsy_ids**
     - *int*
     - Филтър по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$period_id**
     - *int*
     - Филтър по период
   * - **$client_id**
     - *int*
     - Филтър по ID на `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getlist` )
   * - **$client_group_id**
     - *int*
     - Филтър по ID на група на `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clientgroups/getlist` )
   * - **$paymethod_id**
     - *int*
     - Филтър по начин на `плащане </barsy.help/210-dictionary/payment.html>`__ на `сметката </barsy.help/210-dictionary/account.html>`__ ( виж: :doc:`../paymentmethods/getlist` )
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$ref_date**
     - *datetime*
     - Филтър по дата на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$date**
     - *datetime*
     - Филтър по дата на поръчката (период или точна дата) — кога е направена `продажбата </barsy.help/210-dictionary/sale.html>`__
   * - **$served_date**
     - *datetime*
     - Филтър по дата на обслужване на поръчката (период или точна дата)
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$parents_only**
     - *int*
     - Филтър който извежда родителските и нормалните поръчки (комбо меню)
   * - **$exclude_advance_payments**
     - *int*
     - Филтър който извежда поръчките като не включва `артикул </barsy.help/210-dictionary/article.html>`__ (и) "Авансово `плащане </barsy.help/210-dictionary/payment.html>`__"
   * - **$common_reason**
     - *int*
     - Филтър по стандартна причина
   * - **$output_pos**
     - *int*
     - Филтър по output `каса </barsy.help/210-dictionary/pos.html>`__
   * - **$service_status_id**
     - *int*
     - Филтър по статус обслужване на `сметка </barsy.help/210-dictionary/account.html>`__ ( виж: :doc:`../accounts/servicestatusgetlist` )
   * - **$status**
     - *int*
     - Филтър по статус на поръчката (напр. продадена/сторно/чакаща)
   * - 
     - 
     - 
   * - :category_header:`Анализ на продажби`
     - 
     - 
   * - **$article_id**
     - *int*
     - Филтър по ID на `артикул </barsy.help/210-dictionary/article.html>`__ — `продажби </barsy.help/210-dictionary/sale.html>`__ на конкретен `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articles/getlist` )
   * - **$category_id**
     - *int*
     - Филтър по `категория </barsy.help/210-dictionary/category.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__ — `продажби </barsy.help/210-dictionary/sale.html>`__ по `категория </barsy.help/210-dictionary/category.html>`__ ( виж: :doc:`../categories/getlist` )
   * - **$user_id**
     - *int*
     - Филтър по ID на `потребителя </barsy.help/210-dictionary/user.html>`__, направил поръчката (продавач/касиер) — `продажби </barsy.help/210-dictionary/sale.html>`__ по `потребител </barsy.help/210-dictionary/user.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$served_by**
     - *int*
     - Филтър по ID на `потребителя </barsy.help/210-dictionary/user.html>`__, обслужил поръчката ( виж: :doc:`../users/getlist` )
   * - **$stream_id**
     - *int*
     - Филтър по ID на `поток </barsy.help/210-dictionary/flow.html>`__ (кухня/бар) на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../streams/getlist` )
   * - **$pos_id**
     - *int*
     - Филтър по ID на `каса </barsy.help/210-dictionary/pos.html>`__, на която е направена поръчката ( виж: :doc:`../poses/getlist` )
   * - **$tax_id**
     - *int*
     - Филтър по ДДС група на поръчката ( виж: :doc:`../taxgroups/getlist` )

-----

OrdersListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към всяка поръчка в списъка (Orders_getlist).
		Всяко свойство е булев флаг — при `true` поръчката се обогатява със съответната допълнителна информация (данни за `сметката </barsy.help/210-dictionary/account.html>`__/`клиента </barsy.help/210-dictionary/client.html>`__, финансови показатели за анализ на `продажби </barsy.help/210-dictionary/sale.html>`__, `модификатори </barsy.help/210-dictionary/modificator.html>`__, групови атрибути, изходи/output екрани).

.. list-table::
   :header-rows: 1
   :align: center
   :name: OrdersListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
   * - **$account_data**
     - *bool*
     - Данни за `сметката </barsy.help/210-dictionary/account.html>`__ (вальор, отстъпка, `клиент </barsy.help/210-dictionary/client.html>`__) **По подразбиране:** false
   * - **$client_data**
     - *bool*
     - Данни за `клиента </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** false
   * - **$category**
     - *bool*
     - `Категории </barsy.help/210-dictionary/category.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__ **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Артикул`
     - 
     - 
   * - **$modificators**
     - *bool*
     - Данни за `модификаторите </barsy.help/210-dictionary/modificator.html>`__ **По подразбиране:** false
   * - **$article_attributes**
     - *bool*
     - Данни за груповите атрибути **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Изход`
     - 
     - 
   * - **$outputs**
     - *bool*
     - Данни за насочването на поръчката

			Към кои `каси </barsy.help/210-dictionary/pos.html>`__ и `потоци </barsy.help/210-dictionary/flow.html>`__ е насочена поръчката. **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
   * - **$discount**
     - *bool*
     - Отстъпка на реда в проценти **По подразбиране:** false
   * - **$tax**
     - *bool*
     - ДДС данни на реда

			*Ставка, ДДС група, данъчен код и данъчен регион.* **По подразбиране:** false
   * - **$line_total**
     - *bool*
     - Сума на реда

			Количество по единична цена с приспадната отстъпка на `сметката </barsy.help/210-dictionary/account.html>`__ — брутни `продажби </barsy.help/210-dictionary/sale.html>`__ на реда. **По подразбиране:** false
   * - **$base_price**
     - *bool*
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__

			*за анализ на отстъпки/маржове* **По подразбиране:** false
   * - **$original_price**
     - *bool*
     - Първоначална единична цена преди корекции **По подразбиране:** false
   * - **$pricelist**
     - *bool*
     - ID на ценоразписа, по който е продаден редът **По подразбиране:** false
   * - 
     - 
     - 
   * - :category_header:`Състояние`
     - 
     - 
   * - **$reason**
     - *bool*
     - Причина за реда (`продажба </barsy.help/210-dictionary/sale.html>`__/връщане/сторно/авансово `плащане </barsy.help/210-dictionary/payment.html>`__) **По подразбиране:** false
   * - **$storno**
     - *bool*
     - Дали редът е сторниран **По подразбиране:** false

-----

OrdersListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с поръчки (Orders_getlist).
		Подава се като асоциативен масив колона⇒посока (напр. ["date" => "desc", "order_id" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

.. list-table::
   :header-rows: 1
   :align: center
   :name: OrdersListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
   * - **$order_id**
     - *string*
     - Подреждане по ID на поръчка
   * - **$article_id**
     - *string*
     - Подреждане по ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$barsy_id**
     - *string*
     - Подреждане по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
   * - **$date**
     - *string*
     - Подреждане по дата на поръчката
   * - **$served_date**
     - *string*
     - Подреждане по дата на обслужване
   * - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
   * - **$article_name**
     - *string*
     - Подреждане по име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
   * - **$amount**
     - *string*
     - Подреждане по количество
   * - **$status**
     - *string*
     - Подреждане по статус

-----

OrderData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Един ред-поръчка (`продажба </barsy.help/210-dictionary/sale.html>`__ на конкретен `артикул </barsy.help/210-dictionary/article.html>`__ в `сметка </barsy.help/210-dictionary/account.html>`__) — резултатен запис на Orders_getlist.
		Базовите полета се връщат винаги; останалите се попълват само когато съответната опция е поискана през `extra_properties` (виж OrdersListExtraPropertiesData). Свойствата нямат стойност по подразбиране — непоисканите остават нехидратирани и **не присъстват** в резултата (JSON), за да не подвеждат получателя, че данните са `null`. Хидратира се автоматично от резултатния ред (BaseType).

.. list-table::
   :header-rows: 1
   :align: center
   :name: OrderData

   * - Параметър
     - Тип
     - Описание
   * - **$order_id**
     - *int*
     - ID на поръчката (ред в `сметка </barsy.help/210-dictionary/account.html>`__)
   * - **$account_id**
     - *int*
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__, към която е поръчката ( виж: :doc:`../accounts/getlist` )
   * - **$barsy_id**
     - *int*
     - ID на търговския обект ( виж: :doc:`../barsys/getlist` )
   * - **$pos_id**
     - *int*
     - ID на `касата </barsy.help/210-dictionary/pos.html>`__, на която е направена поръчката ( виж: :doc:`../poses/getlist` )
   * - **$place_id**
     - *int*
     - ID на място, към което е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../articles/getlist` )
   * - **$article_name**
     - *string*
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name_ml**
     - MultiLanguageData_ 
     - Многоезично име на `артикула </barsy.help/210-dictionary/article.html>`__ (не включва системното article_name)
   * - **$article_type**
     - *int*
     - Тип на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$stream_id**
     - *int*
     - ID на `поток </barsy.help/210-dictionary/flow.html>`__ (кухня/бар) на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../streams/getlist` )
   * - **$cat_name**
     - *string*
     - `Категория </barsy.help/210-dictionary/category.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__ — при extra_properties.category ( виж: :doc:`../categories/getlist` )
   * - **$amount**
     - *float*
     - Количество за този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$new_amount**
     - *float*
     - Ново количество (за операции по редакция)
   * - **$amount_unit**
     - *float*
     - Единица `продажба </barsy.help/210-dictionary/sale.html>`__ за този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount_type_id**
     - *int*
     - ID на типа количество ( виж: :doc:`../amounttypes/getlist` )
   * - **$amount_type_name_short**
     - *string*
     - Кратко име на типа количество ( виж: :doc:`../amounttypes/getlist` )
   * - **$current_price**
     - *float*
     - Текуща (продажна) единична цена
   * - **$actual_price**
     - *float*
     - Актуална цена на `артикула </barsy.help/210-dictionary/article.html>`__ (по ценоразпис)
   * - **$discount**
     - *float*
     - Отстъпка на реда в проценти — при extra_properties.discount
   * - **$tax**
     - *float*
     - Процент ДДС на реда — при extra_properties.tax
   * - **$tax_id**
     - *int*
     - ID на ДДС група — при extra_properties.tax ( виж: :doc:`../taxgroups/getlist` )
   * - **$tax_code**
     - *string*
     - Данъчен код (ДДС група) — при extra_properties.tax
   * - **$tax_region_id**
     - *int*
     - Данъчен регион — при extra_properties.tax
   * - **$line_total**
     - *float*
     - Сума на реда (количество × цена с отстъпката на `сметката </barsy.help/210-dictionary/account.html>`__) — при extra_properties.line_total
   * - **$actual_price_base**
     - *float*
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__ — при extra_properties.base_price
   * - **$original_current_price**
     - *float*
     - Първоначална единична цена преди корекции — при extra_properties.original_price
   * - **$current_pricelist_id**
     - *int*
     - ID на ценоразписа, по който е продаден редът — при extra_properties.pricelist
   * - **$reason_id**
     - *int*
     - Причина за реда (`продажба </barsy.help/210-dictionary/sale.html>`__/връщане/сторно/авансово `плащане </barsy.help/210-dictionary/payment.html>`__) — при extra_properties.reason
   * - **$storno_of_account_id**
     - *int*
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__, която сторнира този ред (NULL ако не е сторниран) — при extra_properties.storno ( виж: :doc:`../accounts/getlist` )
   * - **$status**
     - *int*
     - Статус на поръчката
   * - **$order_status_title**
     - *string*
     - Заглавие на статуса на поръчката
   * - **$date**
     - *string*
     - Дата на поръчката
   * - **$ref_date**
     - *string*
     - Вальор (документна дата) на `сметката </barsy.help/210-dictionary/account.html>`__ — при extra_properties.account_data
   * - **$start_service_date**
     - *string*
     - Дата, от която поръчката трябва да започне да се обслужва
   * - **$served_date**
     - *string*
     - Дата на обслужване
   * - **$served_by**
     - *int*
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, обслужил поръчката ( виж: :doc:`../users/getlist` )
   * - **$served_by_user**
     - *string*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, обслужил поръчката
   * - **$user_name**
     - *string*
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, направил поръчката (продавач/касиер)
   * - **$process_time**
     - *int*
     - Време за приготвяне в секунди (за следене на закъснения; ако липсва — взема се от `потока </barsy.help/210-dictionary/flow.html>`__)
   * - **$order_ref_id**
     - *int*
     - ID на поръчката според външна система
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ — при extra_properties.account_data/client_data ( виж: :doc:`../clients/getlist` )
   * - **$client_name**
     - *string*
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ — при extra_properties.account_data/client_data
   * - **$modificators**
     - ModificatorData_ []
     - Списък с `модификатори </barsy.help/210-dictionary/modificator.html>`__ за този `артикул </barsy.help/210-dictionary/article.html>`__ — при extra_properties.modificators
   * - **$article_attributes**
     - ArticleAttributesData_ 
     - Групови атрибути за този `артикул </barsy.help/210-dictionary/article.html>`__ — при extra_properties.article_attributes
   * - **$outputs**
     - PosStreamOutputsData_ 
     - Изходи/output екрани на поръчката (`потоци </barsy.help/210-dictionary/flow.html>`__ към `каси </barsy.help/210-dictionary/pos.html>`__) — при extra_properties.outputs

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

ModificatorData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ModificatorData

   * - Параметър
     - Тип
     - Описание
   * - **$mod_id**
     - *int*
     - ID на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_name**
     - *string*
     - Име на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$description**
     - *string*
     - Описание на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$operation**
     - *int*
     - Вид операция ('без' `модификатора </barsy.help/210-dictionary/modificator.html>`__ или 'с' `модификатора </barsy.help/210-dictionary/modificator.html>`__) **По подразбиране:** 0
   * - **$weight**
     - *int*
     - Тежест при подреждане на мофификатори в `категория </barsy.help/210-dictionary/category.html>`__
   * - **$mod_color**
     - *string*
     - Цвят на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_type**
     - *int*
     - Тип `модификатор </barsy.help/210-dictionary/modificator.html>`__

			* **1** - *Липсва описание*
			* **2** - *Липсва описание*
   * - **$categories**
     - *array*
     - Списък с `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран този `модификатор </barsy.help/210-dictionary/modificator.html>`__ ( виж: :doc:`../categories/getlist` ) **По подразбиране:** []

-----

ArticleAttributesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleAttributesData

   * - Параметър
     - Тип
     - Описание
   * - **$article_id**
     - *int*
     - 
   * - **$article_name**
     - *string*
     - 
   * - **$amount**
     - *float*
     - 
   * - **$attributes**
     - ArticleAttributeData_ []
     - 
   * - **$article_type**
     - *int*
     - 

-----

ArticleAttributeData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleAttributeData

   * - Параметър
     - Тип
     - Описание
   * - **$attr_id**
     - *string*
     - 
   * - **$name**
     - *string*
     - 
   * - **$values**
     - *string*
     - 
   * - **$props**
     - *string*
     - 
   * - **$value**
     - *string*
     - 

-----

PosStreamOutputsData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PosStreamOutputsData

   * - Параметър
     - Тип
     - Описание
   * - **$printers**
     - StreamPosOutputData_ []
     - 
   * - **$screens**
     - StreamPosOutputData_ []
     - 
   * - **$labelprinters**
     - StreamPosOutputData_ []
     - 
   * - **$remotesystems**
     - StreamPosOutputData_ []
     - 
   * - **$timers**
     - StreamPosOutputData_ []
     - 
   * - **$client_pager_controllers**
     - *array*
     - 
   * - **$pagercontrollers**
     - *array*
     - 

-----

StreamPosOutputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: StreamPosOutputData

   * - Параметър
     - Тип
     - Описание
   * - **$output_id**
     - *int*
     - 
   * - **$group_id**
     - *int*
     - 

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

     .. literalinclude:: ../../sources/orders_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/orders_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/orders_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/orders_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/orders_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/orders_getlist/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

