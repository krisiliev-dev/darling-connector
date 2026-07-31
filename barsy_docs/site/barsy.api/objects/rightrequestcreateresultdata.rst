.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

RightRequestCreateResultData
======================================================================================
Резултат от подаване на заявка за права.

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Rightrequests\\Data\\RightRequestCreateResultData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$request_id**
     - *int*
     - 
     - Идентификатор на създадената заявка.
   * - **$skipped_rights**
     - *string*
     - []
     - Имена на права, които са били пропуснати, защото вече имат чакаща заявка.
   * - **$review_url**
     - *string*
     - 
     - Директен линк към диалога за преглед на заявката. Същият линк се праща и по имейл

			*на вишестоящите — заявителят може да го копира и изпрати ръчно.*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/rightrequests/create`

