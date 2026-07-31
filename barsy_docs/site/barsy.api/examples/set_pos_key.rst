Задаване на конкретна каса за всички заявки
===========================================

Описание
---------

Barsy API поддържа регистриране и специфициране на точно определена `каса </barsy.help/210-dictionary/pos.html>`__ за рекуестите, които изискват такава. Това са рекуестите управляващи `сметки </barsy.help/210-dictionary/account.html>`__, плащания и `клиентски заявки </barsy.help/210-dictionary/client-order.html>`__.

За постигане на желание ефект, `касата </barsy.help/210-dictionary/pos.html>`__ трябва да бъде регистрирана. За целта се изпъляване *еднократно* метода Poses_register, който връща нейния ключ pos_key. Този ключ трябва да се подава към всеки рекуест по някой от възможните начини:

* като URL параметър с име "poskey"
* като HTTP Header с име "POSKEY"
* като HTTP Cookie с име "poskey"


.. attention:: Необходимо е да се предвиди, че ново регистриране на дадена каса я дерегистрира автоматично от предходни нейни регистрация. Т.е. една каса може да се ползва само от едно място


Примери
---------

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

      .. literalinclude:: ../examples_sources/set_pos_key.php
        :language: php

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

    .. code-block:: none
      :name: example_get_short

      https://demo.barsyonline.com/endpoints/json/Poses_GetCurrent?poskey=hdh3Rs97h38nmFah28dfnj2fha01

  .. tab:: CURL

      .. code-block:: bash
       :name: example_curl

        curl -i -X POST -u user:password \
          -H "POSKEY: abcdefjh123456789" \
         https://demo.barsyonline.com/endpoints/json/Poses_getCurrent


Забележка:
  В повечето случай, за кокретното определяне на `каса </barsy.help/210-dictionary/pos.html>`__ е достатъчно да се подаде само желания `търговски обект </barsy.help/210-dictionary/barsy.html>`__

  Виж също: :doc:`Задаване на конкретен търговски обект <set_barsy_id>`

Виж също
--------

 * `Каса </barsy.help/210-dictionary/pos.html>`__

