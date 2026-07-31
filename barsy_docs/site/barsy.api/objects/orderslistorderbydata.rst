.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

OrdersListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с поръчки (Orders_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като асоциативен масив колона⇒посока (напр. ["date" => "desc", "order_id" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Orders\\Data\\OrdersListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - 
     - 
     - 
     - 
   * - :category_header:`Идентификатори`
     - 
     - 
     - 
   * - **$order_id**
     - *string*
     - 
     - Подреждане по ID на поръчка
   * - **$article_id**
     - *string*
     - 
     - Подреждане по ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$barsy_id**
     - *string*
     - 
     - Подреждане по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$date**
     - *string*
     - 
     - Подреждане по дата на поръчката
   * - **$served_date**
     - *string*
     - 
     - Подреждане по дата на обслужване
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$article_name**
     - *string*
     - 
     - Подреждане по име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$amount**
     - *string*
     - 
     - Подреждане по количество
   * - **$status**
     - *string*
     - 
     - Подреждане по статус

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/orders/getlist`

