import '../App.css';
import Table from '../components/Table'
import FileUpload from "../components/FileUpload";
import Form from 'react-bootstrap/Form';
import axios from "axios";
import Container from "react-bootstrap/Container";

const RulesTable = () => {
    const url = 'http://tfg_server.localhost/api/rules/list';
    const urlEnableDisable = 'http://tfg_server.localhost/api/rules/enable_disable';
    const defaultValue = [{
        "actualizaciones": 1,
        "descripcion": "SURICATA TLS overflow heartbeat encountered, possible exploit attempt",
        "estado": "activada",
        "id": "2230012",
        "regla": "alert tls any any -> any any"
    }]

    const manejarAccion = async (identifier = null, value = null) => {
        console.log(identifier)
        console.log(value)
        const accion = value === "activada" ? "enable" : "disable";
        try {
                const response = await axios.post(urlEnableDisable, {"sid": identifier, "action": accion});
                console.log(response.data)
            } catch (error) {
                console.error("Error: server unreachable");
            }
    };

    const columns = [
        {header: 'Identificador', accesor: 'id'},
        {header: 'Regla', accesor: 'regla'},
        {header: 'Descripcion', accesor: 'descripcion'},
        {header: 'Actualizaciones', accesor: 'actualizaciones'},
        {header: 'Estado', accesor: 'estado', action: true}
    ]

    return (
        <Container maxWidth={"lg"}>
            <h1 className={"h1"}>Reglas del IDS</h1>
            <Table
                data={defaultValue}
                columns={columns}
                url={url}
                handleAction={manejarAccion}
            />
        </Container>
    );
}

function Rules() {
    return (
        <Container maxWidth={"lg"}>
            <RulesTable/>
            <div>
                <Form.Label>Añadir nuevas reglas</Form.Label>
                <FileUpload label={"Añadir nuevas reglas"}/>
            </div>
        </Container>
    );
}

export default Rules;