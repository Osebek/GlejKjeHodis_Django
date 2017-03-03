from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from AppBackend.models import Location, Path
from django.contrib.auth.models import User

class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Location
        fields = ('id','created','owner','latitude','longtitude','text','picture','title','name','address')

    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.latitude = validate_data.get('latitude',instance.latitude)
        instance.longtitude = validate_data.get('longtitude',instance.longtitude)
        instance.text = validate_data.get('text',instance.text)
        instance.picture = validate_data.get('picture',instance.picture)
        instance.title = validate_data.get('title',instance.title)
        instance.name = validate_data.get('name',instance.name)
        instance.address = validate_data.get('address',instance.address)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'locations')

class PathSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Path
        fields= ('id','created','owner','pathLocations','name','city','description')

    def create(self,validated_data):
        return Path.objects.create(**validated_data)

class PathUploadSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Path
        fields = ('id','created','owner','name','city','description')




