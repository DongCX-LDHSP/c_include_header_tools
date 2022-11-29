#!/usr/bin/python3
"""
从某个文件开始查找头文件
"""
import os
import sys
from typing import List

import core
import config
import include_paths


def search_header_from_file(filepath: str, target_header: str, include_paths: List[str]) -> None:
    """
    从一个文件开始查找头文件
    :param filepath: 文件的绝对路径
    :param target_header: 目标头文件
    :param include_paths: 头文件包含路径
    """
    core.search_header_in(filepath, target_header, include_paths)


if __name__ == '__main__':
    # 文件的相对路径，相对代码工程的根目录的文件路径
    file_relative_path: str = sys.argv[1]
    # 要查找的头文件名称
    header: str = sys.argv[2]
    search_header_from_file(
        os.path.realpath(os.path.join(config.PROJECT_BASE_DIR, file_relative_path)),
        header,
        include_paths.include_paths
    )
