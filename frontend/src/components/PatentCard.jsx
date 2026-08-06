import { Link } from "react-router-dom";


function PatentCard({ patent }) {


    return (

        <div className="card">


            <h3>

                {patent.title}

            </h3>


            <p>

                Year:
                {patent.year}

            </p>


            <p>

                Status:
                {patent.status}

            </p>


            <Link
                to={`/patent/${patent.patent_id}`}
            >

                View Graph

            </Link>


        </div>


    )


}


export default PatentCard;