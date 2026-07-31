.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ArticleDetailKeyData
======================================================================================
Една характеристика (детайл) от номенклатурата на характеристиките на артикулите.

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*Основните полета се връщат винаги; останалите — само ако са поискани чрез extra_properties.*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Articledetails\\Data\\ArticleDetailKeyData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$key_id**
     - *int*
     - 
     - ID на характеристиката
   * - **$detail_name**
     - *string*
     - 
     - Име на характеристиката
   * - **$detail_suffix**
     - *string*
     - 
     - Наставка (мерна единица) към стойността на характеристиката
   * - **$type**
     - *string*
     - 
     - Тип на въвеждане ("text", "select", "autocomplete", "checkbox", "date", "datetime")
   * - **$group_id**
     - *int*
     - 
     - ID на групата, към която принадлежи характеристиката
   * - **$parent_id**
     - *int*
     - 
     - ID на родителската характеристика (0, ако няма родител)
   * - **$is_service**
     - *int*
     - 
     - Дали характеристиката е служебна (системна)
   * - **$is_required**
     - *bool*
     - 
     - Дали попълването на характеристиката е задължително
   * - **$is_multiple**
     - *bool*
     - 
     - Дали характеристиката допуска няколко стойности едновременно
   * - **$detail_weight**
     - *int*
     - 
     - Тежест за подреждане на характеристиката
   * - **$description**
     - *string*
     - 
     - Описание на характеристиката
   * - **$detail_is_public**
     - *bool*
     - 
     - Дали характеристиката е публична (видима извън системата)
   * - **$update_article_last_update**
     - *string*
     - 
     - Дата на последна промяна, при която `артикулите </barsy.help/210-dictionary/article.html>`__ да се маркират за обновяване
   * - **$is_summable**
     - *bool*
     - 
     - Дали стойностите на характеристиката могат да се сумират
   * - **$value_type**
     - *int*
     - 
     - Тип на стойността (текст, цяло число, десетична стойност)
   * - **$values**
     - *string*
     - 
     - Възможните стойности на характеристиката (суров списък).

			*Връща се само при extra_properties "values"*

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/articledetails/getlist`

Виж също
--------

 * `Артикул </barsy.help/210-dictionary/article.html>`__

