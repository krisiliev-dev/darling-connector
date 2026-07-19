.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

UserCurrentData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Users\\Data\\UserCurrentData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$user_id**
     - *int*
     - -1
     - 
   * - **$original_user_id**
     - *int*
     - 
     - в него се пази ID на оригиналния `потребител </barsy.help/210-dictionary/user.html>`__ - това може да е само SU, когато е в режим да вижда системта, като друг `потребител </barsy.help/210-dictionary/user.html>`__
   * - **$user_name**
     - 
     - 'anonymous'
     - 
   * - **$fname**
     - 
     - 'Anonymous'
     - 
   * - **$lname**
     - 
     - 
     - 
   * - **$role_name**
     - 
     - 
     - 
   * - **$max_discount**
     - *int*
     - 0
     - 
   * - **$role_id**
     - *int*
     - 0
     - 
   * - **$role_cat_id**
     - *int*
     - 0
     - 
   * - **$show_total**
     - *bool*
     - false
     - 
   * - **$print_totals**
     - *bool*
     - false
     - 
   * - **$articles_report**
     - 
     - false
     - 
   * - **$streams_report**
     - 
     - false
     - 
   * - **$email**
     - 
     - 
     - 
   * - **$email_verification**
     - *int*
     - 
     - 
   * - **$auth_type**
     - *string*
     - 
     - 

			* **PIN** - *Липсва описание*
			* **ID** - *Липсва описание*
			* **PASS** - *Липсва описание*
			* **REMOTE_SYSTEM** - *Липсва описание*
			* **WEB_AUTHN** - *Липсва описание*
   * - **$sales_auto_logout**
     - 
     - 
     - 
   * - **$delete_flag**
     - 
     - 0
     - 
   * - **$picture**
     - 
     - 
     - 
   * - **$lang_id**
     - *string*
     - 
     - 
   * - **$user_theme**
     - 
     - 
     - 
   * - **$user_posx_theme**
     - 
     - 'white_theme'
     - 
   * - **$user_admin_theme**
     - 
     - 'white_theme'
     - 
   * - **$reports_limit**
     - 
     - 0
     - 
   * - **$session_timeout**
     - 
     - 
     - 
   * - **$reset_password**
     - 
     - 
     - 
   * - **$role_id_path**
     - 
     - 
     - 
   * - **$max_credit_limit**
     - 
     - 
     - 
   * - **$token_is_expired**
     - 
     - 
     - 
   * - **$token_label**
     - 
     - 
     - 
   * - **$access_profile_id**
     - *int*
     - 
     - 
   * - **$auth_remote_system**
     - *RemoteSystemsData*
     - 
     - 
   * - **$blocked_time**
     - *string*
     - 
     - 
   * - **$max_markup**
     - *int*
     - 0
     - 
   * - **$card_code_login**
     - *bool*
     - 
     - 
   * - **$card_code_length**
     - *int*
     - 
     - 
   * - **$request_limiter**
     - *int*
     - 0
     - 
   * - **$request_limiter_1min**
     - *int*
     - 0
     - 
   * - **$has_pin**
     - *bool*
     - 
     - Флаг дали `потребителя </barsy.help/210-dictionary/user.html>`__ има ПИН
   * - **$pin**
     - 
     - 
     - 
   * - **$card_code**
     - 
     - 
     - 
   * - **$description**
     - 
     - 
     - 
   * - **$barsys**
     - 
     - 
     - 
   * - **$barsys_names**
     - 
     - 
     - 
   * - **$create_date**
     - 
     - 
     - 
   * - **$last_update**
     - 
     - 
     - 
   * - **$phone**
     - 
     - 
     - 
   * - **$has_password**
     - 
     - 
     - 
   * - **$pager_num**
     - 
     - 
     - 
   * - **$lang_name**
     - 
     - 
     - 
   * - **$role_path**
     - 
     - 
     - 
   * - **$role_delete_flag**
     - 
     - 
     - 
   * - **$rights**
     - *stdClass*
     - 
     - 
   * - **$system_contact**
     - *int*
     - 
     - 
   * - **$print_totals_name**
     - 
     - 
     - 
   * - **$streams_report_name**
     - 
     - 
     - 
   * - **$passwd_attempts**
     - *int*
     - 
     - 
   * - **$user_entity_id**
     - *string*
     - 
     - 
   * - **$poses**
     - *array* | *string*
     - []
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/users/getcurrent`

