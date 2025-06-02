from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Helper to get tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def register_user(request):
    data = request.data
    if User.objects.filter(username=data['email']).exists():
        return Response({'error': 'User already exists'}, status=400)

    user = User.objects.create_user(
        username=data['email'],
        email=data['email'],
        password=data['password'],
        first_name=data.get('name', ''),
    )
    return Response({'message': 'User created successfully'}, status=201)


@api_view(['POST'])
def login_user(request):
    data = request.data
    user = authenticate(username=data['email'], password=data['password'])

    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response({'message': 'Login successful', 'tokens': tokens})
    else:
        return Response({'error': 'Invalid credentials'}, status=401)
