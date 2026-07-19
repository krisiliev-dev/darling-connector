.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientsListOrderByData
======================================================================================
Позволените колони за подреждане на списъка с клиенти (Clients_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Подава се като асоциативен масив колона⇒посока (напр. ["client_name" => "asc"]). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clients\\Data\\ClientsListOrderByData


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
   * - **$client_id**
     - *string*
     - 
     - Подреждане по ID на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$export_id**
     - *string*
     - 
     - Подреждане по "Export ID"
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$client_name**
     - *string*
     - 
     - Подреждане по име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$tel**
     - *string*
     - 
     - Подреждане по телефон
   * - **$email**
     - *string*
     - 
     - Подреждане по имейл
   * - **$town**
     - *string*
     - 
     - Подреждане по град
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$group_id**
     - *string*
     - 
     - Подреждане по клиентска група
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$discount**
     - *string*
     - 
     - Подреждане по отстъпка
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$client_create_date**
     - *string*
     - 
     - Подреждане по дата на създаване
   * - **$last_update**
     - *string*
     - 
     - Подреждане по дата на последна промяна

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clients/getlist`

Виж също
--------

 * `Клиент </barsy.help/210-dictionary/client.html>`__

