
// import InicialFisioterapeuta from './components/InicialFisioterapeuta'
'use client'
import Sidebar from './components/sidebar'
import Routers from './router/router'

export default function Home() {
  return (
    <> 
        <Routers>
          <Sidebar/>
        </Routers>
    </>
  )
}
