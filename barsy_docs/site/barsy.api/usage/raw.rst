Директна връзка
===============

Директната връзка се използва когато външната системата изгража сама рекуестите към Barsy API и не се използва :doc:`/usage/barsy_api_client`.
В този случай, трябва да бъдат направите стандартни HTTP 1.1 заявки към входната точка на желаната barsy система.

Postman Collection
----------------------------

На разположение на разработващите интеграция с barsy е стандартна колекция за Postman, която можете да изтеглите от  `тук </downloads/BarsyApi.postman_collection.json>`__

Необходими данни за вход:
----------------------------

* Протокол (http или https) - посред настройката на системата
* Хост+порт - осигурява се от администратора на системата 
* `Потребител </barsy.help/210-dictionary/user.html>`__ (username) - осигурява се от администратора на системата 
* Парола (password) - осигурява се от администратора на системата 

Ауторизацията е стандартна HTTP Basic Authentication (http://en.wikipedia.org/wiki/Basic_access_authentication).

Примерни начини за изпращане на заявка

1. Единичен метод
----------------------------
Може да се прилага в случайте, когато е една заявка се извиква само един метод от Barsy API (най-чест случай)

Формат на заявката::
  
  |http://{barsy-domain}/endpoints/{output}/{method}?{params}

Примери
^^^^^^^

.. code-block:: http
  :emphasize-lines: 1
  :caption: Request

  GET /endpoints/json/articles_get?article_id=123 HTTP/1.1
  Host: http://demo.barsyonline.com

.. code-block:: json
  :caption: Responce

   {
    "article_id":24737,
    "article_name":"Capuchino",
    "actual_price":2.40,
    "composite":0,
    "article_type":1,
    "amount_type_id":1,
    "picture":"capuchino.jpg",
    "last_update":"2012-09-2717:12:29",
    "amount_unit":1,
    "stream_id":181,
    "ref_num":null,
    "code":null,
    "is_for_sale":1,
    "barcode":null,
    "stream_name":"Bar",
    "current_price":2.00
    }

2.Множестово методи в един рекуест
----------------------------------

  Подходящо за оптимизация на множество рекуести в една заявка. Така се редуцира броя на заявките при нужда от изтеглянет на различни данни

Пример:
^^^^^^^

.. code-block:: http
    :caption: Request

    POST /endpoints/json/ HTTP/1.1
    Host: http://moon.barsy.bg

    {
      "Articles_get":{
        "article_id":"123"
      },
      "Categories_get":{
        "cat_id":"45"
      }
    }
      
Отговор::
  
  {
    Articles_get:{    
      "article_id":24737,
      "article_name":"Capuchino",
      …....
    },
    Categories_get:{
      "cat_id": "1",
      "parent_id": "46",
      "cat_name": "Hot drinks",
      "cat_path": "Main > Bar > Hot drinks",
      "description": "Hot drinks",
      "child_articles_cnt": "68"
    }
  }

3. Задаване на търговски обект (barsy_id)
----------------------------------------------

За укажете `търговски обект </barsy.help/210-dictionary/barsy.html>`__ (различен от дефолтния за подадения `потребител </barsy.help/210-dictionary/user.html>`__) трябва да се добави GET параметър към основния URL адрес

Параметър: bid
Стойност: {id на търговския обект }

Примери
^^^^^^^


http://domain.barsy.bg/endpoints/json/articles_get?bid=2

Можете да проверите кой е текущия ви `търговски обект </barsy.help/210-dictionary/barsy.html>`__ с :doc:`този метод </methods/barsys/getcurrent>`

..
