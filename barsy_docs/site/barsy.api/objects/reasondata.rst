.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReasonData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reasons\\Data\\ReasonData


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
     - ID на причината
   * - **$name**
     - *string*
     - 
     - Име на причината
   * - **$upd_store**
     - *int*
     - 
     - Флаг дали тази причина изтегля от `склада </barsy.help/210-dictionary/store.html>`__ при финализиране на `сметката </barsy.help/210-dictionary/account.html>`__

			* **0** - Изтегля от `склада </barsy.help/210-dictionary/store.html>`__
			* **1** - Не изтегля от `склада </barsy.help/210-dictionary/store.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reasons/getlist`

