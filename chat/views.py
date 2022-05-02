from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import Comment
from .serializers import CommentSerializer

# A View correspondente terá um método chamado get e post
# que bate com o nome do método do request.
class CommentView(APIView):
    def get(self, request, comment_id=''):
        comment = Comment.objects.all()
        # Aqui estamos buscando todas as instâncias no banco de dados
        serializer = CommentSerializer(comment, many=True)

        # Estamos fazendo essa condicional, pois estamos usando 
        # o mesmo método get para listagem e filtragem
        if comment_id:
            try:
                comment = Comment.objects.get(id=comment_id)
                serializer = CommentSerializer(comment)
                # Caso o id informado seja inválido, um erro é retornado
            except ObjectDoesNotExist:
                return Response({'errors': 'invalid comment_id'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

#    def get(self, request):
#        comments = Comment.objects.all()
#        serializerComments = CommentSerializer(comments, many=True)
#
#        return Response(serializerComments.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Aqui vamos fazer uma verificação se os dados 
        # informados na requisição são válidos.
        # O serializer fará essa verificação para nós
        serializer = CommentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Agora faremos a criação de um novo comentário 
        # conforme os dados retornados pelo serializer.validated_data
        comment = Comment.objects.create(**serializer.validated_data)
        serializer = CommentSerializer(comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
