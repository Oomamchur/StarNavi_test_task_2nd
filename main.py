from fastapi import FastAPI

from workflow import router as workflow_router

app = FastAPI()


app.include_router(workflow_router.router)
