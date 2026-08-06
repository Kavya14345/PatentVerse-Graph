from fastapi import APIRouter

from database import get_driver

from queries import COMPANY_PATENTS



router=APIRouter(

prefix="/companies",

tags=["Companies"]

)



@router.get("/{company_id}/patents")

def company_patents(company_id:str):

    driver=get_driver()


    with driver.session() as session:


        result=session.run(

            COMPANY_PATENTS,

            id=company_id

        )


        return [

            r.data()

            for r in result

        ]