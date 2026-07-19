Налични методи
=======================================================

.. weight:: 50

.. summary::
  Kаталог на част от наличните методи за работа с Barsy API

.. sidebar:: Postman Collection

    .. raw:: html

      <div class="postman-run-button" data-postman-action="collection/fork" data-postman-var-1="3465473-ee90ecea-1b28-4463-b453-19a55ab300b5" data-postman-collection-url="entityId=3465473-ee90ecea-1b28-4463-b453-19a55ab300b5&entityType=collection&workspaceId=68d7a94d-8984-46f0-9cea-503ce5247319"></div>
      <script type="text/javascript">(function (p,o,s,t,m,a,n) {!p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild(((n = o.createElement("script")),(n.id = s+t), (n.async = 1), (n.src = m), n));}(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));</script>

      <a href="https://docs.lukanet.com/downloads/BarsyApi.postman_collection.json">Алтернативен линк</a>

Страницата съдържа каталог на част от наличните методи за работа с Barsy API. Всички методи за представени с техния входни и изход параметри и типове данни.
За всеки от тях има предоставен примерен код в няколко варианта.
При забелязан проблем - :doc:`свържете се с нас</helpme/index>`

.. warning::

  Ако използвате за първи път Barsy API - моля, запознайте се с :doc:`/integrations/index`


Най-често използвани методи
-----------------------------

