.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Modificators_getlist
===========================================================
Списък с модификатори

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `110-admin/100-catalog/modifiers/index </barsy.help/110-admin/100-catalog/modifiers/index.html>`__
	 * barsy.help: `210-dictionary/modificator </barsy.help/210-dictionary/modificator.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с конфигурираните в системата `модификатори </barsy.help/210-dictionary/modificator.html>`__ — кратки текстови указания към поръчки (например "без лук", "леко изпечено", "за вкъщи"), които не влияят на цена/`склад </barsy.help/210-dictionary/store.html>`__, но се отразяват на бележките и кухненските дисплеи. Поддържа филтри (по име, `категория </barsy.help/210-dictionary/category.html>`__), сортиране (азбучен ред, най-нови, най-стари), странициране и `extra_properties` за асоциация с `категории </barsy.help/210-dictionary/category.html>`__.

Типични случаи: попълване на бутонна лента в POS интерфейса с бързи `модификатори </barsy.help/210-dictionary/modificator.html>`__, автокомплийт при въвеждане на специално искане, изграждане на меню за самообслужване с опции "без/с" в kiosk терминал.

**Име**: Modificators_getlist
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
   * - **$filters**
     - ModificatorsListFiltersData_ 
     - 
   * - **$extra_properties**
     - *array*
     - Допълнилтени данни за всеки мофификатор

			* **categories** - Списък с `категории </barsy.help/210-dictionary/category.html>`__, към който е категоризиран всеки мофификатор
			* **articles** - Списък с `артикули </barsy.help/210-dictionary/article.html>`__, към които е закачен всеки `модификатор </barsy.help/210-dictionary/modificator.html>`__ **По подразбиране:** []
   * - **$pattern**
     - *string*
     - @depricated филтрира резултата по подаден стринг
   * - **$order**
     - *int*
     - тип на подреждането на резултатите

			* **1** - *азбучен ред*
			* **2** - *най-новите първи*
			* **3** - *най-старите първи* **По подразбиране:** 1
   * - **$offset**
     - *int*
     - Номер на ред от който да бъде започне списъка.

			*Използва се при странициране, когато трябва да се прескочат Х записа* **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 50


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ModificatorData_                                                       
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ModificatorsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ModificatorsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$modificator_id**
     - *int*
     - Филтър по id на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$user_id**
     - *int*
     - Филтър по id на `потребител </barsy.help/210-dictionary/user.html>`__ (създател)
   * - **$mod_name**
     - *string*
     - Филтър по име на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$create_date**
     - *datetime*
     - Филтър по дата на създаване
   * - **$delete_flag**
     - *int*
     - Филтър по флаг "Изтрит" **По подразбиране:** 0

-----

ModificatorData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ModificatorData

   * - Параметър
     - Тип
     - Описание
   * - **$mod_id**
     - *int*
     - ID на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_name**
     - *string*
     - Име на `модификатор </barsy.help/210-dictionary/modificator.html>`__
   * - **$description**
     - *string*
     - Описание на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$operation**
     - *int*
     - Вид операция ('без' `модификатора </barsy.help/210-dictionary/modificator.html>`__ или 'с' `модификатора </barsy.help/210-dictionary/modificator.html>`__) **По подразбиране:** 0
   * - **$weight**
     - *int*
     - Тежест при подреждане на мофификатори в `категория </barsy.help/210-dictionary/category.html>`__
   * - **$mod_color**
     - *string*
     - Цвят на `модификатора </barsy.help/210-dictionary/modificator.html>`__
   * - **$mod_type**
     - *int*
     - Тип `модификатор </barsy.help/210-dictionary/modificator.html>`__

			* **1** - *Липсва описание*
			* **2** - *Липсва описание*
   * - **$categories**
     - *array*
     - Списък с `категории </barsy.help/210-dictionary/category.html>`__, в които е категоризиран този `модификатор </barsy.help/210-dictionary/modificator.html>`__ ( виж: :doc:`../categories/getlist` ) **По подразбиране:** []

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

     .. literalinclude:: ../../sources/modificators_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/modificators_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/modificators_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/modificators_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/modificators_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/modificators_getlist/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Модификатор </barsy.help/210-dictionary/modificator.html>`__


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

