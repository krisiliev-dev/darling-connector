.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PricelistArticleData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Pricelists\\Data\\PricelistArticleData


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
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "2"
   * - **$custom_price**
     - *float*
     - 
     - Предпочитана продажна цена за дадения `артикул </barsy.help/210-dictionary/article.html>`__ в това `ценово правило </barsy.help/210-dictionary/pricelist.html>`__.

			*Когато е налично, надписва изчислената цена*

			 пример: "2.3"
   * - **$price_change_group**
     - *int*
     - 
     - ID на група, към която принадлежи `артикула </barsy.help/210-dictionary/article.html>`__.

			*Необходимо за Mix-and-match промоции. Стойности 1-10*

			 пример: "1"
   * - **$req_amount**
     - *float*
     - 
     - Необходимо минимално количество, което ще трябва да присъства в `сметката </barsy.help/210-dictionary/account.html>`__ за да бъде удовлетворено правилото

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/pricelists/save_articles`

