"""
在一个文件中查找一个头文件
"""

import os
from typing import List, Set

import core
import tools
import config

# 查找过的头文件，用于避免重复查找
searched_headers: Set[str] = set()
# 最大查找深度
max_search_depth: int = 0


def dfs(start_header: str, target_header: str, path_to_header: str, include_paths: List[str], depth: int) -> None:
    """
    在一个头文件中递归查找另一个头文件
    :param start_header: 出发头文件
    :param target_header: 要查找的头文件
    :param path_to_header: 到达目标头文件的路径
    :param include_paths: 头文件路径
    :param depth: 查找深度
    """

    # 到达查找深度，直接返回
    if depth == 0:
        return
    # 检查头文件是否被屏蔽
    if start_header in config.black_headers:
        return

    searched_headers.add(start_header)
    tools.logger_core.debug(f'在头文件 {start_header} 中查找')

    # 更新最大查找深度
    global max_search_depth
    max_search_depth = max(max_search_depth, config.search_depth - depth + 1)

    header_paths: List[str] = core.get_include_path_of(start_header, include_paths)
    tools.logger_core.debug(f'{start_header} 使用了路径：\n'
                            f'    {header_paths}')
    for start_path in header_paths:
        headers: List[str] = core.extract_header(tools.read_file_to_lines(start_path))
        tools.logger_core.debug(f'{start_path} 中包含了头文件：\n'
                                f'    {", ".join(headers)}')
        if target_header in headers:
            tools.logger_core.info(f'{path_to_header} -> {target_header}')

        # 递归向深处查找
        for header in headers:
            # 跳过已查找过的头文件
            if header in searched_headers:
                continue
            dfs(header, target_header, f'{path_to_header} -> {header}', include_paths, depth - 1)


def search_header_in(filepath: str, target_header: str, include_paths: List[str]) -> None:
    """
    从一个文件出发，查找头文件
    :param filepath: 出发文件
    :param target_header: 要查找的头文件
    :param include_paths: 头文件包含路径
    """

    tools.logger_core.info(f'开始查找文件：{os.path.basename(filepath)}')

    global max_search_depth
    max_search_depth = 0

    headers: List[str] = core.extract_header(tools.read_file_to_lines(filepath))
    if target_header in headers:
        tools.logger_core.info(f'PATH: {target_header}')

    # 递归搜索其他头文件中是否包含该头文件
    for start_header in headers:
        dfs(start_header, target_header, f'PATH: {start_header}', include_paths, config.search_depth)

    tools.logger_core.info(f'统计：查找深度：{config.search_depth}，最大查找深度：{max_search_depth}')
