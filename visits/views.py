from rest_framework import generics, status
from rest_framework.response import Response
from .models import Visit, Store
from .serializers import StoreSerializer, VisitSerializer


class StoreListView(generics.ListAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        phone_number = self.kwargs.get('phone_number')
        return Store.objects.filter(worker__phone_number=phone_number)


class CreateVisitView(generics.CreateAPIView):
    serializer_class = VisitSerializer

    def create(self, request, *args, **kwargs):
        phone_number = self.kwargs.get('phone_number')
        store = request.data.get('store')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            store = Store.objects.get(pk=store)
            if store.worker.phone_number != phone_number:
                return Response(
                    {"error": "Номер телефона работника не привязан к данной Торговой точке"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            visit = Visit.objects.create(store=store, latitude=latitude, longitude=longitude)
            serializer = VisitSerializer(visit)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Store.DoesNotExist:
            return Response(
                {"error": "Торговая точка не найдена"},
                status=status.HTTP_404_NOT_FOUND
            )
