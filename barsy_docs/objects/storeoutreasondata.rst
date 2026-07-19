.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreOutReasonData
======================================================================================
Причина за изписване на артикул в операция изписване

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeouts\\Data\\StoreOutReasonData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$reason_id**
     - *int*
     - 
     - Id на причината
   * - **$type_id**
     - *int*
     - 
     - ID на типа `изписване </barsy.help/210-dictionary/storeout.html>`__, към който принадлежи причината.

			*Ако е празно - причината е глобална (видима във всички типове изписвания)*
   * - **$name**
     - *int*
     - 
     - Име на причината
   * - **$color**
     - *int*
     - 
     - Цвят на причината (в списъците)
   * - **$delete_flag**
     - *int*
     - 
     - Флаг дали е маркиран като изтрит

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeouts/reasons_getlist`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__
 * `Изписване </barsy.help/210-dictionary/storeout.html>`__

