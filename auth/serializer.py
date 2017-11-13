from django.contrib.auth.models import User
from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
        #extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):

        user = User.objects.create(username = validated_data['username'])
        print(validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user
