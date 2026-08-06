import random
import os
import pandas as pd

random.seed(42)

SEED_FOLDER = os.path.join(os.path.dirname(__file__), "..", "seed")

os.makedirs(SEED_FOLDER, exist_ok=True)

##################################################
# CONFIG
##################################################

NUM_PATENTS = 200
NUM_INVENTORS = 100
NUM_COMPANIES = 30
NUM_TECHNOLOGIES = 25
NUM_CATEGORIES = 10

##################################################
# TECHNOLOGIES
##################################################

technology_names = [
    "Machine Learning",
    "Deep Learning",
    "Blockchain",
    "Quantum Computing",
    "Computer Vision",
    "Natural Language Processing",
    "Cloud Computing",
    "Edge AI",
    "Cyber Security",
    "IoT",
    "Robotics",
    "Big Data",
    "Data Mining",
    "Autonomous Vehicles",
    "5G Networks",
    "Digital Twin",
    "Augmented Reality",
    "Virtual Reality",
    "Healthcare AI",
    "Bioinformatics",
    "Speech Recognition",
    "Generative AI",
    "Reinforcement Learning",
    "Predictive Analytics",
    "Green Computing"
]

##################################################
# CATEGORIES
##################################################

category_names = [
    "Healthcare",
    "Transportation",
    "Finance",
    "Education",
    "Agriculture",
    "Energy",
    "Cyber Security",
    "Artificial Intelligence",
    "Manufacturing",
    "Telecommunication"
]

##################################################
# COMPANIES
##################################################

company_names = [
    "Google",
    "Microsoft",
    "IBM",
    "Intel",
    "Tesla",
    "Apple",
    "Amazon",
    "Samsung",
    "Oracle",
    "NVIDIA",
    "Cisco",
    "Meta",
    "Adobe",
    "Qualcomm",
    "Sony",
    "Infosys",
    "TCS",
    "Wipro",
    "Accenture",
    "SAP",
    "Dell",
    "HP",
    "Siemens",
    "Bosch",
    "Honeywell",
    "Philips",
    "SpaceX",
    "OpenAI",
    "DeepMind",
    "Zoho"
]

##################################################
# FIRST NAMES
##################################################

first_names = [
    "John","David","Sarah","Emily","Michael",
    "Alice","Chris","Robert","Daniel","Sophia",
    "James","Emma","Liam","Olivia","Noah",
    "Ava","Ethan","Mia","Lucas","Grace"
]

##################################################
# LAST NAMES
##################################################

last_names = [
    "Smith","Johnson","Brown","Williams",
    "Jones","Miller","Davis","Wilson",
    "Moore","Taylor","Thomas","Lee",
    "Martin","White","Clark"
]

##################################################
# COUNTRIES
##################################################

countries = [
    "USA",
    "India",
    "Canada",
    "Germany",
    "UK",
    "Japan",
    "France",
    "Australia"
]

##################################################
# PATENT WORDS
##################################################

patent_words = [
    "AI",
    "Smart",
    "Autonomous",
    "Quantum",
    "Secure",
    "Predictive",
    "Medical",
    "Cloud",
    "Vision",
    "Learning",
    "Analysis",
    "Detection",
    "Monitoring",
    "Control",
    "Optimization",
    "Platform",
    "Framework",
    "System"
]

##################################################
# PATENTS
##################################################

patents=[]

for i in range(1,NUM_PATENTS+1):

    title=" ".join(random.sample(patent_words,3))

    patents.append({

        "patent_id":f"P{i:03}",

        "title":title,

        "abstract":f"This patent describes {title}.",

        "year":random.randint(2018,2025),

        "patent_number":f"US{100000+i}",

        "status":random.choice(["Granted","Pending"])

    })

pd.DataFrame(patents).to_csv(

    f"{SEED_FOLDER}/patents.csv",

    index=False

)

##################################################
# INVENTORS
##################################################

inventors=[]

for i in range(1,NUM_INVENTORS+1):

    inventors.append({

        "inventor_id":f"I{i:03}",

        "name":

        random.choice(first_names)+" "+random.choice(last_names),

        "country":random.choice(countries)

    })

pd.DataFrame(inventors).to_csv(

    f"{SEED_FOLDER}/inventors.csv",

    index=False

)

##################################################
# COMPANIES
##################################################

companies=[]

for i,name in enumerate(company_names,start=1):

    companies.append({

        "company_id":f"C{i:03}",

        "name":name,

        "industry":"Technology",

        "country":"USA"

    })

pd.DataFrame(companies).to_csv(

    f"{SEED_FOLDER}/companies.csv",

    index=False

)

##################################################
# TECHNOLOGIES
##################################################

tech=[]

for i,name in enumerate(technology_names,start=1):

    tech.append({

        "technology_id":f"T{i:03}",

        "name":name,

        "description":name

    })

pd.DataFrame(tech).to_csv(

    f"{SEED_FOLDER}/technologies.csv",

    index=False

)

##################################################
# CATEGORIES
##################################################

cats=[]

for i,name in enumerate(category_names,start=1):

    cats.append({

        "category_id":f"CAT{i:03}",

        "name":name

    })

pd.DataFrame(cats).to_csv(

    f"{SEED_FOLDER}/categories.csv",

    index=False

)

##################################################
# RELATIONSHIPS
##################################################

invented=[]
works=[]
owns=[]
uses=[]
belongs=[]
cites=[]

for i in range(1,NUM_PATENTS+1):

    pid=f"P{i:03}"

    inventor=random.randint(1,NUM_INVENTORS)

    company=random.randint(1,NUM_COMPANIES)

    category=random.randint(1,NUM_CATEGORIES)

    invented.append({

        "inventor_id":f"I{inventor:03}",

        "patent_id":pid

    })

    works.append({

        "inventor_id":f"I{inventor:03}",

        "company_id":f"C{company:03}"

    })

    owns.append({

        "company_id":f"C{company:03}",

        "patent_id":pid

    })

    belongs.append({

        "patent_id":pid,

        "category_id":f"CAT{category:03}"

    })

    techs=random.sample(range(1,NUM_TECHNOLOGIES+1),2)

    for t in techs:

        uses.append({

            "patent_id":pid,

            "technology_id":f"T{t:03}"

        })

    if i>1:

        cites.append({

            "source_patent":pid,

            "target_patent":f"P{random.randint(1,i-1):03}"

        })

pd.DataFrame(invented).to_csv(

    f"{SEED_FOLDER}/invented.csv",

    index=False

)

pd.DataFrame(works).drop_duplicates().to_csv(

    f"{SEED_FOLDER}/works_at.csv",

    index=False

)

pd.DataFrame(owns).to_csv(

    f"{SEED_FOLDER}/owns.csv",

    index=False

)

pd.DataFrame(uses).to_csv(

    f"{SEED_FOLDER}/uses.csv",

    index=False

)

pd.DataFrame(belongs).to_csv(

    f"{SEED_FOLDER}/belongs_to.csv",

    index=False

)

pd.DataFrame(cites).to_csv(

    f"{SEED_FOLDER}/cites.csv",

    index=False

)

print("\nSeed Data Generated Successfully!\n")

print("Patents:",NUM_PATENTS)
print("Inventors:",NUM_INVENTORS)
print("Companies:",NUM_COMPANIES)
print("Technologies:",NUM_TECHNOLOGIES)
print("Categories:",NUM_CATEGORIES)