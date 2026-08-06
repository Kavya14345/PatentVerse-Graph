import {useState} from "react";
function SearchBar({onSearch}){
const [query,setQuery]=useState("");
function submit(){
if(query.trim()){
onSearch(query);
}
}
return (
<div>
<input
placeholder="Search patents..."
value={query}
onChange={
e=>setQuery(e.target.value)
}
/>
<button onClick={submit}>
Search
</button>
</div>)
}
export default SearchBar;