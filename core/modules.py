#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# author：chenjianwen
# email：1071179133@qq.com

import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.init_db_dir import databases
from lib.logger import logger
from lib import read_and_write_file as rw

class School(object):
    def __init__(self,schoo_name,school_address,school_desc):
        self.schoo_name = schoo_name
        self.school_address = school_address
        self.school_desc = school_desc
        self.data = rw.read(databases)

    def create_school(self):
        '''
        创建学校
        :return: self.data
        '''
        if self.schoo_name in self.data["school"]:
            logger.error("[{}]已存在，不可重复创建".format(self.schoo_name))
        else:
            self.data["school"][self.schoo_name] = {}
            self.data["school"][self.schoo_name] = {
                "name":self.schoo_name,
                "address":self.school_address,
                "desc":self.school_desc
            }
            if rw.write(self.data,databases):
                logger.info("[{}]写入数据库，创建成功".format(self.schoo_name))
            else:
                logger.error("[{}]创建失败".format(self.schoo_name))

    def create_course(self,course_name,course_desc,course_price,study_cycle):
        '''
        创建课程
        :param course_name: 课程名字
        :param course_desc: 课程描述
        :param course_price: 课程价格
        :param study_cycle: 课程周期
        :return: self.data
        '''
        if course_name in self.data["course"]:
            logger.error("[{}]课程已存在，不可重复创建".format(course_name))
        else:
            self.data["course"][course_name] = {}
            self.data["course"][course_name] = {
                "course_name":course_name,
                "course_desc":course_desc,
                "course_price":course_price,
                "study_cycle":study_cycle,
                "belong_to_school":self.schoo_name
            }
            if rw.write(self.data,databases):
                logger.info("[{}]课程写入数据库，创建成功".format(course_name))
            else:
                logger.error("[{}]课程创建失败".format(course_name))

    def create_classes(self,classes_name,classes_actives,classes_max_number,belong_to_course,belong_to_teacher):
        '''
        创建班级
        :param classes_name: 班级名字
        :param classes_actives: 班级最新活动
        :param classes_max_number: 班级人数
        :param belong_to_course: 班级课程
        :param belong_to_teacher：班级讲师
        :return: self.data
        '''
        if classes_name in self.data["classes"]:
            logger.error("[{}]已存在，不可重复创建".format(classes_name))
        else:
            self.data["classes"][classes_name] = {}
            self.data["classes"][classes_name] = {
                "classes_name":classes_name,
                "classes_actives":classes_actives,
                "classes_max_number":classes_max_number,
                "belong_to_course":belong_to_course,
                "belong_to_teacher":belong_to_teacher,
                "classing_status": False
            }
            if rw.write(self.data,databases):
                logger.info("[{}]写入数据库，创建班级成功".format(classes_name))
            else:
                logger.error("[{}]创建失败".format(classes_name))

    def create_teacher(self,teacher_name,teacher_ID,teacher_age,teacher_sex,teacher_major,teacher_salary,belong_to_school):
        '''
        创建讲师
        :param teacher_name: 讲师名字
        :param teacher_ID: 讲师省份证号
        :param teacher_age: 讲师年龄
        :param teacher_sex: 讲师性别
        :param teacher_major: 讲师专业技术
        :param teacher_salary: 讲师薪酬
        :return: self.data
        '''
        if teacher_name in self.data["teacher"]:
            logger.error("[{}]讲师已存在，不可重复创建".format(teacher_name))
        else:
            self.data["teacher"][teacher_name] = {}
            self.data["teacher"][teacher_name] = {
                "teacher_name":teacher_name,
                "teacher_ID":teacher_ID,
                "teacher_age":teacher_age,
                "teacher_sex":teacher_sex,
                "teacher_major":teacher_major,
                "teacher_salary":teacher_salary,
                "belong_to_school":belong_to_school
            }
            if rw.write(self.data,databases):
                logger.info("[{}]讲师写入数据库，创建讲师成功".format(teacher_name))
            else:
                logger.error("[{}]讲师创建失败".format(teacher_name))


# sc = School("北京大学","北京","描述信息")
# sc.create_school()
# sc.create_course("python自动化运维开发","python自动化运维开发-描述信息",7000,"240天")
# sc.create_course("linux云计算","python自动化运维开发-描述信息",7000,"240天")
# sc.create_course("go语言开发","python自动化运维开发-描述信息",7000,"240天")
# sc.create_classes("python_1班","无",40,"python自动化运维开发","陈建文",)
# sc.create_teacher("陈建文","440921199109245137",23,"男","python",10000,"北京大学")
# sc.create_teacher("谢美君","440921199109245137",23,"男","python",10000,"北京大学")


