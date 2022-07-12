import os.path
from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    # 调试模式
    APP_DEBUG: bool = True
    #     项目信息
    VERSION: str = '0.0.1'
    PROJECT_NAME: str = 'fastapi_demo'
    DESCRIPTION: str = 'fastapi项目'
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), 'static')
    # 模板目录
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")
    # 跨域请求
    CORS_OPTIONS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']


setting = Config()
