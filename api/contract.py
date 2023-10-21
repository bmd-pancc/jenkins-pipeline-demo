# 合同模块
import requests
import config

class ContractAPI:

    def __init__(self):

        self.upload_url = config.BASE_URL + '/api/common/upload'
        self.add_url = config.BASE_URL + '/api/contract'
        self.select_url = config.BASE_URL + '/api/contract/list'

    # 1.合同上传
    def contract_upload(self,data,token):

        res = requests.post(url=self.upload_url,files={"file":data},headers={"Authorization":token})
        return res

    # 2.合同新增
    def contract_add(self,data,token):

        res = requests.post(url=self.add_url,json=data,headers={"Authorization":token})
        return res

    # 3.合同列表查询
    def contract_select(self,token):

        res = requests.get(url=self.select_url,headers={"Authorization":token})
        return res

