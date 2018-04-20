#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# author：chenjianwen
# email：1071179133@qq.com
import os
import sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.admin import admin_action
from core.teacher import teacher_action
from core.student import student_action

if __name__ == "__main__":
    menu = u'''
    ################## 选课系统 ##################\033[32;1m
            1. 管理员视图
            2. 讲师视图
            3. 学员视图
            4. 退出...
            \033[0m'''
    menu_dic = {
        "1": admin_action,
        "2": teacher_action,
        "3": student_action
    }

    while True:
        print(menu)
        choice = input("请输入操作序号：").strip()
        if choice == '4':
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