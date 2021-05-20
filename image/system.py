# -*- coding: utf-8 -*

from django.db import connection
from PIL import Image, ImageDraw, ImageFont


# 合成图片方法
def compound(son_img, user_id, name):
    # 字体样式
    regular_font = ImageFont.truetype('simhei.ttf', size=32, encoding="utf-8")
    # 工牌模板图片 位置
    M_Img = Image.open('../stores/u/mo.jpg')
    try:
        # 缩小为原来的一半
        # factor = 2

        # size_w = int(S_Img_w / factor)
        # size_h = int(S_Img_h / factor)
        # 防止子图尺寸大于母图
        # if S_Img_w > size_w:
        #     S_Img_w = size_w
        # if S_Img_h > size_h:
        #     S_Img_h = size_h
        # 基础宽度
        basewidth = 370
        baseheight = 520
        # 员工头像
        S_Img = Image.open(son_img)
        # 获取小图的大小（子图）
        S_Img_w, S_Img_h = S_Img.size
        wpercent = (basewidth / float(S_Img_w))
        hsize = int(float(S_Img_h) * float(wpercent))
        if hsize > baseheight:
            hsize = baseheight
        print hsize
        # 获取母图
        draw = ImageDraw.Draw(M_Img)
        icon = S_Img.resize((basewidth, hsize), Image.ANTIALIAS)
        # 粘贴的位置
        coordinate = (130, 140)
        # 粘贴操作
        M_Img.paste(icon, coordinate, mask=None)
        # 利用ImageDraw的内置函数，在图片上写入文字
        if len(name) == 2:
            name_position = (285, 714)
        elif len(name) == 3:
            name_position = (272, 714)
        draw.text(name_position, name, font=regular_font)
        # 保存图片 (这里没有文件夹需要新建文件夹)
        save_img = '../stores/u/0520/' + str(user_id) + '_' + name + '.jpg'
        M_Img.save(save_img)
        print name + u"工牌生成成功"
    except:
        pass


sql = """
    select u.id,u.REALNAME from USERS u
    inner join USERS_POSTS up
    on u.id= up.USER_ID
    where u.STATUS=200 and up.STATUS=200
    and up.IS_MAIN=1 and up.UNIT_ID=2
"""
cursor = connection.cursor()
cursor.execute(sql)
users = cursor.fetchall()
for user in users:
    user_id = user[0]
    name = user[1]
    son_img = "../stores/u/" + str(user_id) + "/photo.jpg"
    compound(son_img, user_id, name)
