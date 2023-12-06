"use client";
import axios from "axios";
import { useState } from "react";


export default function CadastraExercicios() {
    const [name,setName] = useState("");
    const [password,setpassword] = useState("");
    const [documento,setDocumento] = useState(0);
    const [type,setType] = useState(0);
    const [birth_date, setBirth_date] = useState(0);

    const novoUsuario = event => {
        event.preventDefault();

        axios({
            method: 'post',
            url: 'http://18.231.170.222:8080/users/',
            data: {
                name: name,
                password: password,
                document: documento,
                type_id: type,
                birth_date: birth_date
            },
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            console.log("Usuario "+response.data.name+ " cadastrado com sucesso!");
        }).catch(err => console.log(err));
    }

  return (
    <div className="p-4 sm:ml-64">
      <div className="p-16 bg-gray-800 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-10">
        <div className="grid grid-cols-1 gap-0 mb-0">
          <form onSubmit={novoUsuario}>
            <div className="grid gap-10 mb-10 md:grid-cols-2">
              <div>
                <label htmlFor="name" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"> Nome Completo: </label>
                <input
                  name="name"
                  type="text"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Digite seu nome completo"
                  value={name}
                  onChange={(ev) => setName(ev.target.value)}/>
              </div>
              <br />
              <div>
                <label
                  htmlFor="password"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Senha:
                </label>
                <input
                  name="password"
                  type="password"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Informe uma senha"
                  value={password}
                  onChange={(ev) => setpassword(ev.target.value)}
                />
              </div>
              <br />
              <div>
                <label
                  htmlFor="document"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  CPF:
                </label>
                <input
                  name="document"
                  type="text"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Informe o seu CPF"
                  value={documento}
                  onChange={(ev) => setDocumento(ev.target.value)}
                />
              </div>
              <br />
              <div>
                <label
                  htmlFor="type_id"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Tipo:
                </label>
                <select
                  name="type_id"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  value={type}
                  onChange={(ev) => setType(ev.target.value)}
                ><option value="0">Selecione</option>
                  <option value="1">Fisioterapeuta</option>
                  <option value="2">Paciente</option>
                </select>
              </div>
              <br />
              <div>
                <label
                  htmlFor="birth_date"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Data de Nascimento:
                </label>
                <input
                  name="birth_date"
                  type="text"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="2000-01-01"
                  value={birth_date}
                  onChange={(ev) => setBirth_date(ev.target.value)}
                />
              </div>
              <br/>
          <input type="submit"
            value="Salvar"
            className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
            </input>  
            </div>
          </form>            
        </div>
      </div>
    </div>
  );
}
