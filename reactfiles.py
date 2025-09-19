"""
Setting up MERN Client side
Using Vite React, Tailwindcss, Bootstrap icons
Created by @MGH2005
https://github.com/MGH-2005-10-15/CreateMinimalReactJSX
Last Update : 2025-09-19
"""
from textwrap import dedent # for easier text

indexhtml = dedent(
"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Website</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""
)

tailwindconfigjs = dedent(
"""
/* tailwind.config.js */
// https://v3.tailwindcss.com/docs/guides/vite
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,css}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
""")

indexcss = dedent(
"""
/* index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

html {
  font-size: 16px;
}

body {
  font-size: 16px;
  min-height: 100vh;
}

button, input {
  outline: none;
}
"""
)

appcss = dedent(
"""
/* App.css */
#root {
  width: 100%;
  height: 100vh;
}
"""
)

mainjsx = dedent(
"""
/* main.jsx */
import { BrowserRouter } from 'react-router-dom'
import { createRoot } from 'react-dom/client'
import 'bootstrap-icons/font/bootstrap-icons.css'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
)
"""
)

homejsx = dedent(
"""
/* Home.jsx */
import { useNavigate } from "react-router-dom"
import styles from "./Home.module.css"

export default function Home(){

    const navigate = useNavigate();

    return(
        <>
        <header className={styles['header']}>
            <div className={styles['account']}>
                <button className={styles['signup']} onClick={() => navigate('/signup')}>
                    Signup
                </button>
                <button className={styles['login']} onClick={() => navigate('/login')}>
                    Login
                </button>
            </div>
        </header>
        <main className={styles['main']}>
            <div className={styles['container']}>
                Welcome Developer
            </div>
        </main>
        </>
    );

}
"""
)

homemodulecss = dedent(
"""
/* Home.module.css */
.header {
    @apply w-full h-16 bg-transparent flex overflow-hidden justify-end items-center fixed z-50;
}

.account {
    @apply min-w-56 h-16 inline-flex justify-evenly items-center bg-transparent;
}

.signup {
    @apply min-w-24 h-12 rounded-full bg-blue-500 text-blue-50 
    inline-flex justify-center items-center text-center text-nowrap text-lg font-medium overflow-hidden;
}

.login {
    @apply min-w-24 h-12 rounded-full bg-blue-50 text-blue-500
    inline-flex justify-center items-center text-center text-nowrap text-lg font-medium overflow-hidden;
}

.main {
    @apply w-full h-full overflow-hidden flex justify-center items-center bg-blue-300;
}

.container {
    @apply w-80 h-32 bg-blue-50 rounded-full inline-flex justify-center items-center text-center text-nowrap text-xl font-sans font-medium;
    color: rgb(1, 1, 17);
}
"""
)

signupjsx = dedent(
"""
/* Signup.jsx */
import { useState } from 'react'
import styles from './Signup.module.css'
import { useNavigate } from 'react-router-dom';

function safeStr(obj){
    return (typeof obj === 'string' ? obj : '');
}

function Signup(){

    const [name, setname] = useState('');
    const [username, setusername] = useState('');
    const [email, setemail] = useState('');
    const [password, setpassword] = useState('');

    const [isSending, setIsSending] = useState(false);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState(false);

    function handleForm(event){

        event.preventDefault();
        setSuccess(false);
        setError('');

        const Name = safeStr(name).trim();
        const Username = safeStr(username).trim();
        const Email = safeStr(email).trim().toLowerCase();
        const Password = safeStr(password);

        if(!Name || !Username || !Password){
            setError('Please fill the form');
            return;
        }

        if(Password.length < 8){
            setError('Password must be minimum 8 characters');
            return;
        }

        const data = {name:Name, username:Username, email:Email, password:Password};
        // write the rest yourself :D
    }

    const navigate = useNavigate();

    return(
        <>
        <main className={styles['main']}>
            <main className={styles['container']}>
                <div className={styles['title']}>
                    Signup
                </div>
                <form action="#" method='POST' className={styles['form']} onSubmit={handleForm}>
                    <div className={styles['input-group']}>
                        <label htmlFor="name">Name</label>
                        <input type="text" placeholder='Enter your name' name='name' required onChange={(e) => setname(e.target.value)}/>
                    </div>
                    <div className={styles['input-group']}>
                        <label htmlFor="username">Username</label>
                        <input type="text" placeholder='Enter a username' name='username' required onChange={(e) => setusername(e.target.value)}/>
                    </div>
                    <div className={styles['input-group']}>
                        <label htmlFor="email">Email</label>
                        <input type="text" placeholder='Enter your email' name='email' onChange={(e) => setemail(e.target.value)}/>
                    </div>
                    <div className={styles['input-group']}>
                        <label htmlFor="password">Password</label>
                        <input type="password" placeholder='Min 8 characters' name='password' onChange={(e) => setpassword(e.target.value)}/>
                    </div>
                    <div className={styles['submit-container']}>
                        <button className={styles['submit']} type='submit' disabled={isSending}>
                            {isSending ? 'Sending...' : 'Submit'}
                        </button>
                    </div>
                </form>
                {error ? <div className={styles['errorbox']}>{error}</div> : null}
                {success ? <div className={styles['success']}>Signup is successful</div> : null}
                <div className={styles['helpers']}>
                    <a href="#" onClick={() => navigate('/login')}>Do you have an account ? login</a>
                </div>
            </main>
        </main>
        </>
    );
}

export default Signup
"""
)

