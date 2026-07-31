.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

RolesListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Roles\\Data\\RolesListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$role_id**
     - *int*
     - 
     - Филтър по ID на `роля </barsy.help/210-dictionary/role.html>`__
   * - **$role_name**
     - *string*
     - 
     - Филтър по име на `роля </barsy.help/210-dictionary/role.html>`__.

			 пример: "\"\\u0423\\u043f\\u0440\\u0430\\u0432\\u0438\\u0442\\u0435\\u043b\""
   * - **$role_weight**
     - *int*
     - 
     - Филтър по тежест на `роля </barsy.help/210-dictionary/role.html>`__
   * - **$delete_flag**
     - *int*
     - 
     - Филтър по флаг за изтрит
   * - **$parent_id**
     - *int*
     - 
     - Филтър по родител
   * - **$role_path**
     - *string*
     - 
     - Филтър по път на `роля </barsy.help/210-dictionary/role.html>`__.
   * - **$role_id_path**
     - *string*
     - 
     - Филтър по път на `роля </barsy.help/210-dictionary/role.html>`__.

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/roles/getlist`

