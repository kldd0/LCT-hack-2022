import aiohttp
import asyncio
import os
import json
from typing import Mapping, List, Union
from .models import Entity, Region, District
from .register import get_session


API_KEY = "<apidata_mos>"


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        curr_url = f"https://apidata.mos.ru/v1/datasets/624/features?api_key={API_KEY}"
        async with session.get(curr_url) as resp:
            res = await resp.json(content_type=None)
            with open("datasets/metro.json", "x") as file:
                file.write(json.dumps(res, indent=4, ensure_ascii=False).encode("utf-8").decode())

asyncio.run(main())


async def make_request(path: str, obj: Union[Entity, Region, District]) -> int:
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://0.0.0.0:8000/{path}", json=obj.dict()) as resp:
            res = await resp.json(content_type=None)
            return res["id"]


async def preload_regions_to_db() -> None:
    with open("/app/src/database/datasets/regions.json") as file:
        data = json.load(file)
        for r in data:
            region = Region(name=r["name"])
            reg_id = await make_request("regions", region)
            for dist_n in region["districts"]:
                district = District(
                    name=dist_n,
                    region_id=reg_id
                )
                await make_request("districts", district)


async def calculate_distances(obj: Entity) -> List[int]:
    pass


async def preload_to_db() -> None:
    await preload_regions_to_db()
    # order = ["mfc", "sport_entities", "culture_entities", "library_entities", "metro"]
    order = ["mfc", "metro"]
    for fname in order:
        file_path = f"/app/src/database/datasets/{fname}.json"
        if fname == "metro":
            with open(file_path) as json_file:
                data = json.load(json_file)
                for i in range(20): # len(data)
                    if not data[i]: continue
                    obj = Entity(
                        type_name=fname,
                        name=data[i]["NameOfStation"],
                        address=data[i]["Name"],
                        coordinates=data[i]["geoData"]["coordinates"], # long, lat
                        distances=None,
                        district=data[i]["District"]
                    )
                    with open("reqs.json", "w") as file:
                        file.write(json.dumps(obj.dict(), indent=4, ensure_ascii=False).encode("utf-8").decode())
                    async with aiohttp.ClientSession() as session:
                        async with session.post("http://0.0.0.0:8000/entities", json=obj.dict()) as resp:
                            res = await resp.json(content_type=None)
        else:
            with open(file_path) as json_file:
                data = json.load(json_file)["features"]
                for i in range(20):
                    if not data[i]: continue
                    obj = Entity(
                        type_name=fname,
                        name=data[i]["properties"]["Attributes"]["CommonName"],
                        address=data[i]["properties"]["Attributes"]["Address"],
                        coordinates=data[i]["geometry"]["coordinates"],
                        distances=None,
                        district=data[i]["properties"]["Attributes"]["District"]
                    )
                    async with aiohttp.ClientSession() as session:
                        async with session.post("http://0.0.0.0:8000/entities", json=obj.dict()) as resp:
                            res = await resp.json(content_type=None)


# async def main_load_to_db() -> None:
#     await preload_to_db()
#     pass

