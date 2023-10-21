# 课程模块
import requests
import config

class CourseAPI:

    def __init__(self):

        self.add_course_url = config.BASE_URL + '/api/clues/course'
        self.select_course_url = config.BASE_URL + '/api/clues/course/list'

    # 1.添加课程
    def add_course(self,data,token):

        res = requests.post(url=self.add_course_url,json=data,headers={"Authorization":token})
        return res

    # 2.课程列表查询
    def select_course(self,test_data,token):

        res = requests.get(url=self.select_course_url + f'/{test_data}',headers={"Authorization":token})
        return res

    # 3.修改课程
    def update_course(self,data,token):

        res = requests.put(url=self.add_course_url,json=data,headers={"Authorization":token})
        return res

    # 4.删除课程
    def delete_course(self,data,token):

        res = requests.delete(url=self.add_course_url + f'/{data}',headers={"Authorization":token})
        return res