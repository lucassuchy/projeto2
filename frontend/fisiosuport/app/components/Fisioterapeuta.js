"use client";
import axios from "axios";
import { useEffect, useState,useContext, useNavigate } from "react";

export default function Fisioterapeutas() {

  const url = "http://18.230.187.219:8080";
  let endpoint = url.concat("/physiotherapist/");

  const [listaFisioterapeutas, setlistaFisioterapeutas] = useState([]);

  useEffect(() => {
    axios.get(endpoint).then(function (response) {
      setlistaFisioterapeutas(response.data);
    });
  }, []);

  return listaFisioterapeutas.map((fisioterapeuta) => (
    <div className="sm:ml-64">
      <div className="p-12 bg-slate-300 bg-auto border-0 border-gray-200 border-dashed rounded-lg mt-6">
        <ul role="list" className="divide-y divide-gray-100">
          <li className="flex justify-between gap-x-1 py-1">
            <div className="flex min-w-0">
              <img
                className="h-12 w-12 flex-none rounded-full bg-gray-50"
                src="fernanda.png"
                alt=""
              />
              <div className="min-w-0 flex-auto">
                <p className="text-sm font-semibold leading-6 text-gray-900">
                  {fisioterapeuta.name}
                </p>
                <p className="mt-1 truncate text-xs leading-5 text-gray-500">
                  {fisioterapeuta.specialty}
                </p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  ));
}
