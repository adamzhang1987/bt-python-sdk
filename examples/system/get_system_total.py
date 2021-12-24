# 系统状态相关接口api
from pybt.system import System


api = System(YOUR_PANEL_ADDRESS, YOUR_API_KEY)
response = api.get_system_total()
print(response)