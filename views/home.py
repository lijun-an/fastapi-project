from fastapi import Request, Form


async def home(req: Request, id: str):
    return req.app.state.views.TemplateResponse('index.html', {"request": req, "id": id})


# 注册页面
async def register(req: Request):
    return req.app.state.views.TemplateResponse('register.html', {"request": req})


# 注册结果页面
async def reg_result(req: Request, username: str = Form(...), password: str = Form(...)):
    return req.app.state.views.TemplateResponse('reg_result.html',
                                                {"request": req, "username": username, "password": password})
