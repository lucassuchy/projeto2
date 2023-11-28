
// import InicialFisioterapeuta from './components/InicialFisioterapeuta'
import Navbar from './components/navbar'
import Sidebar from './components/sidebar'
import CadastradoUsuarios from "./components/CadastradoUsuarios"
import InicialFisioterapeuta from './components/Fisioterapeuta'

export default function Home() {
  return (
    <>
        <Navbar/>
        <Sidebar/>
        <InicialFisioterapeuta />
    </>
    
  )
}
