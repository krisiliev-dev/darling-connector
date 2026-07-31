.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

StoreMovesListExtraProperties
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Storemoves\\Data\\StoreMovesListExtraProperties


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$common**
     - *bool*
     - true
     - Основни данни за `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$user**
     - *bool*
     - true
     - `Потребител </barsy.help/210-dictionary/user.html>`__, създал `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$from**
     - *bool*
     - true
     - Показва данни за `склада </barsy.help/210-dictionary/store.html>`__ и търговския обект, от които се изтегля стоката
   * - **$to**
     - *bool*
     - true
     - Показва данни за `склада </barsy.help/210-dictionary/store.html>`__ и търговския обект, към които се изпраща стоката
   * - **$doc_date**
     - *bool*
     - false
     - Документална дата на операцията
   * - **$inspector_user_name**
     - *bool*
     - false
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, проверил `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__ ( виж: :doc:`../methods/users/getlist` )
   * - **$description**
     - *bool*
     - false
     - Описание на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$inspector_description**
     - *bool*
     - false
     - Описание, въведено от `потребителя </barsy.help/210-dictionary/user.html>`__, проверил `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$status**
     - *bool*
     - false
     - ID статус на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$status_title**
     - *bool*
     - false
     - 

			* **0** - *Отворено*
			* **1** - *Приключено*
			* **2** - *На път*
			* **3** - *Отказано*
			* **10** - *За получаване*
			* **11** - *Изпратено*
   * - **$close_date**
     - *bool*
     - false
     - Дата на затваряне на `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__
   * - **$details**
     - *bool*
     - false
     - Данни за `артикулите </barsy.help/210-dictionary/article.html>`__ в `прехвърлянето </barsy.help/210-dictionary/storemove.html>`__

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/storemoves/getlist`

