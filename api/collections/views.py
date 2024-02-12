# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class CollectionListView(APIView):
    def get(self, request):
        data = {'message': 'Hello, REST API!'}
        return Response(data)
