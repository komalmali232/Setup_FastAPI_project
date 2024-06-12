from fastapi import FastAPI
from views import addition_view
from views import addition_view

app = FastAPI()

app.include_router(addition_view.router)
