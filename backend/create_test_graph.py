from database import get_driver


def create_test_graph():
    driver = get_driver()

    query = """
    MERGE (company:Company {company_id: $company_id})
    SET company.name = $company_name,
        company.industry = $company_industry,
        company.country = $company_country

    MERGE (inventor:Inventor {inventor_id: $inventor_id})
    SET inventor.name = $inventor_name,
        inventor.country = $inventor_country

    MERGE (technology:Technology {technology_id: $technology_id})
    SET technology.name = $technology_name,
        technology.description = $technology_description

    MERGE (category:Category {category_id: $category_id})
    SET category.name = $category_name

    MERGE (patent:Patent {patent_id: $patent_id})
    SET patent.title = $patent_title,
        patent.abstract = $patent_abstract,
        patent.year = $patent_year,
        patent.patent_number = $patent_number,
        patent.status = $patent_status

    MERGE (inventor)-[:INVENTED]->(patent)
    MERGE (inventor)-[:WORKS_AT]->(company)
    MERGE (company)-[:OWNS]->(patent)
    MERGE (patent)-[:USES]->(technology)
    MERGE (patent)-[:BELONGS_TO]->(category)

    RETURN patent.title AS patent_title
    """

    parameters = {
        "company_id": "C001",
        "company_name": "NovaTech Research",
        "company_industry": "Artificial Intelligence",
        "company_country": "USA",

        "inventor_id": "I001",
        "inventor_name": "John Smith",
        "inventor_country": "USA",

        "technology_id": "T001",
        "technology_name": "Machine Learning",
        "technology_description": "Algorithms that learn patterns from data.",

        "category_id": "CAT001",
        "category_name": "Healthcare",

        "patent_id": "P001",
        "patent_title": "AI-Based Medical Diagnosis",
        "patent_abstract":
            "A machine learning system for assisting medical diagnosis.",

        "patent_year": 2024,
        "patent_number": "US-100001",
        "patent_status": "Granted"
    }

    try:
        with driver.session() as session:
            result = session.run(query, parameters)
            record = result.single()

            if record:
                print("Test graph created successfully.")
                print("Patent:", record["patent_title"])

    except Exception as error:
        print("Failed to create test graph.")
        print(error)


if __name__ == "__main__":
    create_test_graph()