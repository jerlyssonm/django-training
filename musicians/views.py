from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Musician
from .serializers import MusicianSerializer
from django.core.exceptions import ObjectDoesNotExist
import ipdb


class MusicianView(APIView):
    def post(self, request):

        serializer = MusicianSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        musician = Musician.objects.create(**serializer.validated_data)

        serializer = MusicianSerializer(musician)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, musician_id=''):
        if musician_id:
            try: 
                musician = Musician.objects.get(id=musician_id)
                serializer = MusicianSerializer(musician)
                return Response(serializer.data)

            except ObjectDoesNotExist:
                return Response({'errors': 'invalid musician_id'}, status.HTTP_404_NOT_FOUND)

        instrument = request.GET.get('instrument', None)
        if instrument:
            try:
                x = instrument.lower()
                musician = Musician.objects.get(instrument=x)
                serializer = MusicianSerializer(musician)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'errors': 'musician with instrument not found'}, status.HTTP_404_NOT_FOUND)
        # ipdb.set_trace()

        try: 
            musicians = Musician.objects.all()
            serializer = MusicianSerializer(musicians, many=True)

            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response([])
        # Aqui o campo many=True é obrigatório, pois uma lista está sendo informada para o serializador
