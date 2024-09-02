import 'bootstrap/dist/css/bootstrap.css'
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import NavigationBar from "./components/NavigationBar";
import Alerts from "./pages/AlertsPage";
import Rules from "./pages/RulesPage";
import ErrorPage from "./pages/ErrorPage";
import Firewall from "./pages/FirewallPage";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <Router>
            <NavigationBar/>
            <Routes>
                <Route exact path="/" element={<App/>}/>
                <Route path="/alerts" element={<Alerts/>}/>
                <Route path="/rules" element={<Rules/>}/>
                <Route path="/firewall" element={<Firewall/>}/>
                <Route path="/*" element={<ErrorPage/>}/>
            </Routes>
        </Router>
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
