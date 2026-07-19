.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientsListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към клиент. Всяка опция включва съответната колона към данните за всеки

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
`клиент </barsy.help/210-dictionary/client.html>`__ от списъка. Основните данни се връщат винаги, а останалите при стойност true.

*Приема и стария формат — списък с имена (напр. ["email","tel"]) — който се превежда към булеви флагове.*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clients\\Data\\ClientsListExtraPropertiesData


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
   * - **$client_id**
     - *bool*
     - true
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$client_name**
     - *bool*
     - true
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$lang_id**
     - *bool*
     - true
     - ID на езика на `клиента </barsy.help/210-dictionary/client.html>`__
   * - **$export_id**
     - *bool*
     - false
     - "Export ID" на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
     - 
   * - **$discount**
     - *bool*
     - true
     - Отстъпка на `клиента </barsy.help/210-dictionary/client.html>`__ (форматирана)
   * - **$make_invoice_auto**
     - *bool*
     - false
     - Автоматично създаване на `фактура </barsy.help/210-dictionary/invoice.html>`__

			Показва дали за `клиента </barsy.help/210-dictionary/client.html>`__ автоматично се създава `фактура </barsy.help/210-dictionary/invoice.html>`__. Взема се настройката на `клиента </barsy.help/210-dictionary/client.html>`__, при липса — тази на групата му, а накрая стойността по подразбиране.

			 пример: "1"
   * - **$send_invoice_auto**
     - *bool*
     - false
     - Автоматично изпращане на `фактура </barsy.help/210-dictionary/invoice.html>`__

			Показва дали за `клиента </barsy.help/210-dictionary/client.html>`__ автоматично се изпраща `фактура </barsy.help/210-dictionary/invoice.html>`__. Взема се настройката на `клиента </barsy.help/210-dictionary/client.html>`__, при липса — тази на групата му, а накрая стойността по подразбиране.

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$group_id**
     - *bool*
     - true
     - ID на клиентската група
   * - **$recruit_client_id**
     - *bool*
     - false
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__-източник ("Източник `клиент </barsy.help/210-dictionary/client.html>`__")

			 пример: "1"
   * - **$client_source_id**
     - *bool*
     - false
     - ID на източника на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$agent_client_id**
     - *bool*
     - false
     - ID на агента на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
     - 
   * - **$tel**
     - *bool*
     - false
     - Телефон на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$email**
     - *bool*
     - false
     - Имейл на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$email_invoices**
     - *bool*
     - false
     - Имейл за `фактури </barsy.help/210-dictionary/invoice.html>`__

			 пример: "1"
   * - **$client_auth**
     - *bool*
     - false
     - Потребителско име на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$client_code**
     - *bool*
     - false
     - Клиентски код

			 пример: "1"
   * - **$company_name**
     - *bool*
     - false
     - Име на компанията

			 пример: "1"
   * - **$address**
     - *bool*
     - false
     - Адрес

			 пример: "1"
   * - **$bulstat**
     - *bool*
     - false
     - БУЛСТАТ

			 пример: "1"
   * - **$vat_num**
     - *bool*
     - false
     - ДДС номер

			 пример: "1"
   * - **$mol**
     - *bool*
     - false
     - МОЛ

			 пример: "1"
   * - **$town**
     - *bool*
     - false
     - Град

			 пример: "1"
   * - **$zip**
     - *bool*
     - false
     - Пощенски код

			 пример: "1"
   * - **$delivery_address**
     - *bool*
     - false
     - Адрес за доставка

			 пример: "1"
   * - **$delivery_zone_id**
     - *bool*
     - false
     - Зона за доставка

			 пример: "1"
   * - **$description**
     - *bool*
     - false
     - Описание/бележка за `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$ml_subscribed**
     - *bool*
     - false
     - Дали `клиентът </barsy.help/210-dictionary/client.html>`__ е абониран за бюлетин

			 пример: "1"
   * - **$is_guest**
     - *bool*
     - false
     - Дали `клиентът </barsy.help/210-dictionary/client.html>`__ е гост

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
     - 
   * - **$client_create_date**
     - *bool*
     - false
     - Дата на създаване на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$last_update**
     - *bool*
     - false
     - Дата на последна промяна

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clients/getlist`
	 * :doc:`../methods/clients/getlistsmart`

Виж също
--------

 * `Клиент </barsy.help/210-dictionary/client.html>`__

