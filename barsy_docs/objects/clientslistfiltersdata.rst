.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clients\\Data\\ClientsListFiltersData


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
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$barsy_id**
     - *int*
     - 
     - Филтър по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__

			 пример: "1" ( виж: :doc:`../methods/barsys/get` , :doc:`../methods/barsys/getlist` )
   * - **$client_group_id**
     - *int*
     - 
     - Филтър по ID на клиентска група

			 пример: "1" ( виж: :doc:`../methods/clientgroups/getlist` )
   * - **$delivery_zone_id**
     - *string*
     - 
     - Филтър по зона за доставка

			 пример: "123"
   * - **$recruit_client_id**
     - *int*
     - 
     - Филтър по "Източник `клиент </barsy.help/210-dictionary/client.html>`__"

			 пример: "1" ( виж: :doc:`../methods/clients/get` , :doc:`../methods/clients/getlist` )
   * - **$client_source_id**
     - *int*
     - 
     - Филтър по "Препоръчан от"

			 пример: "1"
   * - **$agent_client_id**
     - *int*
     - 
     - Филтър по "Агент"

			 пример: "1" ( виж: :doc:`../methods/clients/get` , :doc:`../methods/clients/getlist` )
   * - **$remote_ref_id**
     - *int*
     - 
     - Id на `клиента </barsy.help/210-dictionary/client.html>`__ в отдалечена система

			 пример: "1" ( виж: :doc:`../methods/remotesystems/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
     - 
   * - **$client_id**
     - *int*
     - 
     - Филтър по ID на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$export_id**
     - *int*
     - 
     - Филтър по "Export ID"

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$client_name**
     - *string*
     - 
     - Филтър по име на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "\"Beer\""
   * - **$get_smart**
     - *string*
     - 
     - Филтър по име на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "\"Beer\""
   * - **$client_name_match_i**
     - *string*
     - 
     - Филтър по точно име на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "\"Beer\""
   * - **$tel**
     - *string*
     - 
     - Филтър по телефон на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "934803928"
   * - **$recommended**
     - *string*
     - 
     - Филтър по признака "Препоръчан"

			 пример: "1"
   * - **$description**
     - *string*
     - 
     - Филтър по описание на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "\"\\u0422\\u0435\\u043a\\u0441\\u0442\""
   * - **$client_code**
     - *string*
     - 
     - Филтър по клиентски код

			 пример: "123"
   * - **$client_code_match**
     - *string*
     - 
     - Филтър по точно подаден клиентски код

			 пример: "123"
   * - **$company_name**
     - *string*
     - 
     - Филтър по име на компания

			 пример: "123"
   * - **$address**
     - *string*
     - 
     - Филтър по адрес

			 пример: "123"
   * - **$bulstat**
     - *string*
     - 
     - Филтър по БУЛСТАТ

			 пример: "123"
   * - **$vat_num**
     - *string*
     - 
     - Филтър по ДДС номер

			 пример: "123"
   * - **$mol**
     - *string*
     - 
     - Филтър по MOL

			 пример: "123"
   * - **$email**
     - *string*
     - 
     - Филтър по имейл

			*Намира съвпадение и по част от имейл адреса.*

			 пример: "123"
   * - **$email_match**
     - *string*
     - 
     - Филтър по имейл по точно подадена стойност

			 пример: "123"
   * - **$email_invoices**
     - *string*
     - 
     - Филтър по имейл за `фактура </barsy.help/210-dictionary/invoice.html>`__

			 пример: "123"
   * - **$delivery_address**
     - *string*
     - 
     - Филтър по адрес за доставка

			 пример: "123"
   * - **$index**
     - *string*
     - 
     - Филтър по символ

			 пример: "\"A\""
   * - **$email_invoices_smart**
     - *string*
     - 
     - Филтър по email за фактута

			 пример: "\"gmail\""
   * - **$client_auth**
     - *string*
     - 
     - Филтър по потребителско име

			 пример: "\"ChichoGosho85@gmail.com\""
   * - **$client_auth_match**
     - *string*
     - 
     - Филтър по точно потребителско име

			 пример: "\"ChichoGosho85@gmail.com\""
   * - **$query**
     - *string*
     - 
     - Филтър по текстово търсене

			 пример: "\"gmail\""
   * - **$zip**
     - *string*
     - 
     - Филтър по пощенски код

			 пример: "1000"
   * - **$town**
     - *string*
     - 
     - Филтър по град

			 пример: "\"\\u0421\\u043e\\u0444\\u0438\\u044f\""
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$client_create_date**
     - *string*
     - 
     - Филтър по дата на създаване на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "\"2018-01-01\""
   * - **$last_update**
     - *string*
     - 
     - Филтър по последен ъпдейт на `клиент </barsy.help/210-dictionary/client.html>`__.

			*Точна стойност.*

			 пример: "1"
   * - **$remote_last_update**
     - *string*
     - 
     - Дата на последен ъпдейт в отдалечената система

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$discount**
     - *int*
     - 
     - Филтър по отстъпка на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по изтритите `клиенти </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$ml_subscribed**
     - *int*
     - 
     - Филтър по `абонамент </barsy.help/210-dictionary/subscription.html>`__ за бюлетин

			 пример: "1"
   * - **$is_guest**
     - *int*
     - 
     - Филтър по флаг за гост

			 пример: "1"
   * - **$hide_anonymous**
     - *int*
     - 1
     - Скрива анонимния `клиент </barsy.help/210-dictionary/client.html>`__ (CLIENT_ID = 1) от резултата

			 пример: "1"
   * - **$for_remote_update**
     - *int*
     - 
     - Филтер по това дали `клиента </barsy.help/210-dictionary/client.html>`__ е за обновяване в отдалечената система

			 пример: "1"
   * - **$credit_limit**
     - *float*
     - 
     - Филтер по клиентски лимит

			 пример: "100"
   * - **$make_invoice_auto**
     - *float*
     - 
     - Филтър по автоматично създаване на `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$send_invoice_auto**
     - *float*
     - 
     - Филтър по автоматично изпращане на `фактури </barsy.help/210-dictionary/invoice.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clients/getlist`
	 * :doc:`../methods/clients/getlistsmart`

