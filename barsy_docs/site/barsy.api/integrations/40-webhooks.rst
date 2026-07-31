Webhooks
========

Webhook е способ, чрез който в реално време може да получите id-тата на обекти, в които е настъпила промяна.

Абониране
---------

За да се използва функционалността, е нужно да се създаде `абонамент </barsy.help/210-dictionary/subscription.html>`__ за съществуващ `потребител </barsy.help/210-dictionary/user.html>`__.
В `абонамента </barsy.help/210-dictionary/subscription.html>`__ се задават типът на обекта (event_type_id), който ни интересува и url на който да бъдат изпращани промените.

*вижте метода* :doc:`/methods/webhooks/subscribe`

Поддържаните типове обекти са:

================ =============
Обект за данни   event_type_id
================ =============
Артикули         1
Сметки           2
Клиентски заявки 3
Клиенти          4
Поръчки          5
Категории        6
Резервации       7
Модификатори     8
================ =============

*виж списъка с типовете обекти през API* :doc:`/methods/webhooks/event_type_getlist`

За промени се считат следните операции и се отбелязват със следните кодове:

  * Създаване - "C"
  * Редакция - "U"
  * Изтриване - "D"

.. warning::

  * За всеки `потребител </barsy.help/210-dictionary/user.html>`__ може да има по един `абонамент </barsy.help/210-dictionary/subscription.html>`__ за всеки тип събитие.
  * Когато се създава нов `абонамент </barsy.help/210-dictionary/subscription.html>`__, към посочения URL се изпраща тестова заявка (с request type: HEAD). За успешен считаме теста, ако отговорът е с HTTP код: 200–299, 401, 403, 405, 500 или 501.
  * Ако кодът е различен от 2xx, съобщението след абонирането ще бъде придружено с бележка, описваща кода, с който е отговорил вашият сървър.
  * Всички други върнати кодове водят до неуспешно създаване на `абонамента </barsy.help/210-dictionary/subscription.html>`__. В такъв случай ще получите съобщение за неуспеха и придружена грешката, която ВАШИЯТ сървър е върнал.


Верификация
-----------

Като хедъри във всеки изпратен webhook ще получите:

 * X-Signature: = 'sha256=' . hash_hmac('sha256', <тялото на рекуеста>, <secret – създаден след `абонамент </barsy.help/210-dictionary/subscription.html>`__, можете да го вземете с :doc:`/methods/webhooks/get_subscription` >);
 * X-Webhook-ID: = Уникален код на webhook-а, записва се в events – :doc:`/methods/webhooks/get_events`

Ползването на тази информация не е задължително, но благодарение на нея можете да проверите автентичността на webhook-а. Трябва да конструирате по описания начин X-Signature и след това да го сравните с този, който ви изпращаме.

.. note::

  При тестването на URL-а не се изпраща X-Signature (тъй като Secret все още не съществува), така че ако сайтът ви изисква оторизация, най-вероятно ще върне HTTP код 401 (който е сред позволените).


Начин на работа
---------------

* На всяка минута се проверява за променени обекти на база на `абонаментите </barsy.help/210-dictionary/subscription.html>`__. Ако такива бъдат намерени, те биват изпратени на URL-a, който сте посочили в `абонамента </barsy.help/210-dictionary/subscription.html>`__.
* Webhook-a съдържа само типа и id на обекта, както и типа на промяната му.
  НЕ ИЗПРАЩА самия обект или промените по него.
  За да получите тази информация, трябва да я вземете с ваша заявка към съответния обект.
* Ако отсрещната страна (посоченият url) не успее да приеме webhook-a, това се счита за неуспешно събитие и ще бъде направен нов опит за изпращане.
* След всяко следващо неуспешно изпращане времевият диапазон за изпращания се увеличава линейно (1 мин, 2мин, 4 мин, 8 мин...), като максимално ще достигне до 1 час.
* След всяко **петото** неуспешно изпращане `потребителят </barsy.help/210-dictionary/user.html>`__, абониран за събитието, ще получава предупредителен email с:

  * Уведомление, че има проблем с доставната точка на `абонамента </barsy.help/210-dictionary/subscription.html>`__.
  * Грешката, която се е получила.
  * Обобщена информация за данните в webhook-a (`сметки </barsy.help/210-dictionary/account.html>`__ - създадени 2, променени - 10).
  * Самата информация (ако не е твърде обемна).
  * Дата и час на следващия планиран опит за изпращане.

.. warning::

  Ако в следващите 14 дни няма нито едно успешно изпращане, `абонаментът </barsy.help/210-dictionary/subscription.html>`__ бива деактивиран. След това трябва да бъде активиран наново със заявка :doc:`/methods/webhooks/restart`


!!!Данните за променените обекти се натрупват, докато не бъде направено успешно получаване (т.е. отговор с код 200)
Конкретен `потребител </barsy.help/210-dictionary/user.html>`__ може да има по един `абонамент </barsy.help/210-dictionary/subscription.html>`__ за промени във всеки един от типовете обекти.

Формата на изпращаните данни е json, съставен от масив със следната структура:

 * [<тип обект> => [<id на обекта>] => [<буква символизираща извършената операция>]]

Пример
------

