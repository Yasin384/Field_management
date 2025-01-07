from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Field
from .serializers import FieldSerializer
from .utils import get_user_from_token

class FieldListCreateView(generics.ListCreateAPIView):
    """
    Список полей и создание нового
    """
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        token = self.request.headers.get("Authorization").split(" ")[1]
        user = get_user_from_token(token)
        return self.queryset.filter(farmer_id=user["id"])

    def perform_create(self, serializer):
        token = self.request.headers.get("Authorization").split(" ")[1]
        user = get_user_from_token(token)
        serializer.save(farmer_id=user["id"])


class FieldDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Просмотр, обновление и удаление поля
    """
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        token = self.request.headers.get("Authorization").split(" ")[1]
        user = get_user_from_token(token)
        return self.queryset.filter(farmer_id=user["id"])
