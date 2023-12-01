"use client";
import axios from "axios";
import { useEffect, useState } from "react";

export default function Login() {

    const [usuario, setUsuario] = useState("");
    const [password, setPassword] = useState("");
    const validaUsuario = event => {
        event.preventDefault();
    const url = 'http://localhost:8000'
    let endpoint = url.concat('/users/')
    
    const [listaUsers, setlistaUsers] = useState([]);

    useEffect(() => { 
        axios.get(endpoint)
        .then(function (response) {  
            setlistaUsers(response.data);})
        }, [])
    };

    return(
        <>
            <div className="grid place-items-center">
                <img
                    src="/Fisiosuport_logo.png"
                    alt="Logotipo FisioSuport"
                    className="logo_inicial object-cover h-30 w-80"
                />
            </div>
            <div>
                <p className="faca_login grid place-items-center">Faça login em sua conta</p>
            </div>
            <br />
            <br />
            <form onSubmit={validaUsuario}>
                <div className="container grid place-items-center text-black">
                    <input required="" type="text" name="text" className="input" value={usuario} onChange={(ev) => setUsuario(ev.target.value)} />
                    <label className="label ">Usuário</label>
                </div>
                <br /><br />
                <div className="container grid place-items-center text-black">
                    <input required="" id="pass" type="password" name="text" className="input" minlength="1" maxlength="200" value={password} onChange={(ev) => setPassword(ev.target.value)}/>
                    <label for="pass" className="label">Senha</label>
                </div>
                <br /><br />
                <div className="button_enter grid place-items-center">
                    <button>Entrar</button>
                </div>
            </form>
        </>
    )   
}