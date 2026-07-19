.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

MessagesCreateInputData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Messages\\Data\\MessagesCreateInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$recipients**
     - *array*
     - []
     - Списък с получатели подадени като имена разделени със запейтака, или като масив от имена, или като масив от ID-та

			 пример: "\"ivan,miroslav\""
   * - **$subject**
     - *string*
     - 
     - Тема на съобщението

			 пример: "\"Happy New Year\""
   * - **$text**
     - *string*
     - 
     - Съдържание на съобщението

			 пример: "\"Best Regards\""
   * - **$msg_type**
     - *int*
     - 5
     - Тип на съобщението

			 пример: "5"
   * - **$send_date**
     - *string*
     - 
     - Дата за отложено изпращане

			 пример: "\"2015-01-01\""
   * - **$parent_id**
     - *int*
     - 
     - ID на съобщение, на което това съобщение отговаря

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/messages/create`

