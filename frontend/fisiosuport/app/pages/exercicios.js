import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import CadastraExercicios from "../components/CadastroExercicios";

export default function Exercicios(){
    return(
        <>
        <br/>
        <br/>
        <br/>
        <Navbar Title={"Exercicios"} Fisioterapeuta={"Nome Fisioterapeuta"}/>
        <Sidebar/>
        <CadastraExercicios/>
        </>
    )
}