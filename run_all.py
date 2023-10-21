import pytest
import os

if __name__=='__main__':

    # --clean-alluredir: 清除之前的allure报告
    # -o: 输出文件到某个目录
    pytest.main(["-s", "-q", "scripts/test06_del_course_case.py","--clean-alluredir","--junitxml=report/xml/result.xml"])
    os.system(r'allure generate ./report/xml -o ./report/allure-report --clean')


"""
pytest.main()命令参数:
-s: 显示程序中的print/logging输出
-v: 丰富信息模式,输出更详细的用例执行信息
-q: 安静模式,不输出环境信息
-x: 出现一条用例失败,就退出
-k: 可以使用and,not,or来区分匹配范围(文件名、类名、函数名)

junitxml: 运行后的junitxml结果文件
jenkins可以识别这个文件,并对它进行解析
"""