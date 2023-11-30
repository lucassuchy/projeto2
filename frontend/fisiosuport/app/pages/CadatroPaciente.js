import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import CadastradoPaciente from "../components/cadastroPaciente";

export default function CadastrardoPacientes(){
    return(
        <>
        <Navbar  Title={"Cadastrar Pacientes"}/>
        <Sidebar/>
        <CadastradoPaciente/>
        </>
    )
}