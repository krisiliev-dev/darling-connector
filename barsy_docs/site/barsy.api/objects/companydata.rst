.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CompanyData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Companies\\Data\\CompanyData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$company_id**
     - *int*
     - 
     - ID на `фирмата </barsy.help/210-dictionary/company.html>`__ ( виж: :doc:`../methods/companies/get` )
   * - **$name**
     - *string*
     - 
     - Показвано име (популярно име или официално, ако популярното липсва)
   * - **$pop_name**
     - *string*
     - 
     - Популярно име на `фирмата </barsy.help/210-dictionary/company.html>`__
   * - **$company_name**
     - *string*
     - 
     - Официално име на `фирмата </barsy.help/210-dictionary/company.html>`__ по регистрация
   * - **$bulstat**
     - *string*
     - 
     - ЕИК/БУЛСТАТ
   * - **$vat_num**
     - *string*
     - 
     - ДДС номер
   * - **$mol**
     - *string*
     - 
     - МОЛ
   * - **$address**
     - *string*
     - 
     - Адрес по регистрация
   * - **$town**
     - *string*
     - 
     - Град по регистрация
   * - **$zip**
     - *string*
     - 
     - Пощенски код
   * - **$contact_name**
     - *string*
     - 
     - Лице за контакти
   * - **$phone**
     - *string*
     - 
     - Телефон
   * - **$fax**
     - *string*
     - 
     - Факс
   * - **$email**
     - *string*
     - 
     - Основен имейл
   * - **$email_invoices**
     - *string*
     - 
     - Имейл за `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$min_inv_num**
     - *string*
     - 
     - Стартов номер на `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$inv_additional_text**
     - *string*
     - 
     - Допълнителен текст за `фактури </barsy.help/210-dictionary/invoice.html>`__
   * - **$email_offers**
     - *string*
     - 
     - Имейл за `оферти </barsy.help/210-dictionary/offer.html>`__
   * - **$delete_flag**
     - *int*
     - 
     - Флаг за изтрита `фирма </barsy.help/210-dictionary/company.html>`__
   * - **$office_address**
     - *string*
     - 
     - Адрес за контакт
   * - **$inv_default_dds_reason**
     - *int*
     - 
     - Текст основание за `фактури </barsy.help/210-dictionary/invoice.html>`__ при нулева ставка
   * - **$identity_num**
     - *string*
     - 
     - ЕИК/БУЛСТАТ (идентификационен номер)

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/companies/getlist`
	 * :doc:`../methods/companies/get`

