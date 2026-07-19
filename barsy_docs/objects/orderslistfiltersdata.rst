.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

OrdersListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Orders\\Data\\OrdersListFiltersData


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

			 пример: "123" ( виж: :doc:`../methods/accounts/getlist` )
   * - **$order_id**
     - *int*
     - 
     - Филтър по ID на поръчката

			 пример: "123"
   * - **$order_barsy_id**
     - *int*
     - 
     - Филтър по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ на поръчката

			 пример: "3" ( виж: :doc:`../methods/barsys/getlist` )
   * - **$order_account_id**
     - *int*
     - 
     - Филтър по ID на `сметка </barsy.help/210-dictionary/account.html>`__ на поръчката

			 пример: "123" ( виж: :doc:`../methods/accounts/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$barsy_ids**
     - *int*
     - 
     - Филтър по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__

			 пример: "3" ( виж: :doc:`../methods/barsys/getlist` )
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
   * - **$paymethod_id**
     - *int*
     - 
     - Филтър по начин на `плащане </barsy.help/210-dictionary/payment.html>`__ на `сметката </barsy.help/210-dictionary/account.html>`__

			 пример: "1" ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$ref_date**
     - *datetime*
     - 
     - Филтър по дата на `сметка </barsy.help/210-dictionary/account.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$date**
     - *datetime*
     - 
     - Филтър по дата на поръчката (период или точна дата) — кога е направена `продажбата </barsy.help/210-dictionary/sale.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$served_date**
     - *datetime*
     - 
     - Филтър по дата на обслужване на поръчката (период или точна дата)

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$parents_only**
     - *int*
     - 
     - Филтър който извежда родителските и нормалните поръчки (комбо меню)

			 пример: "1"
   * - **$exclude_advance_payments**
     - *int*
     - 
     - Филтър който извежда поръчките като не включва `артикул </barsy.help/210-dictionary/article.html>`__ (и) "Авансово `плащане </barsy.help/210-dictionary/payment.html>`__"

			 пример: "1"
   * - **$common_reason**
     - *int*
     - 
     - Филтър по стандартна причина

			 пример: "1"
   * - **$output_pos**
     - *int*
     - 
     - Филтър по output `каса </barsy.help/210-dictionary/pos.html>`__

			 пример: "1"
   * - **$service_status_id**
     - *int*
     - 
     - Филтър по статус обслужване на `сметка </barsy.help/210-dictionary/account.html>`__

			 пример: "1" ( виж: :doc:`../methods/accounts/servicestatusgetlist` )
   * - **$status**
     - *int*
     - 
     - Филтър по статус на поръчката (напр. продадена/сторно/чакаща)

			 пример: "2"
   * - 
     - 
     - 
     - 
   * - :category_header:`Анализ на продажби`
     - 
     - 
     - 
   * - **$article_id**
     - *int*
     - 
     - Филтър по ID на `артикул </barsy.help/210-dictionary/article.html>`__ — `продажби </barsy.help/210-dictionary/sale.html>`__ на конкретен `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "42" ( виж: :doc:`../methods/articles/getlist` )
   * - **$category_id**
     - *int*
     - 
     - Филтър по `категория </barsy.help/210-dictionary/category.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__ — `продажби </barsy.help/210-dictionary/sale.html>`__ по `категория </barsy.help/210-dictionary/category.html>`__

			 пример: "5" ( виж: :doc:`../methods/categories/getlist` )
   * - **$user_id**
     - *int*
     - 
     - Филтър по ID на `потребителя </barsy.help/210-dictionary/user.html>`__, направил поръчката (продавач/касиер) — `продажби </barsy.help/210-dictionary/sale.html>`__ по `потребител </barsy.help/210-dictionary/user.html>`__

			 пример: "1" ( виж: :doc:`../methods/users/getlist` )
   * - **$served_by**
     - *int*
     - 
     - Филтър по ID на `потребителя </barsy.help/210-dictionary/user.html>`__, обслужил поръчката

			 пример: "1" ( виж: :doc:`../methods/users/getlist` )
   * - **$stream_id**
     - *int*
     - 
     - Филтър по ID на `поток </barsy.help/210-dictionary/flow.html>`__ (кухня/бар) на `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "2" ( виж: :doc:`../methods/streams/getlist` )
   * - **$pos_id**
     - *int*
     - 
     - Филтър по ID на `каса </barsy.help/210-dictionary/pos.html>`__, на която е направена поръчката

			 пример: "1" ( виж: :doc:`../methods/poses/getlist` )
   * - **$tax_id**
     - *int*
     - 
     - Филтър по ДДС група на поръчката

			 пример: "1" ( виж: :doc:`../methods/taxgroups/getlist` )

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/orders/getlist`

