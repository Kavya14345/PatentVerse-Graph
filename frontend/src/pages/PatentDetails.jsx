import {useParams} from "react-router-dom";

import {useEffect,useState} from "react";

import API from "../api/api";

import GraphViewer from "../components/GraphViewer";

function PatentDetails(){


const {id}=useParams();
const [graph,setGraph]=useState(null);

useEffect(()=>{


API.get(`/graph/${id}`)

.then(
res=>setGraph(res.data)
);


},[]);



return (

<div>


<h1>
Patent Graph
</h1>


{

graph ?

<GraphViewer data={graph}/>

:

<p>
Loading graph...
</p>


}



</div>


)


}


export default PatentDetails;