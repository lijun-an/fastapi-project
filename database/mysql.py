from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

DB_ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': "47.108.90.106",
                'user': 'lijun',
                'password': '123456',
                'port': 3306,
                'database': 'fastapi_pro',
            }
        }
    },
    "apps": {
        "base": {"models": ["models.base"], "default_connection": "base"},
        # "db2": {"models": ["models.db2"], "default_connection": "db2"},
        # "db3": {"models": ["models.db3"], "default_connection": "db3"}
    },
}


async def register_mysql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        # 自动载数据库中生成相应的数据表
        generate_schemas=False,
        add_exception_handlers=True,
    )
