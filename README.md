“Телефонная книга”

В проекте есть возможность ввести исходные данные сформировав телефонную книгу. 
Корректировка данных абонентов, а так же их контактных данных. Передача данных клиента через REST API.

Запуск приложения- "python manage.py runserver"

"http://127.0.0.1:8000/api/contacts/" -по урлу можно увидеть все контакты людей внесенные в БД. 
                                        Также реализовано добавление новых контактных данных.

"http://127.0.0.1:8000/api/contacts/1" - Выбираем конкретные данные человека для редактирования или удаления.
"http://127.0.0.1:8000/api/person/" -по урлу можно увидеть всех людей внесенные в БД. 
                                        Также реализовано добавление новых людей.

"http://127.0.0.1:8000/api/contacts/1" - Выбираем конкретного человека для редактирования или удаления.

В приложении используется:
python == 3.6.1

djangorestframework==3.11.0

Django==2.2

sqlite3
