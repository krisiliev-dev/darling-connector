.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PaymentMethodsListFiltersData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Paymentmethods\\Data\\PaymentMethodsListFiltersData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$return_mode**
     - *int*
     - 2
     - 

			 пример: "1"
   * - **$paymethod_id**
     - *int*
     - 
     - Филтър по ID на начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "3"
   * - **$barsy_id**
     - *int*
     - 
     - Филтър по `търговски обект </barsy.help/210-dictionary/barsy.html>`__

			 пример: "0"
   * - **$role_id**
     - *int*
     - 
     - Филтър по `роля </barsy.help/210-dictionary/role.html>`__

			 пример: "0"
   * - **$is_public**
     - *int*
     - 
     - Филтър по публичност на начин на `плащане </barsy.help/210-dictionary/payment.html>`__ - филтира начини на `плащане </barsy.help/210-dictionary/payment.html>`__ разрешени за текущия публичен достъп, ако има такъв

			 пример: "1"
   * - **$delete_flag**
     - *int*
     - 0
     - Филтър дали е изтрит начин на `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "0"
   * - **$type_id**
     - *int*
     - 
     - Филтър по Тип

			 пример: "1"
   * - **$has_provider**
     - *int*
     - 
     - 

			 пример: "1"
   * - **$provider_name**
     - *string*
     - 
     - Филтрира по служебно име на външна система

			 пример: "\"borica_vpos\""
   * - **$show_in_invoice**
     - *int*
     - 
     - Филтър по "дали начина на `плащане </barsy.help/210-dictionary/payment.html>`__ се показва във `фактура </barsy.help/210-dictionary/invoice.html>`__"

			 пример: "1"
   * - **$storno_enable**
     - *int*
     - 
     - Филтър по флаг за възможност за задаване на сторно `плащане </barsy.help/210-dictionary/payment.html>`__

			 пример: "1"
   * - **$country_id**
     - *int*
     - 
     - Филтър по страна на доставка

			 пример: "\"BG\""
   * - **$currency_id**
     - *int*
     - 
     - Филтър по страна на доставка

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/paymentmethods/getlist`

