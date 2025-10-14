from rest_framework import serializers
from content_app.models import Episode, Testimonial, Book, Event, Partner
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = [
            'id',
            'link',
            'guest_name',
            'title',
            'summarized_title',
            'description',
            'img'
        ]

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id',
            'name',
            'country',
            'testimony',
            'img'
        ]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'description',
            'summary',
            'img',
            'price',
            'purchase_link'
        ]
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'host',
            'description',
            'price',
            'summary',
            'img',
            'event_date'
        ]

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            'id',
            'name',
            'description',
            'img',
            'website'
        ]