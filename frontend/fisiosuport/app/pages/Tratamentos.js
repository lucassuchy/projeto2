import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import CadastradoTratamento from "../components/cadastroTratamentos";

export default function Tratamento(){
    return(
        <>
        <Navbar  Title={"Cadastrar Tratamento"} Fisioterapeuta={"Nome Fisioterapeuta"}/>
        <Sidebar/>
        <CadastradoTratamento/>
        </>
    )
}