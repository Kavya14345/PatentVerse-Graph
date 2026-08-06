from pydantic import BaseModel
from typing import List, Optional


class Patent(BaseModel):

    patent_id: str
    title: str
    abstract: Optional[str]
    year: int
    status: str


class Inventor(BaseModel):

    inventor_id: str
    name: str
    country: str


class Company(BaseModel):

    company_id: str
    name: str
    industry: str
    country: str


class GraphNode(BaseModel):

    id: str
    label: str
    type: str


class GraphRelationship(BaseModel):

    source: str
    target: str
    relationship: str


class GraphResponse(BaseModel):

    nodes: List[GraphNode]

    relationships: List[GraphRelationship]