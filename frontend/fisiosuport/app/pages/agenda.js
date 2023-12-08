import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import Agenda from "../components/Agenda";

export default function Agendas(){
    return(
        <>
        <br/>
        <br/>
        <br/>
        <Navbar Title={"Agenda"} Fisioterapeuta={"Nome Fisioterapeuta"}/>
        <Sidebar/>
        <Agenda/>
        </>
    )
}