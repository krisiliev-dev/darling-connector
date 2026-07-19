.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreOutDetailData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeouts\\Data\\StoreOutDetailData


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
   * - **$article_id**
     - *int*
     - 
     - ID на изписания `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/articles/getlist` )
   * - **$article_name**
     - *string*
     - 
     - Име на изписания `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/articles/getlist` )
   * - **$amount**
     - *float*
     - 
     - Изписано количество
   * - **$current_price**
     - *float*
     - 
     - Продажна цена към момента на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$avg_delivery_price**
     - *float*
     - 
     - Средна доставна цена към момента на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$reason_id**
     - *int*
     - 
     - ID на причината за `изписване </barsy.help/210-dictionary/storeout.html>`__ на този `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/storeouts/reasons_getlist` )
   * - **$tax**
     - *int*
     - 
     - Данъчна ставка на този `артикул </barsy.help/210-dictionary/article.html>`__ към момента на `изписването </barsy.help/210-dictionary/storeout.html>`__
   * - **$tax_id**
     - *int*
     - 
     - ID на данъчната група на този `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$notes**
     - *string*
     - 
     - Свободен текст към всеки ред/`артикул </barsy.help/210-dictionary/article.html>`__ в `изписването </barsy.help/210-dictionary/storeout.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeouts/getlist`

