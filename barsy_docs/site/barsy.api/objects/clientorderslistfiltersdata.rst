.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientOrdersListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clientorders\\Data\\ClientOrdersListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_order_id**
     - *int*
     - 
     - ID на `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__ (по barsy номенклатура)
   * - **$order_num**
     - *string*
     - 
     - Номер на заявката от външна номенклатура
   * - **$client_id**
     - *int*
     - 
     - Филтриране по `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който текущо се обработва заявката
   * - **$delivery_barsy_id**
     - *int*
     - 
     - ID на търговския обект, в който ще се получава заявката (ако е до `търговски обект </barsy.help/210-dictionary/barsy.html>`__)
   * - **$from_barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който е направена заявката
   * - **$last_update**
     - *datetime*
     - 
     - Дата на последна промяна в `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__ (период или точна дата)

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$delivery_date**
     - *datetime*
     - 
     - Дата за доставка (период или точна дата)

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$status_id**
     - *int*
     - 
     - Статус на `клиентската заявка </barsy.help/210-dictionary/client-order.html>`__

			 пример: "4"
   * - **$search**
     - *string*
     - 
     - Търсене по client_order_id и order_num

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientorders/getlist`

