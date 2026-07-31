.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReservationSaveData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reservations\\Data\\ReservationSaveData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_id**
     - *int*
     - 1
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__ на `резервацията </barsy.help/210-dictionary/reservation.html>`__ ( виж: :doc:`../methods/clients/getlist` )
   * - **$client**
     - *ClientInputData*
     - 
     - Данни за `клиент </barsy.help/210-dictionary/client.html>`__.

			Използват се за откриване на `клиент </barsy.help/210-dictionary/client.html>`__ в системата, ако нямаме предоставено client_id. Ако не е открит, ще създадем.
   * - **$person_id**
     - *int*
     - 
     - ID на `представителя </barsy.help/210-dictionary/person.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__. ( виж: :doc:`../methods/persons/getlist` )
   * - **$person_name**
     - *string*
     - 
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__.

			Ако няма подаден $person_id, ще се въздаде нов `представител </barsy.help/210-dictionary/person.html>`__ с това име
   * - **$contact_name**
     - *string*
     - 
     - Лице за контакт за тази `резервация </barsy.help/210-dictionary/reservation.html>`__
   * - **$phone**
     - *string*
     - 
     - Телефонен номер за контакт за тази `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$from_date**
     - *string*
     - 
     - Начална дата и час на `резервацията </barsy.help/210-dictionary/reservation.html>`__

			 пример: "\"2026-07-18 18:20:13\""
   * - **$to_date**
     - *string*
     - 
     - Крайна дата и час на `резервацията </barsy.help/210-dictionary/reservation.html>`__

			 пример: "\"2026-07-18 18:20:13\""
   * - **$persons**
     - *int*
     - 
     - Брой посетители към `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$wait_interval**
     - *int*
     - 
     - Време за изчакване на `резервацията </barsy.help/210-dictionary/reservation.html>`__ в минути
   * - **$discount**
     - *float*
     - 0
     - Очаквана сума за капариране на `резервацията </barsy.help/210-dictionary/reservation.html>`__ в проценти
   * - **$description**
     - *string*
     - 
     - Описание (свободен текст)
   * - **$places**
     - *array*
     - []
     - Места към `резервацията </barsy.help/210-dictionary/reservation.html>`__

			 пример: "[1,2]" ( виж: :doc:`../methods/places/getlist` )
   * - **$status_id**
     - *int*
     - 4
     - Статус на `резервацията </barsy.help/210-dictionary/reservation.html>`__.

			По подразбиране Непотвърдена (4) — потвърждава се ръчно или автоматично при `плащане </barsy.help/210-dictionary/payment.html>`__
   * - **$servers**
     - *array*
     - []
     - Списък с `потребители </barsy.help/210-dictionary/user.html>`__, които ще обслужват `резервацията </barsy.help/210-dictionary/reservation.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$person_type_count**
     - *array*
     - []
     - Брой на вида хора
   * - **$delete_flag**
     - *int*
     - 0
     - Флаг за изтриване на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - :deprecated:`$caparo`
     - *float*
     - 0
     - Очаквана сума за капариране на `резервацията </barsy.help/210-dictionary/reservation.html>`__ :deprecated_text:`Отхвърлено: Да се използва списък от плащания`
   * - **$special**
     - *int*
     - 0
     - Маркер за разпознаване на `резервации </barsy.help/210-dictionary/reservation.html>`__ чрез емотикони

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reservations/create`
	 * :doc:`../methods/reservations/update`

