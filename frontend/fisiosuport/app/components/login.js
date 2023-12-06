"use client";
import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate  } from "react-router-dom";


export default function Login() {
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");
  const [login, setLogin] = useState("");
  const navigate = useNavigate();
  const url = "http://18.231.170.222:8080";
  let endpoint = url.concat("/user_login/");


  // To com problema pra ele chamar o usuario no banco e validar
  // Posso mudar pra fazer uma requisição pro back e validar no back, retorna true ou alguma coisa assim
  
  axios({
    method: "post",
    url: endpoint,
    data: {
      name: name,
      password: "passwordUsuarios",
    },
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })

  const validaUsuario = (event) => {
    event.preventDefault();

    console.log(login)
    if (login.password == password){
      navigate("/paciente");
    }
  };

  return (
    <>
      <div className="grid place-items-center">
        <img
          src="/Fisiosuport_logo.png"
          alt="Logotipo FisioSuport"
          className="logo_inicial object-cover h-15 w-80"
        />
      </div>
      <div>
        <p className="faca_login grid place-items-center">
          Faça login em sua conta
        </p>
      </div>
      <br />
      <br />

      <form onSubmit={validaUsuario}>
        <label className="labelUsuario ">Usuário</label>
        <div className="container grid place-items-center text-black">
          <input
            required=""
            type="text"
            name="text"
            className="input"
            value={usuario}
            onChange={(ev) => setUsuario(ev.target.value)}
          />
        </div>
        <br />
        <br />
        <label htmlFor="label_senha" className="label">
          Senha
        </label>
        <div className="container grid place-items-center text-black">
          <input
            required=""
            id="pass"
            type="password"
            name="text"
            className="input"
            minLength="1"
            maxLength="200"
            value={password}
            onChange={(ev) => setPassword(ev.target.value)}
          />
        </div>
        <br />
        <br />
        <div className="button_enter">
          <button>Entrar</button>
        </div>
      </form>
    </>
  );
}
