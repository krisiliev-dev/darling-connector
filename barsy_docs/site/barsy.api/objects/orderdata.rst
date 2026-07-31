.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

OrderData
======================================================================================
Един ред-поръчка (продажба на конкретен артикул в сметка) — резултатен запис на Orders_getlist.

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Базовите полета се връщат винаги; останалите се попълват само когато съответната опция е поискана през `extra_properties` (виж OrdersListExtraPropertiesData). Свойствата нямат стойност по подразбиране — непоисканите остават нехидратирани и **не присъстват** в резултата (JSON), за да не подвеждат получателя, че данните са `null`. Хидратира се автоматично от резултатния ред (BaseType).

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Orders\\Data\\OrderData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$order_id**
     - *int*
     - 
     - ID на поръчката (ред в `сметка </barsy.help/210-dictionary/account.html>`__)
   * - **$account_id**
     - *int*
     - 
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__, към която е поръчката ( виж: :doc:`../methods/accounts/getlist` )
   * - **$barsy_id**
     - *int*
     - 
     - ID на търговския обект ( виж: :doc:`../methods/barsys/getlist` )
   * - **$pos_id**
     - *int*
     - 
     - ID на `касата </barsy.help/210-dictionary/pos.html>`__, на която е направена поръчката ( виж: :doc:`../methods/poses/getlist` )
   * - **$place_id**
     - *int*
     - 
     - ID на място, към което е `сметката </barsy.help/210-dictionary/account.html>`__
   * - **$article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/articles/getlist` )
   * - **$article_name**
     - *string*
     - 
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name_ml**
     - *MultiLanguageData*
     - 
     - Многоезично име на `артикула </barsy.help/210-dictionary/article.html>`__ (не включва системното article_name)
   * - **$article_type**
     - *int*
     - 
     - Тип на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$stream_id**
     - *int*
     - 
     - ID на `поток </barsy.help/210-dictionary/flow.html>`__ (кухня/бар) на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/streams/getlist` )
   * - **$cat_name**
     - *string*
     - 
     - `Категория </barsy.help/210-dictionary/category.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__ — при extra_properties.category ( виж: :doc:`../methods/categories/getlist` )
   * - **$amount**
     - *float*
     - 
     - Количество за този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$new_amount**
     - *float*
     - 
     - Ново количество (за операции по редакция)
   * - **$amount_unit**
     - *float*
     - 
     - Единица `продажба </barsy.help/210-dictionary/sale.html>`__ за този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount_type_id**
     - *int*
     - 
     - ID на типа количество ( виж: :doc:`../methods/amounttypes/getlist` )
   * - **$amount_type_name_short**
     - *string*
     - 
     - Кратко име на типа количество ( виж: :doc:`../methods/amounttypes/getlist` )
   * - **$current_price**
     - *float*
     - 
     - Текуща (продажна) единична цена
   * - **$actual_price**
     - *float*
     - 
     - Актуална цена на `артикула </barsy.help/210-dictionary/article.html>`__ (по ценоразпис)
   * - **$discount**
     - *float*
     - 
     - Отстъпка на реда в проценти — при extra_properties.discount
   * - **$tax**
     - *float*
     - 
     - Процент ДДС на реда — при extra_properties.tax
   * - **$tax_id**
     - *int*
     - 
     - ID на ДДС група — при extra_properties.tax ( виж: :doc:`../methods/taxgroups/getlist` )
   * - **$tax_code**
     - *string*
     - 
     - Данъчен код (ДДС група) — при extra_properties.tax
   * - **$tax_region_id**
     - *int*
     - 
     - Данъчен регион — при extra_properties.tax
   * - **$line_total**
     - *float*
     - 
     - Сума на реда (количество × цена с отстъпката на `сметката </barsy.help/210-dictionary/account.html>`__) — при extra_properties.line_total
   * - **$actual_price_base**
     - *float*
     - 
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__ — при extra_properties.base_price
   * - **$original_current_price**
     - *float*
     - 
     - Първоначална единична цена преди корекции — при extra_properties.original_price
   * - **$current_pricelist_id**
     - *int*
     - 
     - ID на ценоразписа, по който е продаден редът — при extra_properties.pricelist
   * - **$reason_id**
     - *int*
     - 
     - Причина за реда (`продажба </barsy.help/210-dictionary/sale.html>`__/връщане/сторно/авансово `плащане </barsy.help/210-dictionary/payment.html>`__) — при extra_properties.reason
   * - **$storno_of_account_id**
     - *int*
     - 
     - ID на `сметката </barsy.help/210-dictionary/account.html>`__, която сторнира този ред (NULL ако не е сторниран) — при extra_properties.storno ( виж: :doc:`../methods/accounts/getlist` )
   * - **$status**
     - *int*
     - 
     - Статус на поръчката
   * - **$order_status_title**
     - *string*
     - 
     - Заглавие на статуса на поръчката
   * - **$date**
     - *string*
     - 
     - Дата на поръчката

			 пример: "\"2024-01-01 12:30:00\""
   * - **$ref_date**
     - *string*
     - 
     - Вальор (документна дата) на `сметката </barsy.help/210-dictionary/account.html>`__ — при extra_properties.account_data
   * - **$start_service_date**
     - *string*
     - 
     - Дата, от която поръчката трябва да започне да се обслужва
   * - **$served_date**
     - *string*
     - 
     - Дата на обслужване
   * - **$served_by**
     - *int*
     - 
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, обслужил поръчката ( виж: :doc:`../methods/users/getlist` )
   * - **$served_by_user**
     - *string*
     - 
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, обслужил поръчката
   * - **$user_name**
     - *string*
     - 
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, направил поръчката (продавач/касиер)
   * - **$process_time**
     - *int*
     - 
     - Време за приготвяне в секунди (за следене на закъснения; ако липсва — взема се от `потока </barsy.help/210-dictionary/flow.html>`__)

			 пример: "15"
   * - **$order_ref_id**
     - *int*
     - 
     - ID на поръчката според външна система
   * - **$client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ — при extra_properties.account_data/client_data ( виж: :doc:`../methods/clients/getlist` )
   * - **$client_name**
     - *string*
     - 
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__ — при extra_properties.account_data/client_data
   * - **$modificators**
     - *ModificatorData*
     - 
     - Списък с `модификатори </barsy.help/210-dictionary/modificator.html>`__ за този `артикул </barsy.help/210-dictionary/article.html>`__ — при extra_properties.modificators
   * - **$article_attributes**
     - *ArticleAttributesData*
     - 
     - Групови атрибути за този `артикул </barsy.help/210-dictionary/article.html>`__ — при extra_properties.article_attributes
   * - **$outputs**
     - *PosStreamOutputsData*
     - 
     - Изходи/output екрани на поръчката (`потоци </barsy.help/210-dictionary/flow.html>`__ към `каси </barsy.help/210-dictionary/pos.html>`__) — при extra_properties.outputs

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getbytaxes`
	 * :doc:`../methods/accounts/getlist`
	 * :doc:`../methods/accounts/get`
	 * :doc:`../methods/orders/getlist`
	 * :doc:`../methods/places/getlistwithaccountsonly`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__
 * `Продажба </barsy.help/210-dictionary/sale.html>`__
 * `Сметка </barsy.help/210-dictionary/account.html>`__

