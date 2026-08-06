from fastapi import APIRouter

from database import get_driver

from queries import (
    SEARCH_PATENTS,
    GET_PATENT
)


router = APIRouter(

    prefix="/patents",

    tags=["Patents"]

)



@router.get("/search")


def search_patents(q:str):

    driver=get_driver()


    with driver.session() as session:

        result=session.run(

            SEARCH_PATENTS,

            keyword=q

        )


        return [

            record.data()

            for record in result

        ]




@router.get("/{patent_id}")


def get_patent(patent_id:str):

    driver=get_driver()


    with driver.session() as session:

        result=session.run(

            GET_PATENT,

            id=patent_id

        )


        record=result.single()


        if record:

            return record.data()


        return {

            "message":
            "Patent not found"

        }