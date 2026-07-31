.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

InvoiceItemData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Invoices\\Data\\InvoiceItemData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$item_id**
     - *int*
     - 
     - 
   * - **$item_name**
     - *string*
     - 
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__
   * - :deprecated:`$single_price`
     - *float*
     - 
     - Служебна стойност за единична цена без ДДС.

			*Изполвайте original_single_price* :deprecated_text:`Отхвърлено: */`
   * - **$original_single_price**
     - *float*
     - 
     - Единична цена без ДДС
   * - :deprecated:`$single_price_with_tax`
     - *float*
     - 
     - Служебна стойност за единична цена с ДДС.

			*Изполвайте original_single_price_with_tax* :deprecated_text:`Отхвърлено: */`
   * - **$original_single_price_with_tax**
     - *float*
     - 
     - Единична цена с ДДС
   * - **$quantity**
     - *float*
     - 
     - Колиество на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$line_total**
     - *float*
     - 
     - Тотал на цената спрямо това дали са поискани тотали в оригинална или системна валута и дали са с ДДС или без ДДС
   * - **$measure**
     - *string*
     - 
     - Мерна единица на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_id**
     - *int*
     - 
     - ДДС група на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax**
     - *int*
     - 
     - ДДС на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$inv_ref_num**
     - *string*
     - 
     - Референтен номер на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$tax_reason**
     - *string*
     - 
     - 
   * - **$discount**
     - *float*
     - 0
     - 
   * - **$remote_ref_id**
     - *int*
     - 
     - Номер на `артикула </barsy.help/210-dictionary/article.html>`__ спрямо отдалечената система
   * - **$uuid**
     - *string*
     - 
     - Уникален номер на редър
   * - **$lot_value**
     - *string*
     - 
     - Номер на партида

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/invoices/get_by_sid`
	 * :doc:`../methods/invoices/getlist`
	 * :doc:`../methods/invoices/get`

