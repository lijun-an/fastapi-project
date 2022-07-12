import os
from fastapi.staticfiles import StaticFiles
from config import setting
from fastapi import FastAPI, HTTPException
from core import Exception, Event, Middleware
from core.Event import startup, stopping
from fastapi.exceptions import RequestValidationError
from core.Router import AllRouter
from fastapi.middleware.cors import CORSMiddleware
from core.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, UnicornException
from fastapi.templating import Jinja2Templates

application = FastAPI(
    debug=setting.APP_DEBUG,
    description=setting.DESCRIPTION,
    version=setting.VERSION,
    title=setting.PROJECT_NAME
)

# 事件监听
application.add_event_handler('startup', startup(application))
application.add_event_handler('shutdown', stopping(application))
# 异常错误处理
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http422_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)
# 路由
application.include_router(AllRouter)
# 中间件
application.add_middleware(Middleware.BaseMiddleware)

application.add_middleware(
    CORSMiddleware,
    allow_origins=setting.CORS_OPTIONS,
    allow_credentials=setting.CORS_ALLOW_CREDENTIALS,
    allow_methods=setting.CORS_ALLOW_METHODS,
    allow_headers=setting.CORS_ALLOW_HEADERS,
)
# 静态资源目录
application.mount('/', StaticFiles(directory=setting.STATIC_DIR), name="static")
application.state.views = Jinja2Templates(directory=setting.TEMPLATE_DIR)
app = application
