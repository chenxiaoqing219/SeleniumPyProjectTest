# -*- coding: UTF-8 -*-
# @Time : 2022/4/1 16:55
# @File : read_image.py
# @Software : PyCharm
import base64
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
'''
image = Image.open('./renren.png')
text = pytesseract.image_to_string(image)
print(text)
'''
with open('./renren.png', 'rb') as fp:
    image_base64 = str(base64.b64encode(fp.read()), encoding='utf-8')
r = ShowapiRequest("http://route.showapi.com/2360-2","904965","ef5258484b1b49e68ce675b72b97a923" )
r.addBodyPara("file_base64", image_base64)
res = r.post()
print(res.text) # 返回信息
res.json()['showapi_res_body']['']