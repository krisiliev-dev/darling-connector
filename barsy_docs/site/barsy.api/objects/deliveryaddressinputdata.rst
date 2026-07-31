.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

DeliveryAddressInputData
======================================================================================
Данни за начина и локация на доставка

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\DeliveryAddress\\Data\\DeliveryAddressInputData


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

			 пример: "\"address\""
   * - **$country_id**
     - *string*
     - 
     - ID на държава (двубуквен код, напр. "BG").

			*При подаден country_id системата го валидира срещу b_countries и попълва country_name. Приоритет: country_id > country_name.* ( виж: :doc:`../methods/destinations/getlistcountries` )
   * - **$country_name**
     - *string*
     - 
     - Алтернатива на country_id — наименование на държавата (напр. "България").

			*Използва се само ако country_id НЕ е подаден. При намиране — попълва country_id автоматично. Ако не бъде намерена — не е грешка: стойността се записва в адреса както е подадена, но без country_id.  Приоритет: country_id > country_name.*
   * - **$dest_id**
     - *int*
     - 
     - ID на населено място от номенклатурата на Barsy.

			*При подаден dest_id системата го валидира срещу b_destinations и попълва dest_name_full; невалиден dest_id е грешка. Ако разполагате с ID по номенклатурата на куриер — подайте го в speditor_dest_id, не тук.  Приоритет при резолвиране: speditor_dest_id > dest_id > dest_name_full.*

			 пример: "1" ( виж: :doc:`../methods/destinations/getlist` )
   * - **$dest_name_full**
     - *string*
     - 
     - Алтернатива на dest_id — пълно наименование на населено място (напр. "гр. София").

			*Използва се само ако dest_id НЕ е подаден. Системата търси в следния ред: точно съвпадение по DEST_NAME, после LIKE по DEST_NAME, после точно съвпадение по DEST_NAME_FULL_TEXT, накрая LIKE по DEST_NAME_FULL_TEXT — при намиране попълва dest_id автоматично. Частично съвпадение се приема само ако е еднозначно (един кандидат). Ако не бъде намерено — не е грешка: стойността се записва в адреса както е подадена, но без dest_id.  Приоритет: dest_id > dest_name_full.*
   * - **$speditor_dest_id**
     - *int*
     - 
     - ID на населено място по номенклатурата на куриера (НЕ е Barsy DEST_ID).

			*Използва се когато куриерът подава своя city_id (напр. от собствен checkout widget или API). Изисква едновременно подаден speditor_id (или намерим speditor_name) — без разпознат куриер се хвърля грешка. Системата маппира speditor_dest_id към Barsy dest_id чрез таблица b_destination_speditors (SPEDITOR_REF_ID → DEST_ID); при липсващ mapping — грешка. При намиране — попълва dest_id и dest_name_full автоматично. Не се записва в базата — служи само за резолвиране.  Приоритет: speditor_dest_id > dest_id > dest_name_full.* ( виж: ``Speditors_GetList за стойността на speditor_id`` )
   * - **$address**
     - *string*
     - 
     - Адрес за доставка (бул/ул)

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
     - ID на `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (ако типа на доставката е "Взимане от `търговски обект </barsy.help/210-dictionary/barsy.html>`__").

			*При подаден barsy_id системата го валидира и попълва barsy_name_address. Приоритет: barsy_id > barsy_name_address.*

			 пример: "1" ( виж: :doc:`../methods/barsys/getlist` )
   * - **$barsy_name_address**
     - *string*
     - 
     - Алтернатива на barsy_id — наименование на `търговски обект </barsy.help/210-dictionary/barsy.html>`__.

			*Използва се само ако barsy_id НЕ е подаден. Търси се първо по PUBLIC_NAME, след това по NAME (само сред неизтритите обекти). При намиране — попълва barsy_id, а тук се записва вътрешното NAME на обекта (PUBLIC_NAME служи само за търсене). Ако не бъде намерен — не е грешка: стойността се записва в адреса както е подадена, но без barsy_id.  Приоритет: barsy_id > barsy_name_address.*
   * - **$speditor_id**
     - *int*
     - 
     - ID на спедитор (ако типа на доставката е "Доставка с куриер").

			*При подаден speditor_id системата го валидира и попълва speditor_name. Приоритет: speditor_id > speditor_name.* ( виж: :doc:`../methods/speditors/getlist` )
   * - **$speditor_name**
     - *string*
     - 
     - Алтернатива на speditor_id — наименование на куриера (напр. "Спиди").

			*Използва се само ако speditor_id НЕ е подаден. Търси се по точно съответствие (case-insensitive) само сред активните куриери. При намиране — попълва speditor_id автоматично. Ако не бъде намерен — не е грешка: стойността се записва в адреса както е подадена, но без speditor_id (освен ако е подаден и speditor_dest_id — тогава е грешка).  Приоритет: speditor_id > speditor_name.*
   * - **$office_id**
     - *int*
     - 
     - ID на офис на куриер по номенклатурата на съответния куриер ( виж: :doc:`../methods/speditors/getofficelist` )
   * - **$office_type**
     - *string*
     - 
     - 
   * - **$zip**
     - *string*
     - 
     - Пощенски код

			 пример: "1234"
   * - **$coords**
     - *string*
     - 
     - Координати на адреса
   * - **$description**
     - *string*
     - 
     - Допълнителна информация към адреса за доставка

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/accounts/createfromclientorder`
	 * :doc:`../methods/accounts/create`
	 * :doc:`../methods/accounts/place`
	 * :doc:`../methods/clientorders/create`
	 * :doc:`../methods/clientorders/update`
	 * :doc:`../methods/clients/create`
	 * :doc:`../methods/clients/update`
	 * :doc:`../methods/reservations/create`
	 * :doc:`../methods/reservations/update`

