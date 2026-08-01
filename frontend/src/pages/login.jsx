import './login.css'
import { useNavigate } from 'react-router-dom';
import logo from '../assets/dev_logo.png';

function Login(){
    const navigate = useNavigate();
    function handleLogin(){
        navigate("/dashboard")
    };
    return(
        <header className="login-page">
            <form className="login-form">
                <img src={logo} alt="DevBoard" className='login-logo' />
                <label className="login-label">User</label>
                <input className='login-input' type="text" placeholder='User'/>

                <label className="login-label">Password</label>
                <input className='login-input' type="password" placeholder='Password'/>

                <button type='button' className='login-button' onClick={handleLogin}>Login</button>
            </form>
        </header>
    );
}

export default Login