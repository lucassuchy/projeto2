'use client'
import axios from "axios";
import { useState } from "react";


export default function CadastradoUsuarios(){

    const [name,setName] = useState("");
    const [password,setpassword] = useState("");
    const [documento,setDocumento] = useState(0);
    const [type,setType] = useState(0);
    const [birth_date, setBirth_date] = useState(0);


    const novoUsuario = event => {
        event.preventDefault();

        axios.post("http://localhost:8000/users", {
            name: nome,
            password: password,
            document: documento,
            type_id: type,
            birth_date: birth_date
        }).then((response) => { 
            alert("Usuario "+response.data.id+ " cadastrado com sucesso!");
            setName(""); 
            setpassword("");
            setDocumento(0);
            setType(1);
            setBirth_date(0);
        }).catch(err => console.log(err))

    }

    return(

        <div className="p-4 sm:ml-64">
        <div className="p-16 bg-slate-300 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14"> 
            <form onSubmit={novoUsuario}>
            <label  htmlFor="name">Nome Completo</label>  
                <input name="name" type="text" placeholder="Nome Completo" value={name} onChange={(ev) => setName(ev.target.value)} /> 
            <br/>
            <label htmlFor="password">Senha</label>
                <input name="password" type="password" placeholder="Senha" value={password} onChange={(ev) => setpassword(ev.target.value)} />
            <br/>
            <label htmlFor="document">Documento</label>  
                <input name="document" type="text" placeholder="Documento" value={documento} onChange={(ev) => setDocumento(ev.target.value)}/>
            <br/>
            <label  htmlFor="type_id">Tipo</label>
                <select name="type_id" value={type} onChange={(ev) => setType(ev.target.value)}>
                <option value="1">Fisioterapeuta</option>
                <option value="2">Paciente</option>
                </select>
            <br/>
            <label htmlFor="birth_date">Data de Nascimento</label>  
                <input name="birth_date" type="text" placeholder="2000-01-01" value={birth_date} onChange={(ev) => setBirth_date(ev.target.value)}/>
            <br/>
            <input type="submit"></input>
        </form>
        </div>
    </div>
        


    )


}