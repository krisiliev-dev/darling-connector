.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Companies_get
===========================================================
Подробни данни за фирма

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/company </barsy.help/210-dictionary/company.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща пълен запис за една `фирма </barsy.help/210-dictionary/company.html>`__ по нейното ID — популярно и официално име, ЕИК/БУЛСТАТ, ДДС номер, МОЛ, адрес по регистрация, данни за контакт (телефон, факс, имейли), настройки за фактуриране (стартов номер на `фактури </barsy.help/210-dictionary/invoice.html>`__, допълнителен текст, основание за нулева ставка) и флаг за изтрита `фирма </barsy.help/210-dictionary/company.html>`__. Изтрити `фирми </barsy.help/210-dictionary/company.html>`__ не се връщат — при опит за достъп се връща грешка.

Типични случаи: `зареждане </barsy.help/210-dictionary/storeload.html>`__ на данните на `фирма </barsy.help/210-dictionary/company.html>`__-продавач при издаване на `фактура </barsy.help/210-dictionary/invoice.html>`__, синхронизация на фирмени реквизити към счетоводна система, преглед на `фирма </barsy.help/210-dictionary/company.html>`__ в админ панела.

**Име**: Companies_get
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
   * - **$company_id**
     - *int*
     - ID на `фирмата </barsy.help/210-dictionary/company.html>`__


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
CompanyData_                                                           
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

CompanyData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CompanyData

   * - Параметър
     - Тип
     - Описание
   * - **$company_id**
     - *int*
     - ID на `фирмата </barsy.help/210-dictionary/company.html>`__ ( виж: :doc:`../companies/get` )
   * - **$name**
     - *string*
     - Показвано име (популярно име или официално, ако популярното липсва)
   * - **$pop_name**
     - *string*
     - Популярно име на `фирмата </barsy.help/210-dictionary/company.html>`__
   * - **$company_name**
     - *string*
     - Официално име на `фирмата </barsy.help/210-dictionary/company.html>`__ по регистрация
   * - **$bulstat**
     - *string*
     - ЕИК/БУЛСТАТ
   * - **$vat_num**
     - *string*
     - ДДС номер
   * - **$mol**
     - *string*
     - МОЛ
   * - **$address**
     - *string*
     - Адрес по регистрация
   * - **$town**
     - *string*
     - Град по регистрация
   * - **$zip**
     - *string*
     - Пощенски код
   * - **$contact_name**
     - *string*
     - Лице за контакти
   * - **$phone**
     - *string*
     - Телефон
   * - **$fax**
     - *string*
     - Факс
   * - **$email**
     - *string*
     - Основен имейл
   * - **$email_invoices**
     - *string*
     - Имейл за `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$min_inv_num**
     - *string*
     - Стартов номер на `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$inv_additional_text**
     - *string*
     - Допълнителен текст за `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$email_offers**
     - *string*
     - Имейл за `оферти </barsy.help/210-dictionary/offer.html>`__
   * - **$delete_flag**
     - *int*
     - Флаг за изтрита `фирма </barsy.help/210-dictionary/company.html>`__
   * - **$office_address**
     - *string*
     - Адрес за контакт
   * - **$inv_default_dds_reason**
     - *int*
     - Текст основание за `фактури </barsy.help/210-dictionary/invoice.html>`__ при нулева ставка
   * - **$identity_num**
     - *string*
     - ЕИК/БУЛСТАТ (идентификационен номер)

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

     .. literalinclude:: ../../sources/companies_get/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/companies_get/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/companies_get/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/companies_get/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/companies_get/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/companies_get/barsy_api_client_simple.php
     .. code-block:: bash


Виж също
--------

 * `Фирма </barsy.help/210-dictionary/company.html>`__


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

