.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

DeliveryAddressData
======================================================================================
Съдържа всички данни за адреса на клиент

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\DeliveryAddress\\Data\\DeliveryAddressData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$delivery_type**
     - *string*
     - 'no'
     - Тип на доставката

			* **no** - *Без доставка*
			* **home** - *За вкъщи*
			* **address** - *Доставка до адрес*
			* **barsy** - Получаване от `търговски обект </barsy.help/210-dictionary/barsy.html>`__
			* **office** - *Получаване от офис на куриер*
   * - **$country_name**
     - *string*
     - 
     - Име на държава
   * - **$country_id**
     - *string*
     - 
     - ID на държава
   * - **$dest_id**
     - *int*
     - 
     - ID на населено място

			 пример: "1" ( виж: :doc:`../methods/destinations/getlist` )
   * - **$address**
     - *string*
     - 
     - Адрес за доставка (кв,бул/ул,№,бл,вх,ет)

			 пример: "\"\\u0431\\u0443\\u043b. \\u0411\\u044a\\u043b\\u0433\\u0430\\u0440\\u0438\\u044f \\u21161, \\u0432\\u0445\\u043e\\u0434 \\u0410, \\u0435\\u0442.4\""
   * - **$address_neighborhood**
     - *string*
     - 
     - Квартал на адреса за доставка
   * - **$address_number**
     - *string*
     - 
     - Номер на улица/булевард за доставка
   * - **$address_building**
     - *string*
     - 
     - Блок за доставка
   * - **$address_entry**
     - *string*
     - 
     - Вход на блок за доставка
   * - **$address_floor**
     - *string*
     - 
     - Номер на етаж за доставка
   * - **$address_ap**
     - *string*
     - 
     - Номер на апартамент за доставка
   * - **$barsy_id**
     - *int*
     - 
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (ако типа на доставката е "Взимане от `търговски обект </barsy.help/210-dictionary/barsy.html>`__")

			 пример: "1" ( виж: :doc:`../methods/barsys/getlist` )
   * - **$speditor_id**
     - *int*
     - 
     - ID на спедитор ( виж: :doc:`../methods/speditors/getlist` )
   * - **$office_id**
     - *int*
     - 
     - ID на офис на куриер по номенклатурата на съответния куриер ( виж: :doc:`../methods/speditors/getofficelist` )
   * - **$office_type**
     - *string*
     - 
     - 
   * - **$coords**
     - *string*
     - 
     - Координати на адреса
   * - **$zip**
     - *string*
     - 
     - Пощенски код

			 пример: "1234"
   * - **$description**
     - *string*
     - 
     - Допълнителна информация към адреса за доставка

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/getbytaxes`
	 * :doc:`../methods/accounts/getlist`
	 * :doc:`../methods/accounts/get`
	 * :doc:`../methods/clientorders/create`
	 * :doc:`../methods/clientorders/getlist`
	 * :doc:`../methods/clientorders/get`
	 * :doc:`../methods/clientorders/update`
	 * :doc:`../methods/clients/getlist`
	 * :doc:`../methods/clients/get`
	 * :doc:`../methods/invoices/get_by_sid`
	 * :doc:`../methods/invoices/getlist`
	 * :doc:`../methods/invoices/get`
	 * :doc:`../methods/places/getlistwithaccountsonly`

Виж също
--------

 * `Клиент </barsy.help/210-dictionary/client.html>`__

