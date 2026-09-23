import { useEffect, useState } from "react";
import logo from "../assets/dev_logo.png";
import profileIcon from "../assets/profile_icon.svg";
import './Header.css'

function Header({onMenuClick}){
    const [user, setUser] = useState("");
    useEffect(() => {
        fetch("http://localhost:8000/me", {
            credentials: "include"
        })
        .then(response => response.json())
        .then(data => {
            setUser(data.username);
        });
    }, []);
    return(
         <header className="dashboard-header">
            <button className="sidebar-button" onClick={onMenuClick}>
                ☰
            </button>
             <img src={logo} alt="DevBoard" className='dashboard-logo'/>
            <h1 className='dashboard-title'>Bienvenido {user}</h1>
            <div className='dashboard-profile'>
                <img src={profileIcon} className="profile-icon" />
            </div>
        </header> 
    )
}

export default Header;
