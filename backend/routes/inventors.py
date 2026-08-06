from fastapi import APIRouter

from database import get_driver

from queries import INVENTOR_PATENTS



router=APIRouter(

prefix="/inventors",

tags=["Inventors"]

)



@router.get("/{inventor_id}/patents")


def inventor_patents(inventor_id:str):


    driver=get_driver()


    with driver.session() as session:


        result=session.run(

            INVENTOR_PATENTS,

            id=inventor_id

        )


        return [

            r.data()

            for r in result

        ]