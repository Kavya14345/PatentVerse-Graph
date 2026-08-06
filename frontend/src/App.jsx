import {

BrowserRouter,

Routes,

Route

}

from "react-router-dom";


import Navbar from "./components/Navbar";

import Home from "./pages/Home";

import PatentDetails from "./pages/PatentDetails";



function App(){


return (

<BrowserRouter>


<Navbar/>


<Routes>


<Route

path="/"

element={<Home/>}

/>


<Route

path="/patent/:id"

element={<PatentDetails/>}

/>


</Routes>


</BrowserRouter>

)


}


export default App;