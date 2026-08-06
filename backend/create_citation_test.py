from database import get_driver


def create_citation_test():
    driver = get_driver()

    query = """
    MERGE (p2:Patent {patent_id: $patent_id})
    SET p2.title = $title,
        p2.abstract = $abstract,
        p2.year = $year,
        p2.patent_number = $patent_number,
        p2.status = $status

    WITH p2

    MATCH (p1:Patent {patent_id: $source_patent_id})

    MERGE (p1)-[:CITES]->(p2)

    RETURN
        p1.title AS source,
        p2.title AS cited
    """

    parameters = {
        "patent_id": "P002",

        "title":
            "Deep Learning for Medical Image Analysis",

        "abstract":
            "Deep learning methods for analysing medical images.",

        "year": 2022,

        "patent_number":
            "US-100002",

        "status":
            "Granted",

        "source_patent_id":
            "P001"
    }

    try:
        with driver.session() as session:
            result = session.run(query, parameters)

            record = result.single()

            if record:
                print("Citation created successfully.")

                print(
                    record["source"],
                    "CITES",
                    record["cited"]
                )

            else:
                print("Source patent not found.")

    except Exception as error:
        print("Failed to create citation.")
        print(error)


if __name__ == "__main__":
    create_citation_test()