.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreMoveDetailData
======================================================================================
Данни за един ред от прехвърлянето

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storemoves\\Data\\StoreMoveDetailData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$row_id**
     - *int*
     - 
     - ID на реда
   * - **$article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/articles/getlist` )
   * - **$article_name**
     - *string*
     - 
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *float*
     - 
     - Количество за `прехвърляне </barsy.help/210-dictionary/storemove.html>`__
   * - **$avg_delivery_price**
     - *float*
     - 
     - Средна доставна цена
   * - **$inspection_amount**
     - *float*
     - 
     - Проверено/получено количество
   * - **$notes**
     - *string*
     - 
     - Бележки към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_price**
     - *float*
     - 
     - Текуща цена на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$tax**
     - *float*
     - 
     - Данъчна ставка в проценти
   * - **$tax_id**
     - *int*
     - 
     - ID на данъчната ставка ( виж: :doc:`../methods/taxgroups/getlist` )

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storemoves/getlist`
	 * :doc:`../methods/storemoves/get`

Виж също
--------

 * `Прехвърляне </barsy.help/210-dictionary/storemove.html>`__

