# Colorful Contact Book

Добро пожаловать в **Colorful Contact Book** — удобное настольное приложение для управления контактами с красивым и функциональным интерфейсом. Создано на Python, это приложение поможет вам организовать ваши контакты стильно и эффективно.

## Оглавление

- Функциональность
- Почему стоит выбрать Colorful Contact Book?
- Используемые библиотеки
- Установка
- Технологии
- Ключевые особенности

## Функциональность

Colorful Contact Book предоставляет следующие возможности:

- **Добавление, редактирование и удаление контактов**: Легко добавляйте новые контакты, редактируйте существующие или удаляйте их.
- **Расширенный поиск**: Быстро находите контакты по имени, телефону, email или категории с помощью мощного поиска.
- **Фильтрация по категориям**: Организуйте контакты по категориям (например, Друзья, Семья, Работа) и фильтруйте их одним кликом.
- **Сортировка**: Сортируйте контакты по имени, категории или другим полям для удобства.
- **Валидация email**: Проверяйте корректность email-адресов перед сохранением контакта с помощью встроенной валидации.

## Почему стоит выбрать Colorful Contact Book?

Наша программа выделяется благодаря:

- **Красивому интерфейсу**: Современный дизайн с темами оформления, созданный с помощью `ttkthemes`, делает управление контактами приятным.
- **Надёжности**: Использование PostgreSQL обеспечивает стабильное и масштабируемое хранение данных.
- **Простоте использования**: Интуитивно понятный интерфейс, который подойдёт любому пользователю, даже без технических знаний.
- **Кроссплатформенности**: Работает на Windows (с упакованным `.exe`), и может быть адаптировано для других платформ.
- **Открытому коду**: Вы можете вносить изменения или улучшать приложение под свои нужды!

## Используемые библиотеки

Colorful Contact Book использует следующие библиотеки Python:

- `sqlalchemy` **(2.0.40)**: Для управления базой данных и работы с ORM.
- `psycopg2-binary` **(2.9.10)**: Драйвер для подключения SQLAlchemy к PostgreSQL.
- `ttkthemes` **(3.2.2)**: Для улучшения интерфейса Tkinter с помощью тем оформления.
- `pyinstaller` **(6.8)**: Для упаковки приложения в единый `.exe` файл для Windows (не требуется для работы приложения).

## Установка

Следуйте этим шагам, чтобы настроить и запустить Colorful Contact Book на вашем компьютере.

### Требования

- **Python 3.8+**: Убедитесь, что Python установлен. Скачайте с python.org.
- **pip**: Менеджер пакетов Python (идёт вместе с Python).
- **PostgreSQL**: Установите PostgreSQL с официального сайта.

### Шаги

1. **Клонируйте репозиторий**\
   Склонируйте этот репозиторий на ваш компьютер:

   ```
   git clone https://github.com/qwrtzz/colorful_contact_book.git
   cd colorful-contact-book
   ```

2. **Настройте виртуальное окружение** (Рекомендуется)\
   Создайте и активируйте виртуальное окружение для изоляции зависимостей:

   ```
   python -m venv venv
   .\venv\Scripts\activate  # На Windows
   source venv/bin/activate  # На macOS/Linux
   ```

3. **Установите зависимости**\
   Установите необходимые библиотеки с помощью `requirements.txt`:

   ```
   pip install -r requirements.txt
   ```

   Если `requirements.txt` отсутствует, установите вручную:

   ```
   pip install sqlalchemy==2.0.40 psycopg2-binary==2.9.10 ttkthemes==3.2.2
   ```

4. **Настройте базу данных PostgreSQL**

   - Убедитесь, что PostgreSQL установлен и запущен:

     ```
     net start postgresql-x64-16  # На Windows
     ```

   - Создайте базу данных `contact_book`:

     ```
     psql -U postgres -c "CREATE DATABASE contact_book;"
     ```

   - Убедитесь, что в `database.py` указаны правильные данные для подключения:

     ```python
     DATABASE_URL = "postgresql://postgres:your_password@localhost/contact_book"
     ```

     Замените `your_password` на ваш пароль PostgreSQL.

5. **Запустите приложение**\
   Запустите приложение с помощью Python:

   ```
   python app.py
   ```

### Для пользователей Windows (Использование .exe)

Если вы предпочитаете запуск без установки Python:

1. Скачайте `app.exe` из раздела Releases.
2. Убедитесь, что PostgreSQL установлен и настроен (см. шаг 4 выше).
3. Дважды щёлкните по `app.exe`, чтобы запустить приложение.

## Технологии

Colorful Contact Book построен с использованием следующих технологий:

- **Python 3**: Основной язык программирования приложения.
- **Tkinter**: Стандартная библиотека Python для создания графического интерфейса.
- **SQLAlchemy**: Библиотека ORM для управления базой данных.
- **PostgreSQL**: Мощная база данных для надёжного хранения данных.
- **PyInstaller**: Для упаковки приложения в единый `.exe` файл для Windows.

## Ключевые особенности

Вот несколько выдающихся особенностей Colorful Contact Book:

- **Стильный интерфейс**: Благодаря `ttkthemes` приложение выглядит современно и привлекательно.
- **Расширенный функционал**: Поиск, фильтрация и сортировка делают управление контактами удобным.
- **Валидация email**: Встроенная проверка корректности email-адресов.
- **Простая установка на Windows**: Упаковка в `.exe` позволяет запускать приложение без установки Python (при наличии PostgreSQL).
- **Надёжное хранение**: PostgreSQL обеспечивает безопасное и масштабируемое хранение ваших контактов.

---
