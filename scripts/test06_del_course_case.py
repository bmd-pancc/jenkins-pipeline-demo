# 单接口测试-删除课程接口
from api.login import LoginApi
from api.course import CourseAPI

class TestDeleteCourseCase:

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
        TestDeleteCourseCase.token = login_res.json().get("token")

    def teardown(self):

        pass


    # 1.删除课程成功(存在的课程ID)
    def test01_delete_course_success(self):

        res = self.course_api.delete_course(data=37013,token=TestDeleteCourseCase.token)
        assert 200 == res.status_code
        assert '成功' in res.text
        assert 200 == res.json().get("code")

    # 2.删除课程失败(课程ID为NULL)
    def test02_delete_course_fail(self):

        res = self.course_api.delete_course(data=" ", token=TestDeleteCourseCase.token)
        assert 200 == res.status_code
        assert '失败' in res.text
        assert 500 == res.json().get("code")

    # 3.删除课程失败(课程ID为非数字)
    def test03_delete_course_fail(self):

        res = self.course_api.delete_course(data="abc", token=TestDeleteCourseCase.token)
        assert 200 == res.status_code
        assert '失败' in res.text
        assert 500 == res.json().get("code")

    # 4.删除课程失败(课程ID不存在)
    def test04_delete_course_fail(self):

        res = self.course_api.delete_course(data=20231007, token=TestDeleteCourseCase.token)
        assert 200 == res.status_code
        assert '失败' in res.text
        assert 500 == res.json().get("code")

    # 5.删除课程失败(未登录)
    def test05_delete_course_fail(self):

        res = self.course_api.delete_course(data=19614, token="xxx")
        assert 200 == res.status_code
        assert '失败' in res.text
        assert 401 == res.json().get("code")