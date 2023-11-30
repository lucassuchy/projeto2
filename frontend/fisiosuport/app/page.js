
// import InicialFisioterapeuta from './components/InicialFisioterapeuta'
'use client'
import Navbar from './components/navbar'
import Sidebar from './components/sidebar'
import Routers from './router/router'

export default function Home() {
  return (
    <>
        <Navbar/>
        <Routers>
          <Sidebar/>
        </Routers>
    </>
  )
}
