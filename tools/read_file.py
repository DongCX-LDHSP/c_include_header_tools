from typing import List
import os

from tools import logger_tool
import config


def read_file_to_lines(filepath: str) -> List[str]:
    """
    读取文件，并将文件内容输出为字符串列表
    :param filepath: 文件的路径
    :return: 文件内容的多行形式
    """

    # 文件不存在
    if os.path.exists(filepath) is False:
        logger_tool.error(f'找不到文件：{filepath}')
        return []

    for encoding in config.support_encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                logger_tool.debug(f'使用编码<{encoding}>成功打开文件')
                return file.readlines()
        except UnicodeDecodeError:
            ...

    # 没有找到合适的文件编码打开文件
    logger_tool.error(f'打开文件失败：{filepath}\n'
                      f'不支持的文件编码格式，支持如下格式：\n'
                      f'    {".".join(config.support_encodings)}\n'
                      f'您可以在配置"config.support_encodings"中添加新的编码')

    return []


if __name__ == '__main__':
    print(read_file_to_lines('not_exists.txt'))
    print(read_file_to_lines(__file__))
