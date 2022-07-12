from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from views.home import home, register, reg_result

ViewsRouter = APIRouter()

ViewsRouter.get('/items/{id}', response_class=HTMLResponse)(home)
ViewsRouter.get('/register', response_class=HTMLResponse)(register)
ViewsRouter.post('/reg_result', response_class=HTMLResponse)(reg_result)
# async def read_item(request: Request, id: str):
#     # return template.TemplateResponse('index.html', {"request": request, 'id': id})
#     return request.app.state.views.TemplateResponse('index.html')
