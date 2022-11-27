from typing import List
import re

"""
匹配多种形式的头文件，例如：
- #include <stdio.h>
- #include "foo.h"
- #include "include/bar.h"
- #include "include/foo/bar.h"
- #include "include\\foo\\bar.h"
- #include "foo.hpp"
"""
header_pattern = r'^#include *["<](\w+([\\/]\w*)*\.[hpp]{1,3})[">]$'
header_extractor = re.compile(header_pattern, re.M)


def extract_header(lines: List[str]) -> List[str]:
    """
    从输入的多行文本中筛选出所有的头文件
    :param lines: 多行文本，将会去除首尾的空字符
    :return: 多个头文件构成的列表
    """
    headers: List[str] = []
    for line in lines:
        match = header_extractor.match(line.strip())
        # 未匹配到头文件
        if match is None:
            continue
        # 头文件匹配
        headers.append(match.group(1))

    return headers


if __name__ == '__main__':
    input_lines: List[str] = [
        r'#include <stdio.h>',
        r'#include "foo.h"',
        r'#include "include/bar.h"',
        r'#include "include/foo/bar.h"',
        r'#include "include\foo\bar.h"',
        r'#include "foo.hpp"',
        r'  #include "bar.hpp"  ',
    ]
    print(extract_header(input_lines))
