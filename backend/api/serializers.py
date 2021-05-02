from django.core.validators import validate_email
from rest_framework import serializers
from api.models import Model, Car, Basket, User, Comment


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()


class ModelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class CarSerializer(serializers.ModelSerializer):
    model = ModelSerializer()

    def create(self, validated_data):
        car = Car()
        car.name = validated_data.get('name', 'default name')
        car.imageLink = validated_data.get('imageLink', 'assets/test.png')
        car.description = validated_data.get('description', 'default description')
        car.price = validated_data.get('price', '$ 19990')
        car.save()
        return car

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.imageLink = validated_data.get('imageLink')
        instance.description = validated_data.get('description')
        instance.price = validated_data.get('price')
        instance.save()
        return instance

    class Meta:
        model = Car
        fields = ('name', 'imageLink', 'price', 'description', 'model')


class BasketSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cars = CarSerializer(many=True)

    class Meta:
        model = Basket
        fields = ('user', 'cars')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate(self, attrs):
        password = attrs['password']
        if not attrs.__contains__('email'):
            raise serializers.ValidationError('email is required')
        email = attrs['email']
        if len(password) < 8:
            raise serializers.ValidationError('Password is too short, minimum length is 8')
        try:
            validate_email(email)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(f"Bad email, details: {e}")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'])
        return user


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_data')


class CommentCreateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)

    class Meta:
        model = Comment
        fields = ('text',)
