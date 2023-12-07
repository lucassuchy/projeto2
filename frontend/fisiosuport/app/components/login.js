"use client";
import { useEffect, useState } from "react";
import { useAuth } from "./autenticacao";


export default function Login() {
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");
  const { Login } = useAuth();


  const validaUsuario = (event) => {
    event.preventDefault();
      Login( usuario,password);
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
