.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreOutTypeData
======================================================================================
Тип на изписването

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeouts\\Data\\StoreOutTypeData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$type_id**
     - *int*
     - 
     - Id на типа
   * - **$name**
     - *string*
     - 
     - Име на типа
   * - **$color**
     - *string*
     - 
     - Цвят на тип в hex (използва се в списъците)
   * - **$delete_flag**
     - *int*
     - 
     - Флаг дали е маркиран като изтрит

			* **0** - *Активен*
			* **1** - *изтрит*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeouts/types_getlist`

Виж също
--------

 * `Изписване </barsy.help/210-dictionary/storeout.html>`__

