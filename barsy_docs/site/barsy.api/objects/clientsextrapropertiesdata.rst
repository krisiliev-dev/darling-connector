.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

ClientsExtraPropertiesData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Clients\\Data\\ClientsExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$client_code**
     - *bool*
     - false
     - Ако е подадено, се връща самия код на картата, ако `потребителя </barsy.help/210-dictionary/user.html>`__ има право да редактира `представители </barsy.help/210-dictionary/person.html>`__
   * - **$used_delivery_addresses**
     - *bool*
     - false
     - Добавя се списък от вече използваните адреси за доставка от този `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$default_person_name**
     - *bool*
     - false
     - Добавя се информация име на `представител </barsy.help/210-dictionary/person.html>`__ по подразбиране

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/clients/get`

