from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Region(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    districts: Optional[List["District"]] = Relationship(back_populates="region")


class District(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    entities: Optional[List["Entity"]] = Relationship(back_populates="district")
    
    region_id: Optional[int] = Field(default=None, foreign_key="region.id")
    region: Optional[Region] = Relationship(back_populates="districts")


class Entity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type_name: str = Field(index=True)
    name: str
    address: str
    coordinates: List[int]

    district_id: Optional[int] = Field(default=None, foreign_key="district.id")
    district: Optional[District] = Relationship(back_populates="entities")


# class TradeEntity(EntityBase, table=True):
#     pass


# class SportEntity(EntityBase, table=True):
#     pass


# class StateEntity(EntityBase, table=True):
#     pass


# class CultureEntity(EntityBase, table=True):
#     pass