signupmodulecss = dedent(
"""
/* Signup.module.css */
.main {
    @apply w-full h-screen flex justify-center items-center bg-blue-300;
}

.container {
    @apply flex flex-col bg-blue-100 items-center;
    width: min(100%, 40rem);
    min-height: 20rem;
    box-shadow: 0 0 10px rgba(71, 71, 71, 0.4);
    border-radius: 15px;
}

.title {
    @apply w-full h-10 inline-flex justify-center items-center text-center text-nowrap text-2xl font-medium line-clamp-1;
    color: rgb(16, 110, 204);
}

.form {
    @apply w-full min-h-60 flex flex-col bg-transparent items-center;
}

.input-group {
    @apply w-4/5 h-20 flex flex-col bg-transparent;
}

.input-group label {
    @apply w-full h-10 inline-flex text-base font-sans text-blue-800 items-center justify-start line-clamp-1 text-nowrap;
}

.input-group input {
    @apply w-full h-10 inline-flex items-center text-sm line-clamp-1 text-nowrap outline-none bg-transparent px-3 bg-blue-200 text-blue-900 font-medium;
    border: 1px solid rgb(16, 110, 204);
    border-radius: 5px;
}

.input-group input::placeholder {
    @apply text-nowrap line-clamp-1 text-sm font-normal;
    color: rgb(13, 85, 157);
}

.input-group input:focus {
    border: 2px solid rgb(16, 110, 204);
}

.submit-container {
    @apply w-4/5 h-20 flex items-center justify-center bg-transparent;
}

.submit {
    @apply min-w-52 w-2/5 h-10 inline-flex justify-center items-center text-center text-nowrap text-base font-medium bg-blue-400 text-blue-100;
    border-radius: 10px;
    transition: all ease-in-out 150ms;
}

.submit:hover {
    @apply bg-blue-300;
}

.submit:disabled:hover {
    @apply bg-blue-400;
}

.errorbox {
    @apply w-4/5 min-h-10 inline-flex justify-start items-center text-base font-medium px-4;
    border: 3px solid rgb(223, 35, 15);
    color: rgb(221, 22, 0);
    background: rgb(223, 146, 136);
    border-radius: 5px;
}

.success {
    @apply w-4/5 min-h-10 inline-flex justify-start items-center text-base font-medium px-4;
    border: 3px solid rgb(15, 223, 32);
    color: rgb(0, 221, 15);
    background: rgb(143, 219, 148);
    border-radius: 5px;
}

.helpers {
    @apply w-full h-10 inline-flex bg-transparent justify-center items-center line-clamp-1 text-nowrap text-blue-700 text-sm font-normal;
}

.helpers a:hover {
    color: rgb(9, 39, 148);
}
"""
)

loginjsx = dedent(
"""
import { useState } from 'react'
import styles from './Signup.module.css'
import { useNavigate } from 'react-router-dom';

function safeStr(obj){
    return (typeof obj === 'string' ? obj : '');
}

function Login(){

    const [username, setusername] = useState('');
    const [email, setemail] = useState('');
    const [password, setpassword] = useState('');

    const [isSending, setIsSending] = useState(false);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState(false);

    function handleForm(event){

        event.preventDefault();
        setSuccess(false);
        setError('');

        const Username = safeStr(username).trim();
        const Email = safeStr(email).trim().toLowerCase();
        const Password = safeStr(password);

        if(!Username || !Password){
            setError('Please fill the form');
            return;
        }

        if(Password.length < 8){
            setError('Password must be minimum 8 characters');
            return;
        }

        const data = {username:Username, email:Email, password:Password};
        // write the rest yourself :D
    }

    const navigate = useNavigate();

    return(
        <>
        <main className={styles['main']}>
            <main className={styles['container']}>
                <div className={styles['title']}>
                    Login
                </div>
                <form action="#" method='POST' className={styles['form']} onSubmit={handleForm}>
                    <div className={styles['input-group']}>
                        <label htmlFor="username">Username</label>
                        <input type="text" placeholder='Enter a username' name='username' required onChange={(e) => setusername(e.target.value)}/>
                    </div>
                    <div className={styles['input-group']}>
                        <label htmlFor="email">Email</label>
                        <input type="text" placeholder='Enter your email' name='email' onChange={(e) => setemail(e.target.value)}/>
                    </div>
                    <div className={styles['input-group']}>
                        <label htmlFor="password">Password</label>
                        <input type="password" placeholder='Min 8 characters' name='password' onChange={(e) => setpassword(e.target.value)}/>
                    </div>
                    <div className={styles['submit-container']}>
                        <button className={styles['submit']} type='submit' disabled={isSending}>
                            {isSending ? 'Sending...' : 'Submit'}
                        </button>
                    </div>
                </form>
                {error ? <div className={styles['errorbox']}>{error}</div> : null}
                {success ? <div className={styles['success']}>Login is successful</div> : null}
                <div className={styles['helpers']}>
                    <a href="#" onClick={() => navigate('/signup')}>Want to create account ? signup</a>
                </div>
            </main>
        </main>
        </>
    );
}

export default Login
"""
)

appjsx = dedent(
"""
/* App.jsx */
import './App.css'
import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Signup from './pages/Signup'
import Login from './pages/Login'

function App() {

  return (
    <>
      <Routes>
        <Route path='/' element={<Home></Home>}></Route>
        <Route path='/signup' element={<Signup></Signup>}></Route>
        <Route path='/login' element={<Login></Login>}></Route>
      </Routes>
    </>
  )
}

export default App
"""
)

