import { BrowserRouter, Routes, Route } from "react-router-dom";
import Fisioterapeuta from '../pages/fisioterapeuta'
import CadastradarUsuarios from "../pages/cadastroUsuarios";
import Paciente from "../pages/pacientes";
import CadastrardoPacientes from "../pages/CadatroPaciente";


export default function Routers() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/fisioterapeuta" element={<Fisioterapeuta />} />
          <Route path="/cadastroUsuarios" element={<CadastradarUsuarios />}/>
          <Route path="/paciente" element={<Paciente/>}/>
          <Route path="/cadastroPaciente" element={<CadastrardoPacientes />}/>
        </Routes>
      </BrowserRouter>
    );
  }