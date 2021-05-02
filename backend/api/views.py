from rest_framework.permissions import IsAuthenticated
from api.models import Model, Car, Basket, User, Comment
from api.serializers import ModelSerializer, BasketSerializer, CarSerializer, UserRegisterSerializer, UserSerializer, \
    CommentSerializer, CommentCreateSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response


@api_view(['GET'])
def car_by_model(request, pk):
    try:
        model = Model.objects.get(id=pk)
    except Exception as e:
        return Response({'error': str(e)})

    serializer = CarSerializer(model.cars.all(), many=True)
    return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = CarsListSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response({'error': 'Only Get request is accepted'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def model(request, pk):
    try:
        model = Model.objects.get(id=pk)
    except Model.DoesNotExist as e:
        return Response({'error': str(e)})
    serializer = ModelSerializer(model)
    return Response(serializer.data)
    # elif request.method == 'PUT':
    #     serializer = ModelsListSerializer(instance=model, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response({'error': serializer.errors})
    # if request.method == 'DELETE':
    #     model.delete()
    #     return Response({'deleted': True})
    # return Response({'error': 'Only Get request is accepted'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def model_detail(request, id):
    try:
        model = Model.objects.get(id=id)
    except Model.DoesNotExist as e:
        return Response({'error': str(e)})

    serializer = ModelSerializer(model)
    return Response(serializer.data)


class CarsListAPIView(APIView):
    def get(self, request):
        cars_list = Car.objects.all()
        serializer = CarSerializer(cars_list, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def car_details(request, pk):
    try:
        car = Car.objects.get(id=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    ser = CarSerializer(car)
    print(ser.data)
    return Response(ser.data, status=status.HTTP_200_OK)


class ModelsListAPIView(APIView):
    def get(self, request):
        models_list = Model.objects.all()
        serializer = ModelSerializer(models_list, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = ModelsListSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cars_of_basket(request):
    try:
        basket = request.user.basket
    except Basket.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        print(basket.cars)
        cars = basket.cars
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_basket(request, pk):
    try:
        car = Car.objects.get(id=pk)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
    user = request.user
    try:
        if not user.basket.cars.get(id=car.id) == Car.DoesNotExist:
            return Response({'error': 'This car is already on your basket'},
                            status=status.HTTP_400_BAD_REQUEST)
    except Car.DoesNotExist as e:
        user.basket.cars.add(car)
        user.basket.save()
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    ser = BasketSerializer(user.basket)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_basket(request, pk):
    try:
        car = Car.objects.get(id=pk)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    user = request.user
    try:
        user.basket.cars.remove(car)
        user.basket.save()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    ser = BasketSerializer(user.basket)
    return Response(ser.data, status=status.HTTP_200_OK)


class UserRegisterView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserRegisterSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                ser = UserSerializer(instance=user)
                return Response(ser.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


class CommentApiView(APIView):

    @permission_classes([IsAuthenticated, ])
    def post(self, request, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error': 'Authorization failed, log in with your credentials!'})
        data = request.data
        comment = Comment.objects.create(text=data['text'], author=request.user, on_car_id=pk)
        ser = CommentSerializer(comment)
        return Response(ser.data, status=status.HTTP_200_OK)

    def get(self, request, pk):
        comments = Car.objects.get(id=pk).comments.all()
        ser = CommentSerializer(comments, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def comment_edit(request, pk):
    if request.method == 'PUT':
        try:
            data = request.data['text']
            comment = Comment.objects.get(id=pk)
            if not request.user == comment.author:
                return Response({'error': 'It is not your comment!'}, status=status.HTTP_400_BAD_REQUEST)
            comment.text = data
            comment.save()
            ser = CommentSerializer(comment)
            return Response(ser.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            comment = Comment.objects.get(id=pk)
            if not request.user == comment.author:
                return Response({'error': 'It is not your comment!'}, status=status.HTTP_400_BAD_REQUEST)
            comment.delete()
            return Response({}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({}, status=status.HTTP_200_OK)



# @api_view(['GET', 'POST'])
# def car(request):
#     if request.method == 'GET':
#         cars_list = Car.objects.all()
#         serializer = CarSerializer(cars_list, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @api_view(['GET'])
# def cars_of_model(request, id):
#     try:
#         model = Model.objects.get(id=id)
#     except Model.DoesNotExist as e:
#         return Response({'error': str(e)})
#     if request.method == 'GET':
#         cars = model.cars_set.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)
#
#
# class CarsInBasket(APIView):
#     def get_object(self, id):
#         try:
#             return Car.objects.get(id=id)
#         except Car.DoesNotExist as e:
#             return Response({'error': str(e)})
#
#     def delete(self, request, pk):
#         car = self.get_object(pk)
#         basket = Basket.objects.get(id=2)
#         basket.car.remove(car)
#         return Response({'DELETED': True})
#
#     def post(self, request, pk):
#         car = self.get_object(pk)
#         basket = Basket.objects.get(id=2)
#         basket.car.add(car)
#         return Response({'ADDED': True})
#
#
# @api_view(['GET'])
# def carsByModel(request, id):
#     if request.method == 'GET':
#         cars_list = Car.objects.all()
#         carsByModel = []
#         for car in cars_list:
#             if car.model.id == id:
#                 serializer = CarSerializer(car)
#                 carsByModel.append(serializer.data)
#         return Response(carsByModel)
