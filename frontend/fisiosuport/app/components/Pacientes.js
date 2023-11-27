'use client'

export default function InicialFisioterapeuta() {
    return(
        <div class="p-4 sm:ml-64">
        <div class="p-16 bg-slate-300 bg-auto border-0 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14">
            <ul role="list" class="divide-y divide-gray-100">
            <li class="flex justify-between gap-x-6 py-5">
                <div class="flex min-w-0 gap-x-4">
                <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                <div class="min-w-0 flex-auto">
                    <p class="text-sm font-semibold leading-6 text-gray-900">Michele Janete Duarte</p>
                    <p class="mt-1 truncate text-xs leading-5 text-gray-500">michele.duarte@fisiosuport.com</p>
                </div>
                </div>
                <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                <p class="text-sm leading-6 text-gray-900">Lesão de Joelho</p>
                <p class="mt-1 text-xs leading-5 text-gray-500">Última Sessão <time datetime="2023-01-23T13:23Z">há 2 dias</time></p>
                </div>
            </li>
            <li class="flex justify-between gap-x-6 py-5" />
                <div class="flex min-w-0 gap-x-4">
                <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                <div class="min-w-0 flex-auto">
                    <p class="text-sm font-semibold leading-6 text-gray-900">Daniel Hamilton de Branco</p>
                    <p class="mt-1 truncate text-xs leading-5 text-gray-500">daniel.branco@fisiosuport.com</p>
                </div>
                </div>
                <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                <p class="text-sm leading-6 text-gray-900">Mobilidade</p>
                <p class="mt-1 text-xs leading-5 text-gray-500">Última Sessão <time datetime="2023-01-23T13:23Z">há 3 dias</time></p>
                </div>
                <li class="flex justify-between gap-x-6 py-5">
                <div class="flex min-w-0 gap-x-4">
                    <img class="h-12 w-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                    <div class="min-w-0 flex-auto">
                    <p class="text-sm font-semibold leading-6 text-gray-900">Selena Solange Faria de Pena</p>
                    <p class="mt-1 truncate text-xs leading-5 text-gray-500">selena.faria@fisiosuport.com</p>
                    </div>
                </div>
                <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                <p class="text-sm leading-6 text-gray-900">Recuperação Pós Cirúrgica</p>
                    <p class="mt-1 text-xs leading-5 text-gray-500">Última Sessão <time datetime="2023-01-23T13:23Z">há 4 dias </time></p>
                </div>
                </li>
            
            
            </ul>
            
            </div><br/>
            <a href="./formulario.html"><button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Incluir Paciente
            </button></a>
            </div>
    )
}