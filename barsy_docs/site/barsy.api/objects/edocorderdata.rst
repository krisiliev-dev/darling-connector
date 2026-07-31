.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

eDocOrderData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Edocs\\Data\\eDocOrderData


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
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_name**
     - *string*
     - 
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$current_price**
     - *float*
     - 
     - Цена, на която се извършена операцията
   * - **$amount_type_name_short**
     - *string*
     - 
     - Кратко име на тип количество ( виж: :doc:`../methods/amounttypes/getlist` )
   * - **$amount**
     - *float*
     - 
     - Количество, което е включено в операцията
   * - **$lot_value**
     - *string*
     - 
     - Партида на `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$lot_exp_date**
     - *string*
     - 
     - Партида дата - срок на годност
   * - **$rs_tax_id**
     - *int*
     - 
     - ID на ДДС-то на отдалечената система, от която получаваме данните

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/edocs/get_by_sid`
	 * :doc:`../methods/edocs/get`

