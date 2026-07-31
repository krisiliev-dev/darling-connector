.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

DocumentsGetExtraPropertiesData
======================================================================================
Допълнителни данни към Documents_get (групи, редове, суми).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Documents\\Data\\DocumentsGetExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$groups**
     - *bool*
     - false
     - Групи на документа
   * - **$details**
     - *bool*
     - false
     - Редове (`артикули </barsy.help/210-dictionary/article.html>`__) на документа
   * - **$totals**
     - *bool*
     - false
     - Агрегирани суми за документа

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/documents/get`

