.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

RightRequestInputData
======================================================================================
Входни данни за заявка на права.

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Rightrequests\\Data\\RightRequestInputData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$api_actions**
     - *string*
     - []
     - Списък с правата, които се заявяват — по уникалния идентификатор на правото (api_action).
   * - **$reason**
     - *string*
     - 
     - Незадължителна причина/обосновка за заявката.

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/rightrequests/create`

