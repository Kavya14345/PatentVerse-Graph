from database import get_driver


CONSTRAINTS = [
    """
    CREATE CONSTRAINT patent_id_unique IF NOT EXISTS
    FOR (p:Patent)
    REQUIRE p.patent_id IS UNIQUE
    """,

    """
    CREATE CONSTRAINT inventor_id_unique IF NOT EXISTS
    FOR (i:Inventor)
    REQUIRE i.inventor_id IS UNIQUE
    """,

    """
    CREATE CONSTRAINT company_id_unique IF NOT EXISTS
    FOR (c:Company)
    REQUIRE c.company_id IS UNIQUE
    """,

    """
    CREATE CONSTRAINT technology_id_unique IF NOT EXISTS
    FOR (t:Technology)
    REQUIRE t.technology_id IS UNIQUE
    """,

    """
    CREATE CONSTRAINT category_id_unique IF NOT EXISTS
    FOR (c:Category)
    REQUIRE c.category_id IS UNIQUE
    """
]


def create_schema():
    driver = get_driver()

    try:
        with driver.session() as session:

            for constraint in CONSTRAINTS:
                session.run(constraint).consume()

        print("Schema constraints created successfully.")

    except Exception as error:
        print("Could not create schema constraints.")
        print(error)


if __name__ == "__main__":
    create_schema()