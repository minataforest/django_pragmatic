from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Article(models.Model):
    # on_delete=models.SET_NULL: 회원탈퇴 시, 게시글 지워지지 않고 주인 없는 게시글이 됨
    # related_name은 User 객체에서 접근하기 위한 이름이므로 article로 한다
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="article", null=True
    )
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, related_name="article", null=True
    )

    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="article/", null=False)
    content = models.TextField(null=True)

    # auto_now_add=True 생성시간 자동생성
    created_at = models.DateField(auto_now_add=True, null=True)
