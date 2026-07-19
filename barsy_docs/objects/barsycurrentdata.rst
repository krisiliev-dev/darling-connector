.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

BarsyCurrentData
======================================================================================
Описание на текущ търговски обект

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Barsys\\Data\\BarsyCurrentData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$menu_id**
     - *int*
     - 
     - ID на каталог
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$name**
     - *string*
     - 
     - Име на търговския обект
   * - **$logo**
     - *string*
     - 
     - Име на файлът, отговарящ за логото
   * - **$background_color**
     - *string*
     - 
     - Основен цвят за този `търговски обект </barsy.help/210-dictionary/barsy.html>`__.

			*Използва се за условно визуално отличаване на текущия обект*
   * - **$default_payment_method**
     - *int*
     - 
     - ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране
   * - **$app_version**
     - *string*
     - 
     - Текуща версия на инсталацията
   * - **$info_last_update**
     - *int*
     - 
     - timestamp на последната промяна на каталога, използван от този `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$method**
     - *string*
     - 
     - 

			* **IP** - *Липсва описание*
			* **POS_KEY** - *Липсва описание*
			* **PUBLIC** - *Липсва описание*
			* **ID** - *Липсва описание*
			* **AUTO** - *Липсва описание*
			* **REMOTE_SYSTEM** - *Липсва описание*
   * - **$user_pos_id**
     - *int*
     - 
     - 
   * - **$cat_id**
     - 
     - 
     - 
   * - **$delete_flag**
     - 
     - 
     - 
   * - **$set_tab_default**
     - 
     - 
     - 
   * - **$barsy_type_id**
     - 
     - 
     - 
   * - **$delivery_article_id**
     - *int*
     - 
     - 
   * - **$default_company_id**
     - *int*
     - 
     - 
   * - **$lang_id**
     - 
     - 
     - 
   * - **$public_cat_id**
     - 
     - 
     - 
   * - **$public_pictures**
     - 
     - 
     - 
   * - **$public_description**
     - 
     - 
     - 
   * - **$public_address**
     - 
     - 
     - 
   * - **$public_phones**
     - 
     - 
     - 
   * - **$public_website**
     - 
     - 
     - 
   * - **$public_coordinates**
     - 
     - 
     - 
   * - **$export_id**
     - 
     - 
     - 
   * - **$logo_pos**
     - 
     - 
     - 
   * - **$weight**
     - 
     - 
     - 
   * - **$public_name**
     - 
     - 
     - 
   * - **$public_email**
     - 
     - 
     - 
   * - **$public_work_time**
     - 
     - 
     - 
   * - **$set_tabs_visible**
     - 
     - 
     - 
   * - **$franchise_flag**
     - 
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/barsys/getcurrent`

Виж също
--------

 * `Търговски обект </barsy.help/210-dictionary/barsy.html>`__