.. important::

  Най-често използвани методи при класическа интеграция с Barsy API:

  * :doc:`Подробни данни за сметка<accounts/get>`

    Връща пълни данни за конкретна `сметка </barsy.help/210-dictionary/account.html>`__ по нейното ID — основни полета (`клиент </barsy.help/210-dictionary/client.html>`__, обект, маса, валута, `потребител </barsy.help/210-dictionary/user.html>`__-създател, дата на отваряне/затваряне, текущ статус), общи суми (брутна, отстъпки, ДДС, нетна, платена, остатък). Чрез `extra_properties` могат да се поискат допълнителни секции: поръчки с пълни детайли, история на промените (audit log), направени плащания, прикачени документи (`фактури </barsy.help/210-dictionary/invoice.html>`__, бележки), статус на обслужване, разрешени действия за текущия `потребител </barsy.help/210-dictionary/user.html>`__.Типични случаи: отваряне на детайлен изглед на `сметка </barsy.help/210-dictionary/account.html>`__ в касовия интерфейс, презареждане на актуални суми след промяна, проверка на статус от мобилно сервизно приложение, синхронизация на финални данни към счетоводна система.

  * :doc:`Универсална работа със сметка<accounts/place>`

    Най-мощният endpoint в касовия модул, който обхваща пълния жизнен цикъл на `сметка </barsy.help/210-dictionary/account.html>`__ в едно извикване — създаване на нова или продължаване на съществуваща (по `account_id`), добавяне на нови поръчки, прикачване на плащания, фактуриране, локален или мрежов печат на бележка и едновременно приключване. `Клиентът </barsy.help/210-dictionary/client.html>`__ може да се идентифицира по `client_id`, по данни (име/телефон/email според настройка) или по клиентска карта (`client_code`). За идемпотентност при ретрай подавайте уникален UUID — повторно изпратена заявка със същия UUID НЕ създава нова `сметка </barsy.help/210-dictionary/account.html>`__.Типични случаи: основният API call за POS и self-service касиерски системи, мобилни приложения за поръчка, онлайн магазини който приключват `продажбата </barsy.help/210-dictionary/sale.html>`__ в едно извикване, kiosk терминали. Препоръчителна е пред отделните `Accounts_create`/`Accounts_close` за нови интеграции.

  * :doc:`Списък с артикули<articles/getlist>`

    Универсален метод за изтегляне на списък с `артикули </barsy.help/210-dictionary/article.html>`__ от каталога с богат набор от филтри: по име/код/баркод, `категория </barsy.help/210-dictionary/category.html>`__, `поток </barsy.help/210-dictionary/flow.html>`__, `доставчик </barsy.help/210-dictionary/supplier.html>`__, ценова група, ДДС, наличност в `склад </barsy.help/210-dictionary/store.html>`__, активност, дата на промяна. Поддържа странициране (`offset`, `length`) и пореждане по произволна колона. Чрез `extra_properties` за всеки `артикул </barsy.help/210-dictionary/article.html>`__ могат да се поискат допълнителни секции като цена в контекста на конкретна `каса </barsy.help/210-dictionary/pos.html>`__/`клиент </barsy.help/210-dictionary/client.html>`__, текуща наличност, изображения, `ценови правила </barsy.help/210-dictionary/pricelist.html>`__, атрибути.Типични случаи: попълване на каталог в онлайн магазин, синхронизация към външна система с инкрементално сваляне по дата на промяна, попълване на автокомплийт при търсене в POS, експорт за маркетингова кампания. Това е препоръчителният endpoint за основна интеграция на каталога.

  * :doc:`Създаване на клиентска заявка<clientorders/create>`

    Регистрира нова `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__ (предварителна поръчка от `клиент </barsy.help/210-dictionary/client.html>`__ за бъдеща обработка) с основните й данни — `клиент </barsy.help/210-dictionary/client.html>`__, обект на изпълнение, дата на доставка/обслужване, метод на доставка, адрес, бележки. Към заявката могат да се прикрепят редове с поръчвани `артикули </barsy.help/210-dictionary/article.html>`__ (количества, единични цени, отстъпки, `модификатори </barsy.help/210-dictionary/modificator.html>`__) и постъпили авансови плащания (капаро, депозит). Заявката е независима от `сметка </barsy.help/210-dictionary/account.html>`__/`каса </barsy.help/210-dictionary/pos.html>`__ — тя става "`сметка </barsy.help/210-dictionary/account.html>`__" чак при действителното й изпълнение.Типични случаи: онлайн поръчка от уебсайт/мобилно приложение, поръчка по телефон за доставка, кетъринг заявка с дата на изпълнение в бъдеще, `резервация </barsy.help/210-dictionary/reservation.html>`__ с предварително `плащане </barsy.help/210-dictionary/payment.html>`__. След създаването могат да се изпратят webhook събития към интеграции (например `доставчик </barsy.help/210-dictionary/supplier.html>`__).

  * :doc:`Създаване на нов клиент<clients/create>`

    Регистрира нов `клиент </barsy.help/210-dictionary/client.html>`__ в системата с подадените данни — основни идентификатори (име, телефон, email, ЕИК/БУЛСТАТ), адреси за фактуриране и доставка, клиентска група, език за комуникация, потребителски акаунт за самообслужване, отстъпки и кредитни лимити. Подадените данни трябва да спазват конфигурираното правило за уникалност (по подразбиране — име; възможни алтернативи: телефон, email, потребителско име).Типични случаи: добавяне на нов корпоративен `клиент </barsy.help/210-dictionary/client.html>`__ за фактуриране, регистрация при първа `продажба </barsy.help/210-dictionary/sale.html>`__ в POS, импорт от CRM система, самообслужваща регистрация през онлайн магазина. При нарушение на уникалността методът хвърля грешка — за идемпотентно поведение виж `Clients_createsmart`.

  * :doc:`Създаване на плащане<payments/create>`

    Регистрира ново парично движение (приход или разход) в системата с подаден метод на `плащане </barsy.help/210-dictionary/payment.html>`__, сума, `клиент </barsy.help/210-dictionary/client.html>`__, документална дата и референтен номер. `Плащането </barsy.help/210-dictionary/payment.html>`__ може да остане самостоятелно или да се асоциира с една или повече `сметки </barsy.help/210-dictionary/account.html>`__ чрез масива `accounts` — тогава внесената сума се разпределя върху остатъците им. По същия начин през специализирани полета може да се прикачи към `клиентска заявка </barsy.help/210-dictionary/client-order.html>`__, `резервация </barsy.help/210-dictionary/reservation.html>`__ или складово `зареждане </barsy.help/210-dictionary/storeload.html>`__ (за разход към `доставчик </barsy.help/210-dictionary/supplier.html>`__).Типични случаи: внасяне на капаро за бъдеща поръчка, авансово `плащане </barsy.help/210-dictionary/payment.html>`__ към `доставчик </barsy.help/210-dictionary/supplier.html>`__ преди доставка, кеш погасяване на стар дълг на корпоративен `клиент </barsy.help/210-dictionary/client.html>`__, постъпление от банково извлечение което се разнася върху неплатени `фактури </barsy.help/210-dictionary/invoice.html>`__.

  * :doc:`Webhook абонамент<webhooks/subscribe>`

    Създава `абонамент </barsy.help/210-dictionary/subscription.html>`__ на отдалечена услуга, която да получава webhook-известия при настъпване на конкретен тип събитие в Barsy (нова `сметка </barsy.help/210-dictionary/account.html>`__, ново `плащане </barsy.help/210-dictionary/payment.html>`__, промяна в каталога и др.). Подават се `event_type_id` и URL за получаване. По време на регистрацията към URL-а се изпраща тестова заявка — сървърът трябва да отговори с HTTP код 200–299, 401, 403, 405, 500 или 501 за валидна регистрация. След активиране, при всяко настъпване на събитието системата POST-ва JSON payload с детайли.Типични случаи: интеграция с ERP — известяване при ново `зареждане </barsy.help/210-dictionary/storeload.html>`__, маркетингова автоматизация — известие при нова голяма `сметка </barsy.help/210-dictionary/account.html>`__, синхронизация с външен онлайн магазин при промяна в каталога, BI dashboard за реално време.


Всички методи 
-----------------------------


 Каталог основни номенклатури

  * :doc:`Артикули<articles/index>`  -  *13 метода*
  * :doc:`Категории<categories/index>`  -  *7 метода*
  * :doc:`Модификатори<modificators/index>`  -  *6 метода*
  * :doc:`Типове количества<amounttypes/index>`  -  *1 метода*
  * :doc:`Артикули характеристики<articledetails/index>`  -  *4 метода*
  * :doc:`Артикули комбо групи<articlesupplements/index>`  -  *1 метода*
  * :doc:`Артикули атрибутни групи<groupsattr/index>`  -  *2 метода*
  * :doc:`Ценови правила<pricelists/index>`  -  *16 метода*
  * :doc:`Клиенти<clients/index>`  -  *8 метода*
  * :doc:`Клиентски групи<clientgroups/index>`  -  *1 метода*
  * :doc:`Потребители<users/index>`  -  *10 метода*
  * :doc:`Търговски обект<barsys/index>`  -  *3 метода*
  * :doc:`Абонаменти<subscriptions/index>`  -  *1 метода*
  * :doc:`Данъчни групи<taxgroups/index>`  -  *1 метода*
  * :doc:`Доставчици<suppliers/index>`  -  *5 метода*
  * :doc:`Представители<persons/index>`  -  *8 метода*
  * :doc:`Роли<roles/index>`  -  *1 метода*
  * :doc:`Спедитори<speditors/index>`  -  *4 метода*
  * :doc:`Сделки<deals/index>`  -  *1 метода*
  * :doc:`articlerelations<articlerelations/index>`  -  *6 метода*
  * :doc:`cards<cards/index>`  -  *6 метода*
  * :doc:`webhooks<webhooks/index>`  -  *13 метода*

 Каса

  * :doc:`Сметки<accounts/index>`  -  *18 метода*
  * :doc:`Поръчки<orders/index>`  -  *1 метода*
  * :doc:`Плащания<payments/index>`  -  *2 метода*
  * :doc:`Клиентски заявки<clientorders/index>`  -  *8 метода*
  * :doc:`Пакетни карти/Ваучери<cards/index>`  -  *6 метода*
  * :doc:`Резервации<reservations/index>`  -  *5 метода*
  * :doc:`Работен график<workingshift/index>`  -  *1 метода*

 Склад

  * :doc:`Склад зареждане<storeloads/index>`  -  *5 метода*
  * :doc:`Склад прехвърляне <storemoves/index>`  -  *6 метода*
  * :doc:`Склад производство<storeproductions/index>`  -  *2 метода*
  * :doc:`Склад изписвания<storeouts/index>`  -  *4 метода*
  * :doc:`Склад ревизии<revisions/index>`  -  *1 метода*

 Документ

  * :doc:`Фактури<invoices/index>`  -  *5 метода*
  * :doc:`Е-документи<edocs/index>`  -  *5 метода*
  * :doc:`documents<documents/index>`  -  *3 метода*

 Други

  * :doc:`Файлове<files/index>`  -  *3 метода*
  * :doc:`Съобщения<messages/index>`  -  *1 метода*
  * :doc:`Дестинации<destinations/index>`  -  *2 метода*
  * :doc:`Импорт<import/index>`  -  *3 метода*
  * :doc:`Форми<forms/index>`  -  *1 метода*
  * :doc:`Разни<misc/index>`  -  *3 метода*
  * :doc:`Webhooks<webhooks/index>`  -  *0 метода*
  * :doc:`remotesystems<remotesystems/index>`  -  *1 метода*

 Справки

  * :doc:`Склад<store/index>`  -  *2 метода*
  * :doc:`Справки<reports/index>`  -  *10 метода*

 Настройки

  * :doc:`Каси<poses/index>`  -  *3 метода*
  * :doc:`Складове<depots/index>`  -  *4 метода*
  * :doc:`Места<places/index>`  -  *4 метода*
  * :doc:`Начини на плащане<paymentmethods/index>`  -  *1 метода*
  * :doc:`Валути<currencies/index>`  -  *1 метода*
  * :doc:`Потоци<streams/index>`  -  *1 метода*
  * :doc:`Причини<reasons/index>`  -  *2 метода*
  * :doc:`Разфасовки<packages/index>`  -  *2 метода*
  * :doc:`Езици<languages/index>`  -  *1 метода*

 Clientorders

  * :doc:`clientorders<clientorders/index>`  -  *8 метода*

 Invoices

  * :doc:`invoices<invoices/index>`  -  *5 метода*

 Reservations

  * :doc:`reservations<reservations/index>`  -  *5 метода*

 Users

  * :doc:`rightrequests<rightrequests/index>`  -  *1 метода*

 Workschedule

  * :doc:`workschedule<workschedule/index>`  -  *2 метода*


.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

   */index
