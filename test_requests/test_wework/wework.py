import requests


class WeWork:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = 'ww13c64c56510d8bd9'
    token = dict()

    @classmethod
    def get_token(cls, secret):
        if secret not in cls.token.keys():
            r = requests.get(
                cls.token_url,
                params={
                    "corpid": cls.corpid, "corpsectet": secret
                }
            )
            cls.token[secret] = r.json()["access_token"]
        return cls.token[secret]
