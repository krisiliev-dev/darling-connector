.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Pricelists_edit
===========================================================
Запис на ценово правило

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pricelist </barsy.help/210-dictionary/pricelist.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Създава ново или редактира съществуващо `ценово правило </barsy.help/210-dictionary/pricelist.html>`__ — основни данни (име, тип, група, тежест/приоритет, описание), времеви рамки (период от/до дати, дни от седмицата, часови интервали), правила за изчисляване (тип `модификатор </barsy.help/210-dictionary/modificator.html>`__ — процентна отстъпка/надценка, фиксирана сума, замяна с конкретна цена; стойност или прагова таблица; режим с/без ДДС; закръгляне). Според типа на правилото се добавят и специфични полета — например бонус карта за лоялна програма или групи за Mix-and-Match промоции.

Типични случаи: създаване на сезонна промоция "Happy Hour 18-20ч", дефиниране на VIP отстъпка от 10% за лоялна програма, специална цена за корпоративни `клиенти </barsy.help/210-dictionary/client.html>`__, диференциране на ДДС за доставки в различни региони.

**Име**: Pricelists_edit
**Категория**: Catalog


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$action_type**
     - *string*
     - Тип на върнатите данни [content=структура,values=стойности,save=запис,delete=изтриване] **По подразбиране:** 'content'
   * - **$id**
     - *int*
     - ID на обекта, който се обработва

			`Ценово правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$values**
     - *array*
     - Стойности за запис (при $action_type=save)
   * - **$active_struct_id**
     - *int*
     - ID на активната структура


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PricelistsEditResultData_                                              
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PricelistsEditFilters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Филтри на списъка

-----

PricelistsEditResultRowData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Данни за резултата

.. list-table::
   :header-rows: 1
   :align: center
   :name: PricelistsEditResultRowData

   * - Параметър
     - Тип
     - Описание
   * - **$pricelist_id**
     - *int*
     - Служебен идентификатор на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$pricelist_name**
     - *string*
     - Име на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$pricelist_type_id**
     - *string*
     - Тип на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$pricelist_group_id**
     - *string*
     - Група, към която принадлежи `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$pricelist_desc**
     - *string*
     - Вътрешно описание на `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__
   * - **$weight**
     - *int*
     - Тежест за подреждане на `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__, когато се застъпват. По малка цифра, по-голяма важност **По подразбиране:** 3
   * - **$delete_flag**
     - *string*
     - Архивира `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__ и спира прилагането му
   * - **$card_id**
     - *string*
     - *Бонус карта, към която е свързано правилото*
   * - **$periods_date**
     - *string*
     - Задава периоди от дата до дата за които `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__ е в действие.                                 Може да бъде един период или няколко отделени на нов ред.                                 Датите могат да са от две последователни години                                 Формат:                                 1.1-1.3                                 15.10-17.10                                 23.12-15.1
   * - **$periods_weekdays**
     - *string*
     - *Може да бъде един или няколко дни*
   * - **$periods_time**
     - *string*
     - Задава часовите периоди, в които `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__ е в действие.                                 Може да бъде един или няколко периода.Периодите се отделят с нов ред.                                 Формат:                                 15:00-16:00                                  22:05-22:59
   * - **$begin_price_type**
     - *string*
     - *Цена, върху която се изчислява правилото*
   * - **$price_tax_mode**
     - *string*
     - Дали изчислената цена от `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__ да има включено ДДС или не **По подразбиране:** 1
   * - **$price_tax_id**
     - *string*
     - *ДДС група, която се използва при изчисляване на цената*
   * - **$modificator_type**
     - *string*
     - *Начин, по който правилото променя цената*
   * - **$modificator_value**
     - *int*
     - Числова стойност на ценовия `модификатор </barsy.help/210-dictionary/modificator.html>`__. Може и да е множествена, като тогава се определят прагове в лева или в единици, когато типа е Цена-`артикул </barsy.help/210-dictionary/article.html>`__
   * - **$modificator_round_type**
     - *string*
     - *Начин на закръгляне на изчислената цена*
   * - **$price_change_groups**
     - *string*
     - Избиране на групи `артикули </barsy.help/210-dictionary/article.html>`__, на чиято цена да влияе `ценовото правило </barsy.help/210-dictionary/pricelist.html>`__. Използва се в промоции от тип "Mix-and-Match" **По подразбиране:** 1
   * - **$total_period**
     - *string*
     - *Период на оборота, върху който се прилага правилото*
   * - **$price_type**
     - *string*
     - *Вид продажна цена, която се използва при изчисляване*

-----

PricelistsEditResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PricelistsEditResultData

   * - Параметър
     - Тип
     - Описание
   * - **$page_num**
     - *int*
     - Номер на текуща страница
   * - **$total**
     - *int*
     - Общ брой страници
   * - **$records**
     - *int*
     - Общ брой записи
   * - **$rows**
     - PricelistsEditResultRowData_ []
     - Полета на всеки ред от списъка
   * - **$totals**
     - 
     - 
   * - **$filters_resume**
     - *array*
     - 

-----

Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/pricelists_edit/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/pricelists_edit/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/pricelists_edit/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/pricelists_edit/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/pricelists_edit/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/pricelists_edit/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Ценово правило </barsy.help/210-dictionary/pricelist.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

