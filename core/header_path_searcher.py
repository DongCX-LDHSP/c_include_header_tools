"""
根据输入的头文件包含路径，查找一个头文件的路径
"""

import os
from typing import List

from tools import logger_core


def get_include_path_of(header: str, include_paths: List[str]) -> List[str]:
    """
    查找头文件的路径，默认会遍历所有的路径，可能会查找到多个路径
    :param header: 头文件名称
    :param include_paths: 头文件包含路径列表
    :return: 查找到的头文件路径列表
    """
    header_path: List[str] = []
    for path in include_paths:
        temp_path: str = os.path.realpath(os.path.abspath(os.path.join(path, header)))
        logger_core.debug(f'尝试路径：{temp_path}')
        if os.path.exists(temp_path) is False:
            continue
        header_path.append(temp_path)

    if not header_path:
        logger_core.debug(f'找不到头文件 {header} 所在的位置')

    return header_path
