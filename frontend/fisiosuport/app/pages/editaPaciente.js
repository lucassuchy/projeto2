import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import EditaPaciente from "../components/editaPaciente";

export default function EditaPacientes(){
    return(
        <>
        <Navbar  Title={"Edita Pacientes"} Fisioterapeuta={"Nome Fisioterapeuta"} path = {"../../img.ico"}/>
        <Sidebar/>
        <EditaPaciente/>
        </>
    )
}