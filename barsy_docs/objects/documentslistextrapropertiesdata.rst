.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

DocumentsListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към документ. Всяка опция включва съответната колона към данните за

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*всеки запис. Основните данни (base) се връщат винаги, останалите при стойност true.*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Documents\\Data\\DocumentsListExtraPropertiesData


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
   * - **$document_id**
     - *bool*
     - true
     - ID на документа
   * - **$doc_type_id**
     - *bool*
     - true
     - ID на типа документ ( виж: :doc:`../methods/documents/gettypes` )
   * - **$doc_type_name**
     - *bool*
     - true
     - Системно име на типа документ
   * - **$create_date**
     - *bool*
     - true
     - Дата на създаване
   * - **$update_date**
     - *bool*
     - true
     - Дата на последна промяна
   * - **$ref_date**
     - *bool*
     - true
     - Вальор (дата на документа)
   * - **$status_id**
     - *bool*
     - true
     - ID на статуса на документа
   * - **$status_name**
     - *bool*
     - true
     - Име на статуса на документа
   * - **$is_template**
     - *bool*
     - true
     - Флаг дали записът е шаблон
   * - **$document_name**
     - *bool*
     - true
     - Име на документа
   * - **$document_sid**
     - *bool*
     - false
     - SID на документа
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$barsy_id**
     - *bool*
     - false
     - ID на търговския обект

			 пример: "1" ( виж: :doc:`../methods/barsys/get` , :doc:`../methods/barsys/getlist` )
   * - **$user_id**
     - *bool*
     - true
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа ( виж: :doc:`../methods/users/get` , :doc:`../methods/users/getlist` )
   * - **$user_name**
     - *bool*
     - true
     - Име на `потребителя </barsy.help/210-dictionary/user.html>`__, създал документа
   * - **$client_id**
     - *bool*
     - false
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1" ( виж: :doc:`../methods/clients/get` , :doc:`../methods/clients/getlist` )
   * - **$client_name**
     - *bool*
     - false
     - Име на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$email**
     - *bool*
     - false
     - Имейл на `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$parent_id**
     - *bool*
     - false
     - ID на родителски документ ( виж: :doc:`../methods/documents/get` )
   * - **$owner_id**
     - *bool*
     - false
     - ID на отговорника ( виж: :doc:`../methods/users/get` , :doc:`../methods/users/getlist` )
   * - **$owner_name**
     - *bool*
     - false
     - Име на отговорника
   * - **$deal_id**
     - *bool*
     - false
     - ID на сделка ( виж: :doc:`../methods/deals/getlist` )
   * - **$deal_title**
     - *bool*
     - false
     - Заглавие на сделката
   * - **$currency_id**
     - *bool*
     - false
     - ID на валутата на документа ( виж: :doc:`../methods/currencies/getlist` )
   * - **$currency_rate**
     - *bool*
     - false
     - Курс на валутата на документа
   * - **$template_ref_id**
     - *bool*
     - false
     - ID на шаблона, от който е създаден документът ( виж: :doc:`../methods/documents/get` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Допълнителни`
     - 
     - 
     - 
   * - **$text**
     - *bool*
     - false
     - Текст/шаблон на документа
   * - **$description**
     - *bool*
     - false
     - Бележки към документа
   * - **$document_options**
     - *bool*
     - false
     - Допълнителни опции на документа

			*Връща структурираните данни с допълнителни опции на документа.*
   * - **$delete_flag**
     - *bool*
     - true
     - Флаг дали документът е изтрит
   * - **$doc_num**
     - *bool*
     - false
     - Номер на документа
   * - **$lines_count**
     - *bool*
     - false
     - Брой `артикули </barsy.help/210-dictionary/article.html>`__ в документа
   * - **$resolution_status**
     - *bool*
     - false
     - Резултат на `оферта </barsy.help/210-dictionary/offer.html>`__

			*Възможни стойности: 0=няма, 1=приета, 2=отхвърлена, 3=преработена.*
   * - **$send_date**
     - *bool*
     - false
     - Дата на изпращане на `оферта </barsy.help/210-dictionary/offer.html>`__
   * - **$call_date**
     - *bool*
     - false
     - Дата на прозвъняване на `оферта </barsy.help/210-dictionary/offer.html>`__
   * - **$parse_document_options**
     - *bool*
     - false
     - Разпада опциите на документа в отделни полета

			Връща опциите на документа (отстъпка, капаро, дати на `оферта </barsy.help/210-dictionary/offer.html>`__ и др.) като отделни полета в отговора.
   * - 
     - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
     - 
   * - **$total_amount**
     - *bool*
     - false
     - Обща сума на редовете (без документна отстъпка)
   * - **$total_with_discount**
     - *bool*
     - false
     - Обща сума след документна отстъпка/надценка
   * - **$discount**
     - *bool*
     - false
     - Отстъпка или надценка на документа в %
   * - **$caparo**
     - *bool*
     - false
     - Предплащане в %
   * - **$caparo_fixed**
     - *bool*
     - false
     - Капаро във валута

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/documents/getlist`

