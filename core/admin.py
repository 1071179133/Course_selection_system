#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# author：chenjianwen
# email：1071179133@qq.com
import os
import sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.logger import logger
from core.modules import School
from lib.init_db_dir import databases
from lib import read_and_write_file as rw
from lib import get_list
data = rw.read(databases)

def build_school():
    school_name = input("创建学校的名字：").strip()
    school_addr = input("选择学校所在地：").strip()
    school_desc = input("对学校的简要描述：").strip()
    sc = School(school_name,school_addr,school_desc)
    sc.create_school()

def build_course():
    course_name = input("创建课程的名字：").strip()
    get_list.get_school_list()
    school_name = input("课程属于学校名字：").strip()
    #school_addr = input("该学校地址：").strip()
    course_desc = input("对课程的简要描述：").strip()
    course_price = input("课程的价格：").strip()
    study_cycle = input("课程的周期：").strip()
    sc = School(school_name, None, None)
    sc.create_course(course_name,course_desc,course_price,study_cycle)

def build_classes():
    classes_name = input("创建班级的名字：").strip()
    classes_actives = input("班级日常活动：").strip()
    classes_max_number = input("班级容纳最大人数：").strip()
    get_list.get_school_list()
    school_name = input("班级所在学校：").strip()
    #school_addr = input("该学校地址：").strip()
    get_list.get_teacher_list(school_name)
    belong_to_teacher = input("班级所属讲师：").strip()
    get_list.get_course_list(school_name)
    belong_to_course = input("班级授课课程：").strip()
    sc = School(school_name, None, None)
    sc.create_classes(classes_name,classes_actives,classes_max_number,belong_to_course,belong_to_teacher)

def build_teacher():
    teacher_name = input("创建讲师的名字：").strip()
    teacher_ID = input("创建讲师的ID：").strip()
    get_list.get_school_list()
    school_name = input("讲师所在学校：").strip()
    #school_addr = input("该学校所在地：").strip()
    teacher_age = input("讲师的年龄：").strip()
    teacher_sex = input("讲师的性别：").strip()
    teacher_major = input("讲师的专业：").strip()
    teacher_salary = input("讲师的工资：").strip()
    belong_to_school = school_name
    sc = School(school_name, None, None)
    sc.create_teacher(teacher_name,teacher_ID,teacher_age,teacher_sex,teacher_major,teacher_salary,belong_to_school)


def admin_action():
    menu = u'''
################## 管理员视图 ##################\033[32;1m
        1. 创建学校
        2. 创建课程
        3. 创建讲师
        4. 创建班级
        5. 返回上一级
        \033[0m'''
    menu_dic = {
        "1": build_school,
        "2": build_course,
        "3": build_teacher,
        "4": build_classes
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