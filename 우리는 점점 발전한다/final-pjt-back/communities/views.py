from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# # permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import CommunitySerializer, CommunityCommentSerializer
from .models import Community, Community_comment
from accounts.models import User



@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def community_list(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def community_detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    # community = Community.objects.get(pk=community_pk)

    if request.method == 'GET':
        serializer = CommunitySerializer(community)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET','POST'])
def comment(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    username = request.user.username
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        
        comments = community.community_comment_set.all()
        serializer = CommunityCommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommunityCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, community=community)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Community_comment, pk=comment_pk)
    username = request.user.username
    user = get_object_or_404(User, username=username)

    if request.method == 'GET':
        serializer = CommunityCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if comment.user == user:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommunityCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            if comment.user == user:
                serializer.save()
        return Response(serializer.data)




