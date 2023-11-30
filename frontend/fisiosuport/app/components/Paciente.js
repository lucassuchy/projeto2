'use client'
import axios from "axios";
import { useEffect, useState } from "react";


export default function Pacientes() {

    const url = 'http://localhost:8000'
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
                            <img className="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                            <div className="min-w-0 flex-auto">
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Paciente:</b> {paciente.patient}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Quantidade de exercicios:</b> {paciente.quantity}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Duração:</b> {paciente.duration} semanas</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Descrição(se houver):</b> {paciente.description}</p>
                                <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Fisioterapeuta:</b> {paciente.physiotherapist}</p>
                            </div>
                        </div>
                        <div className="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                            <p className="mt-1 truncate text-xs leading-5 text-gray-500"><b>Tipo de tratamento:</b> {paciente.treatment}</p>
                            <p className="mt-1 text-xs leading-5 text-gray-500"><b>Última Sessão</b> <time datetime="2023-01-23T13:23Z">há 2 dias</time></p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        )
        
    )
}
