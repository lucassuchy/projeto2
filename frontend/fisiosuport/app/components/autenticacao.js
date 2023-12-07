// import React, { createContext, useState, useEffect, useContext } from 'react';


// const AuthContext = createContext<AuthContextData>({});

// export const AuthProvider = ({ children }) => {

//   useEffect(() => {
//     const storagedUser = sessionStorage.getItem('@App:user');
//     const storagedToken = sessionStorage.getItem('@App:token');

//     if (storagedToken && storagedUser) {
//       setUser(JSON.parse(storagedUser));
//       api.defaults.headers.Authorization = `Bearer ${storagedToken}`;
//     }
//   }, []);

//     const [users, setUser] = useState("")
//     const url = "http://18.231.170.222:8080";


//     axios.get(endpoint.concat(usuario)).then(function (response) {
//         setUser(response.data);
//       });


//     async function Login(document, password) {
//     const response = await api.post('/login', {
//         document: document,
//         password: password,
//     });

//     console.log(response);
//     }
    
//     setUser(response.data.user);
//     api.defaults.headers.Authorization = `Bearer ${response.data.token}`;

//     sessionStorage.setItem('@App:user', JSON.stringify(response.data.user));
//     sessionStorage.setItem('@App:token', response.data.token);
//   }
//   return (
//     <AuthContext.Provider value={{ signed: Boolean(user), user, Login, Logout }}>
//       {children}
//     </AuthContext.Provider>
//   );;

//   function Logout() {
//     setUser(null);
//   }



// export function useAuth() {
//   const context = useContext(AuthContext);

//   return context;
// }