.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

CardInstanceData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Cards\\Data\\CardInstanceData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$card_instance_id**
     - 
     - 
     - ID на карта/`ваучер </barsy.help/210-dictionary/card.html>`__
   * - **$num**
     - *int*
     - 
     - Номер на карта
   * - **$card_name**
     - *string*
     - 
     - Заглавие на типа карта/`ваучер </barsy.help/210-dictionary/card.html>`__/бонус програма ( виж: :doc:`../methods/cards/getlist` )
   * - **$card_id**
     - 
     - 
     - ID на тип на карта ( виж: :doc:`../methods/cards/getlist` )
   * - **$client_id**
     - *int*
     - 
     - ID на `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/clients/getlist` )
   * - **$client_name**
     - *string*
     - 
     - Име на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$person_id**
     - *int*
     - 
     - ID на `представител </barsy.help/210-dictionary/person.html>`__ на `клиент </barsy.help/210-dictionary/client.html>`__ ( виж: :doc:`../methods/persons/getlist` )
   * - **$person_name**
     - *string*
     - 
     - Име на `представител </barsy.help/210-dictionary/person.html>`__ на `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$discount**
     - *int*
     - 
     - Процент отстъпка, която дава картата
   * - **$av_sum**
     - *float*
     - 
     - Оставаща сума във валута спрямо типът на картата
   * - **$credit_used**
     - *float*
     - 
     - Използвани кредити
   * - **$credit_left**
     - *float*
     - 
     - Оставащи кредити
   * - **$credit_left_curr**
     - *float*
     - 
     - Оставащи кредити във вторична валута, ако има настроена такава
   * - **$used_count**
     - *int*
     - 
     - Брой използвания
   * - **$used_left**
     - *int*
     - 
     - Оставащи брой използвания
   * - **$valid_from**
     - *string*
     - 
     - Валидна от

			 пример: "\"2025-01-01\""
   * - **$valid_to**
     - *string*
     - 
     - Валидна до

			 пример: "\"2029-01-01\""
   * - **$period_limit_interval_end**
     - *string*
     - 
     - Край на периода
   * - **$period_limit_num_left**
     - *int*
     - 
     - Брой оставащи използвания за периода
   * - **$period_limit_sum_left**
     - *float*
     - 
     - Оставащ лимит до края на периода
   * - **$period_limit_sum_left_curr**
     - *float*
     - 
     - Оставащ лимит до края на периода във вторична валута, ако има настроена такава
   * - **$activated**
     - *int*
     - 
     - Дали картата е активна в момента
   * - **$expired**
     - *int*
     - 
     - Дали картата е изтекла
   * - **$reusable**
     - *int*
     - 
     - Дали картата може да бъде преизползвана (заредена, след като е изтекла)
   * - **$delete_flag**
     - *int*
     - 
     - Дали картата е изтрита
   * - **$article_id**
     - *int*
     - 
     - ID на `артикул </barsy.help/210-dictionary/article.html>`__, асоциран с тази карта ( виж: :doc:`../methods/articles/get` )
   * - **$depot_id**
     - *int*
     - 
     - 
   * - **$stream_id**
     - *int*
     - 
     - 
   * - **$tax**
     - *int*
     - 
     - 
   * - **$tax_id**
     - *int*
     - 
     - 
   * - **$articles_price_type**
     - *int*
     - 0
     - 
   * - **$client_check**
     - *int*
     - 0
     - Флаг дали картата изисква `сметката </barsy.help/210-dictionary/account.html>`__ и картата да са на един и същи `клиент </barsy.help/210-dictionary/client.html>`__
   * - **$price_round_type**
     - *int*
     - 0
     - 
   * - **$coefficient**
     - *float*
     - 1
     - 
   * - **$unlimited_flag**
     - *int*
     - 
     - Флаг показваш дали лимитът на картата е неограничен

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/cards/instances_getlist`
	 * :doc:`../methods/cards/instances_get`

