"use client";
import axios from "axios";
import { useEffect, useState } from "react";
import CardVideos from "./cardVideos";

export default function CadastradoTratamento() {
  const [name, setName] = useState("");
  const [documento, setDocumento] = useState(0);
  const [birth_date, setBirth_date] = useState(0);
  const [fisioterapeuta_id, setfisioterapeuta_id] = useState(0);
  const [quantity, setQuantity] = useState(0);
  const [duration, setDuration] = useState(0);
  const [treatment, setTreatment] = useState(0);
  const [description, setdescription] = useState("");

  const url = "http://52.67.213.148:8080";

  // Novo usuario
  const novoTratamento = (event) => {
    event.preventDefault();

    let endpoint = url.concat("/patient/");

    axios({
      method: "post",
      url: endpoint,
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
      .catch((err) => console.log(err));
  };

  // Busca os dados
  let endpoint_videos = url.concat("/videos/");

  const [listaVideos, setlistaVideos] = useState([]);

  useEffect(() => {
    axios.get(endpoint_videos).then(function (response) {
      setlistaVideos(response.data);
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
            <div className="grid gap-10 mb-10 md:grid-cols-2">
              <div>
                  {listaVideos.map((video) => (
                    <CardVideos video={video}/>
                  ))}
                </div>
                </div>
                </div>
                </div>
                </div>
  );
}
