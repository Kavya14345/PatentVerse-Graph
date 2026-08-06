import {useState} from "react";
import API from "../api/api";
import SearchBar from "../components/SearchBar";
import PatentCard from "../components/PatentCard";
function Home(){

const [patents,setPatents]=useState([]);

const [loading,setLoading]=useState(false);

async function search(q){

setLoading(true);

try{

const response =
await API.get(
`/patents/search?q=${q}`
);

setPatents(
response.data
);
}
catch(error){
console.log(error);
}
setLoading(false);
}

return (

<div>


<h1>

Patent Search

</h1>
<SearchBar
onSearch={search}
/>

{
loading &&

<p>
Loading patents...
</p>
}
<div>

{

patents.length===0 &&

<p>
No patents found
</p>

}

{

patents.map(
patent=>(

<PatentCard

key={
patent.patent_id
}
patent={patent}
/>
)
)
}
</div>
</div>
)
}
export default Home;