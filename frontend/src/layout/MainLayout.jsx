import Header from "../components/Header";
import Sidebar from "../components/Sidebar";
import { useState } from "react";
import './MainLayout.css'

function MainLayout({children}){

    const [isSidebarOpen, setisSidebarOpen] = useState(false);

    const toggleSidebar = () => {
        setisSidebarOpen(!isSidebarOpen);
    };
    return(
        <div className="layout">

            <Sidebar isOpen={isSidebarOpen} / >

            <div className="layout-main">

                <Header onMenuClick={toggleSidebar} / >

                <main className="layout-content">

                {children}
                </main>
                
            </div>
        </div>
    );
}

export default MainLayout;