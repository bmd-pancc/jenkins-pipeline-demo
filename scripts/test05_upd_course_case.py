# 单接口测试-修改课程接口
from api.login import LoginApi
from api.course import CourseAPI

class TestUpdateCourseCase:

    token = None

    def setup(self):

        # 初始化
        self.login_api = LoginApi()
        self.course_api = CourseAPI()
        # 登录
        vetify_res = self.login_api.vetify_code()
        uuid = vetify_res.json().get("uuid")
        login_data = {
            "username":"admin",
            "password":"HM_2023_test",
            "code":"2",
            "uuid":uuid
        }
        login_res = self.login_api.login(login_data)
        TestUpdateCourseCase.token = login_res.json()["token"]


    def teardown(self):

        pass

    # 1.修改课程成功(正确的课程id)
    def test01_update_course_success(self):

        test_data = {
            "id":19614
        }
        res = self.course_api.update_course(data=test_data,token=TestUpdateCourseCase.token)
        assert 200 == res.status_code
        assert "成功" in res.text
        assert 200 == res.json()["code"]

    # 2.修改课程成功(全部参数填写正确)
    def test02_update_course_fail(self):

        test_data = {
            "id":19614,
            "name":"测试开发提升课02",
            "subject":"6",
            "price":899,
            "applicablePerson":"2",
            "info":"测试开发提升课02"
        }
        res = self.course_api.update_course(data=test_data, token=TestUpdateCourseCase.token)
        assert 200 == res.status_code
        assert "成功" in res.text
        assert 200 == res.json()["code"]

    # 3.修改课程失败(课程ID为NULL)
    def test03_update_course_fail(self):

        test_data = {
            "id": ""
        }
        res = self.course_api.update_course(data=test_data, token=TestUpdateCourseCase.token)
        assert 200 == res.status_code
        assert "成功" in res.text
        assert 200 == res.json()["code"]

    # 4.修改课程失败(课程ID为非数字)
    def test04_update_course_fail(self):

        test_data = {
            "id": "abc"
        }
        res = self.course_api.update_course(data=test_data, token=TestUpdateCourseCase.token)
        assert 200 == res.status_code
        assert "成功" in res.text
        assert 200 == res.json()["code"]


    # 5.修改课程失败(课程ID不存在)
    def test05_update_course_fail(self):
        test_data = {
            "id": 20231007
        }
        res = self.course_api.update_course(data=test_data, token=TestUpdateCourseCase.token)
        assert 200 == res.status_code
        assert "成功" in res.text
        assert 200 == res.json()["code"]

    # 5.修改课程失败(未登录)
    def test06_update_course_fail(self):

        test_data = {
            "id": 19614
        }
        res = self.course_api.update_course(data=test_data, token="xxx")
        assert 200 == res.status_code
        assert "失败" in res.text
        assert 401 == res.json()["code"]
