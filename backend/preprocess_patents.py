import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

COGNODB_URI = os.getenv("COGNODB_URI")
COGNODB_USER = os.getenv("COGNODB_USER")
COGNODB_PASSWORD = os.getenv("COGNODB_PASSWORD")


def _validate_config():
    missing = []

    if not COGNODB_URI:
        missing.append("COGNODB_URI")

    if not COGNODB_USER:
        missing.append("COGNODB_USER")

    if not COGNODB_PASSWORD:
        missing.append("COGNODB_PASSWORD")

    if missing:
        raise RuntimeError(
            "Missing required environment variables: "
            + ", ".join(missing)
        )


_validate_config()

driver = GraphDatabase.driver(
    COGNODB_URI,
    auth=(COGNODB_USER, COGNODB_PASSWORD)
)


def get_driver():
    return driver


def verify_connection():
    driver.verify_connectivity()


def close_driver():
    driver.close()