Да приемeм, че сме създали два `абонамента </barsy.help/210-dictionary/subscription.html>`__ - за `артикули </barsy.help/210-dictionary/article.html>`__ и за `сметки </barsy.help/210-dictionary/account.html>`__, като информация за прoмените да се получава на адрес: test.webhook.bg
Екшъните за абонирането трябва да изглеждат така:

    * За `артикулите </barsy.help/210-dictionary/article.html>`__ - https://<адрес_на_Вашето_барси>/endpoints/json/Webhooks_subscribe?event_type_id=1&url=test.webhook.bg 
    * За `сметките </barsy.help/210-dictionary/account.html>`__ - https://<адрес_на_Вашето_барси>/endpoints/json/Webhooks_subscribe?event_type_id=2&url=test.webhook.bg

.. note::

  Уточнение - параметрите event_type_id и url могат да бъдат изпратени с POST или с GET, като ако изберете GET метода, **трябва да направите urlencode на параметър url.**

След настъпване на някакви промени в `артикулите </barsy.help/210-dictionary/article.html>`__ или в `сметките </barsy.help/210-dictionary/account.html>`__ Вие ще получите информация на test.webhook.bg в следния формат:

.. code-block:: json
   :name: example_json

   {
      "articles":[
        {
          "101811":"U",
          "102749":"U",
          "102750":"D",
          "102751":"C"
        }
      ]
   }

.. code-block:: json

   {
    "accounts":[
       {
        "190":"U",
        "299":"U",
        "307":"C"
       }
    ]
  }

Тази информация може да бъде разчетена така:

    * В `артикули </barsy.help/210-dictionary/article.html>`__ с ID 101811, 102749 са настъпили промени( били са редактирани). `Артикул </barsy.help/210-dictionary/article.html>`__ 102750 е бил изтрит и имаме новосъздаден `артикул </barsy.help/210-dictionary/article.html>`__ с ID 102751
    * `Сметки </barsy.help/210-dictionary/account.html>`__ 190 и 299 са били променени, а и имаме нова `сметка </barsy.help/210-dictionary/account.html>`__ с ID 307

Ако желаете да получите променените или новосъздадените обекти, можете да ползвате предназначените за целта екшъни:

    * вземане на `артикул </barsy.help/210-dictionary/article.html>`__ - :doc:`/methods/articles/get`
    * вземане на `сметки </barsy.help/210-dictionary/account.html>`__ - :doc:`/methods/accounts/get`
    * вземане на `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__- :doc:`/methods/clientorders/get`
    * вземане на `клиенти </barsy.help/210-dictionary/client.html>`__ - :doc:`/methods/clients/get`
    * вземане на поръчки - :doc:`/methods/orders/getlist`
    * вземане на `категории </barsy.help/210-dictionary/category.html>`__ - :doc:`/methods/categories/get`

Дневник на събития
-------------------

* Всеки опит за изпращане (успешен или не) създава запис, който наричаме "събитие". Може да проверите тези събития с :doc:`/methods/webhooks/get_events` или през административния интерфейс в Настройки » Системни » Webhook събития.
* След всяко събитие има бутон, с който можете да изпратите информацията от събитието отново.

Необходими права
---------------------

При използването на webhooks, в зависимост за какво събитие искате да се абонирате, `потребителят </barsy.help/210-dictionary/user.html>`__ може да се нуждае от различни права. 

Например:
 
 * !!Задължително!! - **Абонамент за webhook**
 
 * Преглед на `артикули </barsy.help/210-dictionary/article.html>`__ (articles_view)      
 * Преглед на `сметка </barsy.help/210-dictionary/account.html>`__ (accounts_account_orders)
 * Преглед на `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__ (clientorders_view)   
 * Преглед на всички поръчки (accounts_order_view_all) 
 * Списък `категории </barsy.help/210-dictionary/category.html>`__ (categories_index)  
 * Преглед на `резервации </barsy.help/210-dictionary/reservation.html>`__ (reservations_view)  
 * `Модификатори </barsy.help/210-dictionary/modificator.html>`__ (modificators_index)
 * Преглед на `артикули </barsy.help/210-dictionary/article.html>`__ (articles_view) 

Всички методи
----------------

Описане на методите, свързани с абониране за webhook:

* :doc:`/methods/webhooks/subscribe` - Създаване на `абонамент </barsy.help/210-dictionary/subscription.html>`__
* :doc:`/methods/webhooks/unsubscribe` - Изтриване на `абонамент </barsy.help/210-dictionary/subscription.html>`__
* :doc:`/methods/webhooks/change_status` - Променя статуса(активира/деактивира) на `абонамент </barsy.help/210-dictionary/subscription.html>`__ за Webhook
* :doc:`/methods/webhooks/deactivate` - Деактивира `абонамент </barsy.help/210-dictionary/subscription.html>`__ за Webhook
* :doc:`/methods/webhooks/update`- Редактиране на `абонамент </barsy.help/210-dictionary/subscription.html>`__
* :doc:`/methods/webhooks/restart` - Подновява работата на деактивиран `абонамент </barsy.help/210-dictionary/subscription.html>`__/Рестартира брояча на грешки и датата на следващо изпращане
* :doc:`/methods/webhooks/test_call` - Предизвиква ръчно изпращане на тестови данни
* :doc:`/methods/webhooks/get_subscription` - Връща информация за подаден `абонамент </barsy.help/210-dictionary/subscription.html>`__
* :doc:`/methods/webhooks/get_subscriptions` - Връща информация за `абонаментите </barsy.help/210-dictionary/subscription.html>`__ на текущия `потребител </barsy.help/210-dictionary/user.html>`__
* :doc:`/methods/webhooks/get_events` - Връща последните събития за текущия `потребител </barsy.help/210-dictionary/user.html>`__
* :doc:`/methods/webhooks/event_type_getlist` - Списък с типовете обекти


