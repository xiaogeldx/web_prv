from django.shortcuts import render
from utils.captcha.captcha import captcha   #utils/captcha/captcha.py   captcha实例
# Create your views here.
from django.http import HttpResponse
from django_redis import get_redis_connection
from django.views import View


class ImageCode(View):
    """
    /image_codes/
    """
    def get(self,request,image_code_id):
        #见captcha.py的最后一行，即输出的元组
        text,image = captcha.generate_captcha()     #获取元组
        # 连接设置中的redis的库名，这种短暂存储一般用redis
        con_redis = get_redis_connection(alias='verify_codes')
        #键值对方式
        img_key = 'img_{}'.format(image_code_id)
        #第一个参数是键，第二个参数是图形验证码有效时长，单位是秒，第三个参数是值
        con_redis.setex(img_key,300,text)
        return HttpResponse(content=image,content_type='image/jpg')



