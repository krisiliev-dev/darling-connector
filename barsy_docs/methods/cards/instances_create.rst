.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Cards_instances_create
===========================================================
Издаване на карта/ваучер

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/card </barsy.help/210-dictionary/card.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Издава нова инстанция (конкретен брой) на предефиниран вид карта/`ваучер </barsy.help/210-dictionary/card.html>`__ — генерира уникален код, асоциира към `клиент </barsy.help/210-dictionary/client.html>`__ (по избор), задава валидност и начален баланс според конфигурацията на вида. Издадената карта става веднага използваема за `плащане </barsy.help/210-dictionary/payment.html>`__ в `касата </barsy.help/210-dictionary/pos.html>`__ (ако е `ваучер </barsy.help/210-dictionary/card.html>`__) или за натрупване на точки (ако е бонус). Инстанциите могат да се разпечатат с QR/баркод за физическа употреба.

Типични случаи: `продажба </barsy.help/210-dictionary/sale.html>`__ на подаръчен `ваучер </barsy.help/210-dictionary/card.html>`__ в магазин, регистрация на нов `клиент </barsy.help/210-dictionary/client.html>`__ в лоялна програма с физическа карта, издаване на корпоративни `ваучери </barsy.help/210-dictionary/card.html>`__ за персонал, конверсия на точки от стара система към нова.

**Име**: Cards_instances_create
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
   * - **$card_data**
     - CardInstanceInputData_ 
     - Основни данни за създаване на инстанция `ваучер </barsy.help/210-dictionary/card.html>`__/карта


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  Id на създадената инстанция на карта
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

CardInstanceInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CardInstanceInputData

   * - Параметър
     - Тип
     - Описание
   * - **$card_id**
     - *int*
     - Тип на картата/`ваучера </barsy.help/210-dictionary/card.html>`__ ( виж: :doc:`../cards/getlist` )
   * - **$num**
     - *string*
     - Номер, по който ще бъде разпознавана картата/`ваучера </barsy.help/210-dictionary/card.html>`__.

			*Ако не е подаден, може да бъде генериран автоматично, според настройките на типа карта*
   * - **$client_id**
     - *int*
     - ID на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../clients/getlist` ) **По подразбиране:** 1
   * - **$person_id**
     - *int*
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ на `клиента </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../persons/getlist` )
   * - **$valid_from**
     - *string*
     - Дата от която картата/`ваучера </barsy.help/210-dictionary/card.html>`__ ще бъде активна за използване
   * - **$valid_to**
     - *string*
     - Дата на която картата/`ваучера </barsy.help/210-dictionary/card.html>`__ ще бъде деактивирана
   * - **$used_left**
     - *int*
     - Оставащи използвания.

			*Ако бъде оставено празно се счита, че няма ограничение.*
   * - **$credit_left**
     - *float*
     - Оставащи кредити за използване.

			*Ако не се попълни се счита, че няма ограничени.*
   * - **$discount**
     - *float*
     - Отстъпка.

			*Използва се за пакетни карти* **По подразбиране:** 0
   * - **$delete_flag**
     - *int*
     - Флаг за изтриване. Ако е зададено на 1, означава, че картата е маркиран като изтрита.

			*Стойност по подразбиране е 0.* **По подразбиране:** 0
   * - **$unlimited_flag**
     - *int*
     - Флаг показваш дали лимитът на картата е неограничен **По подразбиране:** 0

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

     .. literalinclude:: ../../sources/cards_instances_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/cards_instances_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/cards_instances_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/cards_instances_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/cards_instances_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/cards_instances_create/barsy_api_client_simple.php
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

