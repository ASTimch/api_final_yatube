from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст поста", help_text="Введите текст поста"
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
        verbose_name="Картинка",
        help_text="Загрузите картинку",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name="Группа",
        help_text="Группа, к которой будет относиться пост",
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
        help_text="Пост, которому предназначен комментарий",
    )
    text = models.TextField(
        verbose_name="Текст комментария", help_text="Введите текст комментария"
    )
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )

    class Meta():
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Пользователь",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Подписан на автора",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = (
            models.UniqueConstraint(
                fields=["user", "following"], name="unique_user_following"
            ),
        )

    def __str__(self):
        return (
            self.user.get_full_name()
            + " подписан на "
            + self.following.get_full_name()
        )
