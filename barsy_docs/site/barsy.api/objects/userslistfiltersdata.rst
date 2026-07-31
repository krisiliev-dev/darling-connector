.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

UsersListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Users\\Data\\UsersListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - 
     - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
     - 
   * - **$user_id**
     - *int*
     - 
     - Филтър по ID `потребител </barsy.help/210-dictionary/user.html>`__

			 пример: "1" ( виж: :doc:`../methods/users/get` , :doc:`../methods/users/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$log_time**
     - *datetime*
     - 
     - Филтър по последно логване на `потребител </barsy.help/210-dictionary/user.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$create_date**
     - *datetime*
     - 
     - Филтър по дата на създаване на `потребител </barsy.help/210-dictionary/user.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$user_name**
     - *string*
     - 
     - Филтър по име на `потребител </barsy.help/210-dictionary/user.html>`__.

			*Намира и при частично съвпадение*

			 пример: "\"Pesho\""
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$role_id**
     - *int*
     - 
     - Филтър по ID на `роля </barsy.help/210-dictionary/role.html>`__ на `потребител </barsy.help/210-dictionary/user.html>`__

			 пример: "1" ( виж: :doc:`../methods/roles/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по флаг за изтрит

			 пример: "1"
   * - **$role_delete_flag**
     - *int*
     - 
     - Филтър по флаг за изтрита `роля </barsy.help/210-dictionary/role.html>`__ на `потребител </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$no_system_users**
     - *int*
     - 
     - Филтър - изключва системните `потребители </barsy.help/210-dictionary/user.html>`__ (USER_ID <= 1)

			 пример: "1"
   * - **$user_session**
     - *int*
     - 
     - Филтър по активна сесия на `потребителя </barsy.help/210-dictionary/user.html>`__ в текущия период/обект (изисква extra property user_session)

			 пример: "1"
   * - **$has_pin**
     - *int*
     - 
     - Филтър - има ли `потребителят </barsy.help/210-dictionary/user.html>`__ зададен пин
   * - **$transfer_account_flag**
     - *int*
     - 
     - Филтър - право за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__ на `сметка </barsy.help/210-dictionary/account.html>`__

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/users/getlist`

