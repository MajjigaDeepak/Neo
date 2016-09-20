from django.shortcuts import render
from rest_framework import viewsets
from gapp.serializers import querySerializer
from gapp.models import Query
from rest_framework import status
from rest_framework.response import Response
from gapp.Runner import Neo4jWrapper


# Create your views here.


class queryViewset(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = querySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        wrapper = Neo4jWrapper()
        t = wrapper.graphTraversalQuery(request.data['ques'])
        # p=Neo4jWrapper.graphPropertyQuery(serializer.data['traversal'])
        return Response(t)
