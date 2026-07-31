.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleDetailsTreeExtraPropertiesData
======================================================================================
Опции за допълнителни данни към дървото на характеристиките (Articledetails_gettree).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*Приема и стария формат — списък с имена (напр. ["values"]) — който се превежда към булеви флагове.*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articledetails\\Data\\ArticleDetailsTreeExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$values**
     - *bool*
     - false
     - Да се върнат и възможните стойности на всяка характеристика. При голям брой стойности или

			*характеристика тип "autocomplete" вместо изброени стойности се връща източник за подсказване (data_source).*

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/gettree`

