.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PersonsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Persons\\Data\\PersonsListFiltersData


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
     - 
     - Филтър по ID на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$person_id**
     - *int*
     - 
     - Филтър по ID на представиртел
   * - **$person_name**
     - *string*
     - 
     - Филтър по име на `представител </barsy.help/210-dictionary/person.html>`__
   * - **$type_id**
     - *int*
     - 
     - Филтър по ID на тип на представиртел
   * - **$info_value**
     - *string*
     - 
     - Филтър по допълнителни данни на `представител </barsy.help/210-dictionary/person.html>`__
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по флаг за изтрит на `представител </barsy.help/210-dictionary/person.html>`__
   * - **$last_update**
     - *string*
     - 
     - Филтър по последна актуализация

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/persons/getlist`

