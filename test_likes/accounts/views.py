from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, generics


from django.contrib.auth import get_user_model

from accounts.serializers import UserSerializer, UserRegistartionSerializer
from posts.models import Posts
from posts.serializers import PostsSerializer

User = get_user_model()




class UserModelViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(
            methods=['post', ], 
            detail=True, 
            serializer_class=PostsSerializer, 
            permission_classes=[IsAuthenticated, ])
    def add_post(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            post = Posts.objects.create(
                                    author=author,
                                    title=data['title'],
                                    description=data['description'])
            serializer = self.get_serializer_class()(post)

            return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegisterGenericAPIView(generics.GenericAPIView):

    serializer_class = UserRegistartionSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })
