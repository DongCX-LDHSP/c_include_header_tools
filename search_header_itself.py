"""
从某个头文件开始查找自己本身
"""
import sys
from typing import List

import core
import tools
import config
import include_paths


def search_header_itself(header: str, include_paths: List[str]) -> None:
    """
    从某个头文件开始查找自己本身
    :param header: 要查找的头文件
    :param include_paths: 头文件包含路径
    """
    tools.logger_func.info(f'开始查找头文件：{header}')
    header_paths: List[str] = core.get_include_path_of(header, include_paths)
    if not header_paths:
        tools.logger_func.warning(f'找不到该头文件，停止查找')
        return

    tools.logger_func.debug(f'该头文件使用了如下路径：\n'
                            f'    {header_paths}')
    for header_path in header_paths:
        core.search_header_in(header_path, header, include_paths)
    tools.logger_func.info(f'结束查找头文件：{header}')


if __name__ == '__main__':
    # 头文件
    header: str = sys.argv[1]
    # 配置搜索深度，使得可以不限制搜索深度
    config.search_depth = -1
    search_header_itself(header, include_paths.include_paths)
