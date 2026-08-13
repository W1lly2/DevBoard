import logo from "../assets/dev_logo.png";
import profileIcon from "../assets/profile_icon.svg";
import './Header.css'

function Header({onMenuClick}){
    return(
         <header className="dashboard-header">
            <button className="sidebar-button" onClick={onMenuClick}>
                ☰
            </button>
             <img src={logo} alt="DevBoard" className='dashboard-logo'/>
            <h1 className='dashboard-title'>Bienvenido</h1>
            <div className='dashboard-profile'>
                <img src={profileIcon} className="profile-icon" />
            </div>
        </header> 
    )
}

export default Header;