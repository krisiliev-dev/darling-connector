.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Poses_getcurrent
===========================================================
Текуща каса

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pos </barsy.help/210-dictionary/pos.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълни данни за `касата </barsy.help/210-dictionary/pos.html>`__, от която е стартирала текущата сесия — основни полета (ID, име, обект), периферни устройства (статус на фискалния принтер, наличие на CDX дисплей, мрежови устройства), специфични настройки (зустови сигнали, автоматично подреждане на `артикулите </barsy.help/210-dictionary/article.html>`__, показване на клиентска отстъпка), активни отдалечени системи за идентификация на `клиенти </barsy.help/210-dictionary/client.html>`__. Често е първият endpoint при инициализация на POS терминал.

Типични случаи: bootstrap на касов интерфейс след вход, диагностика на свързаните периферни устройства, конфигуриране на UI спрямо специфики на `касата </barsy.help/210-dictionary/pos.html>`__.

**Име**: Poses_getcurrent
**Категория**: Settings


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PosCurrentData_                                                        
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PosCurrentData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Class PosData

.. list-table::
   :header-rows: 1
   :align: center
   :name: PosCurrentData

   * - Параметър
     - Тип
     - Описание
   * - **$pos_id**
     - *int*
     - 
   * - **$name**
     - *string*
     - 
   * - **$salon_id**
     - *int*
     - 
   * - **$barsy_id**
     - *int*
     - 
   * - **$barsy_name**
     - *string*
     - 
   * - **$poskey**
     - *string*
     - 
   * - **$force_account_persons**
     - *int*
     - 
   * - **$pos_sounds**
     - *string*
     - 
   * - **$pos_sound_file**
     - *string*
     - 
   * - **$input_focus**
     - *int*
     - 
   * - **$quantity_popup**
     - *bool*
     - 
   * - **$orders_log_mode**
     - *int*
     - 
   * - **$paied_change_view**
     - *int*
     - 
   * - **$text_to_speech**
     - *string*
     -  **По подразбиране:** 'none'
   * - **$custom_css**
     - *string*
     - 
   * - **$set_tab_default**
     - *string*
     - 
   * - **$set_tabs_visible**
     - *array*
     - 
   * - **$logo_pos**
     - *string*
     - 
   * - **$pos_ip_type**
     - *int*
     - Флаг, дали `касата </barsy.help/210-dictionary/pos.html>`__ е със зададен IP адрес
   * - **$pos_model_id**
     - *int*
     - 
   * - **$mode**
     - *string*
     - 
   * - **$schema_pos**
     - *int*
     -  **По подразбиране:** 0
   * - **$show_cats**
     - *int*
     - 
   * - **$auto_dimmer**
     - *int*
     - Режим на завъртане на схема
   * - **$auto_exit**
     - *int*
     - 
   * - **$button_size**
     - *int*
     - 
   * - **$is_public**
     - *int*
     - 
   * - **$printer_id**
     - *int*
     - 
   * - **$sys_printer_id**
     - *int*
     - 
   * - **$inv_printer_id**
     - *int*
     - 
   * - **$prn_but_printer_id**
     - *int*
     - 
   * - **$display_id**
     - *int*
     - 
   * - **$client_display_id**
     - *int*
     - 
   * - **$scale_id**
     - *int*
     - 
   * - **$label_printer_id**
     - *int*
     - 
   * - **$dvr_id**
     - *int*
     - 
   * - **$has_printer**
     - *int*
     - 
   * - **$has_cdx**
     - *bool*
     - 
   * - **$network_client_devices**
     - *array*
     - 
   * - **$printer_queue**
     - *string*
     - 
   * - **$sys_printer_queue**
     - *string*
     - 
   * - **$inv_printer_queue**
     - *string*
     - 
   * - **$prn_but_printer_queue**
     - *string*
     - 
   * - **$intermediate_recipe**
     - *int*
     - 
   * - **$print_but_recipe**
     - *int*
     - 
   * - **$cat_id**
     - *int*
     - 
   * - **$model**
     - *string*
     - 
   * - **$barsy_sys**
     - *int*
     - 
   * - **$delete_flag**
     - *int*
     - 
   * - **$barsy_delete_flag**
     - *int*
     - 
   * - **$background_color**
     - *string*
     - 
   * - **$pos_orders_size**
     - *int*
     -  **По подразбиране:** 0
   * - **$default_place_id**
     - *int*
     - 
   * - **$account_details_on_open**
     - *array*
     - 
   * - **$account_details_on_close**
     - *array*
     - 
   * - **$method**
     - *string*
     - 

			* **IP** - *Липсва описание*
			* **POS_KEY** - *Липсва описание*
			* **PUBLIC** - *Липсва описание*
			* **ID** - *Липсва описание*
			* **AUTO** - *Липсва описание*
   * - **$generates_unp**
     - *bool*
     - 
   * - **$is_system**
     - *bool*
     - 
   * - **$show_client_discount**
     - *int*
     - 
   * - **$articles_auto_arange**
     - *int*
     - 
   * - **$cdx_showx_group_portrait**
     - *int*
     - 
   * - **$cdx_showx_group_landscape**
     - *int*
     - 
   * - **$auto_login_user_id**
     - *int*
     - `Потребител </barsy.help/210-dictionary/user.html>`__ за автоматичен вход
   * - **$auto_login_pp**
     - *string*
     - 
   * - **$settings**
     - *object*
     - 
   * - **$pos_public_key**
     - *string*
     - 
   * - **$default_payment_method**
     - *string*
     - 
   * - **$kiosk_json**
     - *object*
     - 
   * - **$read_only_mode**
     - *int*
     -  **По подразбиране:** 0
   * - **$theme**
     - *string*
     -  **По подразбиране:** 'default'
   * - **$start_service_date_mode_no**
     - *string*
     - 
   * - **$client_search_remote_systems**
     - *array*
     -  **По подразбиране:** []
   * - **$service_confirmation**
     - *int*
     - 
   * - **$account_transfer**
     - *int*
     - 

			* **0** - *Липсва описание*
			* **1** - *Липсва описание*
			* **2** - *Липсва описание* **По подразбиране:** 0

-----

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/poses_getcurrent/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/poses_getcurrent/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/poses_getcurrent/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/poses_getcurrent/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/poses_getcurrent/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/poses_getcurrent/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Каса </barsy.help/210-dictionary/pos.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

