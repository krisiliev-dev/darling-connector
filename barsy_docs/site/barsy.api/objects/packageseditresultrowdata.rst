.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PackagesEditResultRowData
======================================================================================
Данни за резултата

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Packages\\Data\\PackagesEditResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$package_id**
     - *int*
     - 
     - *ID*
   * - **$package_name**
     - *string*
     - 
     - *Име на разфасовката*
   * - **$package_ratio**
     - *string*
     - 
     - Какво количество от `артикула </barsy.help/210-dictionary/article.html>`__ съдържа разфасовката
   * - **$description**
     - *string*
     - 
     - *Описание на разфасовката*
   * - **$package_weight**
     - *int*
     - 
     - *Тежест за подреждане на разфасовките*
   * - **$round_amount**
     - *string*
     - 
     - *Закръгляне на количеството до цяла разфасовка*

			 пример: "0"
   * - **$delete_flag**
     - *string*
     - 
     - *Блокира записа за използване в системата*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/packages/edit`

