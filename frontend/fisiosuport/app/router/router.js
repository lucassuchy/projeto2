import { BrowserRouter, Routes, Route } from "react-router-dom";
import Fisioterapeuta from '../pages/fisioterapeuta'
import CadastradarUsuarios from "../pages/cadastroUsuarios";
import Agenda from "../pages/Agenda/Agenda";

export default function Routers() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/fisioterapeuta" element={<Fisioterapeuta />} />
          <Route path="/cadastroUsuarios" element={<CadastradarUsuarios/>}/>
          <Route path="/agenda" element={<Agenda/>}/>
        </Routes>
      </BrowserRouter>
    );
  }