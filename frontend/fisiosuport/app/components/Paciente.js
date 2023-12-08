'use client'
import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";



export default function Pacientes() {

    const url = 'http://18.230.187.219:8080'
    const endpoint = url.concat('/patient/')
    
    const [listaPacientes, setlistaPacientes] = useState([]);

    useEffect(() => { 
            axios.get(endpoint)
            .then(function (response) {  
                setlistaPacientes(response.data);})
    }, []);
    
    return(
        listaPacientes.map((paciente) =>
        <div className="sm:ml-64">
            <div className="p-12 bg-slate-300 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">
                <ul role="list" className="divide-y divide-gray-100">
                    <li className="flex justify-between gap-x-1 py-1">
                        <div className="flex min-w-0">
                            <div className="min-w-0 flex-auto">
                            
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Paciente:</b> {paciente.patient}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Quantidade de exercicios:</b> {paciente.quantity}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Duração:</b> {paciente.duration} semanas</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Descrição(se houver):</b> {paciente.description}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Tipo de tratamento:</b> {paciente.treatment}</p><br></br>
                                <button className="flex items-center w-25 p-3 text-white rounded-lg dark:text-blue bg-slate-900 dark:hover:bg-gray-700 group">
                                <Link to={`/editaPaciente/${paciente.patient_id}`}>Editar</Link>
                                </button>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        )
        
    )
}
