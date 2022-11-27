"""
头文件包含路径
"""

from typing import List

include_paths: List[str] = [
    "",
]

# 对头文件路径去重并进行排序
include_paths = sorted(set(include_paths))
