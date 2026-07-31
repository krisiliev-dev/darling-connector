.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Poses_register
===========================================================
Регистрация на каса

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/pos </barsy.help/210-dictionary/pos.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Регистрира конкретно физическо устройство като POS `каса </barsy.help/210-dictionary/pos.html>`__ в системата и връща уникален криптографски ключ (`poskey`) и публичен ключ на сървъра за изграждане на сигурна комуникация. След успешна регистрация устройството може да изпраща API заявки автономно без интерактивен потребителски вход. Сесията на регистрационния `потребител </barsy.help/210-dictionary/user.html>`__ се прекратява автоматично — `касата </barsy.help/210-dictionary/pos.html>`__ вече работи със своя ключ.

*Типични случаи: първоначална настройка на нов POS терминал, преинсталация след хардуерен срив, регистрация на мобилно касово приложение, конфигуриране на kiosk терминал.*

**Име**: Poses_register
**Категория**: Settings


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :align: center
   :name: main_params

   * - Параметър
     - Тип
     - Описание
   * - **$pos_id**
     - *int*
     - ID на желаната `каса </barsy.help/210-dictionary/pos.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
PosRegisterResponseData_                                               Ключ за оторизиране
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

PosRegisterResponseData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: PosRegisterResponseData

   * - Параметър
     - Тип
     - Описание
   * - **$poskey**
     - *string*
     - 
   * - **$barsy_public_key**
     - *string*
     - 
   * - **$has_cdx**
     - *bool*
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

     .. literalinclude:: ../../sources/poses_register/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/poses_register/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/poses_register/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/poses_register/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/poses_register/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/poses_register/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Каса </barsy.help/210-dictionary/pos.html>`__


.. include:: /_includes/more_examples.txt


.. note:: Нещо не е наред?

  Ако изпитвате трудност или проблем при работа с Barsy API, изпробвайте следните варианти:

   * Прочетете :doc:`/integrations/index`
   * Разгледайте :doc:`/faq/index`
   * Пишете ни на *helpme at lukanet dot com*

