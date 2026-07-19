.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientOrderStatus
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clientorders\\Data\\ClientOrderStatus


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$status_id**
     - *int*
     - 
     - ID на статус
   * - **$status_name**
     - *string*
     - 
     - Име на статус
   * - **$delete_flag**
     - *int*
     - 
     - Флаг за изтрит статус
   * - **$color**
     - *string*
     - 
     - Настройка за цвят на статус в списъци
   * - **$ask_for_barsy**
     - *int*
     - 
     - Настройка за питане за обработващ `търговски обект </barsy.help/210-dictionary/barsy.html>`__ при назначаване на статус

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientorders/getstatuslistdata`

