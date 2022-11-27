import logging.config
import config


# 日志配置
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',  # 默认输出到 stderr
            'formatter': 'default',
            'level': config.log_level,
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': config.log_file_path,
            'mode': config.log_file_open_mode,
            'encoding': 'utf8',
            'level': config.log_level,
        },
    },
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(levelname)s]<%(name)s> %(message)s'
        }
    },
    'root': {
        'handlers': ['console', 'file', ],
        'level': config.log_level,
    }
}

# 设置 logging 模块的配置
logging.config.dictConfig(LOGGING)

# core 使用
logger_core = logging.getLogger("CORE")
# tools 使用
logger_tool = logging.getLogger("TOOL")
