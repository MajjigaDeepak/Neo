from django.shortcuts import render
from rest_framework import viewsets
from gapp.serializers import querySerializer, questionSerializer
from gapp.models import Query, question
from rest_framework import status
from rest_framework.response import Response
from gapp.Runner import Neo4jWrapper
from textblob.classifiers import NaiveBayesClassifier


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


class questionViewset(viewsets.ModelViewSet):
    queryset = question.objects.all()
    serializer_class = questionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        train = [
            ('Show my stats', 'Show my stats'),
            ('my expenses', 'Show my stats'),
            ('show my expenses', 'Show my stats'),
            ('expense charts', 'Show my stats'),
            ('graphs on my data', 'Show my stats'),
            ('Show 5 transactions', 'Show 5 transactions'),
            ('Five transactions', 'Show 5 transactions'),
            ('last 5 transactions', 'Show 5 transactions'),
            ('Show all transactions', 'Show all transactions'),
            ('all my transactions', 'Show all transactions'),
            ('show my transactions', 'Show all transactions'),
            ('Show lastyear transactions', 'Show lastyear transactions'),
            ('lastyear transactions', 'Show lastyear transactions'),
            ('last 360days transactions', 'Show lastyear transactions'),
            ('360days transactions', 'Show lastyear transactions'),
            ('Show demat account details', 'Show demat account details'),
            ('demat account info', 'Show demat account details'),
            ('Show demat details', 'Show demat details'),
            ('demat details', 'Show demat details'),
            ('Show linked trading account details', 'Show stock details'),
            ('all my transactions', 'Show stock details'),
            ('show my transactions', 'Show stock details')

        ]
        test = [
            ('my expenses', 'Show my stats'),
            ('show my transactions', 'Show stock details'),
            ('demat details', 'Show demat details'),
            ('show my transactions', 'Show all transactions'),
        ]
        cl = NaiveBayesClassifier(train)
        return Response(cl.classify(request.data))
