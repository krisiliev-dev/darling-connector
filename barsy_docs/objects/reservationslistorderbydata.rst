.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReservationsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с резервации (Reservations_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като низ ("from_date asc") или масив колона⇒посока. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc` — това пази срещу SQL injection през order_by.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reservations\\Data\\ReservationsListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$reservation_id**
     - *string*
     - 
     - Подреждане по ID на `резервация </barsy.help/210-dictionary/reservation.html>`__
   * - **$from_date**
     - *string*
     - 
     - Подреждане по начална дата
   * - **$to_date**
     - *string*
     - 
     - Подреждане по крайна дата
   * - **$create_date**
     - *string*
     - 
     - Подреждане по дата на създаване
   * - **$client_name**
     - *string*
     - 
     - Подреждане по име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$status_id**
     - *string*
     - 
     - Подреждане по статус

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reservations/getlist`

Виж също
--------

 * `Резервация </barsy.help/210-dictionary/reservation.html>`__

