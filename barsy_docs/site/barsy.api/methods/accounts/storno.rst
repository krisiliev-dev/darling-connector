.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Accounts_storno
===========================================================
Сторно на сметка

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/account </barsy.help/210-dictionary/account.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Създава сторно (анулираща) `сметка </barsy.help/210-dictionary/account.html>`__ спрямо съществуваща приключена `сметка </barsy.help/210-dictionary/account.html>`__. Подадените `article_ids` посочват кои `артикули </barsy.help/210-dictionary/article.html>`__ да се сторнират — ако списъкът е празен, сторнира се цялата `сметка </barsy.help/210-dictionary/account.html>`__. Подадените `payments` указват кои плащания да се възстановят на `клиента </barsy.help/210-dictionary/client.html>`__; празен списък означава пълно връщане. Изисква се валидна причина за сторно (виж `Accounts_getstornoreasons`), която се изпраща към фискалното устройство съгласно регулаторните изисквания. Сторно `сметката </barsy.help/210-dictionary/account.html>`__ получава собствен УНП и фискална бележка-сторно.

Типични случаи: връщане на покупка от `клиент </barsy.help/210-dictionary/client.html>`__ в магазин, отказ от част от поръчка след приготвянето й, корекция на грешно издадена бележка, оперативна грешка от касиер. Сторно операцията е необратима.

**Име**: Accounts_storno
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
   * - **$account_id**
     - *int*
     - Номер на `сметката </barsy.help/210-dictionary/account.html>`__ от която ще се сторнира
   * - **$article_ids**
     - *array*
     - Списък от `артикул </barsy.help/210-dictionary/article.html>`__ ID-та, които да бъдат сторнирани.

			Ако не се подаде, всички `артикули </barsy.help/210-dictionary/article.html>`__ се сторнират. **По подразбиране:** []
   * - **$payments**
     - *array*
     - Списък от плащания, които да бъдат възстановени на `клиента </barsy.help/210-dictionary/client.html>`__ след сторнирането.

			*Ако не се подаде, счита се че всичко е върнато.* **По подразбиране:** []
   * - **$storno_data**
     - InputStornoData_ 
     - Данни за сторно бележката


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  Номер на сторниращата сметка
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

InputStornoData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: InputStornoData

   * - Параметър
     - Тип
     - Описание
   * - **$storno_reason**
     - *string*
     - Причина за сторното

			* **return** - *Връщане / рекламация*
			* **mistake** - *Операторска грешка*
			* **reduction_tax_base** - *Намаление на данъчната основа* ( виж: :doc:`../accounts/getstornoreasons` )
   * - **$unp**
     - *string*
     - УНП на сторнираната бележка
   * - **$receipt_num**
     - *string*
     - Номер на сторнираната бележка
   * - **$receipt_date**
     - *string*
     - Дата на сторнираната бележка
   * - **$fm_num**
     - *string*
     - Номер на фискална памет на сторнираната бележка

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

     .. literalinclude:: ../../sources/accounts_storno/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/accounts_storno/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/accounts_storno/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/accounts_storno/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/accounts_storno/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/accounts_storno/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

