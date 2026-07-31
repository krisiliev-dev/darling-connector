.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

InputStornoData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Accounts\\Data\\InputStornoData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$storno_reason**
     - *string*
     - 
     - Причина за сторното

			* **return** - *Връщане / рекламация*
			* **mistake** - *Операторска грешка*
			* **reduction_tax_base** - *Намаление на данъчната основа* ( виж: :doc:`../methods/accounts/getstornoreasons` )
   * - **$unp**
     - *string*
     - 
     - УНП на сторнираната бележка
   * - **$receipt_num**
     - *string*
     - 
     - Номер на сторнираната бележка
   * - **$receipt_date**
     - *string*
     - 
     - Дата на сторнираната бележка
   * - **$fm_num**
     - *string*
     - 
     - Номер на фискална памет на сторнираната бележка

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/createfromclientorder`
	 * :doc:`../methods/accounts/create`
	 * :doc:`../methods/accounts/place`
	 * :doc:`../methods/accounts/storno`
	 * :doc:`../methods/clientorders/create`
	 * :doc:`../methods/reservations/create`

