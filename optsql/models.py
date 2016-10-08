#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *
from datetime import datetime

from settings import *

connect(db_name, host=db_host, username=db_username, password=db_password)

class Job(Document):
    name = StringField(required=True, max_length=24, verbose_name=u'职位名称')
    type = StringField(required=True, max_length=24, verbose_name=u'职位类别')
    address = StringField(required=True, max_length=24, default=u'深圳', verbose_name=u'职位类别')
    time = DateTimeField(default=datetime.now(), verbose_name=u'更新时间')
    info = StringField(max_length=1024, verbose_name=u'职位描述')
    require = StringField(max_length=1024, verbose_name=u'职位要求')

if __name__ == "__main__":
    '''仅供测试models代码'''
    job1 = Job(name='软件驱动工程师', type='研发工程师', address='深圳')
    job1.info = '''1、能熟练运用C语言进行软件的设计、调试和开发；
                2、能熟练阅读多种类型的芯片文档及电路原理图等资料，并根据资料进行驱动程序的编写；
                3、能熟悉主流外设（LCD、CAMERA、TP、各种SENSOR等）的调试'''
    job1.require = '''1、男女不限，计算机、电子、通讯等相关专业本科以上；
                    2、最好有1年以上行业工作经验；
                    3、工作积极、主动、灵活，服从工作安排，具有良好的团队合作意识；
                    4、具有一定的数字电子、模拟电子电路基础；
                    5、拥有一定的硬件调试经验、能熟练使用万用表、示波器等调试工具；
                    6、精通mtk6260,6261,2503平台的驱动调试'''
    job1.save()

    job2 = Job(name='高级软件工程师', type='研发工程师', address='深圳')
    job2.info = '''1、智能穿戴产品的人机交互界面设计与开发；
                2、应客户或市场需求对各种特殊功能进行设计与开发；
                3、对产品测试出的问题进行修改，以及对产品功能进行改进'''
    job2.require = '''1、男女不限，计算机、电子、通讯等相关专业本科以上；
                    2、熟悉C语言编程，了解嵌入式产品开发；
                    3、具有良好的表达沟通能力及团队合作精神；
                    4、逻辑思维清晰，对问题的分析解决能力强；
                    5、熟悉mtk6260,6261,2502,2503平台软件架构，能做mmi，及framework层的软件开发及客制化工作；
                    6、肯吃苦，有上进心，学习能力强'''
    job2.save()

    job3 = Job(name='高级硬件工程师', type='研发工程师', address='深圳')
    job3.info = '''1.能独立完成手机硬件设计及调试
                2.新项目评审及试产跟进，对试产不良进行分析，提出改善意见并实施验证
                3.对可靠性试验失败进行深入分析并给出改善方案
                4.对量产机型在生产线和售后发生的批量不良进行分析并给出改善方案
                5.主导项目进度和质量指标保证'''
    job3.require = '''1、本科以上学历，电子类、计算机类、通信类等相关专业毕业，5年以上电子电路设计的工作经验；
                2、熟悉手机开设计流程。具有MTK手机方案硬件研发经验，有手机、GPS、智能硬件等电子产品的开发经验，具备独立设计硬件原理图。
                3、能熟练使用pads工具设计原理图及完成layout。
                4、基本的英语读写和听说能力。
                5、具备良好的沟通能力和团队协作精神，能够吃苦耐劳，具备团队管理经验'''
    job3.save()