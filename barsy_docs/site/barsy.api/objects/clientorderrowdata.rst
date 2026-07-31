.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientOrderRowData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clientorders\\Data\\ClientOrderRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_order_row**
     - *integer*
     - 
     - ID на реда
   * - **$article_id**
     - *integer*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ по номенклатура на barsy

			 пример: "10"
   * - **$article_name**
     - *string*
     - 
     - Име на `артикул </barsy.help/210-dictionary/article.html>`__ по номенклатура на barsy

			 пример: "\"\\u0411\\u043e\\u0437\\u0430\""
   * - **$amount**
     - *float*
     - 
     - Желано количество - може да бъде дробно число до 9-ти знак

			 пример: "\"= 4\""
   * - **$current_price**
     - *float*
     - 
     - Единична цена на поръчката - ако не е подадена, ще бъде ползвана текущата цена за този `търговски обект </barsy.help/210-dictionary/barsy.html>`__/`клиент </barsy.help/210-dictionary/client.html>`__/`артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "4.12"
   * - **$detail_notes**
     - *string*
     - 
     - Свободен текст - Може да съдържа някакви допълнително описание към конкретния `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$details**
     - *object*
     - 
     - Детайли към `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$detail_status**
     - *int*
     - 
     - 
   * - **$user_id**
     - *int*
     - 
     - Id на `потребител </barsy.help/210-dictionary/user.html>`__, въвел `артикула </barsy.help/210-dictionary/article.html>`__
   * - **$last_update**
     - *string*
     - 
     - Последна промяна на `артикула </barsy.help/210-dictionary/article.html>`__ в заявката
   * - **$details_checksum**
     - *string*
     - 
     - Чексума на данните на реда
   * - **$amount_type_name_short**
     - *string*
     - 
     - Тип количество - кратко име
   * - **$package_name**
     - *string*
     - 
     - Име на разфасовката (при използване на разфасовки)
   * - **$package_ratio**
     - *float*
     - 
     - Количеството в една разфасовка (при използване на разфасовки)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clientorders/getdetails`

