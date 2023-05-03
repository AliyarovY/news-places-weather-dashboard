import xlsxwriter


def xls_export(queryset, xls_path):
    with xlsxwriter.Workbook(xls_path) as workbook:
        # Добавляем новый лист в файл
        worksheet = workbook.add_worksheet()

        # Заголовок таблицы
        headers = ['Место', 'Дата', 'Температура', 'Влажность', 'Давление', 'Направление ветра', 'Скорость ветра']
        row = 0
        col = 0
        for header in headers:
            worksheet.write(row, col, header)
            col += 1

        # Заполняем таблицу данными
        row = 1
        col = 0
        for record in queryset.select_related('place').only('place__name', 'created_at', 'temperature', 'humidity',
                                                            'pressure', 'wind_direction', 'wind_speed'):
            worksheet.write(row, col, record.place.name)
            worksheet.write(row, col + 1, record.created_at.strftime("%d.%m.%Y %H:%M:%S"))
            worksheet.write(row, col + 2, record.temperature)
            worksheet.write(row, col + 3, record.humidity)
            worksheet.write(row, col + 4, record.pressure)
            worksheet.write(row, col + 5, record.wind_direction)
            worksheet.write(row, col + 6, record.wind_speed)
            row += 1
