.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Messages_create
===========================================================
Запис на съобщение

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Създава или редактира съобщение до `потребители </barsy.help/210-dictionary/user.html>`__ на системата — вътрешна комуникация между служители, обявления от мениджъра, инструкции за персонала. Чрез `action_type` се избира дали съобщението да бъде запазено като чернова (`save_draft`) или директно изпратено (`save`). Получателите се определят чрез данните в `values` — конкретни `потребители </barsy.help/210-dictionary/user.html>`__, `роли </barsy.help/210-dictionary/role.html>`__, обекти.

*Типични случаи: обявление "От утре нова промоция" до целия персонал, лична задача към конкретен служител, мениджърски инструкции до екипа на смяна, автоматизирани известия от workflow.*

**Име**: Messages_create
**Категория**: Misc


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$id**
     - *int*
     - ID на съобщението
   * - **$values**
     - MessagesCreateInputData_ 
     - 
   * - **$action_type**
     - *string*
     - Изпращане или запис като чернова [save_draft,save] **По подразбиране:** 'save'


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*int*                                                                  ID на създаденото съобщение
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

MessagesCreateInputData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: MessagesCreateInputData

   * - Параметър
     - Тип
     - Описание
   * - **$recipients**
     - *array*
     - Списък с получатели подадени като имена разделени със запейтака, или като масив от имена, или като масив от ID-та **По подразбиране:** []
   * - **$subject**
     - *string*
     - Тема на съобщението
   * - **$text**
     - *string*
     - Съдържание на съобщението
   * - **$msg_type**
     - *int*
     - Тип на съобщението **По подразбиране:** 5
   * - **$send_date**
     - *string*
     - Дата за отложено изпращане
   * - **$parent_id**
     - *int*
     - ID на съобщение, на което това съобщение отговаря

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

     .. literalinclude:: ../../sources/messages_create/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/messages_create/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/messages_create/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/messages_create/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/messages_create/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/messages_create/barsy_api_client_simple.php
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

