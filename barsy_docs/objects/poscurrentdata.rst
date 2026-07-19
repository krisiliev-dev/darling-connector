.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PosCurrentData
======================================================================================
Class PosData

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Poses\\Data\\PosCurrentData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$pos_id**
     - *int*
     - 
     - 
   * - **$name**
     - *string*
     - 
     - 
   * - **$salon_id**
     - *int*
     - 
     - 
   * - **$barsy_id**
     - *int*
     - 
     - 
   * - **$barsy_name**
     - *string*
     - 
     - 
   * - **$poskey**
     - *string*
     - 
     - 
   * - **$force_account_persons**
     - *int*
     - 
     - 
   * - **$pos_sounds**
     - *string*
     - 
     - 
   * - **$pos_sound_file**
     - *string*
     - 
     - 
   * - **$input_focus**
     - *int*
     - 
     - 
   * - **$quantity_popup**
     - *bool*
     - 
     - 
   * - **$orders_log_mode**
     - *int*
     - 
     - 
   * - **$paied_change_view**
     - *int*
     - 
     - 
   * - **$text_to_speech**
     - *string*
     - 'none'
     - 
   * - **$custom_css**
     - *string*
     - 
     - 
   * - **$set_tab_default**
     - *string*
     - 
     - 
   * - **$set_tabs_visible**
     - *array*
     - 
     - 
   * - **$logo_pos**
     - *string*
     - 
     - 
   * - **$pos_ip_type**
     - *int*
     - 
     - Флаг, дали `касата </barsy.help/210-dictionary/pos.html>`__ е със зададен IP адрес
   * - **$pos_model_id**
     - *int*
     - 
     - 
   * - **$mode**
     - *string*
     - 
     - 
   * - **$schema_pos**
     - *int*
     - 0
     - 
   * - **$show_cats**
     - *int*
     - 
     - 
   * - **$auto_dimmer**
     - *int*
     - 
     - Режим на завъртане на схема
   * - **$auto_exit**
     - *int*
     - 
     - 
   * - **$button_size**
     - *int*
     - 
     - 
   * - **$is_public**
     - *int*
     - 
     - 
   * - **$printer_id**
     - *int*
     - 
     - 
   * - **$sys_printer_id**
     - *int*
     - 
     - 
   * - **$inv_printer_id**
     - *int*
     - 
     - 
   * - **$prn_but_printer_id**
     - *int*
     - 
     - 
   * - **$display_id**
     - *int*
     - 
     - 
   * - **$client_display_id**
     - *int*
     - 
     - 
   * - **$scale_id**
     - *int*
     - 
     - 
   * - **$label_printer_id**
     - *int*
     - 
     - 
   * - **$dvr_id**
     - *int*
     - 
     - 
   * - **$has_printer**
     - *int*
     - 
     - 
   * - **$has_cdx**
     - *bool*
     - 
     - 
   * - **$network_client_devices**
     - *array*
     - 
     - 
   * - **$printer_queue**
     - *string*
     - 
     - 
   * - **$sys_printer_queue**
     - *string*
     - 
     - 
   * - **$inv_printer_queue**
     - *string*
     - 
     - 
   * - **$prn_but_printer_queue**
     - *string*
     - 
     - 
   * - **$intermediate_recipe**
     - *int*
     - 
     - 
   * - **$print_but_recipe**
     - *int*
     - 
     - 
   * - **$cat_id**
     - *int*
     - 
     - 
   * - **$model**
     - *string*
     - 
     - 
   * - **$barsy_sys**
     - *int*
     - 
     - 
   * - **$delete_flag**
     - *int*
     - 
     - 
   * - **$barsy_delete_flag**
     - *int*
     - 
     - 
   * - **$background_color**
     - *string*
     - 
     - 
   * - **$pos_orders_size**
     - *int*
     - 0
     - 
   * - **$default_place_id**
     - *int*
     - 
     - 
   * - **$account_details_on_open**
     - *array*
     - 
     - 
   * - **$account_details_on_close**
     - *array*
     - 
     - 
   * - **$method**
     - *string*
     - 
     - 

			* **IP** - *Липсва описание*
			* **POS_KEY** - *Липсва описание*
			* **PUBLIC** - *Липсва описание*
			* **ID** - *Липсва описание*
			* **AUTO** - *Липсва описание*
   * - **$generates_unp**
     - *bool*
     - 
     - 
   * - **$is_system**
     - *bool*
     - 
     - 
   * - **$show_client_discount**
     - *int*
     - 
     - 
   * - **$articles_auto_arange**
     - *int*
     - 
     - 
   * - **$cdx_showx_group_portrait**
     - *int*
     - 
     - 
   * - **$cdx_showx_group_landscape**
     - *int*
     - 
     - 
   * - **$auto_login_user_id**
     - *int*
     - 
     - `Потребител </barsy.help/210-dictionary/user.html>`__ за автоматичен вход
   * - **$auto_login_pp**
     - *string*
     - 
     - 
   * - **$settings**
     - *object*
     - 
     - 
   * - **$pos_public_key**
     - *string*
     - 
     - 
   * - **$default_payment_method**
     - *string*
     - 
     - 
   * - **$kiosk_json**
     - *object*
     - 
     - 
   * - **$read_only_mode**
     - *int*
     - 0
     - 
   * - **$theme**
     - *string*
     - 'default'
     - 
   * - **$start_service_date_mode_no**
     - *string*
     - 
     - 
   * - **$client_search_remote_systems**
     - *array*
     - []
     - 
   * - **$service_confirmation**
     - *int*
     - 
     - 
   * - **$account_transfer**
     - *int*
     - 0
     - 

			* **0** - *Липсва описание*
			* **1** - *Липсва описание*
			* **2** - *Липсва описание*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/poses/getcurrent`

