.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articledetails_gettree
===========================================================
Дърво на характеристиките

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/article </barsy.help/210-dictionary/article.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща йерархично дърво от всички дефинирани характеристики (ключове) и техните възможни стойности — например ключ "Цвят" с възможни стойности "Червено/Синьо/Зелено"; ключ "Сезон" с "Пролет/Лято/Есен/Зима". Резултатът се ползва за изграждане на филтри за каталога, dropdown-и при редакция на `артикул </barsy.help/210-dictionary/article.html>`__, мериндж между подобни характеристики.

Типични случаи: изграждане на филтри-faceted search в онлайн магазин, форма за нов `артикул </barsy.help/210-dictionary/article.html>`__ с автокомплийт за съществуващи стойности, маркетингов анализ "колко `артикули </barsy.help/210-dictionary/article.html>`__ имам с дадена характеристика".

**Име**: Articledetails_gettree
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
     - ArticleDetailsListFiltersData_ 
     - Налични филтри за характеристиките в дървото
   * - **$extra_properties**
     - ArticleDetailsTreeExtraPropertiesData_ 
     - Искане на допълнителни данни (възможни стойности)


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ArticleDetailsTreeGroupData_                                           Групите характеристики с принадлежащите им характеристики
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

ArticleDetailsListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailsListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$detail_name**
     - *string*
     - Филтър по име на характеристиката.

			*Намира и при частично съвпадение*
   * - **$menu_id**
     - *int*
     - Филтър дали id на каталог
   * - **$is_service**
     - *int*
     - Филтър дали е услуга **По подразбиране:** 0
   * - **$type**
     - *string*
     - Филтър по тип на характеристиката
   * - **$group_id**
     - *int*
     - Филтър по ID група
   * - **$special_type**
     - *string*
     - Филтър по специален тип ("expiration_days", "master_article")

-----

ArticleDetailsTreeExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към дървото на характеристиките (Articledetails_gettree).
		*Приема и стария формат — списък с имена (напр. ["values"]) — който се превежда към булеви флагове.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailsTreeExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$values**
     - *bool*
     - Да се върнат и възможните стойности на всяка характеристика. При голям брой стойности или

			*характеристика тип "autocomplete" вместо изброени стойности се връща източник за подсказване (data_source).* **По подразбиране:** false

-----

ArticleDetailsTreeGroupData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Една група характеристики в дървото на характеристиките, заедно с принадлежащите ѝ характеристики.

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailsTreeGroupData

   * - Параметър
     - Тип
     - Описание
   * - **$group_name**
     - *string*
     - Име на групата характеристики
   * - **$group_id**
     - *int*
     - ID на групата характеристики
   * - **$details**
     - ArticleDetailsTreeNodeData_ []
     - Характеристиките в групата, индексирани с ключ "k" + ID на характеристиката (напр. "k12")

-----

ArticleDetailsTreeNodeData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Една характеристика (детайл) в дървото на характеристиките.
		Свойствата `values` и `data_source` са взаимно изключващи се и се връщат само когато са поискани възможните стойности (extra_properties "values"): малък набор стойности → `values`; голям набор или характеристика тип "autocomplete" → `data_source` (източник за подсказване).

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailsTreeNodeData

   * - Параметър
     - Тип
     - Описание
   * - **$detail_name**
     - *string*
     - Име на характеристиката
   * - **$type**
     - *string*
     - Тип на въвеждане ("text", "select", "autocomplete", "checkbox", "date", "datetime")
   * - **$parent_id**
     - *int*
     - ID на родителската характеристика (0, ако няма родител)
   * - **$values**
     - *string*
     - Възможни стойности на характеристиката.

			*Връща се само при поискани стойности и малък набор*
   * - **$data_source**
     - eStructDataSourceAction_ 
     - Източник за подсказване на стойности.

			Връща се вместо `values` при голям набор или тип "autocomplete"

-----

eStructDataSourceAction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Изгражда DataSource от подадено име на action. Стойностите се получават чрез викане на екшъна от `клиента </barsy.help/210-dictionary/client.html>`__ (външен рекуест).
		*Екшънът трябва да връща стардартен списък от стойности - масив от обекти с указани filed_key и field_title*

	*Class Lukanet\Lib\eStruct\Services\eStructDataSourceAction*

.. list-table::
   :header-rows: 1
   :align: center
   :name: eStructDataSourceAction

   * - Параметър
     - Тип
     - Описание
   * - **$type**
     - 
     -  **По подразбиране:** 'action'
   * - **$class_name**
     - *string*
     - 
   * - **$extra_fields**
     - *array*
     - 
   * - **$target**
     - 
     - 
   * - **$field_key**
     - 
     -  **По подразбиране:** 'key'
   * - **$field_title**
     - 
     -  **По подразбиране:** 'title'
   * - **$values**
     - 
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

     .. literalinclude:: ../../sources/articledetails_gettree/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articledetails_gettree/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articledetails_gettree/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articledetails_gettree/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articledetails_gettree/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articledetails_gettree/barsy_api_client_simple.php
     .. code-block:: bash


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

