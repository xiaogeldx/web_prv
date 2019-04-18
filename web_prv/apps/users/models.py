from django.db import models
#把UserManager类重命名_UserManager，用于重写
from django.contrib.auth.models import AbstractUser, UserManager as _UserManager
# Create your models here.

class UserManager(_UserManager):    #继承框架的UserManager
    """
    define user manager for modifing 'no need email'
    定义用于修改“无需电子邮件”的用户管理器当运行  python manager.py createsuperuser
    when 'python manager.py createsuperuser'

    """
    #设置email的默认值为None
    def create_superuser(self,username,password,email=None,**extra_fields):
        super(UserManager,self).create_superuser(username=username,
                                                 password=password,
                                                 email=email,**extra_fields)

class Users(AbstractUser):
    """
    add mobile,email_active fields to django users models
    """
    objects = UserManager()
    # A list of the field names that will be prompted for
    # when creating a user via the createsuperuser management command
    # REQUIRED_FIELS是AbstractUser提供的参数，
    # 除了用户名和密码是必须的，其他的想要添加的字段往参数里添加
    REQUIRED_FIELDS = ['mobile']
    # help_test在api接口文档中会用到
    # verbose_name在admin站点中会用到
    #增加手机号验证字段
    mobile = models.CharField(max_length=11,unique=True,verbose_name='手机号',
                              help_text='手机号',
                              error_messages={'unique':'此手机号已被注册'}
                              ) #指定报错的中文信息
    # 邮箱状态默认为关闭，本项目不用邮箱验证，用手机号验证
    email_active = models.BooleanField(default=False,verbose_name='邮箱验证状态')

 #元类
    class Meta:
        db_table = 'tb_users'   #指明数据库表名
        verbose_name = '用户'     #在admin站点中显示的名称
        verbose_name_plural = verbose_name  #显示的复数名称

    def __str__(self):  #打印对象时调用
        return self.username