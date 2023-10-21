# 单接口测试用例-查询课程列表
from api.login import LoginApi
from api.course import CourseAPI

class TestFindCourseCase:

    token = None

    def setup(self):
        # 初始化
        self.login_api = LoginApi()
        self.course_api = CourseAPI()
        # 登录
        vetify_res = self.login_api.vetify_code()
        uuid = vetify_res.json()["uuid"]
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid
        }
        login_res = self.login_api.login(login_data)
        TestFindCourseCase.token = login_res.json()["token"]


    def teardown(self):
        pass

    # 1.查询成功(存在的课程名称)
    def test01_exits_course_name(self):

        res = self.course_api.select_course(test_data='?name=测试开发提升课01',token=TestFindCourseCase.token)
        print(res.json())
        assert 200 == res.status_code
        assert '成功' in res.text
        assert 200 == res.json().get("code")


    # 2.查询成功(不存在的课程名称)
    def test02_not_exits_course_name(self):

        res = self.course_api.select_course(test_data='?name=测试开发pacc提升课01', token=TestFindCourseCase.token)
        assert 200 == res.status_code
        assert '成功' in res.text
        assert 200 == res.json().get("code")

    # 3.查询成功(输入所有字段)
    def test03_all_params_right(self):

        res = self.course_api.select_course(test_data='?name=测试开发提升课02&subject=6&price=899&applicablePerson=2&info=测试开发提升课02', token=TestFindCourseCase.token)
        assert 200 == res.status_code
        assert '成功' in res.text
        assert 200 == res.json().get("code")

    # 4.查询成功(不输入参数)
    def test04_params_null(self):

        res = self.course_api.select_course(test_data='', token=TestFindCourseCase.token)
        assert 200 == res.status_code
        assert '成功' in res.text
        assert 200 == res.json().get("code")

    # 5.查询失败(未登录)
    def test05_not_login(self):

        res = self.course_api.select_course(test_data='?name=测试开发提升课01', token='xxx')
        assert 200 == res.status_code
        assert '失败' in res.text
        assert 401 == res.json().get("code")
