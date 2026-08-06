import pandas as pd
from database import get_driver
import os

driver = get_driver()

SEED_FOLDER = os.path.join(os.path.dirname(__file__), "..", "seed")

# Load CSVs
patents = pd.read_csv(f"{SEED_FOLDER}/patents.csv")
inventors = pd.read_csv(f"{SEED_FOLDER}/inventors.csv")
companies = pd.read_csv(f"{SEED_FOLDER}/companies.csv")
technologies = pd.read_csv(f"{SEED_FOLDER}/technologies.csv")
categories = pd.read_csv(f"{SEED_FOLDER}/categories.csv")
invented = pd.read_csv(f"{SEED_FOLDER}/invented.csv")
works_at = pd.read_csv(f"{SEED_FOLDER}/works_at.csv")
owns = pd.read_csv(f"{SEED_FOLDER}/owns.csv")
uses = pd.read_csv(f"{SEED_FOLDER}/uses.csv")
belongs_to = pd.read_csv(f"{SEED_FOLDER}/belongs_to.csv")
cites = pd.read_csv(f"{SEED_FOLDER}/cites.csv")


def load_patents():
    with driver.session() as session:
        for _, row in patents.iterrows():
            session.run("""
                MERGE (p:Patent {patent_id:$id})
                SET p.title=$title,
                    p.abstract=$abstract,
                    p.year=$year,
                    p.patent_number=$number,
                    p.status=$status
            """,
            id=row["patent_id"],
            title=row["title"],
            abstract=row["abstract"],
            year=int(row["year"]),
            number=row["patent_number"],
            status=row["status"])
    print("Patents Loaded")


def load_inventors():
    with driver.session() as session:
        for _, row in inventors.iterrows():
            session.run("""
                MERGE (i:Inventor {inventor_id:$id})
                SET i.name=$name,
                    i.country=$country
            """,
            id=row["inventor_id"],
            name=row["name"],
            country=row["country"])
    print("Inventors Loaded")


def load_companies():
    with driver.session() as session:
        for _, row in companies.iterrows():
            session.run("""
                MERGE (c:Company {company_id:$id})
                SET c.name=$name,
                    c.industry=$industry,
                    c.country=$country
            """,
            id=row["company_id"],
            name=row["name"],
            industry=row["industry"],
            country=row["country"])
    print("Companies Loaded")


def load_technologies():
    with driver.session() as session:
        for _, row in technologies.iterrows():
            session.run("""
                MERGE (t:Technology {technology_id:$id})
                SET t.name=$name,
                    t.description=$description
            """,
            id=row["technology_id"],
            name=row["name"],
            description=row["description"])
    print("Technologies Loaded")


def load_categories():
    with driver.session() as session:
        for _, row in categories.iterrows():
            session.run("""
                MERGE (c:Category {category_id:$id})
                SET c.name=$name
            """,
            id=row["category_id"],
            name=row["name"])
    print("Categories Loaded")


def load_invented():
    with driver.session() as session:
        for _, row in invented.iterrows():
            session.run("""
                MATCH (i:Inventor {inventor_id:$inventor})
                MATCH (p:Patent {patent_id:$patent})
                MERGE (i)-[:INVENTED]->(p)
            """,
            inventor=row["inventor_id"],
            patent=row["patent_id"])
    print("Invented Loaded")


def load_works_at():
    with driver.session() as session:
        for _, row in works_at.iterrows():
            session.run("""
                MATCH (i:Inventor {inventor_id:$inventor})
                MATCH (c:Company {company_id:$company})
                MERGE (i)-[:WORKS_AT]->(c)
            """,
            inventor=row["inventor_id"],
            company=row["company_id"])
    print("WorksAt Loaded")


def load_owns():
    with driver.session() as session:
        for _, row in owns.iterrows():
            session.run("""
                MATCH (c:Company {company_id:$company})
                MATCH (p:Patent {patent_id:$patent})
                MERGE (c)-[:OWNS]->(p)
            """,
            company=row["company_id"],
            patent=row["patent_id"])
    print("Owns Loaded")


def load_uses():
    with driver.session() as session:
        for _, row in uses.iterrows():
            session.run("""
                MATCH (p:Patent {patent_id:$patent})
                MATCH (t:Technology {technology_id:$tech})
                MERGE (p)-[:USES]->(t)
            """,
            patent=row["patent_id"],
            tech=row["technology_id"])
    print("Uses Loaded")


def load_belongs_to():
    with driver.session() as session:
        for _, row in belongs_to.iterrows():
            session.run("""
                MATCH (p:Patent {patent_id:$patent})
                MATCH (c:Category {category_id:$cat})
                MERGE (p)-[:BELONGS_TO]->(c)
            """,
            patent=row["patent_id"],
            cat=row["category_id"])
    print("BelongsTo Loaded")


def load_cites():
    with driver.session() as session:
        for _, row in cites.iterrows():
            session.run("""
                MATCH (a:Patent {patent_id:$source})
                MATCH (b:Patent {patent_id:$target})
                MERGE (a)-[:CITES]->(b)
            """,
            source=row["source_patent"],
            target=row["target_patent"])
    print("Citations Loaded")


if __name__ == "__main__":
    load_patents()
    load_inventors()
    load_companies()
    load_technologies()
    load_categories()
    load_invented()
    load_works_at()
    load_owns()
    load_uses()
    load_belongs_to()
    load_cites()
    print("Database Seed Completed")
