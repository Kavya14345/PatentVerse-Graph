import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()



driver = GraphDatabase.driver(
    "bolt+s://db-19e381a1.databases.cognodb.com",
    auth=("cognodb", "d93076043061f39542a02c6f46561c66"),
)
driver.verify_connectivity()


def get_driver():
    return driver


def verify_connection():
    driver.verify_connectivity()


def close_driver():
    driver.close()