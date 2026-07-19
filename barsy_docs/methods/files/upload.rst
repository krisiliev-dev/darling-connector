.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Files_upload
===========================================================
Качване на файлове

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Многофункционален endpoint за работа с прикачени файлове на обекти в системата (`артикули </barsy.help/210-dictionary/article.html>`__, `клиенти </barsy.help/210-dictionary/client.html>`__, `представители </barsy.help/210-dictionary/person.html>`__, `потребители </barsy.help/210-dictionary/user.html>`__, складови зареждания). Според HTTP метода обработва различни операции: `POST` — качване на нови файлове; `GET` — извличане на списък със съществуващи файлове за обекта с опционални допълнителни данни (размер, страници в PDF, кеш статистика). Качените файлове трябва да имат валидно файлово разширение.

Типични случаи: качване на изображение на `артикул </barsy.help/210-dictionary/article.html>`__ от админ панела, прикачване на сканирана `фактура </barsy.help/210-dictionary/invoice.html>`__ към складово `зареждане </barsy.help/210-dictionary/storeload.html>`__, добавяне на профилна снимка от мобилно приложение, импорт на договори за `клиент </barsy.help/210-dictionary/client.html>`__.

**Име**: Files_upload
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
   * - **$files**
     - *array*
     - Масив от файлове за качване
   * - **$obj_type**
     - *string*
     - Тип обект, за който се качва (articles,clients,persons,users,storeloads)
   * - **$obj_id**
     - *string*
     - ID на обекта, за който се качва
   * - **$obj_property**
     - *string*
     - Подтип на обекта, за който се качва (PICTURE)
   * - **$extra_properties**
     - *array*
     - При GET заявака, може да се върнат допълнителни данни за файловете.

			*Възможни са: image_size, pdf_pages, cache_files_count* **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
*array*                                                                Масив от данни за всеки файл
====================================================================== ======================================================================

----
 
Примери
-------
.. raw:: html

  <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
  <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

*BarsyAPI може да бъде достъпено по различни начини - чрез директен HTTP рекуест или чрез помощния BarsyApiClinet. В отделните табове са демонстрирани различните варианти*

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy и предефинирани помощни класове. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/files_upload/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/files_upload/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/files_upload/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/files_upload/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/files_upload/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/files_upload/barsy_api_client_simple.php
     .. code-block:: bash


.. include:: /_includes/more_examples.txt


Необходими права
----------------

За използването на този метод, потребителя трябва да има поне едно от следните права:

 * 
 * 
 * 
 * 
 * 


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

