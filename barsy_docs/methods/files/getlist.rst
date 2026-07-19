.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Files_getlist
===========================================================
Списък с файлове

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с прикачените файлове към конкретен обект (`артикул </barsy.help/210-dictionary/article.html>`__, `клиент </barsy.help/210-dictionary/client.html>`__, `представител </barsy.help/210-dictionary/person.html>`__, складово `зареждане </barsy.help/210-dictionary/storeload.html>`__). Параметрите `obj_type`, `obj_id`, `obj_property` дефинират към кой обект и негово свойство принадлежат файловете. Чрез `extra_properties` могат да се поискат допълнителни мета-данни — размери за изображения, брой страници за PDF, кеш статистика.

Типични случаи: показване на галерия с изображения на `артикул </barsy.help/210-dictionary/article.html>`__, листинг на прикачени документи към складово `зареждане </barsy.help/210-dictionary/storeload.html>`__, проверка дали обект има прикачени файлове преди ново качване.

**Име**: Files_getlist
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
   * - **$obj_type**
     - *string*
     - Обект, към който са закачени файловете

			* **articles** - `Артикули </barsy.help/210-dictionary/article.html>`__
			* **users** - `Потребители </barsy.help/210-dictionary/user.html>`__
			* **clients** - `Клиенти </barsy.help/210-dictionary/client.html>`__
			* **store_loads** - *Зареждания*
			* **persons** - `Представители </barsy.help/210-dictionary/person.html>`__
			* **details** - *Характеристики*
   * - **$obj_id**
     - *string*
     - ID на съответния обект
   * - **$obj_property**
     - *string*
     - Под тип файлове към съответния обект

			* **PICTURE** - *Файлове* **По подразбиране:** 'PICTURE'
   * - **$extra_properties**
     - *array*
     - Допълнителна информация

			* **image_size** - *Размери на файлът (широчина и височина), ако е от тип изображение*
			* **pdf_pages** - *Брой страници на pdf-файл* **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
FileData_                                                              Списък от налични файлове към съответния обект и група
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

FileData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: FileData

   * - Параметър
     - Тип
     - Описание
   * - **$name**
     - *string*
     - Име на файла
   * - **$size**
     - *integer*
     - Размер на файла в байтове
   * - **$type**
     - *string*
     - MIME тип на файла
   * - **$last_modified**
     - *string*
     - Дата на последна модификация на файла
   * - **$url**
     - *string*
     - URL за изтегляне на файла
   * - **$thumbnail_url**
     - *string*
     - URL за преглед на файла
   * - **$delete_url**
     - *string*
     - URL за изтриване на файла
   * - **$delete_cache_url**
     - *string*
     - URL за изтриване на кеша на файла
   * - **$content**
     - *string*
     - 
   * - **$cache_files_count**
     - *int*
     - 
   * - **$alt_files**
     - *array*
     - 
   * - **$width**
     - *int*
     - Ширина на файла ако е картинка (jpeg, jpg, png)
   * - **$height**
     - *int*
     - Височина на файла ако е картинка (jpeg, jpg, png)
   * - **$number_pages**
     - *int*
     - Брой страници (pdf)
   * - **$media_duration**
     - *string*
     - Продължителност на медиата (video, audio) - форматирано

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

     .. literalinclude:: ../../sources/files_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/files_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/files_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/files_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/files_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/files_getlist/barsy_api_client_simple.php
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

