.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReservationsListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към резервация. Всяка опция включва съответните колони към данните за

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*всеки запис. Основните данни се връщат винаги, останалите при стойност true.*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reservations\\Data\\ReservationsListExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$all**
     - *bool*
     - false
     - Пълни данни — места, обслужващи, суми по `резервацията </barsy.help/210-dictionary/reservation.html>`__

			 пример: "1"
   * - **$by_place**
     - *bool*
     - false
     - Данни по място — един ред на място; резултатът се групира по place_id

			 пример: "1"
   * - **$barsy_name**
     - *bool*
     - false
     - Име на търговския обект

			 пример: "1" ( виж: :doc:`../methods/barsys/getlist` )
   * - **$orders**
     - *bool*
     - false
     - `Артикули </barsy.help/210-dictionary/article.html>`__, включени в `резервацията </barsy.help/210-dictionary/reservation.html>`__ (зареждат се след основната заявка)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reservations/getlist`

Виж също
--------

 * `Резервация </barsy.help/210-dictionary/reservation.html>`__

