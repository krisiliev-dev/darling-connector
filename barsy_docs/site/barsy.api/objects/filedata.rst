.. role:: deprecated
   :class: deprecated

.. role:: deprecated_text
   :class: deprecated_text

.. role:: category_header
   :class: category_header

FileData
======================================================================================


.. contents:: Съдържание
   :local:
   :depth: 1

------

Описание
-----------

Име
^^^^^^^^^^^
Lukanet\\Barsy\\Files\\Data\\FileData


Параметри
^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Параметър
     - Тип
     - Подразбиране
     - Описание
   * - **$name**
     - *string*
     - 
     - Име на файла
   * - **$size**
     - *integer*
     - 
     - Размер на файла в байтове
   * - **$type**
     - *string*
     - 
     - MIME тип на файла
   * - **$last_modified**
     - *string*
     - 
     - Дата на последна модификация на файла
   * - **$url**
     - *string*
     - 
     - URL за изтегляне на файла
   * - **$thumbnail_url**
     - *string*
     - 
     - URL за преглед на файла
   * - **$delete_url**
     - *string*
     - 
     - URL за изтриване на файла
   * - **$delete_cache_url**
     - *string*
     - 
     - URL за изтриване на кеша на файла
   * - **$content**
     - *string*
     - 
     - 
   * - **$cache_files_count**
     - *int*
     - 
     - 
   * - **$alt_files**
     - *array*
     - 
     - 
   * - **$width**
     - *int*
     - 
     - Ширина на файла ако е картинка (jpeg, jpg, png)
   * - **$height**
     - *int*
     - 
     - Височина на файла ако е картинка (jpeg, jpg, png)
   * - **$number_pages**
     - *int*
     - 
     - Брой страници (pdf)
   * - **$media_duration**
     - *string*
     - 
     - Продължителност на медиата (video, audio) - форматирано

Използва се в
^^^^^^^^^^^^^^^^^^^^^^
	 * :doc:`../methods/files/getlist`
	 * :doc:`../methods/files/get`

