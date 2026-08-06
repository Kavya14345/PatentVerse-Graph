# PatentGraph AI

## AI-Powered Patent Relationship Explorer using CognoDB

PatentGraph AI is a graph-based web application that enables users to explore patents, inventors, companies, technologies, and categories through an interactive relationship graph. The application is built using **CognoDB** as the graph database, **FastAPI** for the backend, and **React** for the frontend.

The project demonstrates how graph databases simplify relationship-based queries that are difficult to model efficiently in traditional relational databases.

---

# Features

* Search patents by title or keyword
* View detailed patent information
* Explore patent relationships using an interactive graph
* View inventors, companies, technologies, and patent categories
* Multi-hop graph traversal
* Dashboard with graph statistics
* Responsive and user-friendly interface
* Graceful error handling
* Environment-variable-based configuration
* Parameterized Cypher queries

---

# Technology Stack

## Frontend

* React (Vite)
* Axios
* React Force Graph 2D
* CSS

## Backend

* FastAPI
* Neo4j Python Driver
* Pandas
* Python Dotenv

## Database

* CognoDB Cloud
* Bolt Protocol (Neo4j Driver)
* openCypher

---

# Why a Graph Database?

Patent data is highly connected.

Each patent can be connected to:

* Multiple inventors
* One or more companies
* Multiple technologies
* Categories
* Other patents through citations

A graph database models these relationships directly, making complex traversals simple and efficient.

For example:

* Find all patents using Machine Learning created by inventors working at IBM.
* Find patents that cite another patent within two hops.
* Recommend related patents based on shared technologies.
* Discover the most influential inventors through citation networks.

Implementing these queries in a relational database would require many JOIN operations and become increasingly complex as the relationships grow.

Using CognoDB allows these relationships to be represented naturally using nodes and relationships.

---

# Project Architecture

```
                React Frontend
                       │
                  REST API
                       │
                  FastAPI Backend
                       │
          Neo4j Python Driver (Bolt)
                       │
                  CognoDB Cloud
```

---

# Graph Data Model

## Nodes

### Patent

Properties

* patent_id
* title
* abstract
* patent_number
* year
* status

### Inventor

Properties

* inventor_id
* name
* country

### Company

Properties

* company_id
* name
* industry
* country

### Technology

Properties

* technology_id
* name
* description

### Category

Properties

* category_id
* name

---

## Relationships

```
(Inventor)-[:INVENTED]->(Patent)

(Inventor)-[:WORKS_AT]->(Company)

(Company)-[:OWNS]->(Patent)

(Patent)-[:USES]->(Technology)

(Patent)-[:BELONGS_TO]->(Category)

(Patent)-[:CITES]->(Patent)
```

---

# Folder Structure

```
PatentGraphAI

backend/
    main.py
    database.py
    queries.py
    schemas.py
    seed_loader.py
    generate_seed_data.py
    requirements.txt
    routes/

frontend/
    src/
    public/

seed/
    patents.csv
    inventors.csv
    companies.csv
    technologies.csv
    categories.csv
    invented.csv
    works_at.csv
    owns.csv
    uses.csv
    belongs_to.csv
    cites.csv

README.md
.gitignore
```

---

# Generated Dataset

Instead of using a public patent dataset, this project includes a Python-based data generator that creates realistic synthetic patent data.

The generator automatically produces interconnected graph entities while maintaining realistic relationships between patents, inventors, companies, technologies, and categories.

Generated dataset includes approximately:

| Entity        | Count |
| ------------- | ----: |
| Patents       |   200 |
| Inventors     |   100 |
| Companies     |    30 |
| Technologies  |    25 |
| Categories    |    10 |
| Relationships | 1300+ |

The generated data is deterministic when using a fixed random seed, making the project reproducible for evaluation.

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>

cd PatentGraphAI
```

---

## 2. Create CognoDB Instance

1. Create a free CognoDB account.
2. Create a Free (c0) database instance.
3. Copy the Bolt URI.
4. Save the generated password.

---

## 3. Configure Environment Variables

Create a `.env` file inside the backend directory.

```
COGNODB_URI=bolt+s://your-instance.databases.cognodb.cloud
COGNODB_USERNAME=cognodb
COGNODB_PASSWORD=your-password
```

---

## 4. Install Backend

```
cd backend

pip install -r requirements.txt
```

---

## 5. Generate Dataset

```
python generate_seed_data.py
```

This generates all CSV files inside the `seed` directory.

---

## 6. Load Data into CognoDB

```
python seed_loader.py
```

The loader imports all nodes and relationships into CognoDB using parameterized Cypher queries.

---

## 7. Start Backend

```
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

## 8. Install Frontend

```
cd frontend

npm install
```

---

## 9. Run Frontend

```
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# API Endpoints

### Search Patents

```
GET /patents/search?q=AI
```

---

### Patent Details

```
GET /patents/{id}
```

---

### Patent Graph

```
GET /graph/{id}
```

---

### Company Patents

```
GET /companies/{id}/patents
```

---

### Inventor Patents

```
GET /inventors/{id}/patents
```

---

# Example Graph Query

Find all technologies connected to a patent within two hops.

```cypher
MATCH path =
(p:Patent {patent_id:$id})-[*1..2]-(n)

RETURN path
```

This demonstrates multi-hop traversal, one of the primary strengths of graph databases.

---

# Screenshots

Include screenshots such as:

* Home Page
* Patent Search
* Patent Details
* Graph Visualization
* Dashboard
* CognoDB Graph View

---

# Error Handling

The application includes:

* Database connection validation
* Environment variable validation
* Graceful API error responses
* Empty search result handling
* Loading indicators
* Network failure handling

---

# Future Improvements

* User authentication
* Advanced graph analytics
* Patent recommendation engine
* Technology trend analysis
* Timeline visualization
* Graph filtering
* Export graph data
* Full-text search
* AI-assisted patent similarity detection

---

# Learning Outcomes

This project demonstrates:

* Graph database design
* Graph data modeling
* openCypher query development
* FastAPI backend development
* React frontend development
* REST API design
* Interactive graph visualization
* Data generation and ETL
* Environment-based configuration
* Production-style project organization

---

# Author

**SAMPATHIRAO KAVYA**

WEXA AI Candidate Assignment

PatentGraph AI
