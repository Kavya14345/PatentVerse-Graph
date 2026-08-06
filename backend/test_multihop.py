from database import get_driver


def test_multihop():
    driver = get_driver()

    query = """
    MATCH
        (i:Inventor)-[:INVENTED]->(p:Patent)
        -[:USES]->(t:Technology)

    RETURN
        i.name AS inventor,
        p.title AS patent,
        t.name AS technology
    """

    try:
        with driver.session() as session:

            result = session.run(query)

            print("\nMULTI-HOP GRAPH TRAVERSAL")
            print("=" * 60)

            found = False

            for record in result:
                found = True

                print(
                    record["inventor"],
                    "-> INVENTED ->",
                    record["patent"],
                    "-> USES ->",
                    record["technology"]
                )

            if not found:
                print("No multi-hop paths found.")

    except Exception as error:
        print("Multi-hop query failed.")
        print(error)


if __name__ == "__main__":
    test_multihop()