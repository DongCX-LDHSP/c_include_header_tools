import os
import sys
from typing import List


# 头文件工程的根目录
BASE_DIR: str = os.path.realpath(os.path.abspath(os.path.dirname(__file__)))

# C工程的根目录
PROJECT_BASE_DIR: str = os.path.realpath(os.path.abspath(r'../..'))

# 将工程根目录追加到系统环境变量中
sys.path.append(BASE_DIR)

# 读取文件时，支持的文件编码格式
support_encodings: List[str] = [
    'utf-8',
    'gbk',
]

"""
日志等级，从以下字符串中任选其一，从上到下，日志输出逐渐增多：
- CRITICAL
- ERROR
- WARNING
- INFO
- DEBUG
- NOTSET
"""
log_level: str = 'WARNING'
# 日志文件
log_file_path: str = os.path.join(BASE_DIR, 'me.log')
# 日志文件打开默认，默认使用覆盖写模式，即：'w'
log_file_open_mode: str = 'w'

# 查找深度
search_depth: int = 10
