.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

UsersListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с потребители (Users_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като асоциативен масив колона⇒посока (напр. ["user_name" => "asc", "create_date" => "desc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Users\\Data\\UsersListOrderByData


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
     - *string*
     - 
     - Подреждане по ID на `потребител </barsy.help/210-dictionary/user.html>`__
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
     - Подреждане по потребителско име
   * - **$fname**
     - *string*
     - 
     - Подреждане по собствено име
   * - **$lname**
     - *string*
     - 
     - Подреждане по фамилия
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$role_id**
     - *string*
     - 
     - Подреждане по ID на `роля </barsy.help/210-dictionary/role.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$create_date**
     - *string*
     - 
     - Подреждане по дата на създаване
   * - **$last_update**
     - *string*
     - 
     - Подреждане по дата на последна промяна
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$delete_flag**
     - *string*
     - 
     - Подреждане по флаг за изтрит
   * - 
     - 
     - 
     - 
   * - :category_header:`Други`
     - 
     - 
     - 
   * - **$user_session**
     - *string*
     - 
     - Подреждане по състояние на активната сесия (изисква extra property user_session)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/users/getlist`

Виж също
--------

 * `Потребител </barsy.help/210-dictionary/user.html>`__

