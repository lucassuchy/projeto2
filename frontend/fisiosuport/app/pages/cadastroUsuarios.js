import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import CadastradoUsuarios from "../components/CadastradoUsuarios";

export default function CadastrardoUsuarios(){
    return(
        <>
        <Navbar Title={"Cadastrar Usuarios"}/>
        <Sidebar/>
        <CadastradoUsuarios/>
        </>
    )
}