"""
从某个文件的任一头文件开始查找其他该文件包含的头文件
"""

import os
import sys
from typing import List

import core
import tools
import config
import include_paths


def search_self_header_of_file(filepath: str, include_paths: List[str]) -> None:
    """
    从某个文件的任一头文件开始查找其他该文件包含的头文件
    :param filepath: 文件的绝对路径
    :param include_paths: 头文件包含路径
    """
    tools.logger_func.info(f'开始查找文件：{os.path.relpath(filepath, config.PROJECT_BASE_DIR)}')

    headers: List[str] = core.extract_header(tools.read_file_to_lines(filepath))
    tools.logger_func.info(f'该文件包含了头文件：\n'
                           f'    {", ".join(headers)}')
    for start_header in headers:
        header_files: List[str] = core.get_include_path_of(start_header, include_paths)

        tools.logger_func.info(f'在头文件 {start_header} 中查找其他头文件')
        tools.logger_func.info(f'{start_header} 使用了路径：\n'
                               f'    {header_files}')

        for inner_target_header in headers:
            if start_header == inner_target_header:
                continue
            for header_file in header_files:
                core.search_header_in(
                    header_file,
                    inner_target_header,
                    include_paths,
                    include_self=True
                )

        tools.logger_func.info(f'结束在头文件 {start_header} 中查找其他头文件')

    tools.logger_func.info(f'结束查找文件：{os.path.relpath(filepath, config.PROJECT_BASE_DIR)}')


if __name__ == '__main__':
    # 文件的相对路径，相对代码工程的根目录的文件路径
    file_relative_path: str = sys.argv[1]
    search_self_header_of_file(
        os.path.realpath(os.path.join(config.PROJECT_BASE_DIR, file_relative_path)),
        include_paths.include_paths
    )
