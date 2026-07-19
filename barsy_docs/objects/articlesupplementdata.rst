.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleSupplementData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\ArticleSupplementData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, в участва в комбо `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$amount**
     - *float*
     - 
     - Количество на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо
   * - **$supplement_price**
     - *float*
     - 
     - цена на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо (ако не се подаде, се ползва зададената или изчислената)
   * - **$supplement_group_id**
     - *int*
     - 
     - ID на група на комбото, в която участва `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$discount**
     - *float*
     - 
     - Отстъпка на `артикула </barsy.help/210-dictionary/article.html>`__ в това комбо
   * - **$tax_id**
     - *int*
     - 
     - ДДС id на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$tax_region_id**
     - *int*
     - 
     - ID на тип доставка
   * - **$article_attributes**
     - *array*
     - 
     - Атрибути на `артикула </barsy.help/210-dictionary/article.html>`__ (при `артикули </barsy.help/210-dictionary/article.html>`__ с дефинирани атрибути — цвят, размер и т.н.).

			*Структура: [{article_id, amount, attributes: [{key, value}, ...]}]*
   * - **$lot_value**
     - *string*
     - 
     - Партида на supplement-а (за `артикули </barsy.help/210-dictionary/article.html>`__ с LOT_TYPE_ID > 1).
   * - **$supplement_article**
     - 
     - 
     - 

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/create`
	 * :doc:`../methods/accounts/divide`
	 * :doc:`../methods/accounts/place`
	 * :doc:`../methods/reservations/create`
	 * :doc:`../methods/reservations/update`

