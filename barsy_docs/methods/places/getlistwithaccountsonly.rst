.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Places_getlistwithaccountsonly
===========================================================
Места с отворени сметки

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща САМО местата, на които към момента има поне една отворена `сметка </barsy.help/210-dictionary/account.html>`__, заедно с агрегирана информация за тези `сметки </barsy.help/210-dictionary/account.html>`__ — брой `сметки </barsy.help/210-dictionary/account.html>`__, обща сума, последна активност, отговарящ `потребител </barsy.help/210-dictionary/user.html>`__. Това е силно оптимизиран endpoint за основния "зает/свободен" план на залата в реално време. Поддържа checksum за инкрементални обновления — клиентският UI може да полва само при действителна промяна без излишни данни.

Типични случаи: основен изглед на ресторант с цветово маркирани заети маси, kanban на куриерски доставки в подготовка, dashboard на администратор с активен бизнес в момента. За пълен списък независимо от статуса виж `Places_getlist`.

**Име**: Places_getlistwithaccountsonly
**Категория**: Settings


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PlaceAccountsData_                                                     
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PlaceAccountsData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PlaceAccountsData

   * - Параметър
     - Тип
     - Описание
   * - **$place**
     - PlaceData_ 
     - 
   * - **$accounts**
     - AccountData_ 
     - 

-----

PlaceData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PlaceData

   * - Параметър
     - Тип
     - Описание
   * - **$place_id**
     - *int*
     - ID на текущото място
   * - **$place_type**
     - *int*
     - ID на типа на мястото
   * - **$place_num**
     - *int*
     - Номер на мястото (свободно избираем)
   * - **$pos**
     - *string*
     - Координати и размери на текущото място на схемата (x,y,w,h).
   * - **$type_name**
     - *string*
     - Тип на текущото място
   * - **$is_public**
     - *int*
     - Публично видомо ли е мястото
   * - **$picture**
     - *string*
     - Основна снимка
   * - **$salon_id**
     - *int*
     - ID на зона/салон, към която принадлежи текущото място
   * - **$salon_name**
     - *string*
     - Име на зона/салон, към която принадлежи текущото място
   * - **$accounts_count**
     - *int*
     - Брой отворени `сметка </barsy.help/210-dictionary/account.html>`__, асоцирани към мястото
   * - **$id**
     - *int*
     - 
   * - **$type**
     - *int*
     - 
   * - **$num**
     - *int*
     - 
   * - **$acc_count**
     - *int*
     - 
   * - **$name**
     - *string*
     - 

-----

