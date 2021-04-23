from rest_framework.views import APIView
from rest_framework.response import Response


class PlovosAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'test': 'test'})
