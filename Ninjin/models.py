from django.conf import settings
from django.db import models

from accounts.models import CustomUser


class Category(models.Model):
    category_title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す

        :return: （カテゴリ名）
        '''
        return self.category_title



class Post(models.Model):
    post_by_user = models.ForeignKey(
        CustomUser,

        verbose_name='ユーザー',

        on_delete=models.CASCADE
    )
    post_category = models.ForeignKey(
        Category,

        verbose_name='カテゴリ',

        on_delete=models.PROTECT
    )

    theme_title = models.TextField('お題のタイトル')


    updated_at = models.DateTimeField("更新日", auto_now=True)

    image = models.ImageField(
        verbose_name='イメージ',  # フィールドのタイトル
        upload_to='photos'  # MEDIA＿ROOT以下のフォトファイルに保存
    )

    #　投稿日のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True # 日時を自動追加
    )



class Answer(models.Model):
    answer_by = models.ForeignKey(
        CustomUser,

        verbose_name='ユーザー',

        on_delete=models.CASCADE
    )

    answer_to = models.ForeignKey(
        Post,
        verbose_name="大喜利のお題",
        on_delete=models.CASCADE
    )

    text = models.TextField('お題に対する回答')

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',  # フィールドのタイトル
        auto_now_add=True  # 日時を自動追加
    )

    def __str__(self):
        return self.text


class LikeForComment(models.Model):
    """コメントに対するいいね"""
    like_for_to = models.ForeignKey(Answer, on_delete=models.CASCADE)
    like_for_user = models.ForeignKey(
        CustomUser,

        verbose_name='ユーザー',

        on_delete=models.CASCADE
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',  # フィールドのタイトル
        auto_now_add=True  # 日時を自動追加
    )

class LikeForPost(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser,

        verbose_name='ユーザー',

        on_delete=models.CASCADE
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',  # フィールドのタイトル
        auto_now_add=True  # 日時を自動追加
    )





