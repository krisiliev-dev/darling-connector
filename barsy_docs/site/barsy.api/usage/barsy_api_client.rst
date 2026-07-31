Barsy API Client
==========================================

Barsy API Client е малка библиотека, написана на PHP, която опростява връзката на външна система към  barsys API. 
С него се избягва самостоятелното генериране на рекуести, добавяне на ауторизация, обработка на `съобщения </barsy.help/210-dictionary/message.html>`__ за грешки, декодиране на данни.
Работата с него свежда комуникацията до викане на определен метод и подаването на стрингове или масиви, а върнатите данни се получават директно в стрингове, масиви или обекти (според типа им)

.. contents:: Съдържание

Изисквания
-----------

  * php > 7.1
  * php-gettext
  * php-json
  * php-curl


Инсталиране
-------------

Инсталиране чрез Composer
^^^^^^^^^^^^^^^^^^^^^^^^^

Ако проекта ви използва composer (https://getcomposer.org/), може да инсталирате barsy API Client със стандартните комманди на composer cli, като първо добавите Lukanet като repository

.. code-block:: bash

  composer config repositories.lukanet composer https://docs.lukanet.com
  composer require lukanet/barsy-api-client

Самостоятелно инсталиране
^^^^^^^^^^^^^^^^^^^^^^^^^

Изтеглете архива с текущата версия от тук
  `barsy-api-client.zip </downloads/barsy-api-client.zip>`__ или тук
  `barsy-api-client.tar.gz </downloads/barsy-api-client.tar.gz>`__

Zip файлът съдържа:
 * /src/BarsyApiClient.php - основната библиотека за връзка
 * /src/BarsyApiAction.php - помощен клас, за лесно създаване обект, описващ желания екшън с параметри
 * /src/Action/\*.php - помощни класове, даващи възможност екшъните в Barsy API да се викат като локални класове и обекти
 * /src/ca-bundle.pem - верига от сертификати за осъществяване на SSL връзка до Barsy системи
 * /examples/* - папка с примери за използването на библиотеката за връзка

Настройки
-----------------------

 * $host - хост за връзка към конкретната barsy инсталация (пример: https://demo.barsy.bg )
 * $user - потребителско име за оторизация пред конкретната barsy инсталация (осигурява се от администриращ `потребител </barsy.help/210-dictionary/user.html>`__ на системата)
 * $password - парола към потребителско име за оторизация
 * $options - допълнителни опции

   * proxy_host - настройка на proxy хост (ако е необходима за връзка)
   * proxy_port - настройка на proxy порт (по подразбиране - 8888)
   * socket_timeout - максимално време за изчакване на отговор от сървъра в секунди (по подразбиране - 20 секунди)
   * response_type - тип на върнатите данни - json (по подразбиране), xml, res, csv, excel*, print*, html* (* - не е приложимо от всички екшъни)
   * request_type - тип на подадените данни - json (по подразбиране), xml, plain
   * max_redirects - максимален брой препращания (http status:301,302,303) към друг адрес (по подразбиране - 10)
   * auth_type - вид оторизиране пред конкретната barsy инсталация - като `потребител </barsy.help/210-dictionary/user.html>`__ (user) или като `клиент </barsy.help/210-dictionary/client.html>`__ (client) (по подразбиране - user)

Примерно използване:
------------------------

.. literalinclude:: ../examples_sources/misc_ping.php
  :language: php
  :emphasize-lines: 1
  :caption: Пример №1 Проста проверка на връзка (без потребител и парола)


.. literalinclude:: ../sources/depots_getlist/barsy_api_client_simple.php
  :language: php
  :emphasize-lines: 1
  :caption: Пример №2 Изтегля списък с налични складове


Съобщения (exceptions)
----------------------

 * При получаване на нарочно съобщение от насрещната система, barsy API клиент ще "вдигне" стандартен PHP Exception от тип **BarsyApiClientMessage**
 * При получаване на фатална грешка от насрещната система, barsy API клиент ще "вдигне" стандартен PHP Exception от тип **BarsyApiClientFault**

.. literalinclude:: ../examples_sources/clients_get.php
  :language: php
  :emphasize-lines: 1
  :caption: Пример №3

.. include:: /_includes/more_examples.txt