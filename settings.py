import os
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(BASE_DIR)
# ---------------excel相关------------------------
EXCEL_DIR = os.path.join(BASE_DIR, 'excel')
# print(EXCEL_DIR)
EXCEL_PATH = os.path.join(EXCEL_DIR, 'test2.xls')
EXCEL_SHEET_NAME = '示例'

# -----------------日志相关-------------------------
LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_PATH = os.path.join(LOG_DIR, 'test_case.log')

# ----------------自动化报告相关______________________
REPORT_DIR = os.path.join(BASE_DIR, 'report')
REPORT_PATH = os.path.join(REPORT_DIR, 'report.html')

# ----------------测试用例相关------------------------
TESTCASE_DIR = os.path.join(BASE_DIR, 'testcase')

# ----------------邮件相关---------------------------
MAIL_HOST = "smtp.qq.com"  # 设置服务器
MAIL_USER = "448323008@qq.com"  # 用户名
MAIL_PASS = "cxpyruuldbwcbicf"  # 获取授权码
SENDER = '448323008@qq.com'  # 发件人账号
RECEIVERS = ['448323008@qq.com']  # 接收邮件(可以多个)，可设置为你的QQ邮箱或者其他邮箱
