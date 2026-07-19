.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PricelistArticleTemplateData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Pricelists\\Data\\PricelistArticleTemplateData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$pattern_id**
     - *int*
     - 
     - ID на шаблон

			 пример: "1"
   * - **$pattern**
     - *string*
     - 
     - Шаблон за име на `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "\"Coffee\""
   * - **$custom_price**
     - *int*
     - 
     - Предпочитана цена на `артикулите </barsy.help/210-dictionary/article.html>`__, които отговарят на шаблона

			 пример: "2.4"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/pricelists/save_article_patterns`

