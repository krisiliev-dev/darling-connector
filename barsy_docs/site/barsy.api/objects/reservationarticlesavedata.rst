.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ReservationArticleSaveData
======================================================================================
Артикули към резервация

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Reservations\\Data\\ReservationArticleSaveData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$id**
     - *int*
     - 
     - ID на ред от списъка с `артикули </barsy.help/210-dictionary/article.html>`__
   * - **$article_id**
     - *int*
     - 
     - ID на избран `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "1" ( виж: :doc:`../methods/articles/get` )
   * - **$amount**
     - *float*
     - 
     - Количество на избрания `артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - **$current_price**
     - *float*
     - 
     - Текуща продажна цена на избрания `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_id**
     - *int*
     - 
     - ID на ДДС група на `артикула </barsy.help/210-dictionary/article.html>`__ ( виж: :doc:`../methods/taxgroups/getlist` )
   * - **$notes**
     - *string*
     - 
     - Бележки към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$parent_id**
     - *int*
     - 
     - 
   * - **$supplement_group_id**
     - *int*
     - 
     - ID на групата комбо `артикули </barsy.help/210-dictionary/article.html>`__ — попълва се само за supplement редове.
   * - **$supplements**
     - *ArticleSupplementData*
     - 
     - Комбинирани `артикули </barsy.help/210-dictionary/article.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/reservations/create`
	 * :doc:`../methods/reservations/update`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__
 * `Резервация </barsy.help/210-dictionary/reservation.html>`__

