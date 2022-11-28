"""
头文件包含路径
"""

import os
from typing import List

import config

include_paths: List[str] = [
    '',
]

# 对头文件路径去重并进行排序
include_paths = sorted(set(include_paths))
# 构造路径的绝对路径
include_paths = [os.path.abspath(os.path.join(config.PROJECT_BASE_DIR, path)) for path in include_paths]
