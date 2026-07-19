.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReservationData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reservations\\Data\\ReservationData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$reservation_id**
     - *int*
     - 
     - ID на `резервация </barsy.help/210-dictionary/reservation.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__, за който е `резервацията </barsy.help/210-dictionary/reservation.html>`__ ( виж: :doc:`../methods/barsys/getlist` )
   * - **$client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/clients/getlist` )
   * - **$client_group_id**
     - *int*
     - 
     - ID на група на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/clientgroups/getlist` )
   * - **$user_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `резервацията </barsy.help/210-dictionary/reservation.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$person_id**
     - *int*
     - 
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/persons/getlist` )
   * - **$contact_name**
     - *string*
     - 
     - Лице за контакт към `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$phone**
     - *string*
     - 
     - Телефон за контакт към резеревацията
   * - **$from_date**
     - *string*
     - 
     - Начална дата на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$to_date**
     - *string*
     - 
     - Крайна дата на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$wait_interval**
     - *string*
     - 
     - Време за изчакване след начало на `резервацията </barsy.help/210-dictionary/reservation.html>`__, ако не е потвърдено идването
   * - **$caparo**
     - *float*
     - 
     - Сума, необходима за капариране на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$description**
     - *string*
     - 
     - Описание, свободен текст
   * - **$create_date**
     - *string*
     - 
     - Дата на създаване
   * - **$last_update**
     - *string*
     - 
     - Дата на последна актуализация
   * - **$status_id**
     - *int*
     - 
     - Статус на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$delete_flag**
     - *int*
     - 
     - Флаг за изтриване на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$persons**
     - *int*
     - 
     - Брой посетители към `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$discount**
     - *float*
     - 
     - Отстъпка в проценти на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$total_sum**
     - *float*
     - 
     - Сума на `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$total_real**
     - *float*
     - 
     - Сума на `резервацията </barsy.help/210-dictionary/reservation.html>`__ след остъпка
   * - **$total_paid_sum**
     - *float*
     - 
     - Платена сума по `резервацията </barsy.help/210-dictionary/reservation.html>`__
   * - **$total_remain_sum**
     - *float*
     - 
     - Остатък за `плащане </barsy.help/210-dictionary/payment.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reservations/getlist`
	 * :doc:`../methods/reservations/get`

