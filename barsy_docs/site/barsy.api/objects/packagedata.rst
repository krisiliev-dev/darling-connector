.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PackageData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Packages\\Data\\PackageData


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
     - ID на разфасовката ( виж: :doc:`../methods/packages/get` )
   * - **$package_name**
     - *string*
     - 
     - Име на разфасовката
   * - **$package_name_title**
     - *string*
     - 
     - Име на разфасовката с количество (напр. „`Каса </barsy.help/210-dictionary/pos.html>`__ (x12)“)
   * - **$package_ratio**
     - *string*
     - 
     - Количество `артикул </barsy.help/210-dictionary/article.html>`__ в една разфасовка
   * - **$package_weight**
     - *int*
     - 
     - Тежест за подреждане в списъци
   * - **$description**
     - *string*
     - 
     - Описание на разфасовката
   * - **$delete_flag**
     - *int*
     - 
     - Флаг за изтрита разфасовка
   * - **$round_amount**
     - *int*
     - 
     - Тип закръгляне при изчисляване на количество (0 — няма, 1 — до цяла разфасовка и др.)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/packages/getlist`
	 * :doc:`../methods/packages/get`

