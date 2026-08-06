# PatentGraph AI Graph Data Model

PatentGraph AI represents patent intelligence as a connected graph.

## Nodes

### Patent

Properties:

- patent_id
- title
- abstract
- year
- patent_number
- status

### Inventor

Properties:

- inventor_id
- name
- country

### Company

Properties:

- company_id
- name
- industry
- country

### Technology

Properties:

- technology_id
- name
- description

### Category

Properties:

- category_id
- name

## Relationships

Inventor -[:INVENTED]-> Patent

Inventor -[:WORKS_AT]-> Company

Company -[:OWNS]-> Patent

Patent -[:USES]-> Technology

Patent -[:CITES]-> Patent

Patent -[:BELONGS_TO]-> Category

## Graph Model

Company <- WORKS_AT - Inventor

Company - OWNS -> Patent

Inventor - INVENTED -> Patent

Patent - USES -> Technology

Patent - CITES -> Patent

Patent - BELONGS_TO -> Category