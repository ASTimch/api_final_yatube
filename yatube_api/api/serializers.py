from django.contrib.auth import get_user_model
from posts.models import Comment, Follow, Group, Post
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

MESSAGE_FOLLOW_ALREADY_EXISTS = "Пользователь уже подписан на данного автора."

MESSAGE_CANNOT_FOLLOW_HIMSELF = "Нельзя подписаться на самого себя."

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("post",)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        fields = ("user", "following")
        model = Follow
        read_only_fields = ("user",)

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message=MESSAGE_FOLLOW_ALREADY_EXISTS,
            )
        ]

    def validate_following(self, value):
        request = self.context.get("request", None)
        current_user = request.user

        if value == current_user:
            raise serializers.ValidationError(MESSAGE_CANNOT_FOLLOW_HIMSELF)
        return value
