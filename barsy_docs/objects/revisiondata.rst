.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

RevisionData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Revisions\\Data\\RevisionData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$rev_id**
     - *int*
     - 
     - ID на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ ( виж: :doc:`../methods/barsys/getlist` )
   * - **$barsy_name**
     - *string*
     - 
     - Име на търговския обект
   * - **$depot_id**
     - *int*
     - 
     - ID на `склад </barsy.help/210-dictionary/store.html>`__, в който е заредено ( виж: :doc:`../methods/depots/getlist` )
   * - **$status**
     - *int*
     - 
     - Статус на `ревизията </barsy.help/210-dictionary/revision.html>`__ [0=Отворено, 1=Приключено]
   * - **$date**
     - *string*
     - 
     - Дата на създаване на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$close_date**
     - *string*
     - 
     - Дата на приключване на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$amount_date**
     - *string*
     - 
     - Дата на операцията (момент на засичане на наличности)
   * - **$description**
     - *string*
     - 
     - Описание на `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$user_name**
     - *string*
     - 
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `ревизията </barsy.help/210-dictionary/revision.html>`__
   * - **$creator_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, създал `ревизията </barsy.help/210-dictionary/revision.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$closer_id**
     - *int*
     - 
     - ID на `потребител </barsy.help/210-dictionary/user.html>`__, приключил `ревизията </barsy.help/210-dictionary/revision.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$close_count**
     - *int*
     - 
     - Брой пъти, в които `ревизията </barsy.help/210-dictionary/revision.html>`__ е била затворена

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/revisions/getlist`

