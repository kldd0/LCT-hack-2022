import json
from pydantic import BaseModel
from typing import List


class Adm(BaseModel):
    name: str
    districts: List[str] = []


objects = []


def find_reg(name: str) -> Adm:
    for obj in objects:
        if obj.name == name:
            return obj
    obj = Adm(name=name)
    objects.append(obj)
    return obj


with open("datasets/regions_.json") as file:
    data = json.load(file)
    for el in data:
        for key in el:
            obj = find_reg(key)
            obj.districts.append(el[key])
    with open("datasets/regions.json", "x") as out:
        out.write(json.dumps([obj.dict() for obj in objects], indent=4, ensure_ascii=False).encode("utf-8").decode())

# print(objects)
    # file.write(json.dumps(data, indent=4, ensure_ascii=False).encode("utf-8").decode())