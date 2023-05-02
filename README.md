Задание многоуровневое: чем больше функционала будет реализовано, тем лучше.
Постановка задач должна вызвать некоторые вопросы — будет плюсом предоставить вместе с решением и возникшие вопросы с
кратким обоснованием принятых решений.

Разработано Django-приложение с функционалом:

1. CRUD (подсказка: DRF) Новостей с данными:
   • Заголовок новости
   • Главное изображение
   • Превью-изображение (автоматически генерировать из главного изображения путём уменьшения до 200px по наименьшей
   стороне)
   • Текст новости
   • Дата публикации
   • Автор новости
2. Просмотр и редактирование Новостей с rich-текстом (подсказка: summernote) в админке.
3. Выполнение периодической задачи (подсказка: celery) на отправку email о Новостях, опубликованных сегодня, с
   настройками (подсказка: constance):
   • Список адресатов
   • Тема сообщения
   • Текст сообщения
   • Время отправки
4. Импорт Примечательных мест из xlsx-файла с данными:
   • Название места
   • Гео-координаты места (точка)
   • Рейтинг (от 0 до 25)
5. Просмотр и редактирование Примечательных мест в админке, координаты получать с помощью виджета карты.
6. Выполнение периодической задачи (подсказка: celery) на получение Сводки погоды в Примечательном месте:
   • Периодичность выполнения задачи должна редактироваться из админки, по умолчанию - раз в час
   • Провайдера погоды выбрать самостоятельно (можно реализовать сервис в другом приложении)
   • Данные Сводки погоды:
   • Температура по шкале Цельсия
   • Влажность воздуха, в %
   • Атмосферное давление, в мм ртутного столба
   • Направление ветра
   • Скорость ветра, в м/с
   • Данные Сводки погоды должны быть реалистичными и разными (но не обязательно настоящими)
   • Данные Сводки погоды должны сохраняться без возможности редактирования
7. Просмотр Сводки погоды в админке с фильтром по Примечательному месту и дате снятия показаний.
8. Экспорт Сводки погоды в xlsx-файл (подсказка: xlsxWriter) с фильтром по Примечательному месту и дате снятия
   показаний.