.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

RecommendationData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articles\\Data\\RecommendationData


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
     - ID на предложения `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name_public**
     - *string*
     - 
     - Публично име на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$article_name_public_ml**
     - *object*
     - 
     - Публично име на `артикула </barsy.help/210-dictionary/article.html>`__ по езици
   * - **$picture**
     - *string*
     - 
     - URL на основната картинка на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$current_price**
     - *float*
     - 
     - Текуща продажна цена според контекста
   * - **$current_price_curr**
     - *float*
     - 
     - Текуща продажна цена във втора валута

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articlerelations/resolve`

