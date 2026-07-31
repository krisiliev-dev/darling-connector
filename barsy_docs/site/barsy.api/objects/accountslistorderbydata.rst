.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

AccountsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка със сметки (Accounts_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като асоциативен масив колона⇒посока (напр. ["ref_date" => "desc", "account_id" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Accounts\\Data\\AccountsListOrderByData


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
   * - :category_header:`Идентификатори`
     - 
     - 
     - 
   * - **$account_id**
     - *string*
     - 
     - Подреждане по ID на `сметка </barsy.help/210-dictionary/account.html>`__
   * - **$account_num**
     - *string*
     - 
     - Подреждане по номер на `сметка </barsy.help/210-dictionary/account.html>`__
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$create_date**
     - *string*
     - 
     - Подреждане по дата на откриване
   * - **$close_date**
     - *string*
     - 
     - Подреждане по дата на затваряне
   * - **$ref_date**
     - *string*
     - 
     - Подреждане по вальор (документна дата)
   * - **$last_order_date**
     - *string*
     - 
     - Подреждане по дата на последна поръчка
   * - **$total_sum**
     - *string*
     - 
     - Подреждане по обща сума
   * - **$total_remain**
     - *string*
     - 
     - Подреждане по остатък
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$status**
     - *string*
     - 
     - Подреждане по статус
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$client_id**
     - *string*
     - 
     - Подреждане по ID на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$user_id**
     - *string*
     - 
     - Подреждане по ID на `потребител </barsy.help/210-dictionary/user.html>`__
   * - **$barsy_id**
     - *string*
     - 
     - Подреждане по ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__
   * - **$place_id**
     - *string*
     - 
     - Подреждане по ID на място

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getlist`

Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__

