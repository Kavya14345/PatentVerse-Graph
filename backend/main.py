from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import patents
from routes import companies
from routes import inventors
from routes import graph


app = FastAPI(

    title="PatentGraph AI API",

    description=
    "AI Patent Relationship Explorer powered by CognoDB",

    version="1.0"

)


# Allow React frontend

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)



app.include_router(
    patents.router
)


app.include_router(
    companies.router
)


app.include_router(
    inventors.router
)


app.include_router(
    graph.router
)



@app.get("/")

def home():

    return {

        "message":
        "PatentGraph AI API running"

    }