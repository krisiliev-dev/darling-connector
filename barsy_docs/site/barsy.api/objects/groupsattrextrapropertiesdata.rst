.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

GroupsattrExtraPropertiesData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Groupsattr\\Data\\GroupsattrExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$attributes**
     - *bool*
     - false
     - Ако е подадено, се връща информация за атрибутите на групата
   * - **$description**
     - *bool*
     - false
     - Ако е подадено, се връща информация за описанието на групата
   * - **$weight**
     - *bool*
     - false
     - Ако е подадено, се връща информация за теглото (WEIGHT) на групата
   * - **$create_date**
     - *bool*
     - false
     - Ако е подадено, се връща информация за датата на създаване на групата
   * - **$last_update**
     - *bool*
     - false
     - Ако е подадено, се връща информация за датата на последна промяна
   * - **$own_group**
     - *bool*
     - false
     - Ако е подадено, се връща информация за флага OWN_GROUP
   * - **$article_id**
     - *int*
     - 
     - Ако е подадено, се връща и информация за възможните атрибути за посочения `артикул </barsy.help/210-dictionary/article.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/groupsattr/getlist`
	 * :doc:`../methods/groupsattr/get`