AccountData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: AccountData

   * - Параметър
     - Тип
     - Описание
   * - **$account_id**
     - *int*
     - ID на `сметка </barsy.help/210-dictionary/account.html>`__ - уникално за системата
   * - **$barsy_id**
     - *int*
     - ID на `търговските обект </barsy.help/210-dictionary/barsy.html>`__, в който е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$barsy_name**
     - *int*
     - Име на `търговските обект </barsy.help/210-dictionary/barsy.html>`__, в който е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$menu_id**
     - *int*
     - ID на каталог
   * - **$account_sid**
     - *int*
     - текстов идентификатор (ID) на `сметка </barsy.help/210-dictionary/account.html>`__ - уникално за системата
   * - **$create_date**
     - *string*
     - Дата на създаване на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$user_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, отговарящ текущо за `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$user_name**
     - *string*
     - Име на `потребител </barsy.help/210-dictionary/user.html>`__, отговарящ текущо за `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$place_id**
     - *int*
     - ID на място, към което е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$place_num**
     - *int*
     - Номер на място, към което е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$place_type**
     - *int*
     - ID на тип на мястото, към което е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$place_type_name**
     - *string*
     - Тип
   * - **$salon_name**
     - *string*
     - Име на салона, спрямо мястото
   * - **$status**
     - *int*
     - Статус на `сметката </barsy.help/210-dictionary/account.html>`__ (0=открира,1=закрита)
   * - **$is_locked**
     - *int*
     - Флаг за заключена `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$client_id**
     - *int*
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__, асоциран със `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$person_id**
     - *int*
     - ID на `представителя </barsy.help/210-dictionary/person.html>`__ за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$person_name**
     - *int*
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__ за `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_name**
     - *string*
     - Име на `клиент </barsy.help/210-dictionary/client.html>`__, асоциран със `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$total_sum**
     - *float*
     - Пълен тотал на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$total_sum_curr**
     - *float*
     - 
   * - **$discount**
     - *float*
     - Процент отстъпка/надбавка на `сметката </barsy.help/210-dictionary/account.html>`__ (<0 отстъпка, >0 надбавка)
   * - **$skip_account_discount_recalculate_flag**
     - *int*
     - Флаг дали да се прескочи прилагането на `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ тип 3

			(Отстъпка-`сметка </barsy.help/210-dictionary/account.html>`__) върху DISCOUNT. Веднъж вдигнат, остава 1 за целия живот на `сметката </barsy.help/210-dictionary/account.html>`__ - правилото повече не се преприлага. **По подразбиране:** 0
   * - **$close_date**
     - *string*
     - Дата на приключване на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$fx**
     - *int*
     - FX
   * - **$paymethod_id**
     - *string*
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$total_paid**
     - *float*
     - Общо платена сума по `сметката </barsy.help/210-dictionary/account.html>`__ спрямо плащанията
   * - **$total_paid_curr**
     - *float*
     - 
   * - **$total_real**
     - *float*
     - Сума на `сметката </barsy.help/210-dictionary/account.html>`__ с включена отстъпка/надбавка (т.е. краен тотал)
   * - **$total_real_curr**
     - *float*
     - 
   * - **$total_remain**
     - *float*
     - Сума на оттаващо за `плащане </barsy.help/210-dictionary/payment.html>`__ по тази `сметка </barsy.help/210-dictionary/account.html>`__ до този момент
   * - **$total_remain_curr**
     - *float*
     - 
   * - **$total_sum_after_row_discount**
     - *float*
     - Сума на `артикулите </barsy.help/210-dictionary/article.html>`__ с включена отстъпка на ниво поръчка
   * - **$total_sum_after_row_discount_curr**
     - *float*
     - 
   * - **$total_sum_storno**
     - *float*
     - Сума на сторнирани `артикули </barsy.help/210-dictionary/article.html>`__ (вкл. отстъпки)
   * - **$total_paid_sum_storno**
     - *float*
     - Сума на сторнирани плащания
   * - **$last_order_num**
     - *int*
     - Пореден номер на последна поръчка
   * - **$time_calculation**
     - *string*
     - Флаг за времево отчитане на мястото
   * - **$ref_date**
     - *string*
     - Документална дата на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$description**
     - *string*
     - Описание - свободен текст - видим в бележката към `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$notes**
     - *string*
     - Бележки - свободен текст - не се вижда от `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$account_alias**
     - *string*
     - Име на `сметката </barsy.help/210-dictionary/account.html>`__ - свободен текст
   * - **$delivery_address**
     - DeliveryAddressData_ 
     - Данни за доставка
   * - **$contact_name**
     - *string*
     - Лице за контакт
   * - **$phone**
     - *string*
     - Телефон
   * - **$delivery_zone_id**
     - *string*
     - Зона за доставка
   * - **$tracking_number**
     - *string*
     - Номер на товарителница
   * - **$tracking_ref_id**
     - *string*
     - Номер на товарителница от външна система
   * - **$speditor_id**
     - *int*
     - ID на спедитора
   * - **$orders**
     - OrderData_ []
     - Списък с `поръчките към сметката </barsy.help/210-dictionary/account-order.html>`__, групирани по `артикул </barsy.help/210-dictionary/article.html>`__, продажна цена, отстъпка, `модификатор </barsy.help/210-dictionary/modificator.html>`__, атрибути, ДДС (ако са поискани)
   * - **$orders_history**
     - OrderData_ []
     - Списък с `поръчките към сметката </barsy.help/210-dictionary/account-order.html>`__ (ако са поискани)
   * - **$client_group_id**
     - *int*
     - ID на клиентска група
   * - **$pos_id**
     - *int*
     - 
   * - **$pos_name**
     - *string*
     - 
   * - **$close_pos_id**
     - *string*
     - 
   * - **$close_pos_name**
     - *string*
     - 
   * - **$period_id**
     - *int*
     - 
   * - **$persons**
     - *int*
     - Брой хора
   * - **$account_period**
     - *string*
     - Продължителност на `сметката </barsy.help/210-dictionary/account.html>`__ hh:mm:ss
   * - **$payment_name**
     - *string*
     - Начин на `плащането </barsy.help/210-dictionary/payment.html>`__ на `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$paid_due_date**
     - *string*
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$account_num**
     - *string*
     - Пореден номер за текущия касов период
   * - **$unp**
     - *string*
     - Уникален номер на `продажбата </barsy.help/210-dictionary/sale.html>`__ (УНП) XXXХХХХХ-ZZZZ-0000001
   * - **$payments**
     - PaymentGroupedData_ []
     - Списък със сумирани плащания по начин на `плащане </barsy.help/210-dictionary/payment.html>`__ към `сметката </barsy.help/210-dictionary/account.html>`__  (ако са поискани)
   * - **$payments_history**
     - PaymentData_ []
     - Списък с всички плащания към `сметката </barsy.help/210-dictionary/account.html>`__  (ако са поискани)
   * - **$deal_id**
     - *int*
     - 
   * - **$deal_title**
     - *string*
     - 
   * - **$client_order_ids**
     - *string*
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ фигуриращи в `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$detailed_client_order_ids**
     - *string*
     - Списък от номерата на `клиентските заявки </barsy.help/210-dictionary/client-order.html>`__ с дата на издаването им фигуриращи в `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$service_status_id**
     - *int*
     - Статус на обслужването на `сметката </barsy.help/210-dictionary/account.html>`__ - ID

			* **0** - *Липсва описание*
			* **1** - *Липсва описание*
			* **2** - *Липсва описание*
			* **3** - *Липсва описание*
			* **4** - *Липсва описание*
			* **5** - *Липсва описание*
			* **6** - *Липсва описание*
			* **100** - *Липсва описание*
   * - **$service_status_name**
     - *string*
     - Статус на обслужването на `сметката </barsy.help/210-dictionary/account.html>`__ - Име
   * - **$user_can_edit**
     - *bool*
     - Флаг дали текущия `потребител </barsy.help/210-dictionary/user.html>`__ може да редактира тази `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$additional_data**
     - *object*
     - 
   * - **$lang_id**
     - *string*
     - Език за `сметката </barsy.help/210-dictionary/account.html>`__ (в фискалната бележка ще има имената на `артикулите </barsy.help/210-dictionary/article.html>`__ и на посочения език )
   * - **$confirmation_output_screen_check**
     - *bool*
     - Проверка дали `сметката </barsy.help/210-dictionary/account.html>`__ може да се визуализира за потвърждение на екран-ът, който е отворена. **По подразбиране:** true
   * - **$preferred_paymethod_id**
     - *int*
     - 
   * - **$confirmation_outputs**
     - *object*
     - 
   * - **$delivery_date**
     - *string*
     - Дата на доставка (подадена от `клиента </barsy.help/210-dictionary/client.html>`__).
   * - **$delivery_date_internal**
     - *string*
     - Дата на възможна доставка (изчислена от системата).
   * - **$currency_id**
     - *int*
     - ID на валута.

			*Ако е оставена непопълнена, ще се вземе системната валута* ( виж: :doc:`../currencies/getlist` )
   * - **$currency_rate**
     - *float*
     - Курс на валутата.

			*Ако остане непопълнена ще вземе валутата обвързана с currency_id*
   * - **$remote_id**
     - *int*
     - ID на отдалечена система ( виж: :doc:`../remotesystems/getlist` )
   * - **$ref_id**
     - *int* | *string*
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__ в отдалчена система

-----

DeliveryAddressData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Съдържа всички данни за адреса на `клиент </barsy.help/210-dictionary/client.html>`__

.. list-table::
   :header-rows: 1
   :align: center
   :name: DeliveryAddressData

   * - Параметър
     - Тип
     - Описание
   * - **$delivery_type**
     - *string*
     - Тип на доставката

			* **no** - *Без доставка*
			* **home** - *За вкъщи*
			* **address** - *Доставка до адрес*
			* **barsy** - Получаване от `търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **office** - *Получаване от офис на куриер* **По подразбиране:** 'no'
   * - **$country_name**
     - *string*
     - Име на държава
   * - **$country_id**
     - *string*
     - ID на държава
   * - **$dest_id**
     - *int*
     - ID на населено място ( виж: :doc:`../destinations/getlist` )
   * - **$address**
     - *string*
     - Адрес за доставка (кв,бул/ул,№,бл,вх,ет)
   * - **$address_neighborhood**
     - *string*
     - Квартал на адреса за доставка
   * - **$address_number**
     - *string*
     - Номер на улица/булевард за доставка
   * - **$address_building**
     - *string*
     - Блок за доставка
   * - **$address_entry**
     - *string*
     - Вход на блок за доставка
   * - **$address_floor**
     - *string*
     - Номер на етаж за доставка
   * - **$address_ap**
     - *string*
     - Номер на апартамент за доставка
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (ако типа на доставката е "Взимане от `търговски обект </barsy.help/210-dictionary/barsy.html>`__") ( виж: :doc:`../barsys/getlist` )
   * - **$speditor_id**
     - *int*
     - ID на спедитор ( виж: :doc:`../speditors/getlist` )
   * - **$office_id**
     - *int*
     - ID на офис на куриер по номенклатурата на съответния куриер ( виж: :doc:`../speditors/getofficelist` )
   * - **$office_type**
     - *string*
     - 
   * - **$coords**
     - *string*
     - Координати на адреса
   * - **$zip**
     - *string*
     - Пощенски код
   * - **$description**
     - *string*
     - Допълнителна информация към адреса за доставка

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

