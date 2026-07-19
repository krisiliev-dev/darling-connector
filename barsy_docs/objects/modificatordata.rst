.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ModificatorData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Modificators\\Data\\ModificatorData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$mod_id**
     - *int*
     - 
     - ID на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_name**
     - *string*
     - 
     - Име на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$description**
     - *string*
     - 
     - Описание на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$operation**
     - *int*
     - 0
     - Вид операция ('без' `модификатора </barsy.help/210-dictionary/modificator.html>`__ или 'с' `модификатора </barsy.help/210-dictionary/modificator.html>`__)
   * - **$weight**
     - *int*
     - 
     - Тежест при подреждане на мофификатори в `категория </barsy.help/210-dictionary/category.html>`__
   * - **$mod_color**
     - *string*
     - 
     - Цвят на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_type**
     - *int*
     - 
     - Тип `модификатор </barsy.help/210-dictionary/modificator.html>`__

			* **1** - *Липсва описание*
			* **2** - *Липсва описание*
   * - **$categories**
     - *array*
     - []
     - Списък с `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран този `модификатор </barsy.help/210-dictionary/modificator.html>`__ ( виж: :doc:`../methods/categories/getlist` )

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getbytaxes`
	 * :doc:`../methods/accounts/getlist`
	 * :doc:`../methods/accounts/get`
	 * :doc:`../methods/articles/getmodificators`
	 * :doc:`../methods/modificators/create`
	 * :doc:`../methods/modificators/getarticlelist`
	 * :doc:`../methods/modificators/getavailableforarticle`
	 * :doc:`../methods/modificators/getlist`
	 * :doc:`../methods/orders/getlist`
	 * :doc:`../methods/places/getlistwithaccountsonly`

