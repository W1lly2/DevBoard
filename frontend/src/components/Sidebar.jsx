import './Sidebar.css'
import logo from '../assets/dev_logo.png'

function Sidebar({isOpen}) {
    return (
        <aside className={`sidebar ${isOpen ? "open" : ""}`}>
            <img src={logo} alt="DevBoard" className='dashboard-logo'/>
            <nav className="sidebar-nav">
                <a href="#">Tareas</a>
                <a href="#">Usuarios</a>
                <a href="#">Bug Reports</a>
                <a href="#">Configuracion</a>
                <a href="#">Perfil</a>
            </nav>
        </aside>
    );
}

export default Sidebar;