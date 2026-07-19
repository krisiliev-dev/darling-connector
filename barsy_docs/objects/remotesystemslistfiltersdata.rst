.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

RemoteSystemsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Remotesystems\\Data\\RemoteSystemsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$supplier_id**
     - *int*
     - 
     - Филтър по `доставчик </barsy.help/210-dictionary/supplier.html>`__

			 пример: "1"
   * - **$remote_id**
     - *int*
     - 
     - Филтър по ID на отдалечената система

			 пример: "1"
   * - **$remote_id_gt**
     - *int*
     - 0
     - Филтъриране отдалечените системи с позитивен индекс

			 пример: "\"> 0\""
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър дали е изтрит

			 пример: "1"
   * - **$supported_actions**
     - *array* | *string*
     - 
     - Филтър дали е изтрит

			 пример: "\"RemoteDocumentsPullAdapterInterface\""
   * - **$current_barsy**
     - *int*
     - 
     - Флаг филтър за отдалечени системи за ТО в който работим или глобални

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/remotesystems/getlist`

