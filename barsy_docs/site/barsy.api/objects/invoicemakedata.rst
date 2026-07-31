.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

InvoiceMakeData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Invoices\\Data\\InvoiceMakeData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$gen_mode**
     - *int*
     - 1
     - Тип `фактура </barsy.help/210-dictionary/invoice.html>`__

			* **1** - Подробна `фактура </barsy.help/210-dictionary/invoice.html>`__ - всички `артикули </barsy.help/210-dictionary/article.html>`__
			* **2** - обобщена `фактура </barsy.help/210-dictionary/invoice.html>`__ - 1 `артикул </barsy.help/210-dictionary/article.html>`__
			* **3** - Обощена `фактура </barsy.help/210-dictionary/invoice.html>`__ за множество `сметки </barsy.help/210-dictionary/account.html>`__. За всяка `сметка </barsy.help/210-dictionary/account.html>`__ се добавя един `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$receiver_company_name**
     - *string*
     - 
     - Име на `фирма </barsy.help/210-dictionary/company.html>`__ получател

			 пример: "\"\\u0424\\u0438\\u0440\\u043c\\u0430 \\u041e\\u041e\\u0414\""
   * - **$receiver_identity_num**
     - *string*
     - 
     - ЕИК на получател

			 пример: "1234567890"
   * - **$receiver_vat_num**
     - *string*
     - 
     - ДДС № на получател

			 пример: "\"BG123456789\""
   * - **$receiver_mol**
     - *string*
     - 
     - МОЛ на получател

			 пример: "\"\\u0418\\u0432\\u0430\\u043d \\u0418\\u0432\\u0430\\u043d\\u043e\\u0432\""
   * - **$receiver_name**
     - *string*
     - 
     - Име на получател
   * - **$receiver_town**
     - *string*
     - 
     - Град на получател
   * - **$receiver_address**
     - *string*
     - 
     - Адрес на получател

			 пример: "\"\\u0431\\u0443\\u043b. \\u0411\\u044a\\u043b\\u0433\\u0430\\u0440\\u0438\\u044f \\u21161\""
   * - **$print**
     - *bool*
     - false
     - Казва дали да се изпрати `фактурата </barsy.help/210-dictionary/invoice.html>`__, за печат, към настроения служебен принтер на текущата `каса </barsy.help/210-dictionary/pos.html>`__

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/place`

