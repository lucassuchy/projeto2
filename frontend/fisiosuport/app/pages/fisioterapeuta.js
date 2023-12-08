import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import Fisioterapeutas from "../components/Fisioterapeuta";

export default function Fisioterapeuta(){
    return(
        <>
        <br/>
        <br/>
        <br/>
        <Navbar  Title={"Fisioterapeutas"} Fisioterapeuta={"Nome Fisioterapeuta"}/>
        <Sidebar/>
        <Fisioterapeutas/>
        </>
    )
}