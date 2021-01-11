import requests

class ProxyShare:

    HOST = "https://proxy.webshare.io/api"
    PATH_GETPROFILE = "/profile/"
    PATH_SUBSCRIPTION = "/subscription/"
    PATH_PROXYCONFIG = "/config/"
    PATH_RESET_PROXYPASSWORD = "/proxy/config/reset_password/"
    PATH_PROXYLIST = "/proxy/list/"
    PATH_REPLACEMENT_INFO = "/proxy/replacement/info/"
    PATH_REPLACEMENT_REFRESH = "/proxy/replacement/info/refresh/"
    PATH_REPLACEMENT_PROXY = "/proxy/replacement/"

    def __init__(self, keys):
        self.keys = keys
        self.headers = {"Authorization": f"Token {self.keys}"}
        self.session = requests.session()

    def getProfile(self):
        return requests.get(self.HOST + self.PATH_GETPROFILE, headers=self.headers).json()

    def getSubscription(self):
        return requests.get(self.HOST + self.PATH_SUBSCRIPTION, headers=self.headers).json()

    def getProxyConfig(self):
        return requests.get(self.HOST + self.PATH_PROXYCONFIG, headers=self.headers).json()

    def updateProxyConfig(self, data):
        return requests.post(self.HOST + self.PATH_PROXYCONFIG, headers=self.headers, json={"authorized_ips": data}).json()

    def resetProxyPassword(self):
        return requests.get(self.HOST + self.PATH_RESET_PROXYPASSWORD, headers=self.headers).json()

    def getProxyList(self):
        return requests.get(self.HOST + self.PATH_PROXYLIST, headers=self.headers).json()

    def getReplacementInfo(self):
        return requests.get(self.HOST + self.PATH_REPLACEMENT_INFO, headers=self.headers).json()

    def refreshReplacementProxy(self):
        return requests.get(self.HOST + self.PATH_REPLACEMENT_REFRESH, headers=self.headers).json()

    def getProxyReplacementList(self):
        return requests.get(self.HOST + self.PATH_REPLACEMENT_PROXY, headers=self.headers).json()

    def createProxyReplacement(self, ip_address):
        return requests.post(self.HOST + self.PATH_REPLACEMENT_PROXY, headers=self.headers, json={"ip_address": ip_address}).json()

    def deleteProxyReplacement(self, ip_address):
        return requests.delete(self.HOST + self.PATH_REPLACEMENT_PROXY, headers=self.headers, json={"ip_address": ip_address}).json()

if __name__ == "__main__":
    client = ProxyShare(keys="API_KEY")
    print(client.getProfile())
