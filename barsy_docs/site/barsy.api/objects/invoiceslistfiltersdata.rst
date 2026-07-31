.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

InvoicesListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Invoices\\Data\\InvoicesListFiltersData


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
   * - **$inv_id**
     - *int*
     - 
     - ID на `фактурата </barsy.help/210-dictionary/invoice.html>`__ (различно от номер на `фактурата </barsy.help/210-dictionary/invoice.html>`__)

			 пример: "1"
   * - **$remote_ref_id**
     - *string* | *int*
     - 
     - Номер на `фактурата </barsy.help/210-dictionary/invoice.html>`__ спрямо отдалечената система

			 пример: "1" ( виж: :doc:`../methods/remotesystems/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$client_id**
     - *int*
     - 
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__, чията е `фактурата </barsy.help/210-dictionary/invoice.html>`__

			 пример: "1" ( виж: :doc:`../methods/clients/get` , :doc:`../methods/clients/getlist` )
   * - **$user_id**
     - *int*
     - 
     - ID на `потребителя </barsy.help/210-dictionary/user.html>`__, създал `фактурата </barsy.help/210-dictionary/invoice.html>`__

			 пример: "1" ( виж: :doc:`../methods/users/get` , :doc:`../methods/users/getlist` )
   * - **$barsy_id**
     - *int*
     - 
     - ID на търговският обект

			 пример: "1" ( виж: :doc:`../methods/barsys/get` , :doc:`../methods/barsys/getlist` )
   * - **$remote_id**
     - *int*
     - 
     - ID на отдалечената система. Определя обхвата на данните за обвръзка с отдалечена система —

			*ползва се от опциите за отдалечена система в extra_properties.*

			 пример: "1" ( виж: :doc:`../methods/remotesystems/getlist` )
   * - 
     - 
     - 
     - 
   * - :category_header:`Период и дати`
     - 
     - 
     - 
   * - **$term_date**
     - *datetime*
     - 
     - Срок за `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$create_date**
     - *datetime*
     - 
     - Дата на създаване

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$payment_date**
     - *datetime*
     - 
     - Дата на събитие

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - **$last_update**
     - *datetime*
     - 
     - Дата на последно обновяване на `фактура </barsy.help/210-dictionary/invoice.html>`__

			 пример: "[\"2018-01-01 00:00:00\",\"2018-12-31 23:59:00\"]"
   * - 
     - 
     - 
     - 
   * - :category_header:`Търсене по текст`
     - 
     - 
     - 
   * - **$inv_num**
     - *string*
     - 
     - Номер на `фактура </barsy.help/210-dictionary/invoice.html>`__

			 пример: "\"\\\"0000000006\\\"\""

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/invoices/getlist`

