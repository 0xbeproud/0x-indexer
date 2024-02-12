from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    data = {'message': 'this is api index'}
    return Response(data)

