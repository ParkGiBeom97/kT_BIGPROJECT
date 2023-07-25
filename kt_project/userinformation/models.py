from django.db import models
import datetime

from .validators import  validate_id_input, validate_pw_input, validate_phone_input, validate_gender_input
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
    
class user_info(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    disease = models.CharField(max_length=50)
    admin = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default='')
    
class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, password, **extra_fields):
        # 필요한 필드와 유효성 검사를 추가
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, **extra_fields):
        # 필요한 필드와 유효성 검사를 추가
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(user_id, password, **extra_fields)    

class AccountInfo(AbstractBaseUser):
    # 계정 ID. 중복 불가하고 영문 숫자 조합만 가능, 최대 20자
    user_id = models.CharField(max_length=20, unique = True, 
                               error_messages = {'unique' : '이미 있는 아이디입니다.'},
                               validators = [validate_id_input])
    
    #계정 비밀번호. 최소 8자 최대 20자, 영문 숫자 특수문자 조합 가능
    pw = models.CharField(max_length=20,
                          validators = [validate_pw_input])
    
    #사용자 이름. 최대 10자
    name = models.CharField(max_length=10)
    
    #사용자 성별.M 또는 F 만 입력 가능
    gender = models.CharField(max_length=1,
                                     validators = [validate_gender_input])
    
    #계정 이메일.
    # email = models.EmailField(max_length=254)
    
    #휴대전화 번호. 숫자와 -만 입력 가능하고 반드시 13자(010-1234-5678)
    phone = models.CharField(max_length = 13, validators = [validate_phone_input])
    
    # 관리자 여부. default값은 False(환자 계정)
    admin = models.BooleanField(default = False)
    
    # 사용자가 관리자인지 여부를 나타내는 'is_staff' 속성 추가
    is_staff = models.BooleanField(default=True)
    
    #병명 이름
    disease = models.CharField(max_length=200, default =[], blank = True)
    
    #생년월일.
    birthdate = models.DateField(default = datetime.date.today )
    
    #예전 수술 이력 선택. default값에 메세지 달아줘야 하는지? 프론트에서 가능한지?
    has_surgery = models.BooleanField(default = False)
    
    #지금, 예전에 갖고 있는 병 선택. 검색은 텍스트로 하고, 있는지는 선택으로 해야할것같은데...
    #그 외 특이사항. ex_ 흡연, 임부, 알러지 등. 
    
    #계정 생성일, 수정일
    dt_created = models.DateField(auto_now_add=True,)
    dt_modified = models.DateField(auto_now=True,)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'user_id'

    #사용자 먹는 알약 필드
    user_pill = models.CharField(default='', max_length=100)
    
    #특이사항
    user_specialnote = models.CharField(max_length=200, default="", blank=True)

    
    def check_password(self, password):
        return check_password(password, self.pw)
    
    def __str__(self):
        return self.user_id
    
    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    # def save(self, *args, **kwargs):
    #     if self.birthdate and isinstance(self.birthdate, str):
    #         self.birthdate = convert_date_format(self.birthdate)
    #     super().save(*args, **kwargs)

    # def convert_date_format(date_string):
    #     parts = date_string.split('. ')
    #     year = parts[0]
    #     month = parts[1].split('. ')[0].strip()
    #     day = parts[2].strip()
    #     return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    

    