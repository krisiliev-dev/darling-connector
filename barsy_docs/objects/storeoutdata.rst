.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreOutData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeouts\\Data\\StoreOutData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_out_id**
     - *int*
     - 
     - ID на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__, в който е извършено `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../methods/barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - 
     - Име на търговския обект ( виж: :doc:`../methods/barsys/getlist` )
   * - **$depot_id**
     - *int*
     - 
     - ID на `склад </barsy.help/210-dictionary/store.html>`__, от който е направено `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../methods/depots/getlist` )
   * - **$depot_name**
     - *int*
     - 
     - Име на `склад </barsy.help/210-dictionary/store.html>`__, от който е направено `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../methods/depots/getlist` )
   * - **$date**
     - *string*
     - 
     - Дата на създаване на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$doc_date**
     - *string*
     - 
     - Документална дата на операцията
   * - **$close_date**
     - *string*
     - 
     - Дата на приключване на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$status**
     - *int*
     - 
     - Статус на `изписването </barsy.help/210-dictionary/storeout.html>`__

			* **0** - *Отворено*
			* **1** - *Приключено*
   * - **$description**
     - *string*
     - 
     - Описание на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$type_id**
     - *int*
     - 
     - ID на типа на `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../methods/storeouts/types_getlist` )
   * - **$type_name**
     - *string*
     - 
     - Име на типа на `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../methods/storeouts/types_getlist` )
   * - **$ref_id**
     - *int*
     - 
     - Референтен номер, указващ ID на анулиращия или анулирания документ (ако текущият е анулиран или анулиращ - виж.anulate_flag)
   * - **$user_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$user_name**
     - *string*
     - 
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `изписването </barsy.help/210-dictionary/storeout.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$anulate_flag**
     - *int*
     - 
     - Флаг дали `изписването </barsy.help/210-dictionary/storeout.html>`__ е нормално, анулирано или анулиращо

			* **1** - *Анулиран*
			* **-1** - *Анулиращ документ*
			* **0** - *Нормален*
   * - :deprecated:`$is_anulate`
     - *bool*
     - 
     - Синоним на "anulate_flag" :deprecated_text:`Отхвърлено: */`
   * - **$export_id**
     - *string*
     - 
     - Експорт ID
   * - **$deal_id**
     - *int*
     - 
     - ID на сделката, към която е това `изписване </barsy.help/210-dictionary/storeout.html>`__
   * - **$deal_title**
     - *string*
     - 
     - Заглавие на сделката, към която е това `изписване </barsy.help/210-dictionary/storeout.html>`__
   * - **$total_sum**
     - *float*
     - 
     - Обща сума на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$details**
     - *StoreOutDetailData*
     - 
     - Списък с редовете към `изписването </barsy.help/210-dictionary/storeout.html>`__ (ако са поискани)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeouts/getlist`

