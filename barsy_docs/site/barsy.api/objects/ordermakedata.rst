.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

OrderMakeData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Orders\\Data\\OrderMakeData


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

			 пример: "123"
   * - **$amount**
     - *float*
     - 
     - Количество

			 пример: "2"
   * - :deprecated:`$current_price`
     - *float*
     - 
     - Продажна цена (ако се пропусне - ще се използва текущата) :deprecated_text:`Отхвърлено: Използваме original_current_price вместо това поле`

			 пример: "2.4"
   * - **$original_current_price**
     - *float*
     - 
     - Продажна цена (ако се пропусне - ще се използва текущата)

			 пример: "2.4"
   * - **$discount**
     - *float*
     - 
     - Отстъпка/надценка в проценти на продажната цена на `артикул </barsy.help/210-dictionary/article.html>`__ в `сметка </barsy.help/210-dictionary/account.html>`__ (различно от отстъпка на цялата `сметка </barsy.help/210-dictionary/account.html>`__)

			 пример: "-5"
   * - **$tax_id**
     - *int*
     - 
     - ДДС
   * - **$modificators**
     - *ModificatorInputData*
     - 
     - 
   * - **$article_attributes**
     - *ArticleAttributesSimpleData*
     - 
     - 
   * - **$supplements**
     - *ArticleSupplementData*
     - 
     - Комбинирани `артикули </barsy.help/210-dictionary/article.html>`__
   * - **$storno_of_account_id**
     - *int*
     - 
     - Номер на `сметка </barsy.help/210-dictionary/account.html>`__ по което се сторнира тази поръчка (само при отрицателно количество)
   * - **$tax_region_id**
     - *int*
     - 
     - ID на данъчен регион

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/create`
	 * :doc:`../methods/accounts/divide`
	 * :doc:`../methods/accounts/place`

