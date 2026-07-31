.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PlaceData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Salons\\Data\\PlaceData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$place_id**
     - *int*
     - 
     - ID на текущото място
   * - **$place_type**
     - *int*
     - 
     - ID на типа на мястото
   * - **$place_num**
     - *int*
     - 
     - Номер на мястото (свободно избираем)
   * - **$pos**
     - *string*
     - 
     - Координати и размери на текущото място на схемата (x,y,w,h).
   * - **$type_name**
     - *string*
     - 
     - Тип на текущото място
   * - **$is_public**
     - *int*
     - 
     - Публично видомо ли е мястото
   * - **$picture**
     - *string*
     - 
     - Основна снимка
   * - **$salon_id**
     - *int*
     - 
     - ID на зона/салон, към която принадлежи текущото място
   * - **$salon_name**
     - *string*
     - 
     - Име на зона/салон, към която принадлежи текущото място
   * - **$accounts_count**
     - *int*
     - 
     - Брой отворени `сметка </barsy.help/210-dictionary/account.html>`__, асоцирани към мястото
   * - **$id**
     - *int*
     - 
     - 
   * - **$type**
     - *int*
     - 
     - 
   * - **$num**
     - *int*
     - 
     - 
   * - **$acc_count**
     - *int*
     - 
     - 
   * - **$name**
     - *string*
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/places/getlist`
	 * :doc:`../methods/places/getlistwithaccountsonly`
	 * :doc:`../methods/places/getreservedslots`
	 * :doc:`../methods/places/searchavailable`

