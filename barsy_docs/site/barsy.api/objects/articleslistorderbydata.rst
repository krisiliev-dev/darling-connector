.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticlesListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с артикули (Articles_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като асоциативен масив колона⇒посока (напр. {"article_name":"asc"}), низ (`"article_name desc, create_date"`) или списък от низове. Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`. Когато не е подадено подреждане, резултатът не се пренарежда.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticlesListOrderByData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$article_id**
     - *string*
     - 
     - Подреждане по ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$parent_id**
     - *string*
     - 
     - Подреждане по ID на родителски `артикул </barsy.help/210-dictionary/article.html>`__ (групиране на вариантите към базовия `артикул </barsy.help/210-dictionary/article.html>`__)
   * - **$article_name**
     - *string*
     - 
     - Подреждане по вътрешно име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name_public**
     - *string*
     - 
     - Подреждане по публично име на `артикул </barsy.help/210-dictionary/article.html>`__ (с fallback към вътрешното, ако липсва)
   * - **$actual_price**
     - *string*
     - 
     - Подреждане по актуална цена на `артикула </barsy.help/210-dictionary/article.html>`__ (от каталога, без отстъпки и промоции)
   * - **$current_price**
     - *string*
     - 
     - Подреждане по текуща продажна цена в контекста на конкретна `каса </barsy.help/210-dictionary/pos.html>`__/`клиент </barsy.help/210-dictionary/client.html>`__ (с промоции и `ценови правила </barsy.help/210-dictionary/pricelist.html>`__)
   * - **$create_date**
     - *string*
     - 
     - Подреждане по дата на създаване на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$ref_date**
     - *string*
     - 
     - Подреждане по референтна дата (последна промяна — за инкрементална синхронизация)
   * - **$close_date**
     - *string*
     - 
     - Подреждане по дата на закриване/архивиране на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$delete_flag**
     - *string*
     - 
     - Подреждане по флаг за изтриване (активни преди изтрити)
   * - **$cat_weight_deep**
     - *string*
     - 
     - Подреждане по тегло на `артикула </barsy.help/210-dictionary/article.html>`__ в `категория </barsy.help/210-dictionary/category.html>`__, без значение коя `категория </barsy.help/210-dictionary/category.html>`__

			При подаден филтър `cat_id_deep` подреждането се ограничава до съответното поддърво.
   * - **$weight**
     - *string*
     - 
     - Подреждане по тегло (ръчно зададен ред) в конкретна `категория </barsy.help/210-dictionary/category.html>`__

			Прилага се само при подаден филтър `single_cat_id`; иначе се игнорира.

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articles/getlist`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

