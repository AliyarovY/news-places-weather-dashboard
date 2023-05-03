from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import xls_export
from .models import WeatherSummary


class WeatherXLSExportAPIView(APIView):
    @swagger_auto_schema(
        responses={200: 'success export'},
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT, description='Export weather_summaries in xls file',
                properties={
                    'path': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='path for export file',
                        example="/root/work/projects/tw2/export_file.xls"
                    ),
                }
            )
        )
    )
    def post(self, request):
        try:
            query_params = {k:
                                v if isinstance(v, str)
                                else v[0]
                            for k, v in
                            request.query_params.items()
                            }
            queryset = WeatherSummary.objects.filter(**query_params)
            xls_path = self.request.data['path']
        except Exception as e:
            return Response(data={'bad': str(e)}, status=400)
        else:
            xls_export(queryset, xls_path)
            return Response(data={'detail': 'success export'}, status=200)
