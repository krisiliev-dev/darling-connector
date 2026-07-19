.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PersonsExtraPropertiesData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Persons\\Data\\PersonsExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$has_person_code**
     - *bool*
     - false
     - Ако е подадено, се връща флаг, който е 1 или 0 и показва дали ИМА или НЯМА код на карта
   * - **$person_code**
     - *bool*
     - false
     - Ако е подадено, се връща самия код на картата, ако `потребителя </barsy.help/210-dictionary/user.html>`__ има право да редактира `представители </barsy.help/210-dictionary/person.html>`__
   * - **$person_create_date**
     - *bool*
     - false
     - Ако е подадено, се връща датата на създаване на `представителя </barsy.help/210-dictionary/person.html>`__
   * - **$short_info**
     - *bool*
     - false
     - Казва дали да върне само ключа и стойноста на допълнителните данни към `представител </barsy.help/210-dictionary/person.html>`__
   * - **$detailed_info**
     - *bool*
     - false
     - Казва дали да върне подробна информация за допълнителните данни към типът `представител </barsy.help/210-dictionary/person.html>`__

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/persons/getlist`
	 * :doc:`../methods/persons/get`

