.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

AccountsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Accounts\\Data\\AccountsListFiltersData


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
   * - **$account_id**
     - *int*
     - 
     - Филтър по ID на `сметка </barsy.help/210-dictionary/account.html>`__

			 пример: "123"
   * - **$account_sid**
     - *string*
     - 
     - Филтър по точен SID на `сметка </barsy.help/210-dictionary/account.html>`__

			 пример: "\"hf98ry9f28h2\""
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

			 пример: "3" ( виж: :doc:`../methods/barsys/getlist` )
   * - **$user_id**
     - *int*
     - 
     - Филтър по `потребител </barsy.help/210-dictionary/user.html>`__, създал `сметката </barsy.help/210-dictionary/account.html>`__

			 пример: "1" ( виж: :doc:`../methods/users/getlist` )
   * - **$paymethod_id**
     - *int*
     - 
     - Филтър по начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "1" ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$period_id**
     - *int*
     - 
     - Филтър по период

			 пример: "12"
   * - **$client_id**
     - *int*
     - 
     - Филтър по ID на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "12" ( виж: :doc:`../methods/clients/getlist` )
   * - **$client_group_id**
     - *int*
     - 
     - Филтър по ID на група на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "12" ( виж: :doc:`../methods/clientgroups/getlist` )
   * - **$place_id**
     - *int*
     - 
     - Филтър по ID на мястото на `сметката </barsy.help/210-dictionary/account.html>`__

			 пример: "12" ( виж: :doc:`../methods/places/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$status**
     - *int*
     - 
     - Филтър по статус на `сметката </barsy.help/210-dictionary/account.html>`__

			* **0** - *Открита*
			* **1** - *Закрита*

			 пример: "1"
   * - **$list_closed**
     - *string*
     - 
     - Филтър

			 пример: "1"
   * - **$list_opened**
     - *string*
     - 
     - Филтър

			 пример: "1"
   * - **$service_status_id**
     - *string*
     - 
     - Сервизен статус на поръчката

			* **1** - Чака `плащане </barsy.help/210-dictionary/payment.html>`__
			* **2** - *Чака одобрение*
			* **3** - *За обслужване*
			* **4** - *Обслужена*
			* **5** - *Доставена*
   * - :deprecated:`$confirmation_output_screen`
     - *int*
     - 
     - Наличие на потвърдителен екран

			Връща само `сметките </barsy.help/210-dictionary/account.html>`__, за които текущото работно място има потвърдителен екран. :deprecated_text:`Отхвърлено: */`

			 пример: "1"
   * - **$service_statuses_with_confirmation_output_screen**
     - *int* | *int*
     - 
     - Сервизни статуси с потвърдителен екран

			Връща само `сметките </barsy.help/210-dictionary/account.html>`__ с някой от посочените сервизни статуси, за които текущото работно място има потвърдителен екран.

			* **1** - Чака `плащане </barsy.help/210-dictionary/payment.html>`__
			* **2** - *Чака одобрение*
			* **3** - *За обслужване*
			* **4** - *Обслужена*
			* **5** - *Доставена* ( виж: :doc:`../methods/accounts/servicestatusgetlist` )
   * - **$place_zone_current_user**
     - *string*
     - 
     - Филтър по зона на `потребителя </barsy.help/210-dictionary/user.html>`__

			Връща само `сметките </barsy.help/210-dictionary/account.html>`__, чието място попада в зоната на текущия `потребител </barsy.help/210-dictionary/user.html>`__.

			 пример: "1"
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
     - Филтър по дата на откриване на `сметка </barsy.help/210-dictionary/account.html>`__ (период или точна дата)

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$close_date**
     - *datetime*
     - 
     - Филтър по дата на затваряне на `сметката </barsy.help/210-dictionary/account.html>`__ (период или точна дата)

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$ref_date**
     - *datetime*
     - 
     - Филтър по вальор (документна дата) на `сметка </barsy.help/210-dictionary/account.html>`__ (период или точна дата)

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$last_order_date**
     - *datetime*
     - 
     - Филтър по дата на последна поръчка в `сметката </barsy.help/210-dictionary/account.html>`__ (период или точна дата)

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - 
     - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
     - 
   * - **$delivery_date**
     - *datetime*
     - 
     - Филтър по час за доставка (b_account_notes.DELIVERY_DATE) - период или точна дата

			 пример: "[\"2025-09-01 00:00:00\",\"2025-09-01 23:59:00\"]"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getlist`

