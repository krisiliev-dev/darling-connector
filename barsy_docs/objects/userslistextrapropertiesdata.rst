.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

UsersListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към потребител. Всяка опция включва съответната колона към данните за

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
всеки `потребител </barsy.help/210-dictionary/user.html>`__ от списъка. Основните данни се връщат винаги, а останалите при стойност true.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Users\\Data\\UsersListExtraPropertiesData


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
   * - :category_header:`Основни данни`
     - 
     - 
     - 
   * - **$user_id**
     - *bool*
     - true
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__
   * - **$user_name**
     - *bool*
     - true
     - Потребителско име (за вход)
   * - **$fname**
     - *bool*
     - true
     - Собствено име
   * - **$lname**
     - *bool*
     - true
     - Фамилия
   * - **$full_name**
     - *bool*
     - true
     - Пълно име (собствено + фамилия; ако липсват — потребителското име)
   * - **$role_id**
     - *bool*
     - false
     - ID на `ролята </barsy.help/210-dictionary/role.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1" ( виж: :doc:`../methods/roles/getlist` )
   * - **$role_name**
     - *bool*
     - true
     - Име на `ролята </barsy.help/210-dictionary/role.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__
   * - **$description**
     - *bool*
     - false
     - Описание/бележка за `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$delete_flag**
     - *bool*
     - true
     - Флаг дали `потребителят </barsy.help/210-dictionary/user.html>`__ е изтрит
   * - **$picture**
     - *bool*
     - false
     - Изображение (аватар) на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$lang_id**
     - *bool*
     - false
     - ID на езика на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$system_contact**
     - *bool*
     - false
     - Дали `потребителят </barsy.help/210-dictionary/user.html>`__ е системен контакт

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
     - 
   * - **$show_total**
     - *bool*
     - false
     - Дали `потребителят </barsy.help/210-dictionary/user.html>`__ вижда тотали (обороти)

			 пример: "1"
   * - **$max_discount**
     - *bool*
     - false
     - Максимална отстъпка, която `потребителят </barsy.help/210-dictionary/user.html>`__ може да дава

			 пример: "1"
   * - **$max_credit_limit**
     - *bool*
     - false
     - Максимален кредитен лимит на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
     - 
   * - **$email**
     - *bool*
     - false
     - Имейл на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$email_verification**
     - *bool*
     - false
     - Статус на верификация на имейла

			 пример: "1"
   * - **$pin**
     - *bool*
     - false
     - PIN код за вход

			 пример: "1"
   * - **$card_code**
     - *bool*
     - false
     - Код на карта за вход

			 пример: "1"
   * - **$remote_access**
     - *bool*
     - false
     - Право за отдалечен достъп

			 пример: "1"
   * - **$session_timeout**
     - *bool*
     - false
     - Таймаут на сесията (в секунди)

			 пример: "1"
   * - **$sales_auto_logout**
     - *bool*
     - false
     - Автоматичен изход след `продажба </barsy.help/210-dictionary/sale.html>`__

			 пример: "1"
   * - **$articles_report**
     - *bool*
     - false
     - Настройка за справка по `артикули </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$streams_report**
     - *bool*
     - false
     - Настройка за справка по `потоци </barsy.help/210-dictionary/flow.html>`__

			 пример: "1"
   * - **$print_totals**
     - *bool*
     - false
     - Настройка за печат на тотали

			 пример: "1"
   * - **$phone**
     - *bool*
     - false
     - Телефон на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$has_password**
     - *bool*
     - false
     - Има ли `потребителят </barsy.help/210-dictionary/user.html>`__ зададена парола

			 пример: "1"
   * - **$pager_num**
     - *bool*
     - false
     - Номер на пейджър

			 пример: "1"
   * - **$print_totals_name**
     - *bool*
     - false
     - Текстово представяне на настройката за печат на тотали

			 пример: "1"
   * - **$streams_report_name**
     - *bool*
     - false
     - Текстово представяне на настройката за справка по `потоци </barsy.help/210-dictionary/flow.html>`__

			 пример: "1"
   * - **$reset_password**
     - *bool*
     - false
     - Флаг дали се изисква смяна на паролата

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$barsys**
     - *bool*
     - false
     - Списък с ID на `търговските обекти </barsy.help/210-dictionary/barsy.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$barsys_names**
     - *bool*
     - false
     - Имена на `търговските обекти </barsy.help/210-dictionary/barsy.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$role_id_path**
     - *bool*
     - false
     - Път от ID-та на `ролите </barsy.help/210-dictionary/role.html>`__ (йерархия на `ролята </barsy.help/210-dictionary/role.html>`__)

			 пример: "1"
   * - **$role_path**
     - *bool*
     - false
     - Път от имена на `ролите </barsy.help/210-dictionary/role.html>`__ (йерархия на `ролята </barsy.help/210-dictionary/role.html>`__)

			 пример: "1"
   * - **$role_delete_flag**
     - *bool*
     - false
     - Флаг дали `ролята </barsy.help/210-dictionary/role.html>`__ на `потребителя </barsy.help/210-dictionary/user.html>`__ е изтрита

			 пример: "1"
   * - **$rights**
     - *bool*
     - false
     - Списък с правата (API действия) на `потребителя </barsy.help/210-dictionary/user.html>`__ според `ролята </barsy.help/210-dictionary/role.html>`__ му

			 пример: "1"
   * - **$current_barsy_access**
     - *bool*
     - false
     - Има ли `потребителят </barsy.help/210-dictionary/user.html>`__ достъп до текущия `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (изисква контекст на обект)
   * - 
     - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
     - 
   * - **$create_date**
     - *bool*
     - false
     - Дата на създаване на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$last_update**
     - *bool*
     - false
     - Дата на последна промяна на `потребителя </barsy.help/210-dictionary/user.html>`__

			 пример: "1"
   * - **$user_session**
     - *bool*
     - false
     - Състояние на активната сесия на `потребителя </barsy.help/210-dictionary/user.html>`__ в текущия период/обект

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/users/getlist`

Виж също
--------

 * `Потребител </barsy.help/210-dictionary/user.html>`__

