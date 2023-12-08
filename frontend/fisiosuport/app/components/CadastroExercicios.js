"use client";
import axios from "axios";
import { useEffect, useState } from "react";
import CardVideos from "./cardVideos";


export default function listaExercicios() {

  const url = 'http://18.230.187.219:8080'
  const endpoint = url.concat('/exercicios/')
  
  const [listaExercicios, setlistaExercicios] = useState([]);

  useEffect(() => { 
          axios.get(endpoint)
          .then(function (response) {  
            setlistaExercicios(response.data);})
  }, []);
  
  return(
    listaExercicios.map((video) =>

    <div className="sm:ml-64">
      <div className="p-12 bg-slate-300 bg-auto border-0 border-gray-200 border-dashed rounded-lg mt-6">
        <ul role="list" className="divide-y divide-gray-100">
          <li className="flex justify-between gap-x-1 py-1">
            <div className="flex min-w-0">
              <div className="min-w-0 flex-auto">
                <p className="text-sm font-semibold leading-6 text-gray-900">
                <CardVideos video={video}/>
                </p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
      )
  );
}
