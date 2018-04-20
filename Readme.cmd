1.程序文件及说明：
Course_selection_system  #程序主目录
|-- bin #执行目录
|   `-- main.py  #程序入口
|-- conf  #配置文件目录
|-- core  #核心代码
|   |-- admin.py  #管理员视图
|   |-- modules.py  #实现功能类
|   |-- __pycache__
|   |   |-- admin.cpython-35.pyc
|   |   |-- modules.cpython-35.pyc
|   |   |-- student.cpython-35.pyc
|   |   `-- teacher.cpython-35.pyc
|   |-- student.py  #学员视图
|   `-- teacher.py  #讲师视图
|-- db  #数据存放目录
|   |-- database.json  #存放数据文件
|-- lib  #调用工具库
|   |-- init_db_dir.py  #初始化数据目录及数据结构
|   |-- logger.py  #日志调用接口
|   |-- __pycache__
|   |   |-- init_db_dir.cpython-35.pyc
|   |   |-- logger.cpython-35.pyc
|   |   `-- read_and_write_file.cpython-35.pyc
|   `-- read_and_write_file.py  #读写数据接口
`-- log  #日志存放目录
    |-- access.log
    |-- access.log.2018-04-07
    `-- access.log.2018-04-14

2.python版本：python-3.5.3

3.程序使用：python main.py    根据提示使用程序

5.程序功能解析：

    ################## 选课系统 ##################
            1. 管理员视图
            2. 讲师视图
            3. 学员视图
            4. 退出...
            
请输入操作序号：

8.程序博客地址：http://www.cnblogs.com/chenjw-note/p/8523716.html 

9.github项目地址：https://github.com/1071179133/Course_selection_system.git