.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

DocumentData
======================================================================================
Данни за един документ (оферта, договор, протокол, гаранция и др.)

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Documents\\Data\\DocumentData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$document_id**
     - *int*
     - 
     - ID на документа
   * - **$doc_type_id**
     - *int*
     - 
     - ID на типа документ ( виж: :doc:`../methods/documents/gettypes` )
   * - **$doc_type_name**
     - *string*
     - 
     - Системно име на типа документ
   * - **$barsy_id**
     - *int*
     - 
     - ID на търговския обект.

			При `extra_properties.barsy_id` ( виж: :doc:`../methods/barsys/getlist` )
   * - **$user_id**
     - *int*
     - 
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа ( виж: :doc:`../methods/users/getlist` )
   * - **$user_name**
     - *string*
     - 
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа
   * - **$create_date**
     - *string*
     - 
     - Дата на създаване
   * - **$ref_date**
     - *string*
     - 
     - Вальор (дата на документа)
   * - **$update_date**
     - *string*
     - 
     - Дата на последна промяна
   * - **$text**
     - *string*
     - 
     - Текст или шаблон на документа.

			При `extra_properties.text`
   * - **$status_id**
     - *int*
     - 
     - ID на статуса на документа
   * - **$status_name**
     - *string*
     - 
     - Име на статуса на документа
   * - **$is_template**
     - *int*
     - 
     - Флаг дали записът е шаблон (0 или 1)
   * - **$document_name**
     - *string*
     - 
     - Име на документа
   * - **$document_sid**
     - *string*
     - 
     - SID на документа.

			При `extra_properties.document_sid`
   * - **$client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__.

			При `extra_properties.client_id` ( виж: :doc:`../methods/clients/getlist` )
   * - **$client_name**
     - *string*
     - 
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__.

			При `extra_properties.client_name`
   * - **$description**
     - *string*
     - 
     - Бележки към документа.

			При `extra_properties.description`
   * - **$parent_id**
     - *int*
     - 
     - ID на родителски документ.

			При `extra_properties.parent_id` ( виж: :doc:`../methods/documents/get` )
   * - **$document_options**
     - *string*
     - 
     - Допълнителни опции на документа.

			При `extra_properties.document_options`
   * - **$owner_id**
     - *int*
     - 
     - ID на отговорника.

			При `extra_properties.owner_id` ( виж: :doc:`../methods/users/getlist` )
   * - **$owner_name**
     - *string*
     - 
     - Име на отговорника.

			При `extra_properties.owner_name`
   * - **$delete_flag**
     - *int*
     - 
     - Флаг дали документът е изтрит (0 или 1)
   * - **$doc_num**
     - *string*
     - 
     - Номер на документа.

			При `extra_properties.doc_num`
   * - **$deal_id**
     - *int*
     - 
     - ID на сделка.

			При `extra_properties.deal_id` ( виж: :doc:`../methods/deals/getlist` )
   * - **$deal_title**
     - *string*
     - 
     - Заглавие на сделката.

			При `extra_properties.deal_title`
   * - **$email**
     - *string*
     - 
     - Имейл на `клиента </barsy.help/210-dictionary/client.html>`__.

			При `extra_properties.email`
   * - **$currency_id**
     - *int*
     - 
     - ID на валутата на документа.

			При `extra_properties.currency_id`
   * - **$currency_rate**
     - *float*
     - 
     - Курс на валутата на документа.

			При `extra_properties.currency_rate`
   * - **$template_ref_id**
     - *int*
     - 
     - ID на шаблона, от който е създаден документът.

			При `extra_properties.template_ref_id` ( виж: :doc:`../methods/documents/get` )
   * - **$lines_count**
     - *int*
     - 
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в документа.

			При `extra_properties.lines_count`
   * - **$total_amount**
     - *float*
     - 
     - Обща сума на редовете без документна отстъпка.

			При `extra_properties.total_amount`
   * - **$total_with_discount**
     - *float*
     - 
     - Обща сума след документна отстъпка или надценка.

			При `extra_properties.total_with_discount`
   * - **$resolution_status**
     - *int*
     - 
     - Резултат на `оферта </barsy.help/210-dictionary/offer.html>`__: 0=няма, 1=приета, 2=отхвърлена, 3=преработена.

			При `extra_properties.resolution_status`
   * - **$send_date**
     - *string*
     - 
     - Дата на изпращане на `оферта </barsy.help/210-dictionary/offer.html>`__.

			При `extra_properties.send_date`
   * - **$call_date**
     - *string*
     - 
     - Дата на прозвъняване на `оферта </barsy.help/210-dictionary/offer.html>`__.

			При `extra_properties.call_date`
   * - **$discount**
     - *float*
     - 
     - Отстъпка или надценка на документа в %.

			При `extra_properties.discount` или при преглед на един документ
   * - **$caparo**
     - *float*
     - 
     - Предплащане в %.

			При `extra_properties.caparo` или при преглед на един документ
   * - **$caparo_fixed**
     - *float*
     - 
     - Капаро във валута.

			При `extra_properties.caparo_fixed` или при преглед на един документ

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/documents/getlist`
	 * :doc:`../methods/documents/get`

Виж също
--------

 * `Оферта </barsy.help/210-dictionary/offer.html>`__

