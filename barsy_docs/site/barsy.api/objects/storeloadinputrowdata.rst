.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreLoadInputRowData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storeloads\\Data\\StoreLoadInputRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$store_load_row_id**
     - *int*
     - 
     - ID на ред в `зареждането </barsy.help/210-dictionary/storeload.html>`__
   * - **$original_article_name**
     - *string*
     - 
     - Име на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, който се зарежда

			 пример: "101" ( виж: :doc:`../methods/articles/getlist` )
   * - **$amount**
     - *float*
     - 
     - Количество, което се зарежда в `склада </barsy.help/210-dictionary/store.html>`__ (в основна единици: бр, кг, л,...)

			 пример: "3.45"
   * - **$current_price**
     - *float*
     - 
     - Единична доставна цена, на която се зарежда `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "3.23"
   * - **$actual_price**
     - *float*
     - 
     - Единична продажна цена

			 пример: "3.23"
   * - **$delivery_tax_id**
     - *int*
     - 
     - ID на ДДС за доставка
   * - **$notes**
     - *string*
     - 
     - Свободен текст към реда на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$package_name**
     - *string*
     - 
     - Име на опаковката (при използване на опаковки)
   * - **$package_ratio**
     - *float*
     - 
     - Количеството в една опаковка (при използване на опаковки)
   * - **$attributes**
     - *array*
     - 
     - Атрибути
   * - **$return_from_store_load_row_id**
     - *int*
     - 
     - Id на ред в `зареждане </barsy.help/210-dictionary/storeload.html>`__, връзка при връщане на стока
   * - **$deal_id**
     - *int*
     - 
     - Id на сделка
   * - **$lot_value**
     - *string*
     - 
     - Партида номер
   * - **$lot_exp_date**
     - *string*
     - 
     - Партида дата - срок на годност
   * - **$lot_detail_id**
     - *int*
     - 
     - Id на партидата в операцията
   * - **$manufacturer**
     - *string*
     - 
     - Производител
   * - **$add_data**
     - *array*
     - 
     - Допълнителни данни/колони - конфигурируеми
   * - **$discount**
     - *float*
     - 0
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storeloads/create`
	 * :doc:`../methods/storeloads/update`

