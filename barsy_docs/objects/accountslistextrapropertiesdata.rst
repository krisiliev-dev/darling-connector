.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

AccountsListExtraPropertiesData
======================================================================================
Опции за допълнителна информация към всяка сметка в списъка (Accounts_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Всяко свойство е булев флаг — при `true` към `сметката </barsy.help/210-dictionary/account.html>`__ се добавя съответната допълнителна информация.

*Подава се като асоциативен масив флаг⇒bool (напр. {"orders":true,"payments":true}) или списък с имена (напр. ["orders","payments"]).*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Accounts\\Data\\AccountsListExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - 
     - 
     - 
     - 
   * - :category_header:`Основни данни`
     - 
     - 
     - 
   * - **$account_period**
     - *bool*
     - true
     - Времетраене на `сметката </barsy.help/210-dictionary/account.html>`__

			Времето от откриването на `сметката </barsy.help/210-dictionary/account.html>`__ до нейното затваряне (или до момента, ако още е открита).

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`История и движения`
     - 
     - 
     - 
   * - **$orders**
     - *bool*
     - false
     - Сумиран списък на поръчаните `артикули </barsy.help/210-dictionary/article.html>`__

			 пример: "1" ( виж: ``OrderData`` )
   * - **$orders_history**
     - *bool*
     - false
     - Подробен списък с всяка поръчка

			 пример: "0" ( виж: ``OrderData`` )
   * - **$payments**
     - *bool*
     - false
     - Сумиран списък на плащанията по начини на `плащане </barsy.help/210-dictionary/payment.html>`__ към `сметката </barsy.help/210-dictionary/account.html>`__

			 пример: "1"
   * - **$payments_history**
     - *bool*
     - false
     - Подробен списък на плащанията към `сметката </barsy.help/210-dictionary/account.html>`__

			 пример: "0"
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$close_pos_id**
     - *bool*
     - false
     - `Каса </barsy.help/210-dictionary/pos.html>`__, на която е затворена `сметката </barsy.help/210-dictionary/account.html>`__ (ID и име).

			 пример: "1"
   * - **$ref_id**
     - *bool*
     - false
     - Външен идентификатор

			Външен идентификатор на записа за бележка по `сметката </barsy.help/210-dictionary/account.html>`__.

			 пример: "1"
   * - **$remote_id**
     - *bool*
     - false
     - Идентификатор от отдалечена система.

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$next_service_status**
     - *bool*
     - false
     - Следващ сервизен статус (ID и име).

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
     - 
   * - **$user_can_edit**
     - *bool*
     - false
     - Право за редакция

			Дали текущият `потребител </barsy.help/210-dictionary/user.html>`__ има право да редактира `сметката </barsy.help/210-dictionary/account.html>`__.

			 пример: "1"
   * - **$confirmation_output_screen_check**
     - *bool*
     - false
     - Наличие на потвърдителен екран

			Дали за статуса на `сметката </barsy.help/210-dictionary/account.html>`__ е наличен потвърдителен екран към текущото работно място.

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getlist`

Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__

