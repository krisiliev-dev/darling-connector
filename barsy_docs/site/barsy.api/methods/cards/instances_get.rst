.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Cards_instances_get
===========================================================
Преглед на карта/ваучер

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/card </barsy.help/210-dictionary/card.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълни данни за конкретна инстанция на карта/`ваучер </barsy.help/210-dictionary/card.html>`__ — уникален код, тип, асоцииран `клиент </barsy.help/210-dictionary/client.html>`__, текущ баланс (за `ваучери </barsy.help/210-dictionary/card.html>`__ и пакетни карти), валидност, статус (активна/блокирана/изтрита), история на използването. Чрез този endpoint касиерът проверява валидността и баланса преди приемане за `плащане </barsy.help/210-dictionary/payment.html>`__.

Типични случаи: проверка на `ваучер </barsy.help/210-dictionary/card.html>`__ преди приемане за `плащане </barsy.help/210-dictionary/payment.html>`__, преглед на оставащ баланс по пакетна карта в кабинет за козметика, валидиране при онлайн усвояване, изграждане на профил с история на лоялен `клиент </barsy.help/210-dictionary/client.html>`__.

**Име**: Cards_instances_get
**Категория**: Cashdesk


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$card_instance_id**
     - *int*
     - Id на създадената инстанция на карта


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
CardInstanceData_                                                      
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

CardInstanceData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CardInstanceData

   * - Параметър
     - Тип
     - Описание
   * - **$card_instance_id**
     - 
     - ID на карта/`ваучер </barsy.help/210-dictionary/card.html>`__
   * - **$num**
     - *int*
     - Номер на карта
   * - **$card_name**
     - *string*
     - Заглавие на типа карта/`ваучер </barsy.help/210-dictionary/card.html>`__/бонус програма ( виж: :doc:`../cards/getlist` )
   * - **$card_id**
     - 
     - ID на тип на карта ( виж: :doc:`../cards/getlist` )
   * - **$client_id**
     - *int*
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getlist` )
   * - **$client_name**
     - *string*
     - Име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$person_id**
     - *int*
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ на `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../persons/getlist` )
   * - **$person_name**
     - *string*
     - Име на `представител </barsy.help/210-dictionary/person.html>`__ на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$discount**
     - *int*
     - Процент отстъпка, която дава картата
   * - **$av_sum**
     - *float*
     - Оставаща сума във валута спрямо типът на картата
   * - **$credit_used**
     - *float*
     - Използвани кредити
   * - **$credit_left**
     - *float*
     - Оставащи кредити
   * - **$credit_left_curr**
     - *float*
     - Оставащи кредити във вторична валута, ако има настроена такава
   * - **$used_count**
     - *int*
     - Брой използвания
   * - **$used_left**
     - *int*
     - Оставащи брой използвания
   * - **$valid_from**
     - *string*
     - Валидна от
   * - **$valid_to**
     - *string*
     - Валидна до
   * - **$period_limit_interval_end**
     - *string*
     - Край на периода
   * - **$period_limit_num_left**
     - *int*
     - Брой оставащи използвания за периода
   * - **$period_limit_sum_left**
     - *float*
     - Оставащ лимит до края на периода
   * - **$period_limit_sum_left_curr**
     - *float*
     - Оставащ лимит до края на периода във вторична валута, ако има настроена такава
   * - **$activated**
     - *int*
     - Дали картата е активна в момента
   * - **$expired**
     - *int*
     - Дали картата е изтекла
   * - **$reusable**
     - *int*
     - Дали картата може да бъде преизползвана (заредена, след като е изтекла)
   * - **$delete_flag**
     - *int*
     - Дали картата е изтрита
   * - **$article_id**
     - *int*
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, асоциран с тази карта ( виж: :doc:`../articles/get` )
   * - **$depot_id**
     - *int*
     - 
   * - **$stream_id**
     - *int*
     - 
   * - **$tax**
     - *int*
     - 
   * - **$tax_id**
     - *int*
     - 
   * - **$articles_price_type**
     - *int*
     -  **По подразбиране:** 0
   * - **$client_check**
     - *int*
     - Флаг дали картата изисква `сметката </barsy.help/210-dictionary/account.html>`__ и картата да са на един и същи `клиент </barsy.help/210-dictionary/client.html>`__ **По подразбиране:** 0
   * - **$price_round_type**
     - *int*
     -  **По подразбиране:** 0
   * - **$coefficient**
     - *float*
     -  **По подразбиране:** 1
   * - **$unlimited_flag**
     - *int*
     - Флаг показваш дали лимитът на картата е неограничен

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

     .. literalinclude:: ../../sources/cards_instances_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/cards_instances_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/cards_instances_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/cards_instances_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/cards_instances_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/cards_instances_get/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Пакетна карта </barsy.help/210-dictionary/card.html>`__


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

