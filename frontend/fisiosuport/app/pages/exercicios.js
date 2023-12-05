import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import CadastraExercicios from "../components/CadastroExercicios";

export default function Exercicios(){
    return(
        <>
        <Navbar Title={"Exercicios"} Fisioterapeuta={"Nome Fisioterapeuta"}/>
        <Sidebar/>
        <CadastraExercicios/>
        </>
    )
}