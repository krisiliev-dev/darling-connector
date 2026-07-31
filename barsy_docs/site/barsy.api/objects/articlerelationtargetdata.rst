.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleRelationTargetData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticleRelationTargetData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$target_id**
     - *int*
     - 
     - ID на реда-цел
   * - **$relation_id**
     - *int*
     - 
     - ID на връзката, към която принадлежи редът
   * - **$target_type**
     - *int*
     - 
     - Тип на целта — 1=`артикул </barsy.help/210-dictionary/article.html>`__, 2=`категория </barsy.help/210-dictionary/category.html>`__, 3=характеристика, 4=шаблон
   * - **$target_ref_id**
     - *int*
     - 
     - ID на реферирания обект според типа (null при цел от тип шаблон)
   * - **$target_pattern**
     - *string*
     - 
     - Шаблон за име на `артикул </barsy.help/210-dictionary/article.html>`__ с % wildcard (само при цел от тип шаблон)
   * - **$exclude_flag**
     - *int*
     - 
     - 1 = редът изключва резолвнатите `артикули </barsy.help/210-dictionary/article.html>`__ от предложенията
   * - **$sort**
     - *int*
     - 
     - Приоритет при показване и запълване до лимита
   * - **$target_name**
     - *string*
     - 
     - Име на реферирания обект (за административния списък)
   * - **$inherited_from_cat_id**
     - *int*
     - 
     - CAT_ID на `категорията </barsy.help/210-dictionary/category.html>`__, от която редът е наследен (само при preview на наследени връзки)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articlerelations/get`

