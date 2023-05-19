from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from .models import Document
from rest_framework.response import Response
from .serializers import NotesSerializer


class NotesView(APIView):

    @staticmethod
    def get(request):
        request.method = 'GET'
        queryset = Document.objects.all()
        a = NotesSerializer(queryset, many=True)
        return Response(a.data)

    @staticmethod
    def post(request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        if len(request.data) == 0:
            return Response({'message': 'No data provided'})
        return Response(serializer.errors)

    # @staticmethod
    # def get(self, request):
    #     output = [{'title': output.title, 'note': output.note}
    #               for output in Document.objects.all()]
    #     return Response(output)

    # def post(self, request):
    #     serializer = NotesSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)


class NoteDetails(APIView):
    @staticmethod
    def get(request, pk):
        request.method = 'GET'
        queryset = Document.objects.get(pk=pk)
        serializer = NotesSerializer(queryset)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        queryset = Document.objects.get(pk=pk)
        serializer = NotesSerializer(queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @staticmethod
    def delete(request, pk):
        request.method = 'DELETE'
        queryset = get_object_or_404(Document, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
