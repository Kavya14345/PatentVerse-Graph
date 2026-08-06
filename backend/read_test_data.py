from database import driver


def get_patent(patent_id):

    query = """
    MATCH (p:Patent {patent_id: $patent_id})

    OPTIONAL MATCH (i:Inventor)-[:INVENTED]->(p)
    OPTIONAL MATCH (c:Company)-[:OWNS]->(p)
    OPTIONAL MATCH (p)-[:USES]->(t:Technology)
    OPTIONAL MATCH (p)-[:BELONGS_TO]->(cat:Category)

    RETURN
        p.patent_id AS patent_id,
        p.title AS title,
        p.year AS year,
        collect(DISTINCT i.name) AS inventors,
        collect(DISTINCT c.name) AS companies,
        collect(DISTINCT t.name) AS technologies,
        collect(DISTINCT cat.name) AS categories
    """

    with driver.session() as session:

        result = session.run(
            query,
            patent_id=patent_id
        )

        record = result.single()

        if record is None:
            print("Patent not found.")
            return

        print()
        print("PATENT DETAILS")
        print("---------------------------")
        print("ID:", record["patent_id"])
        print("Title:", record["title"])
        print("Year:", record["year"])
        print("Inventors:", record["inventors"])
        print("Companies:", record["companies"])
        print("Technologies:", record["technologies"])
        print("Categories:", record["categories"])


if __name__ == "__main__":

    try:
        get_patent("PAT001")

    finally:
        driver.close()