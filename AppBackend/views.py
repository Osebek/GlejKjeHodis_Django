from django.shortcuts import render
from AppBackend.models import Location, Path
from AppBackend.serializers import LocationSerializer, UserSerializer, PathSerializer, PathUploadSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from AppBackend.permissions import IsOwnerOrReadOnly
from AppBackend.permissions import UserPermissionsDetail
from django.http import HttpResponse, HttpResponseForbidden
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import parser_classes,api_view
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import detail_route,parser_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_403_FORBIDDEN





@parser_classes((MultiPartParser, FormParser,))
class LocationAdd(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = LocationSerializer
	def post(self, request, format=None):
		print(self.request.user)
		print (request.data)
		latitude = request.data['latitude']
		serializer = LocationSerializer(data=request.data, context={'owner': self.request.user})
		print serializer
		print(serializer.is_valid())
		if serializer.is_valid():
			print("Shranil bom")
			serializer.save(owner=self.request.user)
			return Response(serializer.errors,status=HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
@parser_classes((JSONParser,))
class PathAdd(generics.CreateAPIView):
	serializer_class = PathSerializer
	permission_classes = (IsAuthenticated,)
	def post(self,request,format=None):
		print("Prides not?")
		print(request.data)
		serializer = PathUploadSerializer(data=request.data,context={'owner': self.request.user})
		pathLocations = request.data.pathLocations
		if serializer.is_valid():
			serializer.save(owner=self.request.user)
			for loc in pathLocations:
				loc = Location.objects.filter(id=loc).first()
				serializer.pathLocations.add(loc)
				serializer.save()
			return Response(serializer.errors,status=HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class LocationGetAll(generics.ListAPIView):
	permission_classes = (IsAuthenticatedOrReadOnly, )
	serializer_class = LocationSerializer
	queryset = Location.objects.all()

	def get_queryset(self):
		user = self.request.user
		return Location.objects.all()

class PathGetAll(generics.ListAPIView):
	permission_classes = (IsAuthenticatedOrReadOnly, )
	serializer_class = PathSerializer
	queryset = Path.objects.all()

	def get_queryset(self):
		user = self.request.user
		return Path.objects.all()

class LocationGetSpecific(generics.RetrieveAPIView):
	permission_classes = (IsAuthenticatedOrReadOnly, )
	serializer_class = LocationSerializer
	queryset = Location.objects.all()

class PathGetSpecific(generics.RetrieveAPIView):
	serializer_class = Path
	queryset = Path.objects.all()


class UserList(generics.ListAPIView):
	permissions_classes = (IsAuthenticated,)
	serializer_class = UserSerializer
	def get_queryset(self):
		user = self.request.user
		return User.objects.all()


class UserDetail(generics.RetrieveAPIView):
	permissions_classes = (IsAdminUser,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class GetCurrentUser(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self,request):
		serializer = UserSerializer(self.request.user)
		return Response(serializer.data)

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication, BasicAuthentication,)
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = Location
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self,serializer):
        serializer.save(username=self.request.user)
