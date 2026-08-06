SEARCH_PATENTS = """

MATCH (p:Patent)

WHERE 
toLower(p.title)
CONTAINS
toLower($keyword)

RETURN

p.patent_id AS patent_id,
p.title AS title,
p.abstract AS abstract,
p.year AS year,
p.status AS status

LIMIT 20

"""


GET_PATENT = """

MATCH (p:Patent)

WHERE p.patent_id=$id

RETURN

p.patent_id AS patent_id,
p.title AS title,
p.abstract AS abstract,
p.year AS year,
p.status AS status

"""


PATENT_GRAPH = """

MATCH path=

(p:Patent {patent_id:$id})
-[r*1..2]-
(n)


RETURN path

"""


COMPANY_PATENTS = """

MATCH

(c:Company)
-[:OWNS]->
(p:Patent)

WHERE

c.company_id=$id


RETURN

p.patent_id AS patent_id,
p.title AS title,
p.abstract AS abstract,
p.year AS year,
p.status AS status

"""


INVENTOR_PATENTS = """

MATCH

(i:Inventor)
-[:INVENTED]->
(p:Patent)

WHERE

i.inventor_id=$id


RETURN

p.patent_id AS patent_id,
p.title AS title,
p.abstract AS abstract,
p.year AS year,
p.status AS status

"""