class Teacher(object):
    def __init__(self,teacher_ID,teacher_name):
        self.teacher_ID = teacher_ID
        self.teacher_name = teacher_name
        self.data = rw.read(databases)

    def classing_in(self,classes_name):
        '''
        讲师设置班级上课的状态
        :param classes_name: 上课班级的名字
        :return: self.data
        '''
        if classes_name in self.data["classes"]:
            if self.teacher_name == self.data["classes"][classes_name]["belong_to_teacher"]:
                self.data["classes"][classes_name]["classing_status"] = True
                if rw.write(self.data, databases):
                    logger.info("班级[{}]正在上课".format(classes_name))
            else:
                logger.error("[{}]无权限管理班级[{}]，请记住自己负责的班级".format(self.teacher_name,classes_name))
        else:
            logger.error("班级[{}]不存在，无法管理".format(classes_name))

    def classing_out(self,classes_name):
        '''
        讲师设置班级上课的状态
        :param classes_name: 下课班级的名字
        :return: self.data
        '''
        if classes_name in self.data["classes"]:
            if self.teacher_name == self.data["classes"][classes_name]["belong_to_teacher"]:
                self.data["classes"][classes_name]["classing_status"] = False
                if rw.write(self.data, databases):
                    logger.info("班级[{}]已下课".format(classes_name))
            else:
                logger.error("[{}]无权限管理班级[{}]，请记住自己负责的班级".format(self.teacher_name,classes_name))
        else:
            logger.error("班级[{}]不存在，无法管理".format(classes_name))

    def lookup_student_list(self,classes_name):
        '''
        查看班级学生列表
        :param classes_name: 班级名字
        :return: self.data
        '''
        logger.info("=======================查看班级[{}]学生列表=======================".format(classes_name))
        for student_ID in self.data["student"]:
            if classes_name == self.data["student"][student_ID]["belong_to_classes"]:
                student_name = self.data["student"][student_ID]["student_name"]
                student_grade = self.data["student"][student_ID]["student_grade"]
                logger.info("学号:{},名字:{},分数:{}".format(student_ID,student_name,student_grade))
        logger.info("=======================查看班级[{}]学生列表=======================".format(classes_name))

    def marking(self,classes_name,student_ID,student_grade):
        '''
        给某个班级某学生打分
        :param classes_name: 班级名字
        :param student_ID: 学生ID号
        :param student_grade: 给学生打的分数
        :return: self.data
        '''
        student_classes = self.data["student"][student_ID]["belong_to_classes"]
        if student_classes == classes_name and self.teacher_name == self.data["classes"][classes_name]["belong_to_teacher"]:
            self.data["student"][student_ID]["student_grade"] = student_grade
            if rw.write(self.data,databases):
                logger.info("[{}]给学生[{}]打分[{}分]成功".format(self.teacher_name,student_ID,student_grade))
            else:
                logger.error("[{}]给学生[{}]打分失败".format(self.teacher_name,student_ID))
        else:
            logger.error("[{}]不是你负责的学生".format(student_ID))

# th = Teacher("1071179133","陈建文")
# th.classing_in("python_1班")
# th.classing_out("python_1班")
# th.lookup_student_list("python_1班")
# th.marking("python_1班","1071179133",100)

class Student(object):
    def __init__(self,student_ID,student_name):
        self.student_ID = student_ID
        self.student_name = student_name
        self.data = rw.read(databases)

    def create_student(self,student_age,student_sex,student_money,belong_to_school,belong_to_classes,belong_to_course):
        '''
        学生注册
        :param student_age: 学生年龄
        :param student_sex: 学生性别
        :param tuition_status: 学生缴费状态
        :param student_money: 学生钱包
        :param belong_to_school: 学生属于哪间学校
        :param belong_to_classes: 学生属于哪个班级
        :param belong_to_course: 学生报读哪个课程
        :return: self.data
        '''
        if self.student_ID in self.data["student"]:
            logger.error("[{}]已存在，不可重复注册".format(self.student_name))
        else:
            self.data["student"][self.student_ID] = {}
            self.data["student"][self.student_ID] = {
                "student_ID":self.student_ID,
                "student_name":self.student_name,
                "student_age":student_age,
                "student_sex":student_sex,
                "student_grade": 0,
                "tuition_status":None,
                "student_money":student_money,
                "belong_to_school":belong_to_school,
                "belong_to_classes":belong_to_classes,
                "belong_to_course":belong_to_course
            }
            if rw.write(self.data,databases):
                logger.info("[{}]学生写入数据库，创建学生成功".format(self.student_name))
            else:
                logger.error("[{}]学生创建失败".format(self.student_name))

    def pay_tuition(self):
        if not self.student_ID in self.data["student"]:
            logger.error("学号[{}]不存在，不可交学费".format(self.student_ID))
        else:
            belong_to_course = self.data["student"][self.student_ID]["belong_to_course"]
            tuition = self.data["course"][belong_to_course]["course_price"]
            student_money = self.data["student"][self.student_ID]["student_money"]
            if student_money >= tuition:
                self.data["student"][self.student_ID]["student_money"] = student_money - tuition
                self.data["student"][self.student_ID]["tuition_status"] = True
                if rw.write(self.data, databases):
                    logger.info("[{}][{}]缴费[{}元]成功".format(self.student_name,self.student_ID,tuition))
            else:
                logger.error("[{}]的余额小于课程[{}]学费金额，无法缴费".format(self.student_name,belong_to_course))

# st = Student("1071179133","陈建文")
# st.create_student(23,"男",20000,"北京大学","python_1班","linux云计算")
# st.pay_tuition()