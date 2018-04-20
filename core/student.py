#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# author：chenjianwen
# email：1071179133@qq.com
import os
import sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.logger import logger
from core.modules import Student
from lib.init_db_dir import databases
from lib import read_and_write_file as rw
from lib import get_list
data = rw.read(databases)

def enroll():
    logger.info("=============学生注册界面=============")
    student_ID = input("请输入你的注册账号(qq/电话号码)：").strip()
    if student_ID not in data["student"]:
        student_name = input("请输入你的名字：").strip()
        logger.info("=============完善学生信息=============")
        student_age = input("请输入你的年龄：").strip()
        student_sex = input("请输入你的性别：").strip()
        student_money = int(input("请确认你的余额：").strip())

        get_list.get_school_list()
        belong_to_school = input("请选择你报名的学校：").strip()

        get_list.get_course_list(belong_to_school)
        belong_to_course = input("请选择你学习的课程：").strip()

        get_list.get_classes_list(belong_to_course)
        belong_to_classes = input("请选择你的班级：").strip()
        if data["classes"][belong_to_classes]["belong_to_course"] == belong_to_course:
            st = Student(student_ID, student_name)
            st.create_student(student_age,student_sex,student_money,belong_to_school,belong_to_classes,belong_to_course)
        else:
            logger.error("班级{}的课程不是{},注册失败".format(belong_to_classes,belong_to_course))
    else:
        logger.error("学生ID[{}]已被注册，不可重复注册".format(student_ID))


def pay_tuition():
    logger.info("=============学生缴费界面=============")
    student_ID = input("请输入你的学生ID:").strip()
    student_name = input("请输入你的名字：").strip()
    st = Student(student_ID, student_name)
    st.pay_tuition()

def student_action():
    menu = u'''
################## 学生视图 ##################\033[32;1m
        1. 注册
        2. 缴费
        3. 返回上一级
        \033[0m'''
    menu_dic = {
        "1": enroll,
        "2": pay_tuition
    }

    while True:
        print(menu)
        choice = input("请输入操作序号：").strip()
        if choice == '3':
            break
        else:
            if choice in menu_dic:
                menu_dic[choice]()
                #time.sleep(1)
                input('输入任意键继续：')
                print("\n")
                continue
            else:
                print("输入有误，请重新输入")
                continue