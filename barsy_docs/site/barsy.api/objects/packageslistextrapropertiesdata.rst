.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PackagesListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към разфасовка от списъка. Всяка опция включва съответната колона към

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*данните за всеки запис. Основните данни се връщат винаги, останалите при стойност true.*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Packages\\Data\\PackagesListExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$package_id**
     - *bool*
     - true
     - ID на разфасовката ( виж: :doc:`../methods/packages/get` )
   * - **$package_name**
     - *bool*
     - true
     - Име на разфасовката
   * - **$package_name_title**
     - *bool*
     - true
     - Име на разфасовката с количество (напр. „`Каса </barsy.help/210-dictionary/pos.html>`__ (x12)“)
   * - **$package_ratio**
     - *bool*
     - true
     - Количество `артикул </barsy.help/210-dictionary/article.html>`__ в една разфасовка
   * - **$package_weight**
     - *bool*
     - true
     - Тежест за подреждане в списъци
   * - **$description**
     - *bool*
     - false
     - Описание на разфасовката

			 пример: "1"
   * - **$delete_flag**
     - *bool*
     - true
     - Флаг за изтрита разфасовка
   * - **$round_amount**
     - *bool*
     - true
     - Тип закръгляне при изчисляване на количество

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/packages/getlist`

