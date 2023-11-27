
// import InicialFisioterapeuta from './components/InicialFisioterapeuta'
import Navbar from './components/navbar'
import Sidebar from './components/sidebar'
import CadastradoUsuarios from "./components/CadastradoUsuarios"
import Pacientes from './components/Pacientes'

export default function Home() {
  return (
    <>
        <Navbar/>
        <Sidebar/>
        <CadastradoUsuarios />
    </>
    
  )
}
