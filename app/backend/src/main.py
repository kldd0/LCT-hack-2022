from typing import Mapping

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .database.register import *
from .database.models import *
from .database.parser import preload_to_db

from sqlmodel import Session
from pydantic import ValidationError


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup() -> None:
    await init_db()


@app.get("/")
async def home() -> Mapping[str, str]:
    await preload_to_db()
    return {"status": "ok"}


@app.post("/entities")
async def add_entity(entity: Entity, sess: Session = Depends(get_session)):
    try:
        obj = Entity(
            type_name=entity.type_name,
            name=entity.name,
            address=entity.address,
            coordinates=entity.coordinates,
            distances=entity.distances,
            district=entity.district
        )
        sess.add(obj)
        await sess.commit()
        await sess.refresh(obj)
        return obj
    except ValidationError as e:
        return e


@app.post("/districts")
async def add_entity(entity: District, sess: Session = Depends(get_session)):
    try:
        obj = District(
            name=entity.name,
            region_id=entity.region_id
        )
        sess.add(obj)
        await sess.commit()
        await sess.refresh(obj)
        return obj
    except ValidationError as e:
        return e


@app.post("/regions")
async def add_entity(entity: Region, sess: Session = Depends(get_session)):
    try:
        obj = Region(
            name=entity.name
        )
        sess.add(obj)
        await sess.commit()
        await sess.refresh(obj)
        return obj
    except ValidationError as e:
        return e