PaymentGroupedData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PaymentGroupedData

   * - Параметър
     - Тип
     - Описание
   * - **$paymethod_id**
     - *int*
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../paymentmethods/getlist` )
   * - **$name**
     - *string*
     - Име на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../paymentmethods/getlist` )
   * - **$fx**
     - *string*
     - Флаг дали `плащането </barsy.help/210-dictionary/payment.html>`__ е фискално
   * - **$paid_sum**
     - *float*
     - Сума на плащанията от този начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$payments_count**
     - *float*
     - Сума на плащанията от този начин на `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$export_id**
     - *string*
     - Export_id на методът за `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$transaction_id**
     - *string*
     - Номер на трансакцията предоставена от пос терминала

-----

PaymentData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за регистрирано `плащане </barsy.help/210-dictionary/payment.html>`__ (приход или разход)

.. list-table::
   :header-rows: 1
   :align: center
   :name: PaymentData

   * - Параметър
     - Тип
     - Описание
   * - **$operation**
     - *string*
     - Операция на `плащането </barsy.help/210-dictionary/payment.html>`__ (приход или разход)

			* **CRD** - *Приход*
			* **DBT** - *Разход*
   * - **$payment_id**
     - *int*
     - ID на `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$barsy_id**
     - *int*
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../barsys/getlist` )
   * - **$period_id**
     - *int*
     - ID на период (касова смяна)
   * - **$paymethod_id**
     - *int*
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../paymentmethods/getlist` )
   * - **$original_paid_sum**
     - *float*
     - Платена сума във валута на `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$paid_sum**
     - *float*
     - Платена сума в системна валута (изчислена от original_paid_sum и currency_rate)
   * - **$paid_used**
     - *float*
     - Използвана част от платената сума (асоциирана към `сметки </barsy.help/210-dictionary/account.html>`__, зареждания и др.)
   * - **$user_id**
     - *int*
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, приел `плащането </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../users/getlist` )
   * - **$client_id**
     - *int*
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__ (при приходни плащания) ( виж: :doc:`../clients/getlist` )
   * - **$supplier_id**
     - *int*
     - ID на `доставчик </barsy.help/210-dictionary/supplier.html>`__ (при разходни плащания) ( виж: :doc:`../suppliers/getlist` )
   * - **$create_date**
     - *string*
     - Дата на създаване на `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$ref_date**
     - *string*
     - Дата вальор (документна дата)
   * - **$delete_flag**
     - *int*
     - Флаг, дали `плащането </barsy.help/210-dictionary/payment.html>`__ е маркирано като изтрито

			* **0** - *активно*
			* **1** - *изтрито*
   * - **$fx**
     - *int*
     - Флаг, дали `плащането </barsy.help/210-dictionary/payment.html>`__ е фискално (извършва фискална операция)

			* **0** - *нефискално*
			* **1** - *фискално*
   * - **$confirmed**
     - *int*
     - Флаг за потвърдено `плащане </barsy.help/210-dictionary/payment.html>`__

			* **0** - *непотвърдено*
			* **1** - *потвърдено*
   * - **$ref_num**
     - *string*
     - Референтен номер (напр. банково извлечение)
   * - **$description**
     - *string*
     - Свободен текст / описание
   * - **$req_value**
     - *string*
     - Допълнителна информация към `плащането </barsy.help/210-dictionary/payment.html>`__ (настройва се в конкретния начин на `плащане </barsy.help/210-dictionary/payment.html>`__)
   * - **$payment_data**
     - *string* | *stdClass*
     - Допълнителни данни за `плащането </barsy.help/210-dictionary/payment.html>`__ (JSON обект)
   * - **$payment_print_data**
     - *string* | *stdClass*
     - Данни за печат на касова бележка (JSON обект)
   * - **$transaction_id**
     - *string*
     - Номер на транзакция (напр. от POS терминал)
   * - **$storno_sum**
     - *float*
     - Сума на сторнираните плащания по това `плащане </barsy.help/210-dictionary/payment.html>`__ **По подразбиране:** 0
   * - **$storno_parent_id**
     - *int*
     - ID на родителско `плащане </barsy.help/210-dictionary/payment.html>`__ при сторно операция
   * - **$available_sum**
     - *float*
     - Неизползван остатък от платената сума
   * - **$currency_id**
     - *int*
     - ID на валута на `плащането </barsy.help/210-dictionary/payment.html>`__ ( виж: :doc:`../currencies/getlist` )
   * - **$currency_rate**
     - *float*
     - Курс на валутата към момента на `плащането </barsy.help/210-dictionary/payment.html>`__
   * - **$provider_id**
     - *int*
     - ID на платежен оператор (VPOS, POS терминал и др.)
   * - **$type_id**
     - *int*
     - Тип на начина на `плащане </barsy.help/210-dictionary/payment.html>`__

			* **-2** - *Служебен*
			* **-1** - *Неразпознат*
			* **1** - *В брой*
			* **2** - *Банка*
			* **3** - `Ваучер </barsy.help/210-dictionary/card.html>`__
			* **4** - *Чек*
			* **5** - *Карта (присъствена)*
			* **6** - *Карта (неприсъствена)*
			* **7** - *Други*
			* **8** - *Наложен платеж*
			* **9** - *Пощенски паричен превод*
			* **10** - barsy-`Ваучер </barsy.help/210-dictionary/card.html>`__ (фискален)
			* **11** - *Бонус програма*
			* **12** - barsy-`Ваучер </barsy.help/210-dictionary/card.html>`__ (нефискален)

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

     .. literalinclude:: ../../sources/places_getlistwithaccountsonly/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/places_getlistwithaccountsonly/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/places_getlistwithaccountsonly/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/places_getlistwithaccountsonly/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/places_getlistwithaccountsonly/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/places_getlistwithaccountsonly/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__


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

