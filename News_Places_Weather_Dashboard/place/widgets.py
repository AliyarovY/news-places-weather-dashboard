from django.forms.widgets import TextInput


class MapWidget(TextInput):
    template_name = 'widgets/map.html'

    class Media:
        js = (
            'https://api-maps.yandex.ru/2.1/?apikey=YOUR_API_KEY&lang=ru_RU',
            'js/admin/map.js',
        )

    def __init__(self, attrs=None):
        super().__init__(attrs={'class': 'map-widget'})

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['map_id'] = f'map-{name}'
        context['widget']['latitude_id'] = f'latitude-{name}'
        context['widget']['longitude_id'] = f'longitude-{name}'
        return context