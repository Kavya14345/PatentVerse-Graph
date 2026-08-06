from database import get_driver


def show_patents():
    driver = get_driver()

    query = """
    MATCH (p:Patent)
    RETURN
        p.patent_id AS id,
        p.title AS title,
        p.year AS year,
        p.status AS status
    ORDER BY p.year DESC
    """

    try:
        with driver.session() as session:
            result = session.run(query)

            print("\nPATENTS")
            print("-" * 60)

            found = False

            for record in result:
                found = True

                print("ID:", record["id"])
                print("Title:", record["title"])
                print("Year:", record["year"])
                print("Status:", record["status"])
                print("-" * 60)

            if not found:
                print("No patents found.")

    except Exception as error:
        print("Query failed:")
        print(error)


if __name__ == "__main__":
    show_patents()