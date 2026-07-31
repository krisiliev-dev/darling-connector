.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PersonInputData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Persons\\Data\\PersonInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$person_name**
     - *string*
     - 
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__

			 пример: "\"\\u0418\\u0432\\u0430\\u043d \\u0418\\u0432\\u0430\\u043d\\u043e\\u0432\""
   * - **$client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, на който принадлежи `представителя </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../methods/clients/getlist` )
   * - **$description**
     - *string*
     - 
     - Свободен текст
   * - **$type_id**
     - *int*
     - 1
     - ID на типа на `представител </barsy.help/210-dictionary/person.html>`__

			 пример: "1" ( виж: ``*/`` )
   * - **$person_code**
     - *string*
     - 
     - Код на `представител </barsy.help/210-dictionary/person.html>`__.

			Използва се за индентификация на `представителя </barsy.help/210-dictionary/person.html>`__ чрез някакъв носител (например карта)

			 пример: "987"
   * - **$delete_flag**
     - *int*
     - 0
     - Флаг дали `представителя </barsy.help/210-dictionary/person.html>`__ е маркиран като изтрит

			 пример: "0"
   * - **$dynamic_input**
     - *object*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/createfromclientorder`
	 * :doc:`../methods/accounts/create`
	 * :doc:`../methods/accounts/place`
	 * :doc:`../methods/persons/create`
	 * :doc:`../methods/persons/save`

