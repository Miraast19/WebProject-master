from django.urls import path
from api.views import cars_of_basket, CarsListAPIView, CommentApiView, comment_edit, \
    car_details, model, ModelsListAPIView, car_by_model, add_to_basket, UserRegisterView, remove_basket
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('signup/', UserRegisterView.as_view()),

    path('cars/', CarsListAPIView.as_view()),
    path('cars/<int:pk>/', car_details),
    path('cars/<int:pk>/comments', CommentApiView.as_view()),
    path('comments/<int:pk>', comment_edit),

    path('models/', ModelsListAPIView.as_view()),
    path('models/<int:pk>/', model),
    path('models/<int:pk>/cars/', car_by_model),

    path('myprofile/', cars_of_basket),
    path('car/<int:pk>/to_basket', add_to_basket),
    path('car/<int:pk>/remove_basket', remove_basket),
]
