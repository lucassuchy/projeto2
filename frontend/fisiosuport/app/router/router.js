import { BrowserRouter, Routes, Route, useNavigate  } from "react-router-dom";
import Fisioterapeuta from '../pages/fisioterapeuta'
import Paciente from "../pages/pacientes";
import CadastrardoPacientes from "../pages/CadatroPaciente";
import Home from "../pages/home";
import Exercicios from "../pages/exercicios";
import Tratamento from "../pages/Tratamentos";
import EditaPacientes from "../pages/editaPaciente";


export default function Routers() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/fisioterapeuta" element={<Fisioterapeuta />} />
          <Route path="/paciente" element={<Paciente/>}/>
          <Route path="/cadastroPaciente" element={<CadastrardoPacientes />}/>
          <Route path="/exercicios" element={<Exercicios />}/>
          <Route path="/tratamentos" element={<Tratamento />}/>
          <Route path="/editaPaciente/:patient_id" element={<EditaPacientes />}/>
        </Routes>
      </BrowserRouter>
    );
  }