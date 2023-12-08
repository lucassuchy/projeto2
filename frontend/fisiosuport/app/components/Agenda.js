'use client'
import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";



export default function Agendas() {

 
    return(
       <div className="p-4 sm:ml-64">
       <div className="p-16 bg-slate-300 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-10">
          <div className="grid grid-cols-1 gap-0 mb-0">
          <iframe
        src="https://calendar.google.com/calendar/embed?src=rafaelmuller.fotografia%40gmail.com&ctz=America%2FSao_Paulo"
        style={{ border: "0", width: "60rem", height: "60rem", frameborder: "0", scrolling: "no" }}
        ></iframe>

          </div>
          </div>
          </div>
    )
}
