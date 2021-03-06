#! /usr/bin/env python
#-*- coding: utf-8 -*-
#代码来自https://blog.csdn.net/zz683693/article/details/73499646/
from naoqi import ALProxy

robot_ip ="192.168.124.10"#NAO的IP地址。注：确保主机和NAO处于同一局域网
#robot_ip = "117.152.92.95" #NAO的IP地址。注：确保主机和NAO处于同一局域网
robot_port = 9559   # default port : 9559

tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)

#tts.setLanguage("English")
#tts.say("Hello, world! I am Nao robot!")

# 切换语言包需要较长时间，故尽量不要在程序运行时切换；
tts.setLanguage("Chinese")
tts.say("你好，我是闹机器人。")
tts.say("我可以说流利的绕口令:")
tts.say("打南边来了一个喇嘛,手里提着五斤鳎蚂,打北边来了一个哑巴,腰里别着一个喇叭")
tts.say("提搂鳎蚂的喇嘛要拿鳎蚂去换别着喇叭的哑巴的喇叭,别着喇叭的哑巴不愿意拿喇叭去换提搂鳎蚂的喇嘛的鳎蚂")

tts.say('粉红墙上画凤凰，凤凰画在粉红墙。')
tts.say(' 红凤凰、粉凤凰，红粉凤凰、花凤凰。')
tts.say('红凤凰,黄凤凰,红粉凤凰,粉红凤凰,花粉花凤凰。')
