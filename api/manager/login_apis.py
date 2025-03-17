from api.base_api import BaseManagerApi
from common.encry_decry import md5


class ManagerLoginApi(BaseManagerApi):

    # 接口的基本信息，统一封装在init函数中
    def __init__(self,username,password):
        super().__init__()
        self.url = f'{self.host}/admin/systems/admin-users/login'
        self.method = 'get'
        self.params = {
            "username":username,
            "password":md5(password),
            "captcha":'1512',
            "uuid":"asdasdasdasdasdd"
        }


if __name__ == "__main__":
    resp = ManagerLoginApi(username='admin', password='78b157cf49d312ecf69d1335e8b589ef').send()
    print(resp.json())
    print(resp.status_code)