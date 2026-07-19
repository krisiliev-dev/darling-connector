.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

OrdersListExtraPropertiesData
======================================================================================
Опции за допълнителни данни към всяка поръчка в списъка (Orders_getlist).

.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------
Всяко свойство е булев флаг — при `true` поръчката се обогатява със съответната допълнителна информация (данни за `сметката </barsy.help/210-dictionary/account.html>`__/`клиента </barsy.help/210-dictionary/client.html>`__, финансови показатели за анализ на `продажби </barsy.help/210-dictionary/sale.html>`__, `модификатори </barsy.help/210-dictionary/modificator.html>`__, групови атрибути, изходи/output екрани).

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Orders\\Data\\OrdersListExtraPropertiesData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - 
     - 
     - 
     - 
   * - :category_header:`Свързани обекти`
     - 
     - 
     - 
   * - **$account_data**
     - *bool*
     - false
     - Данни за `сметката </barsy.help/210-dictionary/account.html>`__ (вальор, отстъпка, `клиент </barsy.help/210-dictionary/client.html>`__)

			 пример: "1"
   * - **$client_data**
     - *bool*
     - false
     - Данни за `клиента </barsy.help/210-dictionary/client.html>`__

			 пример: "1"
   * - **$category**
     - *bool*
     - false
     - `Категории </barsy.help/210-dictionary/category.html>`__ на `артикула </barsy.help/210-dictionary/article.html>`__

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Артикул`
     - 
     - 
     - 
   * - **$modificators**
     - *bool*
     - false
     - Данни за `модификаторите </barsy.help/210-dictionary/modificator.html>`__

			 пример: "1"
   * - **$article_attributes**
     - *bool*
     - false
     - Данни за груповите атрибути

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Изход`
     - 
     - 
     - 
   * - **$outputs**
     - *bool*
     - false
     - Данни за насочването на поръчката

			Към кои `каси </barsy.help/210-dictionary/pos.html>`__ и `потоци </barsy.help/210-dictionary/flow.html>`__ е насочена поръчката.

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Финансови данни`
     - 
     - 
     - 
   * - **$discount**
     - *bool*
     - false
     - Отстъпка на реда в проценти

			 пример: "1"
   * - **$tax**
     - *bool*
     - false
     - ДДС данни на реда

			*Ставка, ДДС група, данъчен код и данъчен регион.*

			 пример: "1"
   * - **$line_total**
     - *bool*
     - false
     - Сума на реда

			Количество по единична цена с приспадната отстъпка на `сметката </barsy.help/210-dictionary/account.html>`__ — брутни `продажби </barsy.help/210-dictionary/sale.html>`__ на реда.

			 пример: "1"
   * - **$base_price**
     - *bool*
     - false
     - Базова цена преди `ценовите правила </barsy.help/210-dictionary/pricelist.html>`__

			*за анализ на отстъпки/маржове*

			 пример: "1"
   * - **$original_price**
     - *bool*
     - false
     - Първоначална единична цена преди корекции

			 пример: "1"
   * - **$pricelist**
     - *bool*
     - false
     - ID на ценоразписа, по който е продаден редът

			 пример: "1"
   * - 
     - 
     - 
     - 
   * - :category_header:`Състояние`
     - 
     - 
     - 
   * - **$reason**
     - *bool*
     - false
     - Причина за реда (`продажба </barsy.help/210-dictionary/sale.html>`__/връщане/сторно/авансово `плащане </barsy.help/210-dictionary/payment.html>`__)

			 пример: "1"
   * - **$storno**
     - *bool*
     - false
     - Дали редът е сторниран

			 пример: "1"

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/orders/getlist`

