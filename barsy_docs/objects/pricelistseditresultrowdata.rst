.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

PricelistsEditResultRowData
======================================================================================
Данни за резултата

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Pricelists\\Data\\PricelistsEditResultRowData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$pricelist_id**
     - *int*
     - 
     - Служебен идентификатор на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$pricelist_name**
     - *string*
     - 
     - Име на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$pricelist_type_id**
     - *string*
     - 
     - Тип на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__

			 пример: "1"
   * - **$pricelist_group_id**
     - *string*
     - 
     - Група, към която принадлежи `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__

			 пример: "1"
   * - **$pricelist_desc**
     - *string*
     - 
     - Вътрешно описание на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$weight**
     - *int*
     - 3
     - Тежест за подреждане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, когато се застъпват. По малка цифра, по-голяма важност
   * - **$delete_flag**
     - *string*
     - 
     - Архивира `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__ и спира прилагането му
   * - **$card_id**
     - *string*
     - 
     - *Бонус карта, към която е свързано правилото*
   * - **$periods_date**
     - *string*
     - 
     - Задава периоди от дата до дата за които `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__ е в действие.                                 Може да бъде един период или няколко отделени на нов ред.                                 Датите могат да са от две последователни години                                 Формат:                                 1.1-1.3                                 15.10-17.10                                 23.12-15.1
   * - **$periods_weekdays**
     - *string*
     - 
     - *Може да бъде един или няколко дни*

			 пример: "1"
   * - **$periods_time**
     - *string*
     - 
     - Задава часовите периоди, в които `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__ е в действие.                                 Може да бъде един или няколко периода.Периодите се отделят с нов ред.                                 Формат:                                 15:00-16:00                                  22:05-22:59
   * - **$begin_price_type**
     - *string*
     - 
     - *Цена, върху която се изчислява правилото*

			 пример: "1"
   * - **$price_tax_mode**
     - *string*
     - 1
     - Дали изчислената цена от `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__ да има включено ДДС или не
   * - **$price_tax_id**
     - *string*
     - 
     - *ДДС група, която се използва при изчисляване на цената*

			 пример: "2"
   * - **$modificator_type**
     - *string*
     - 
     - *Начин, по който правилото променя цената*

			 пример: "1"
   * - **$modificator_value**
     - *int*
     - 
     - Числова стойност на ценовия `модификатор </barsy.help/210-dictionary/modificator.html>`__. Може и да е множествена, като тогава се определят прагове в лева или в единици, когато типа е Цена-`артикул </barsy.help/210-dictionary/article.html>`__
   * - **$modificator_round_type**
     - *string*
     - 
     - *Начин на закръгляне на изчислената цена*

			 пример: "0"
   * - **$price_change_groups**
     - *string*
     - 1
     - Избиране на групи `артикули </barsy.help/210-dictionary/article.html>`__, на чиято цена да влияе `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__. Използва се в промоции от тип "Mix-and-Match"

			 пример: "1"
   * - **$total_period**
     - *string*
     - 
     - *Период на оборота, върху който се прилага правилото*

			 пример: "\"current\""
   * - **$price_type**
     - *string*
     - 
     - *Вид продажна цена, която се използва при изчисляване*

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/pricelists/edit`

