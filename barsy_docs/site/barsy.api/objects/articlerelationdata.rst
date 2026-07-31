.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleRelationData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticleRelationData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$relation_id**
     - *int*
     - 
     - ID на връзката
   * - **$relation_type**
     - *int*
     - 
     - Тип на връзката — 1=upsell, 2=cross-sell, 3=консумативи
   * - **$source_type**
     - *int*
     - 
     - Тип на източника — 1=`артикул </barsy.help/210-dictionary/article.html>`__, 2=`категория </barsy.help/210-dictionary/category.html>`__, 3=публичен интерфейс
   * - **$source_id**
     - *int*
     - 
     - ID на източника според типа
   * - **$active_flag**
     - *int*
     - 
     - 1 = връзката е активна
   * - **$targets**
     - *ArticleRelationTargetData*
     - 
     - Редове-цели на връзката
   * - **$inherited**
     - *bool*
     - 
     - true = връзката е наследена от `категория </barsy.help/210-dictionary/category.html>`__ (не е собствена на източника)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articlerelations/get`

