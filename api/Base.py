from fastapi import APIRouter, Security
from api.user import user_add, user_del, user_info, get_user_rules, account_login, user_list
from core.Auth import check_permissions
from schemas.user import CurrentUser, UserLogin

ApiRouter = APIRouter(prefix="/api/v1")
AdminRouter = APIRouter(prefix="/admin")
AdminRouter.post("/account/login", response_model=UserLogin, tags=["管理员登陆"], summary="用户登陆")(
    account_login)
AdminRouter.get("/user/info",
                tags=["用户管理"],
                summary="获取当前管理员信息",
                dependencies=[Security(check_permissions)],
                response_model=CurrentUser
                )(user_info)

AdminRouter.get("/user/list",
                tags=["用户管理"],
                summary="获取管理员列表",
                dependencies=[Security(check_permissions, scopes=["user_list"])],
                # response_model=CurrentUser
                )(user_list)

AdminRouter.delete("/user/del",
                   tags=["用户管理"],
                   summary="管理员删除",
                   dependencies=[Security(check_permissions, scopes=["user_delete"])]
                   )(user_del)
AdminRouter.post("/user/add",
                 tags=["用户管理"],
                 summary="管理员添加",
                 dependencies=[Security(check_permissions, scopes=["user_add"])]
                 )(user_add)
ApiRouter.include_router(AdminRouter)
