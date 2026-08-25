import './Login.css'
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import logo from '../assets/dev_logo.png';

function Login(){
    const [loginError, setLoginError] = useState('');
    const navigate = useNavigate();
    const [user_name, setUsername] = useState('');
    const [user_password, setPassword] = useState('');
    // uses fetch to send a POST request to backend with username and password
    async function handleLogin() {
        try {
            const response = await fetch('http://localhost:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ // send username and password in the body of the request
                    user_name,
                    user_password
                })
            });

        if (!response.ok) {
            setLoginError('Invalid username or password');
            return;
        }

        navigate('/dashboard');

        } catch (loginError) {
            console.error('Error during login:', loginError);
            setLoginError('Unable to connect to the server');
        }
    }
    return( // JSX for the login page
        <header className="login-page">
            <form className="login-form">
                <img src={logo} alt="DevBoard" className='login-logo' />
                {loginError && (
                    <label className="login-error">{loginError}</label>
                )}
                <label className="login-label">User</label>
                <input className='login-input' type="text" placeholder='User' value={user_name} onChange={(e) => setUsername(e.target.value)}/>

                <label className="login-label">Password</label>
                <input className='login-input' type="password" placeholder='Password' value={user_password} onChange={(e) => setPassword(e.target.value)}/>

                <button type='button' className='login-button' onClick={handleLogin}>Login</button>
            </form>
        </header>
    );
}

export default Login