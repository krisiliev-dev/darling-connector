.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientGroupData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clientgroups\\Data\\ClientGroupData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$group_id**
     - *int*
     - 
     - ID на групата
   * - **$group_name**
     - *string*
     - 
     - Име на групата
   * - **$default_credit_limit**
     - *float*
     - 
     - Кредитен лимит по подразбиране за всички членове на групата (ако не им е зададена индивидуална)
   * - **$default_discount**
     - *int*
     - 
     - Отстъпка по подразбиране за всички членове на групата (ако не им е зададена индивидуална)
   * - **$description**
     - *string*
     - 
     - Описание - свободен текст
   * - **$weight**
     - *int*
     - 
     - "Тежест" при подреждане на списъка от групи
   * - **$delete_flag**
     - *int*
     - 
     - Флаг дали групата е маркирана като изтрита
   * - **$client_levels_enabled**
     - *int*
     - 
     - Флаг дали групата влиза в клиентските прагове
   * - **$default_paymethod_id**
     - *int*
     - 
     - Начин на `плащане </barsy.help/210-dictionary/payment.html>`__ по подразбиране за тази `клиенти </barsy.help/210-dictionary/client.html>`__ от тази клиентска група ( виж: :doc:`../methods/paymentmethods/getlist` )
   * - **$default_paid_period**
     - *int*
     - 
     - Период за отложено плщане по подразбиране за тази `клиенти </barsy.help/210-dictionary/client.html>`__ от тази клиентска група
   * - **$ml_group_id**
     - *string*
     - 
     - ID на група в maillist външна система, която се използва
   * - **$default_ml_clients_sub**
     - *int*
     - 
     - Настройка дали `клиентите </barsy.help/210-dictionary/client.html>`__ от тази група автоматично да се абонират за настроената maillist външна система

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientgroups/getlist`
	 * :doc:`../methods/clients/getgroups`

