import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import Pacientes from "../components/Paciente";

export default function Paciente(){
    return(
        <>
        <Navbar  Title={"Pacientes"} Fisioterapeuta={"Nome Fisioterapeuta"}/>
        <Sidebar/>
        <Pacientes/>
        </>
    )
}