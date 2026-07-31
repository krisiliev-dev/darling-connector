.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CompaniesListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към фирма от списъка с фирми. Всяка опция включва съответната колона към

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
*данните за всеки запис. Основните данни се връщат винаги, останалите при стойност true.*

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Companies\\Data\\CompaniesListExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$company_id**
     - *bool*
     - true
     - ID на `фирмата </barsy.help/210-dictionary/company.html>`__ ( виж: :doc:`../methods/companies/get` )
   * - **$name**
     - *bool*
     - true
     - Показвано име (популярно име или официално, ако популярното липсва)
   * - **$pop_name**
     - *bool*
     - true
     - Популярно име на `фирмата </barsy.help/210-dictionary/company.html>`__
   * - **$company_name**
     - *bool*
     - true
     - Официално име на `фирмата </barsy.help/210-dictionary/company.html>`__ по регистрация
   * - **$bulstat**
     - *bool*
     - true
     - ЕИК/БУЛСТАТ
   * - **$vat_num**
     - *bool*
     - true
     - ДДС номер
   * - **$mol**
     - *bool*
     - true
     - МОЛ
   * - **$address**
     - *bool*
     - true
     - Адрес по регистрация
   * - **$town**
     - *bool*
     - true
     - Град по регистрация
   * - **$zip**
     - *bool*
     - true
     - Пощенски код
   * - **$contact_name**
     - *bool*
     - true
     - Лице за контакти
   * - **$phone**
     - *bool*
     - true
     - Телефон
   * - **$fax**
     - *bool*
     - true
     - Факс
   * - **$email**
     - *bool*
     - true
     - Основен имейл
   * - **$email_invoices**
     - *bool*
     - true
     - Имейл за `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$min_inv_num**
     - *bool*
     - true
     - Стартов номер на `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$inv_additional_text**
     - *bool*
     - true
     - Допълнителен текст за `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$email_offers**
     - *bool*
     - true
     - Имейл за `оферти </barsy.help/210-dictionary/offer.html>`__
   * - **$delete_flag**
     - *bool*
     - true
     - Флаг за изтрита `фирма </barsy.help/210-dictionary/company.html>`__
   * - **$office_address**
     - *bool*
     - true
     - Адрес за контакт
   * - **$inv_default_dds_reason**
     - *bool*
     - true
     - Текст основание за `фактури </barsy.help/210-dictionary/invoice.html>`__ при нулева ставка
   * - **$identity_num**
     - *bool*
     - true
     - ЕИК/БУЛСТАТ (идентификационен номер)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/companies/getlist`

Виж също
--------

 * `Фирма </barsy.help/210-dictionary/company.html>`__

