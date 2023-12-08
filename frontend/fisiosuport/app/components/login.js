"use client";
import {  useState } from "react";
import { useNavigate  } from "react-router-dom";
import axios from "axios";




export default function Login() {
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const url = "http://18.230.187.219:8080";
  let endpoint = url.concat("/login/");

  const validaUsuario = async (event) => {
    event.preventDefault();
      try {
        const res = await axios({
          method: "post",
          url: endpoint,
          data: {
            document: usuario,
            password: password
    
          },
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
        })
        console.log("resposta:", res.data.ok)
        if (res.data.ok === true) {
          navigate("/home");
        }else{
          alert("Usuario ou senha invalidos");
        }
      } catch (e) {
        alert("Usuario ou senha invalidos");
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
  <p className="faca_login grid place-items-center text-white">
    Faça login em sua conta
  </p>
</div>
<br />
<br />

<form onSubmit={validaUsuario} className="text-center">
  <div className="container grid place-items-center text-white">
    <label className="labelUsuario">Usuário</label>
    <input
      required=""
      type="text"
      name="text"
      className="input text-black"
      value={usuario}
      onChange={(ev) => setUsuario(ev.target.value)}
    />
  </div>
  <br />
  <br />
  <div className="container grid place-items-center text-white">
    <label htmlFor="label_senha" className="label">
      Senha
    </label>
    <input
      required=""
      id="pass"
      type="password"
      name="text"
      className="input text-black"
      minLength="1"
      maxLength="200"
      value={password}
      onChange={(ev) => setPassword(ev.target.value)}
    />
  </div>
  <br />
  <br />
  <div className="button_enter">
    <button className="text-white rounded-lg w-48 dark:text-blue bg-slate-900 dark:hover:bg-gray-700 group">Entrar</button>
  </div>
</form>

    </>
  );
}
