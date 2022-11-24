from rest_framework import serializers
from django.contrib.auth import get_user_model
# from reviews.models import Review
from movies.models import Movie, Comment, Genre
from communities.models import Community_comment, Community
from movies.models import Rank


class ProfileSerializer(serializers.ModelSerializer):


    class CommunitySerializer(serializers.ModelSerializer):

        class Meta:
            model = Community
            fields = ('pk', 'title', 'content', 'user')

    community_set = CommunitySerializer(many=True, read_only=True)


    class CommunityCommentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Community_comment
            fields = ('pk', 'content', 'user', 'community')

    community_comment = CommunityCommentSerializer(many=True, read_only=True)

    

    class CommentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            fields = '__all__'
            read_only_fields = ('movie', 'user')

    comments = CommentSerializer(many=True, read_only=True)



    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    
    followers = UserSerializer(many=True)

    class RankSerializer(serializers.ModelSerializer):

        class Meta:
            model = Rank
            fields = ('user', 'rank', 'movie')

    ranks = RankSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'followings', 'followers', 'like_movies', 'community_set', 'comments', 'community_comment', 'genre_dict', 'genre_recommend_dict', 'ranks')
        # read_only_fields = ()
