Задаване на текущ търговски обект
=================================

Необходимо, когато `потребителя </barsy.help/210-dictionary/user.html>`__, с който се оторизирате има достъп до повече от един `търговски обект </barsy.help/210-dictionary/barsy.html>`__ и искате да специфицирате конкретен в чийто контекст да се изпълняват рекуестите.

.. tabs::

  .. tab:: BarsyApiClient

     Примерът използва php клиент за връзка с Barsy. Повече информация за него виж :doc:`/usage/barsy_api_client`

     .. literalinclude:: ../examples_sources/set_barsy_id.php
       :language: php
       :linenos:

  .. tab:: HTTP link

    Примерно изпълнение с HTTP link

    .. code-block:: none
      :name: example_get_short

      https://demo.barsyonline.com/endpoints/json/Barsys_GetCurrent?bid=2


  Виж също: :doc:`Задаване на конкретна каса <set_pos_key>`

Виж също
--------

 * `Търговски обект </barsy.help/210-dictionary/barsy.html>`__

