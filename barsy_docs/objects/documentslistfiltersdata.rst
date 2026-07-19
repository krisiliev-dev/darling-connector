.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

DocumentsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Documents\\Data\\DocumentsListFiltersData


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
   * - **$document_id**
     - *int*
     - 
     - Филтър по ID на документ

			 пример: "1" ( виж: :doc:`../methods/documents/get` )
   * - **$doc_type_id**
     - *int*
     - 
     - Филтър по тип документ

			 пример: "1" ( виж: :doc:`../methods/documents/gettypes` )
   * - **$deal_id**
     - *int*
     - 
     - Филтър по сделка

			 пример: "1" ( виж: :doc:`../methods/deals/getlist` )
   * - **$parent_id**
     - *int*
     - 
     - Филтър по родителски документ (версия/клон)

			 пример: "1" ( виж: :doc:`../methods/documents/get` )
   * - **$template_ref_id**
     - *int*
     - 
     - Филтър по шаблон, от който е създаден документът

			 пример: "1" ( виж: :doc:`../methods/documents/get` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$barsy_id**
     - *int*
     - 
     - Филтър по `търговски обект </barsy.help/210-dictionary/barsy.html>`__

			 пример: "1" ( виж: :doc:`../methods/barsys/get` , :doc:`../methods/barsys/getlist` )
   * - **$user_id**
     - *int*
     - 
     - Филтър по `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа

			 пример: "1" ( виж: :doc:`../methods/users/get` , :doc:`../methods/users/getlist` )
   * - **$owner_id**
     - *int*
     - 
     - Филтър по отговорник на документа

			 пример: "1" ( виж: :doc:`../methods/users/get` , :doc:`../methods/users/getlist` )
   * - **$client_id**
     - *int*
     - 
     - Филтър по `клиент </barsy.help/210-dictionary/client.html>`__

			 пример: "1" ( виж: :doc:`../methods/clients/get` , :doc:`../methods/clients/getlist` )
   * - **$client_group_id**
     - *int* | *int*
     - 
     - Филтър по група на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1" ( виж: :doc:`../methods/clientgroups/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$doc_type_name**
     - *string*
     - 
     - Филтър по системно име на типа документ.

			*Намира и при частично съвпадение*

			 пример: "\"offer\""
   * - **$article_name**
     - *string*
     - 
     - Филтър по име на `артикул </barsy.help/210-dictionary/article.html>`__ в редовете на документа

			 пример: "\"\\u041a\\u0430\\u0444\\u0435\""
   * - **$document_name**
     - *string*
     - 
     - Филтър по име на документа.

			*Намира и при частично съвпадение*

			 пример: "\"\\u041e\\u0444\\u0435\\u0440\\u0442\\u0430\""
   * - **$doc_num**
     - *string*
     - 
     - Филтър по номер на документ.

			*Намира и при частично съвпадение*

			 пример: "1001"
   * - 
     - 
     - 
     - 
   * - :category_header:`Статус и състояние`
     - 
     - 
     - 
   * - **$status_id**
     - *int* | *int*
     - 
     - Филтър по статус на документ (единична стойност или масив за IN)

			 пример: "1"
   * - **$resolution_status**
     - *int* | *int*
     - 
     - Филтър по резултат на `оферта </barsy.help/210-dictionary/offer.html>`__ (0=няма, 1=приета, 2=отхвърлена, 3=преработена)

			 пример: "1"
   * - **$is_template**
     - *int*
     - 
     - Филтър по флаг за шаблон

			 пример: "0"
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър по флаг за изтрит

			 пример: "0"
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$send_date**
     - *datetime*
     - 
     - Филтър по дата на изпращане на `оферта </barsy.help/210-dictionary/offer.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$call_date**
     - *datetime*
     - 
     - Филтър по дата на прозвъняване на `оферта </barsy.help/210-dictionary/offer.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$create_date**
     - *datetime*
     - 
     - Филтър по дата на създаване

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$update_date**
     - *datetime*
     - 
     - Филтър по дата на последна промяна

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$ref_date**
     - *datetime*
     - 
     - Филтър по вальор (дата на документа)

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/documents/getlist`

