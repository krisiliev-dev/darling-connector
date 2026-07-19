.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StreamsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Streams\\Data\\StreamsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$scales_update**
     - *int*
     - 
     - Филтър по флаг за "Подаване към везна"

			 пример: "1"
   * - **$name**
     - *string*
     - 
     - Филтър по име на `поток </barsy.help/210-dictionary/flow.html>`__.

			*Намира и при частично съвпадение*

			 пример: "\"\\u041a\\u0443\\u0445\\u043d\\u044f\""
   * - **$for_service**
     - *int*
     - 
     - Само `потоци </barsy.help/210-dictionary/flow.html>`__, обслужими от текущата `каса </barsy.help/210-dictionary/pos.html>`__ (подай 1 за активиране)

			 пример: "1"
   * - **$delete_flag**
     - *int*
     - 
     - Филтър по delete_flag (0 — активни, 1 — изтрити).

			Ако не е подаден — връщат се всички `потоци </barsy.help/210-dictionary/flow.html>`__

			 пример: "0"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/streams/getlist`

