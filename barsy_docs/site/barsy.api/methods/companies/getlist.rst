.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

Companies_getlist
===========================================================
Списък с фирми

.. sidebar:: Допълнителна информация за тази операция

	 * barsy.help: `210-dictionary/company </barsy.help/210-dictionary/company.html>`__

------

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Връща списък с `фирмите </barsy.help/210-dictionary/company.html>`__, конфигурирани в системата — популярно и официално име, ЕИК/БУЛСТАТ, ДДС номер, МОЛ, адрес, данни за контакт и настройки за фактуриране. По подразбиране връща само активни (неизтрити) `фирми </barsy.help/210-dictionary/company.html>`__. Поддържа филтри по име и флаг за изтрита `фирма </barsy.help/210-dictionary/company.html>`__, странициране и подреждане.

Типични случаи: попълване на dropdown при избор на `фирма </barsy.help/210-dictionary/company.html>`__-продавач, синхронизация на фирмени реквизити към счетоводна система, листинг на `фирмите </barsy.help/210-dictionary/company.html>`__ в админ панела.

**Име**: Companies_getlist
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
   * - **$filters**
     - CompaniesListFiltersData_ 
     - Налични филтри за списъка с `фирми </barsy.help/210-dictionary/company.html>`__
   * - **$extra_properties**
     - CompaniesListExtraPropertiesData_ 
     - Искане на допълнителни данни за всяка `фирма </barsy.help/210-dictionary/company.html>`__
   * - **$offset**
     - *int*
     - Номер на ред, от който да започне списъкът (странициране) **По подразбиране:** 0
   * - **$length**
     - *int*
     - Брой върнати редове в една заявка **По подразбиране:** 10000
   * - **$order_by**
     - *array*
     - Подреждане — асоциативен масив колона⇒посока (напр. {"pop_name":"asc"}) **По подразбиране:** []


Резултат:
^^^^^^^^^^

====================================================================== ======================================================================
CompanyData_                                                           Списък с фирми с данни според исканите ($extra_properties)
====================================================================== ======================================================================

----
 
Помощни обекти
--------------

*Описание на всички помощни обекти (входни и изходни), използвани в този метод*

CompaniesListFiltersData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

.. list-table::
   :header-rows: 1
   :align: center
   :name: CompaniesListFiltersData

   * - Параметър
     - Тип
     - Описание
   * - **$company_id**
     - *int*
     - Филтър по ID на `фирма </barsy.help/210-dictionary/company.html>`__ ( виж: :doc:`../companies/get` )
   * - **$company_name**
     - *string*
     - Филтър по име на `фирма </barsy.help/210-dictionary/company.html>`__.

			*Намира и при частично съвпадение*
   * - **$delete_flag**
     - *int*
     - Филтър по флаг за изтрита `фирма </barsy.help/210-dictionary/company.html>`__.

			*Стойност -1 премахва филтъра* **По подразбиране:** 0

-----

CompaniesListExtraPropertiesData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	Опции за допълнителни данни към `фирма </barsy.help/210-dictionary/company.html>`__ от списъка с `фирми </barsy.help/210-dictionary/company.html>`__. Всяка опция включва съответната колона към
		*данните за всеки запис. Основните данни се връщат винаги, останалите при стойност true.*

.. list-table::
   :header-rows: 1
   :align: center
   :name: CompaniesListExtraPropertiesData

   * - Параметър
     - Тип
     - Описание
   * - **$company_id**
     - *bool*
     - ID на `фирмата </barsy.help/210-dictionary/company.html>`__ ( виж: :doc:`../companies/get` ) **По подразбиране:** true
   * - **$name**
     - *bool*
     - Показвано име (популярно име или официално, ако популярното липсва) **По подразбиране:** true
   * - **$pop_name**
     - *bool*
     - Популярно име на `фирмата </barsy.help/210-dictionary/company.html>`__ **По подразбиране:** true
   * - **$company_name**
     - *bool*
     - Официално име на `фирмата </barsy.help/210-dictionary/company.html>`__ по регистрация **По подразбиране:** true
   * - **$bulstat**
     - *bool*
     - ЕИК/БУЛСТАТ **По подразбиране:** true
   * - **$vat_num**
     - *bool*
     - ДДС номер **По подразбиране:** true
   * - **$mol**
     - *bool*
     - МОЛ **По подразбиране:** true
   * - **$address**
     - *bool*
     - Адрес по регистрация **По подразбиране:** true
   * - **$town**
     - *bool*
     - Град по регистрация **По подразбиране:** true
   * - **$zip**
     - *bool*
     - Пощенски код **По подразбиране:** true
   * - **$contact_name**
     - *bool*
     - Лице за контакти **По подразбиране:** true
   * - **$phone**
     - *bool*
     - Телефон **По подразбиране:** true
   * - **$fax**
     - *bool*
     - Факс **По подразбиране:** true
   * - **$email**
     - *bool*
     - Основен имейл **По подразбиране:** true
   * - **$email_invoices**
     - *bool*
     - Имейл за `фактури </barsy.help/210-dictionary/invoice.html>`__ **По подразбиране:** true
   * - **$min_inv_num**
     - *bool*
     - Стартов номер на `фактури </barsy.help/210-dictionary/invoice.html>`__ **По подразбиране:** true
   * - **$inv_additional_text**
     - *bool*
     - Допълнителен текст за `фактури </barsy.help/210-dictionary/invoice.html>`__ **По подразбиране:** true
   * - **$email_offers**
     - *bool*
     - Имейл за `оферти </barsy.help/210-dictionary/offer.html>`__ **По подразбиране:** true
   * - **$delete_flag**
     - *bool*
     - Флаг за изтрита `фирма </barsy.help/210-dictionary/company.html>`__ **По подразбиране:** true
   * - **$office_address**
     - *bool*
     - Адрес за контакт **По подразбиране:** true
   * - **$inv_default_dds_reason**
     - *bool*
     - Текст основание за `фактури </barsy.help/210-dictionary/invoice.html>`__ при нулева ставка **По подразбиране:** true
   * - **$identity_num**
     - *bool*
     - ЕИК/БУЛСТАТ (идентификационен номер) **По подразбиране:** true

-----

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

     .. literalinclude:: ../../sources/companies_getlist/barsy_api_client.php
       :language: php
       :linenos:

  .. tab:: JSON

     Примерът съдържа данните в JSON стринг, който трябва да бъде изпратен към входящата API точка (примерно https://demo.barsyonline.com/endpoints/json/?bid=1)

     .. literalinclude:: ../../sources/companies_getlist/json.json
       :language: json
       :linenos:

  .. tab:: CURL

     .. literalinclude:: ../../sources/companies_getlist/curl.txt
       :language: bash
       :linenos:

  .. tab:: CURL + JSON

     .. literalinclude:: ../../sources/companies_getlist/curl_json.txt
       :language: bash
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

     .. literalinclude:: ../../sources/companies_getlist/http.txt
       :language: bash
       :linenos:

  .. tab:: BarsyApiClient (опростен вариант)

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../../sources/companies_getlist/barsy_api_client_simple.php
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

