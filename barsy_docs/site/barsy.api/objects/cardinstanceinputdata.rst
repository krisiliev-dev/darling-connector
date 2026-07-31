.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CardInstanceInputData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Cards\\Data\\CardInstanceInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$card_id**
     - *int*
     - 
     - Тип на картата/`ваучера </barsy.help/210-dictionary/card.html>`__

			 пример: "1" ( виж: :doc:`../methods/cards/getlist` )
   * - **$num**
     - *string*
     - 
     - Номер, по който ще бъде разпознавана картата/`ваучера </barsy.help/210-dictionary/card.html>`__.

			*Ако не е подаден, може да бъде генериран автоматично, според настройките на типа карта*

			 пример: "123"
   * - **$client_id**
     - *int*
     - 1
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/clients/getlist` )
   * - **$person_id**
     - *int*
     - 
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/persons/getlist` )
   * - **$valid_from**
     - *string*
     - 
     - Дата от която картата/`ваучера </barsy.help/210-dictionary/card.html>`__ ще бъде активна за използване

			 пример: "\"2025-06-12 11:31:50\""
   * - **$valid_to**
     - *string*
     - 
     - Дата на която картата/`ваучера </barsy.help/210-dictionary/card.html>`__ ще бъде деактивирана

			 пример: "\"2025-08-10 12:00:00\""
   * - **$used_left**
     - *int*
     - 
     - Оставащи използвания.

			*Ако бъде оставено празно се счита, че няма ограничение.*

			 пример: "5"
   * - **$credit_left**
     - *float*
     - 
     - Оставащи кредити за използване.

			*Ако не се попълни се счита, че няма ограничени.*

			 пример: "123.45"
   * - **$discount**
     - *float*
     - 0
     - Отстъпка.

			*Използва се за пакетни карти*

			 пример: "10"
   * - **$delete_flag**
     - *int*
     - 0
     - Флаг за изтриване. Ако е зададено на 1, означава, че картата е маркиран като изтрита.

			*Стойност по подразбиране е 0.*

			 пример: "1"
   * - **$unlimited_flag**
     - *int*
     - 0
     - Флаг показваш дали лимитът на картата е неограничен

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/cards/instances_create`
	 * :doc:`../methods/cards/instances_update`

