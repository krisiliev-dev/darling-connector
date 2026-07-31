.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReservationsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reservations\\Data\\ReservationsListFiltersData


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
     - Филтър по id на `търговски обект </barsy.help/210-dictionary/barsy.html>`__

			 пример: "1" ( виж: :doc:`../methods/barsys/getlist` )
   * - **$user_id**
     - *int*
     - 
     - Филтър по id на `потребител </barsy.help/210-dictionary/user.html>`__ (създател)

			 пример: "1" ( виж: :doc:`../methods/users/getlist` )
   * - **$client_id**
     - *int*
     - 
     - Филтър по id на `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "1" ( виж: :doc:`../methods/clients/getlist` )
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
     - Филтър по дата на създаване

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$last_update**
     - *datetime*
     - 
     - Филтър по дата на актуализация

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$from_date**
     - *datetime*
     - 
     - Филтър по начална дата на `резервацията </barsy.help/210-dictionary/reservation.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$to_date**
     - *datetime*
     - 
     - Филтър по крайна дата на `резервацията </barsy.help/210-dictionary/reservation.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$date_window**
     - *datetime*
     - 
     - Филтър по "дата от до"

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по флаг "Изтрит"

			 пример: "0"
   * - **$reservations_today**
     - *bool*
     - 
     - Взима `резервациите </barsy.help/210-dictionary/reservation.html>`__ за деня
   * - **$status_and_interval**
     - *int* | *array*
     - 
     - Филтър по статус и сегашна дата + интервал 5 часа
   * - **$status_id**
     - *int* | *array*
     - 
     - Филтър по статус

			 пример: "1"
   * - **$for_today**
     - *bool*
     - 
     - Филтър по днешният ден
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$q**
     - *string*
     - 
     - Smart search по име, телефон или `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "\"Pesho\""
   * - 
     - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
     - 
   * - **$reservation_id**
     - *int*
     - 
     - Филтър по id на `резервация </barsy.help/210-dictionary/reservation.html>`__

			 пример: "1" ( виж: :doc:`../methods/reservations/get` )

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reservations/getlist`

