.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PersonData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Persons\\Data\\PersonData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$person_id**
     - *int*
     - 
     - ID на `представител </barsy.help/210-dictionary/person.html>`__
   * - **$person_name**
     - *string*
     - 
     - Име на `представителя </barsy.help/210-dictionary/person.html>`__
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
     - 
     - ID на типа на `представител </barsy.help/210-dictionary/person.html>`__ ( виж: :doc:`../methods/persons/gettypes` )
   * - **$person_code**
     - *string*
     - 
     - Флаг за наличие на записан код на `представител </barsy.help/210-dictionary/person.html>`__.

			Използва се за индентификация на `представителя </barsy.help/210-dictionary/person.html>`__ чрез някакъв носител (например карта). Не може да бъде извлечен в явен вид
   * - **$delete_flag**
     - *int*
     - 
     - Флаг дали `представителя </barsy.help/210-dictionary/person.html>`__ е маркиран като изтрит

			 пример: "0"
   * - **$person_create_date**
     - *string*
     - 
     - Дата на създаване на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$last_update**
     - *string*
     - 
     - Дата на последна актуализация на данните на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$info**
     - *object*
     - 
     - Допълнителни динамични данни за `представителя </barsy.help/210-dictionary/person.html>`__ (според типа му) ( виж: :doc:`../methods/persons/gettypes` )

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/persons/get`

