import requests
import time

from .token import get_token
from .exceptions import *


class Client:
    def __init__(self, panel_address, api_key):
        self.__panel_address = panel_address
        self.__api_key = api_key
        self.session = requests.Session()
        self.__cookies = None
        self.config = {
                        "AddDirBinding": "/site?action=AddDirBinding",
                        "CloseHasPwd": "/site?action=CloseHasPwd",
                        "CloseLimitNet": "/site?action=CloseLimitNet",
                        "CloseSSLConf": "/site?action=CloseSSLConf",
                        "CloseToHttps": "/site?action=CloseToHttps",
                        "CreateProxy": "/site?action=CreateProxy",
                        "DelDirBinding": "/site?action=DelDirBinding",
                        "Get301Status": "/site?action=Get301Status",
                        "GetDirBinding": "/site?action=GetDirBinding",
                        "GetDirRewrite": "/site?action=GetDirRewrite",
                        "GetDirUserINI": "/site?action=GetDirUserINI",
                        "GetDiskInfo": "/system?action=GetDiskInfo",
                        "GetFileBody": "/files?action=GetFileBody",
                        "GetLimitNet": "/site?action=GetLimitNet",
                        "GetNetWork": "/system?action=GetNetWork",
                        "GetPHPVersion": "/site?action=GetPHPVersion",
                        "GetProxyList": "/site?action=GetProxyList",
                        "GetRewriteList": "/site?action=GetRewriteList",
                        "GetSSL": "/site?action=GetSSL",
                        "GetSecurity": "/site?action=GetSecurity",
                        "GetSiteLogs": "/site?action=GetSiteLogs",
                        "GetSitePHPVersion": "/site?action=GetSitePHPVersion",
                        "GetSystemTotal": "/system?action=GetSystemTotal",
                        "GetTaskCount": "/ajax?action=GetTaskCount",
                        "HttpToHttps": "/site?action=HttpToHttps",
                        "ModifyProxy": "/site?action=ModifyProxy",
                        "ResDatabasePass": "/database?action=ResDatabasePassword",
                        "SQLDelBackup": "/database?action=DelBackup",
                        "SQLToBackup": "/database?action=ToBackup",
                        "SaveFileBody": "/files?action=SaveFileBody",
                        "Set301Status": "/site?action=Set301Status",
                        "SetHasPwd": "/site?action=SetHasPwd",
                        "SetLimitNet": "/site?action=SetLimitNet",
                        "SetPHPVersion": "/site?action=SetPHPVersion",
                        "SetSSL": "/site?action=SetSSL",
                        "SetSecurity": "/site?action=SetSecurity",
                        "SetStatus": "/ftp?action=SetStatus",
                        "SetUserPassword": "/ftp?action=SetUserPassword",
                        "SetupPackage": "/plugin?action=a&name=deployment&s=SetupPackage",
                        "UpdatePanel": "/ajax?action=UpdatePanel",
                        "WebAddDomain": "/site?action=AddDomain",
                        "WebAddSite": "/site?action=AddSite",
                        "WebBackupList": "/data?action=getData&table=backup",
                        "WebDelBackup": "/site?action=DelBackup",
                        "WebDelDomain": "/site?action=DelDomain",
                        "WebDeleteSite": "/site?action=DeleteSite",
                        "WebDomainList": "/data?action=getData&table=domain",
                        "WebFtpList": "/data?action=getData&table=ftps",
                        "WebGetIndex": "/site?action=GetIndex",
                        "WebSetEdate": "/site?action=SetEdate",
                        "WebSetIndex": "/site?action=SetIndex",
                        "WebSetPs": "/data?action=setPs&table=sites",
                        "WebSiteStart": "/site?action=SiteStart",
                        "WebSiteStop": "/site?action=SiteStop",
                        "WebSqlList": "/data?action=getData&table=databases",
                        "WebToBackup": "/site?action=ToBackup",
                        "Websites": "/data?action=getData&table=sites",
                        "Webtypes": "/site?action=get_site_types",
                        "deployment": "/plugin?action=a&name=deployment&s=GetList&type=0",
                        "download": "/download?filename="
                    }

    def __get_key(self):
        now_time = time.time()
        p_data = {
            "request_token": get_token(now_time, self.__api_key),
            "request_time": now_time
        }
        return p_data
    
    def post_data(self, endpoint, data={}):
        url = self.__panel_address + endpoint
        body = self.__get_key()
        
        if data:
            body.update(data)
        
        try:
            if self.__cookies:
                response = self.session.post(url, body, cookies=self.__cookies)
            else:
                response = self.session.post(url, body)
        except requests.exceptions.ConnectionError:
            raise ConnectionRefused
            
        if response.status_code == 200:
            if '密钥校验失败' in response.text:
                raise InvalidAPIKey(response.text)
            
            elif 'IP校验失败,您的访问IP为' in response.text:
                raise IPBlocked(response.text)
            else:
                self.__cookies = response.cookies
                return response.json()
        else:
            raise BadRequest("Problem with connection, status code: %s" % response.status_code)
