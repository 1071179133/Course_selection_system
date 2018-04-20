#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# author：chenjianwen
# email：1071179133@qq.com
import os
import sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.logger import logger
from core.modules import Teacher
from lib.init_db_dir import databases
from lib import read_and_write_file as rw
data = rw.read(databases)

def begin_classes():
    logger.info("===============设置班级上课===============")
    teacher_ID = input("请输入讲师ID:").strip()
    teacher_name = input("请输入讲师名字：").strip()
    logger.info("===============班级列表===============")
    for classes_name in data["classes"]:
        print(classes_name)
    classes_name = input("请输入需要上课的班级：").strip()
    th = Teacher(teacher_ID,teacher_name)
    th.classing_in(classes_name)

def end_classes():
    logger.info("===============设置班级下课===============")
    teacher_ID = input("请输入讲师ID:").strip()
    teacher_name = input("请输入讲师名字：").strip()
    logger.info("===============班级列表===============")
    for classes_name in data["classes"]:
        print(classes_name)
    classes_name = input("请输入需要下课的班级：").strip()
    th = Teacher(teacher_ID, teacher_name)
    th.classing_out(classes_name)

def see_student_list():
    logger.info("===============查看班级学员信息===============")
    teacher_ID = input("请输入讲师ID:").strip()
    teacher_name = input("请输入讲师名字：").strip()
    logger.info("===============班级列表===============")
    for classes_name in data["classes"]:
        print(classes_name)
    classes_name = input("请输入查看班级学员信息的班级名字：").strip()
    th = Teacher(teacher_ID, teacher_name)
    th.lookup_student_list(classes_name)

def marking_grade():
    logger.info("===============给学生评分===============")
    teacher_ID = input("请输入讲师ID:").strip()
    teacher_name = input("请输入讲师名字：").strip()
    logger.info("===============班级列表===============")
    for classes_name in data["classes"]:
        print(classes_name)
    classes_name = input("学生所在班级：").strip()
    student_ID = input("学生ID号：").strip()
    student_grade = input("学生分数:").strip()
    th = Teacher(teacher_ID,teacher_name)
    th.marking(classes_name,student_ID,student_grade)

def teacher_action():
    menu = u'''
################## 讲师视图 ##################\033[32;1m
        1. 设定班级上课
        2. 设定班级下课
        3. 查看班级学员列表信息
        4. 给学员评分
        5. 返回上一级
        \033[0m'''
    menu_dic = {
        "1": begin_classes,
        "2": end_classes,
        "3": see_student_list,
        "4": marking_grade
    }

    while True:
        print(menu)
        choice = input("请输入操作序号：").strip()
        if choice == '5':
            break
        else:
            if choice in menu_dic:
                menu_dic[choice]()
                # time.sleep(1)
                input('输入任意键继续：')
                print("\n")
                continue
            else:
                print("输入有误，请重新输入")
                continue
