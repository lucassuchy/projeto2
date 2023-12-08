"use client";
import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate  } from "react-router-dom";


export default function CadastradoPaciente() {
  const [name, setName] = useState("");
  const [documento, setDocumento] = useState(0);
  const [birth_date, setBirth_date] = useState(0);
  const [fisioterapeuta_id, setfisioterapeuta_id] = useState(0);
  const [quantity, setQuantity] = useState(0);
  const [duration, setDuration] = useState(0);
  const [treatment, setTreatment] = useState(0);
  const [description, setdescription] = useState("");
  const url = "http://18.230.187.219:8080"
  const navigate = useNavigate();


  // Novo usuario
  const novoPaciente = (event) => {
    event.preventDefault();

    const navigate = useNavigate();

    axios({
      method: "post",
      url: url.concat("/patient/"),
      data: {
        name: name,
        password: "passwordUsuarios",
        document: documento,
        type_id: "2",
        birth_date: birth_date,
        quantity: quantity,
        duration: duration,
        treatment_id: treatment,
        description: description,
        physiotherapist_id: fisioterapeuta_id,
      },
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
      .then(function (response) {
        console.log("Usuario " + response.data.id + " cadastrado com sucesso!");
      })
      navigate("/paciente")
      .catch((err) => console.log(err));
  };

  // Busca os dados
  let endpoint_physiotherapist = url.concat("/physiotherapist/");

  const [listaFisioterapeutas, setlistaFisioterapeutas] = useState([]);

  useEffect(() => {
    axios.get(endpoint_physiotherapist).then(function (response) {
      setlistaFisioterapeutas(response.data);
    });
  }, []);

  let endpoint_treatment = url.concat("/treatment/");

  const [listatreatment, setlistaTreatment] = useState([]);

  useEffect(() => {
    axios.get(endpoint_treatment).then(function (response) {
      setlistaTreatment(response.data);
    });
  }, []);

  return (
    <div className="p-4 sm:ml-64">
      <div className="p-16 bg-gray-800 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-10">
        <div className="grid grid-cols-1 gap-0 mb-0">
          <form onSubmit={novoPaciente}>
            <div className="grid gap-10 mb-10 md:grid-cols-2">
              <div>
                <label
                  htmlFor="name"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  {" "}
                  Nome Completo:{" "}
                </label>
                <input
                  name="name"
                  type="text"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Digite seu nome completo"
                  value={name}
                  onChange={(ev) => setName(ev.target.value)}
                />
              </div>
              <br />
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
              <br />
              <div>
                <label
                  htmlFor="type_id"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Fisioterapeuta:
                </label>
                <select
                  name="type_id"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  value={fisioterapeuta_id}
                  onChange={(ev) => setfisioterapeuta_id(ev.target.value)}
                >
                  {listaFisioterapeutas.map((fisioterapeuta) => (
                    <option value={fisioterapeuta.id}>
                      {fisioterapeuta.name}
                    </option>
                  ))}
                </select>
              </div>
              <br />
              <div>
                <label
                  htmlFor="birth_date"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Quantidade de Repetições:
                </label>
                <input
                  name="birth_date"
                  type="text"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="2000-01-01"
                  value={quantity}
                  onChange={(ev) => setQuantity(ev.target.value)}
                />
              </div>
              <br />
              <div>
                <label
                  htmlFor="birth_date"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Quantidade de semanas:
                </label>
                <input
                  name="birth_date"
                  type="text"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="2000-01-01"
                  value={duration}
                  onChange={(ev) => setDuration(ev.target.value)}
                />
              </div>
              <br />
              <div>
                <label
                  htmlFor="type_id"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Tratamento:
                </label>
                <select
                  name="type_id"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  value={treatment}
                  onChange={(ev) => setTreatment(ev.target.value)}
                >
                  {listatreatment.map((tratamento) => (
                    <option value={tratamento.id}>{tratamento.name}</option>
                  ))}
                </select>
              </div>
              <br />
              <div>
                <label
                  htmlFor="birth_date"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Descrição:
                </label>
                <input
                  name="birth_date"
                  type="text"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Descrição do tratamento"
                  value={description}
                  onChange={(ev) => setdescription(ev.target.value)}
                />
              </div>
              <br />
              <input
                type="submit"
                value="Salvar"
                className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              ></input>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
