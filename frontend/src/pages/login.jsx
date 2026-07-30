import './login.css'
import logo from '../assets/dev_logo.png';

function Login(){
    return(
        <header className="login-page">
            <form className="login-form">
                <img src={logo} alt="DevBoard" className='login-logo' />
                <label className="login-label">User</label>
                <input className='login-input' type="text" placeholder='User'/>

                <label className="login-label">Password</label>
                <input className='login-input' type="password" placeholder='Password'/>

                <button className='login-button'>Login</button>
            </form>
        </header>
    );
}

export default Login