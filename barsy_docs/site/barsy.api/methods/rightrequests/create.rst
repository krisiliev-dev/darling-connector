.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Rightrequests_create
===========================================================
Подаване на заявка за права

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Създава заявка, с която текущият `потребител </barsy.help/210-dictionary/user.html>`__ изисква изброените права. Заявката се записва със статус „чакаща" и подлежи на одобрение/отхвърляне от вишестоящ `потребител </barsy.help/210-dictionary/user.html>`__, който може да управлява права. При подаване вишестоящите (с `роля </barsy.help/210-dictionary/role.html>`__-родител на заявителя) получават имейл уведомление.

Типични случаи: `потребител </barsy.help/210-dictionary/user.html>`__ няма дадено право и го заявява от екрана „Заявка за права" в профила си; заявка директно от съобщението за липсващо право (бутон „Заяви право").

**Име**: Rightrequests_create
**Категория**: Users


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$request**
     - RightRequestInputData_ 
     - Данни за заявката — заявени права (api_action) и причина


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
RightRequestCreateResultData_                                          Идентификатор на създадената заявка
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

RightRequestInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Входни данни за заявка на права.

.. list-table::
   :header-rows: 1
   :align: center
   :name: RightRequestInputData

   * - Параметър
     - Тип
     - Описание
   * - **$api_actions**
     - *string*
     - Списък с правата, които се заявяват — по уникалния идентификатор на правото (api_action). **По подразбиране:** []
   * - **$reason**
     - *string*
     - Незадължителна причина/обосновка за заявката.

-----

RightRequestCreateResultData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Резултат от подаване на заявка за права.

.. list-table::
   :header-rows: 1
   :align: center
   :name: RightRequestCreateResultData

   * - Параметър
     - Тип
     - Описание
   * - **$request_id**
     - *int*
     - Идентификатор на създадената заявка.
   * - **$skipped_rights**
     - *string*
     - Имена на права, които са били пропуснати, защото вече имат чакаща заявка. **По подразбиране:** []
   * - **$review_url**
     - *string*
     - Директен линк към диалога за преглед на заявката. Същият линк се праща и по имейл

			*на вишестоящите — заявителят може да го копира и изпрати ръчно.*

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

     .. literalinclude:: ../../sources/rightrequests_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/rightrequests_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/rightrequests_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/rightrequests_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/rightrequests_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/rightrequests_create/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

