.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientOrderInputRowData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clientorders\\Data\\ClientOrderInputRowData


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
     - ID на реда (празно при подаване на нов ред в поръчката)
   * - **$article_id**
     - *integer*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__ по номенклатура на barsy

			 пример: "10"
   * - **$amount**
     - *float*
     - 
     - Желано количество - може да бъде дробно число до 9-ти знак

			 пример: "4.2"
   * - **$current_price**
     - *float*
     - 
     - 
   * - **$original_price**
     - *float*
     - 
     - Единична цена на поръчката - ако не е подадена, ще бъде ползвана текущата цена за този `търговски обект </barsy.help/210-dictionary/barsy.html>`__/`клиент </barsy.help/210-dictionary/client.html>`__/`артикул </barsy.help/210-dictionary/article.html>`__

			 пример: "4.12"
   * - **$tax_id**
     - *int*
     - 
     - ID на данъчна група от номенклатурата им ( виж: :doc:`../methods/taxgroups/getlist` )
   * - **$detail_notes**
     - *string*
     - 
     - Свободен текст - Може да съдържа някакви допълнително описание към конкретния `артикул </barsy.help/210-dictionary/article.html>`__
   * - **$details**
     - *FormFieldInputData*
     - 
     - Детайли към `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "[{\"field_name_1\":{\"value\":123,\"title\":\"test\"}},{\"field_name_2\":{\"value\":999,\"title\":\"test\"}}]" ( виж: :doc:`../methods/articles/get` , :doc:`../methods/forms/get` )
   * - **$detail_status**
     - *int*
     - 1
     - 
   * - **$discount**
     - *float*
     - 0
     - Отстъпка на ниво ред/`артикул </barsy.help/210-dictionary/article.html>`__
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
	 * :doc:`../methods/clientorders/create`
	 * :doc:`../methods/clientorders/update`

