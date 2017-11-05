from rest_framework import status
from rest_framework.response import Response


class CreaMultiMixin(object):
    def create(self, request, *args, **kwargs):
        datos = request.data
        for data in datos:
            serializer = self.get_serializer(data=data)
            if serializer.is_valid(raise_exception=False):
                self.perform_create(serializer)

        return Response({"success": True}, status=status.HTTP_201_CREATED)