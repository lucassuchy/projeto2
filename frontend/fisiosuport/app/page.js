
import 'w3-css/3/w3.css'

export default function Home() {
  return (
    <>
    <header>
      <div className="w3-container">
        <div className="w3-bar w3-theme">
          <a href="#" className="w3-bar-item w3-button">
            <img src="img.ico" alt='Fisiosuport Logo'/>
          </a>
          <a href="#" className="w3-bar-item w3-button"> INICIO</a>
        </div> 
      </div>
    </header>
    <body>
      <div className="w3-sidebar w3-theme">
        <nav>
      <a href="#" className="w3-bar-item w3-button">Agenda</a>
      <a href="#" className="w3-bar-item w3-button">Pacientes </a>
      <a href="#" className="w3-bar-item w3-button">Exercícios</a>
      <a href="#" className="w3-bar-item w3-button">Fisioterapeuta</a>
      <a href="#" className="w3-bar-item w3-button">Sair</a>
      </nav>
      </div>
    </body>
    </>
  )
}