Как да сметна правилно общата сума на сметка?
================================================

Тази документация описва как Barsy смята сумата за `плащане </barsy.help/210-dictionary/payment.html>`__ на една `сметка </barsy.help/210-dictionary/account.html>`__.

Формула за изчисление на сума за 1 артикул от сметка
----------------------------------------------------------

.. code:: sql

   row_total = round( ( amount * current_price ) + round( ( amount * current_price ) * ( discount / 100 ), 2 ), 2 )

Където:
 * **row_total** - обща сума на `продажбата </barsy.help/210-dictionary/sale.html>`__
 * **amount** – количество
 * **current_price** – продажна цена
 * **discount** – процентна отстъпка

Формула за изчисление на общата сума на цялата сметка
---------------------------------------------------------

.. code:: sql

   sum( row_total ) + round( ( sum( row_total ) / 100 ) * account_discount, 2 )

Където:
  * **sum(row_total)** – сбор на сумите на всички `артикули </barsy.help/210-dictionary/article.html>`__
  * **account_discount** – процент отстъпка на цялата `сметка </barsy.help/210-dictionary/account.html>`__

Пример
-------

.. list-table::
   :header-rows: 1

   * - `Артикул </barsy.help/210-dictionary/article.html>`__
     - Количество
     - Единична цена
     - Отстъпка (%)
     - Общо след отстъпка
   * - `Артикул </barsy.help/210-dictionary/article.html>`__ 1
     - 2
     - 12.99 лв
     - -50 %
     - 12.99 лв
   * - `Артикул </barsy.help/210-dictionary/article.html>`__ 2
     - 12
     - 18.97 лв
     - -37.38 %
     - 142.55 лв
   * - `Артикул </barsy.help/210-dictionary/article.html>`__ 3
     - 9
     - 0.99 лв
     - 0 %
     - 8.91 лв

Обща сума на `артикулите </barsy.help/210-dictionary/article.html>`__: **164.45** лв

Отстъпка на цялата `сметка </barsy.help/210-dictionary/account.html>`__: **12** %

Крайна сума на `сметката </barsy.help/210-dictionary/account.html>`__: **144.72** лв

Виж също
--------

 * `Сметка </barsy.help/210-dictionary/account.html>`__

