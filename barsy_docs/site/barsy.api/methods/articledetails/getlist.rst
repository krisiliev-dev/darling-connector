.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Articledetails_getlist
===========================================================
Списък с характеристики

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/article </barsy.help/210-dictionary/article.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с дефинираните характеристики (детайли) на `артикулите </barsy.help/210-dictionary/article.html>`__ за текущия каталог — например "Цвят", "Сезон", "Размер" — с тип на въвеждане, група и признаци (множествена, сумируема и др.). Поддържа филтриране (вкл. търсене по име), странициране и подреждане.

Типични случаи: падащо меню/автокомплийт за избор на характеристика при редакция на `артикул </barsy.help/210-dictionary/article.html>`__ или етикет, избор на колона за справка, импорт на `артикули </barsy.help/210-dictionary/article.html>`__ с характеристики.

**Име**: Articledetails_getlist
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
     - Налични филтри за списъка
   * - **$extra_properties**
     - ArticleDetailsListExtraPropertiesData_ 
     - Желани допълнителни колони за всяка характеристика
   * - **$offset**
     - *int*
     - Номер на ред, от който да започне списъкът (странициране) **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - ArticleDetailsListOrderByData_ 
     - Подреждане — низ, масив или обект колона⇒посока (напр. {"detail_name":"asc"})


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
ArticleDetailKeyData_                                                  Списък с характеристики с данни според исканите ($extra_properties)
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

ArticleDetailsListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към характеристика (детайл) от списъка с характеристики. Всяка опция
		*включва съответната колона към данните за всеки запис. Основните данни се връщат винаги, а останалите при стойност true.*

	*Приема и стария формат — списък с имена (напр. ["is_required"]) — който се превежда към булеви флагове.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailsListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$key_id**
     - *bool*
     - ID на характеристиката **По подразбиране:** true
   * - **$detail_name**
     - *bool*
     - Име на характеристиката **По подразбиране:** true
   * - **$type**
     - *bool*
     - Тип на въвеждане на характеристиката (текст, списък, отметка, дата и др.) **По подразбиране:** true
   * - **$group_id**
     - *bool*
     - ID на групата, към която принадлежи характеристиката **По подразбиране:** true
   * - **$parent_id**
     - *bool*
     - ID на родителската характеристика (за каскадни/зависими характеристики) **По подразбиране:** true
   * - **$is_summable**
     - *bool*
     - Дали стойностите на характеристиката могат да се сумират **По подразбиране:** true
   * - **$is_multiple**
     - *bool*
     - Дали характеристиката допуска няколко стойности едновременно **По подразбиране:** true
   * - **$detail_suffix**
     - *bool*
     - Наставка (мерна единица) към стойността на характеристиката **По подразбиране:** false
   * - **$is_service**
     - *bool*
     - Дали характеристиката е служебна (системна) **По подразбиране:** false
   * - **$is_required**
     - *bool*
     - Дали попълването на характеристиката е задължително **По подразбиране:** false
   * - **$detail_weight**
     - *bool*
     - Тежест за подреждане на характеристиката **По подразбиране:** false
   * - **$description**
     - *bool*
     - Описание на характеристиката **По подразбиране:** false
   * - **$detail_is_public**
     - *bool*
     - Дали характеристиката е публична (видима извън системата) **По подразбиране:** false
   * - **$value_type**
     - *bool*
     - Тип на стойността (текст, цяло число, десетична стойност) **По подразбиране:** false
   * - **$values**
     - *bool*
     - Възможните стойности на всяка характеристика (суров списък). Зарежда се допълнително след основната

			*заявка — не е колона* **По подразбиране:** false

-----

ArticleDetailsListOrderByData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Позволените колони за подреждане на списъка с характеристики (Articledetails_getlist).
		Подава се като низ, масив или асоциативен масив колона⇒посока (напр. {"detail_name":"asc"}). Допускат се само изброените по-долу колони, а посоката може да е само `asc` или `desc`.

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailsListOrderByData

   * - Параметър
     - Тип
     - Описание
   * - **$detail_name**
     - *string*
     - Подреждане по име на характеристиката
   * - **$group_id**
     - *string*
     - Подреждане по група
   * - **$key_id**
     - *string*
     - Подреждане по ID на характеристиката

-----

ArticleDetailKeyData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Една характеристика (детайл) от номенклатурата на характеристиките на `артикулите </barsy.help/210-dictionary/article.html>`__.
		*Основните полета се връщат винаги; останалите — само ако са поискани чрез extra_properties.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: ArticleDetailKeyData

   * - Параметър
     - Тип
     - Описание
   * - **$key_id**
     - *int*
     - ID на характеристиката
   * - **$detail_name**
     - *string*
     - Име на характеристиката
   * - **$detail_suffix**
     - *string*
     - Наставка (мерна единица) към стойността на характеристиката
   * - **$type**
     - *string*
     - Тип на въвеждане ("text", "select", "autocomplete", "checkbox", "date", "datetime")
   * - **$group_id**
     - *int*
     - ID на групата, към която принадлежи характеристиката
   * - **$parent_id**
     - *int*
     - ID на родителската характеристика (0, ако няма родител)
   * - **$is_service**
     - *int*
     - Дали характеристиката е служебна (системна)
   * - **$is_required**
     - *bool*
     - Дали попълването на характеристиката е задължително
   * - **$is_multiple**
     - *bool*
     - Дали характеристиката допуска няколко стойности едновременно
   * - **$detail_weight**
     - *int*
     - Тежест за подреждане на характеристиката
   * - **$description**
     - *string*
     - Описание на характеристиката
   * - **$detail_is_public**
     - *bool*
     - Дали характеристиката е публична (видима извън системата)
   * - **$update_article_last_update**
     - *string*
     - Дата на последна промяна, при която `артикулите </barsy.help/210-dictionary/article.html>`__ да се маркират за обновяване
   * - **$is_summable**
     - *bool*
     - Дали стойностите на характеристиката могат да се сумират
   * - **$value_type**
     - *int*
     - Тип на стойността (текст, цяло число, десетична стойност)
   * - **$values**
     - *string*
     - Възможните стойности на характеристиката (суров списък).

			*Връща се само при extra_properties "values"*

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

     .. literalinclude:: ../../sources/articledetails_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/articledetails_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/articledetails_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/articledetails_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/articledetails_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/articledetails_getlist/barsy_api_client_simple.php
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

