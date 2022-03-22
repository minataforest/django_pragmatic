from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # OneToOneField: Profile과 User 객체를 하나씩 연결해줌.
    # CASCADE: 연결되어 있는 User 객체가 사라지면 Profile는 어떻게 할지 설정. 여기서는 삭제한다.
    # related_name: 후에 request.user.profile 형식으로 해당 객체를 쓸 수 있음
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    #  upload_to : 이미지가 업로드 되는 경로 (여기서는 media/profile)
    image = models.ImageField(upload_to="profile/", null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
