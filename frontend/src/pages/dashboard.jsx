import logo from '../assets/dev_logo.png'
import profileIcon from '../assets/profile_icon.svg'
import './dashboard.css'

function Dashboard(){
    return(
        <div className="dashboard-page">
            <header className="dashboard-header">
                <img src={logo} alt="DevBoard" className='dashboard-logo'/>
                <h1 className='dashboard-title'>Bienvenido</h1>
                <div className='dashboard-profile'>
                    <img src={profileIcon} className="profile-icon" />
                </div>
            </header> 

            <main className='dashboard-content'>
                <section className='task-table'>
                    <div className='table-toolbar'>
                        <input className='toolbar-search' type='text' placeholder='Buscar tarea'/>

                        <select className='toolbar-select'>
                            <option>Todas las prioridades</option>
                            <option>Alta</option>
                            <option>Media</option>
                            <option>Baja</option>
                        </select>
                        <button className='toolbar-button'>Crear tarea</button>
                    </div>

                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Tarea</th>
                                <th>Prioridad</th>
                                <th>Estado</th>
                                <th>Fecha</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td>Crear Login</td>
                                <td>Alta</td>
                                <td>En progreso</td>
                                <td>31/07/2026</td>
                            </tr>

                            <tr>
                                <td>2</td>
                                <td>Diseñar Dashboard</td>
                                <td>Media</td>
                                <td>Pendiente</td>
                                <td>05/08/2026</td>
                            </tr>
                        </tbody>
                    </table>
                </section>
            </main> 
        </div>
    );
}

export default Dashboard;