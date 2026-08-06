from fastapi import APIRouter

from database import get_driver



router=APIRouter(

prefix="/graph",

tags=["Graph"]

)



@router.get("/{patent_id}")


def patent_graph(patent_id:str):

    driver=get_driver()


    query="""

    MATCH path=

    (p:Patent {patent_id:$id})

    -[r*1..2]-

    (n)


    RETURN path

    """



    nodes=[]

    relationships=[]


    with driver.session() as session:


        result=session.run(

            query,

            id=patent_id

        )


        for record in result:


            path=record["path"]


            for node in path.nodes:


                nodes.append({

                    "id":

                    str(node.id),

                    "label":

                    node.get("title",
                             node.get("name")),

                    "type":

                    list(node.labels)[0]

                })



            for rel in path.relationships:


                relationships.append({

                    "source":

                    str(rel.start_node.id),


                    "target":

                    str(rel.end_node.id),


                    "relationship":

                    rel.type

                })



    return {

        "nodes":

        list(

            {

            n["id"]:n

            for n in nodes

            }.values()

        ),


        "relationships":

        relationships

    }