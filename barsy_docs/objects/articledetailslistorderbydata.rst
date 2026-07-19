.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleDetailsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с характеристики (Articledetails_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като низ, масив или асоциативен масив колона⇒посока (напр. {"detail_name":"asc"}). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articledetails\\Data\\ArticleDetailsListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$detail_name**
     - *string*
     - 
     - Подреждане по име на характеристиката
   * - **$group_id**
     - *string*
     - 
     - Подреждане по група
   * - **$key_id**
     - *string*
     - 
     - Подреждане по ID на характеристиката

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/getlist`

