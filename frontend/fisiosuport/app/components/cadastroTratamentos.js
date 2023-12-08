"use client";
import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate  } from "react-router-dom";
import Select from 'react-select';

export default function CadastradoTratamento() {
  const [name, setName] = useState("");
  const [video_id, setVideo_id] = useState([])
  const url = "http://18.230.187.219:8080"
  const navigate = useNavigate();


  // Novo usuario
  const novoTratamento = (event) => {
    event.preventDefault();
    
    console.log("v",video_id);

    axios({
      method: "post",
      url: url.concat("/treatment/"),
      data: {
        name: name,
        video_id: video_id

      },
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
    navigate("/paciente");
  };

        // Copiei do rocketlog
  var handleChange = (video) => {
    setVideo_id(video.map(valor => valor.value));
    console.log("2",video_id);
  };

  // Busca os dados de pacientes cadastrados
  let endpoint_treatment = url.concat("/treatment/");

  const [listatreatment, setlistaTreatment] = useState([]);

  useEffect(() => {
    axios.get(endpoint_treatment).then(function (response) {
      setlistaTreatment(response.data);
    });
  }, []);




  // Busca os dados de pacientes cadastrados
  let endpoint_videos = url.concat("/videos/");

  const [listVideos, setlistVideos] = useState([]);

  useEffect(() => {
    axios.get(endpoint_videos).then(function (response) {
      setlistVideos(response.data);
    });
    
  }, []);
  return (
    <div className="p-4 sm:ml-64">
      <div className="p-16 bg-gray-800 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-10">
        <div className="grid-cols-1 gap-0 mb-0">
          <form onSubmit={novoTratamento}>
            <div className="gap-10 mb-10 md:grid-cols-2">
            <div>
                <label
                  htmlFor="birth_date"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Nome Tratamento:
                </label>
                <input
                  name="name"
                  type="text"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-1/2 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Tratamento"
                  value={name}
                  onChange={(ev) => setName(ev.target.value)}
                />
              </div>
              <br />
            <div>
                <label
                  htmlFor="type_id"
                  className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >
                  Videos:
                </label>
                <Select
                  defaultValue={video_id}
                  isMulti
                  className="dark:text-black w-1/2"
                  onChange={handleChange}
                  options={listVideos}
                />

              </div>
              <br/>
              <input
                type="submit"
                value="Salvar"
                className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-1/2 px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              ></input>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
