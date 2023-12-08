'use client'
import axios from "axios";
import { useEffect, useState } from "react";
import CardVideos from "./cardVideos";



export default function Home() {

    const url = 'http://18.230.187.219:8080'
    const endpoint_patient = url.concat('/patient/')
    
    const [listaPacientes, setlistaPacientes] = useState([]);

    useEffect(() => { 
            axios.get(endpoint_patient)
            .then(function (response) {  
                setlistaPacientes(response.data);})
    }, []);

    const endpoint_videos = url.concat('/exercicios/')
  
    const [listaExercicios, setlistaExercicios] = useState([]);
  
    useEffect(() => { 
            axios.get(endpoint_videos)
            .then(function (response) {  
              setlistaExercicios(response.data);})
    }, []);
    
    return(
        <div className="gap-4 flex inset-y-10 sm:ml-64">
            
            <div className="w-1/2 p-12 bg-slate-300 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">
            <h1>Pacientes Recentes:</h1>
            {listaPacientes.map((paciente) =>
                <ul role="list" className="divide-y divide-gray-100">
                    <li className="flex justify-between gap-x-1 py-1">
                        <div className="flex min-w-0">
                            <div className="min-w-0 flex-auto">
                            <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Paciente:</b> {paciente.patient}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Quantidade de exercicios:</b> {paciente.quantity}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Duração:</b> {paciente.duration} semanas</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Descrição(se houver):</b> {paciente.description}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Tipo de tratamento:</b> {paciente.treatment}</p>
                            </div>
                        </div>
                    </li>
                </ul> )}
            </div>
            <div className="w-1/2 p-12 bg-slate-300 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">
            <h1> Tratamentos Recentes:</h1>
                {listaExercicios.map((video) =>
                <CardVideos video={video}/>
                )
                }
            </div>
        </div>
        
    )
}
