import '../App.css';
import Table from '../components/Table'
import Container from "react-bootstrap/Container";
import ListComponent from "../components/ListComponent";
import {Stack} from "react-bootstrap";

const FirewallTable = () => {
    const url = 'http://tfg_server.localhost/api/firewall/rules';
    const defaultValue = [{
        "action": "drop",
        "bytes": "0",
        "chain": "input",
        "comment": "denegar conex. invalidas",
        "packets": "0"
    }]

    const columns = [
        {header: 'Info', accesor: 'comment'},
        {header: 'Accion', accesor: 'action'},
        {header: 'Cadena', accesor: 'chain'},
        {header: 'Bytes', accesor: 'bytes'},
        {header: 'Paquetes', accesor: 'packets'},
        {header: 'Protocolo', accesor: 'protocol'},
        {header: 'Origen', accesor: 'src-address'},
        {header: 'Destino', accesor: 'dst-address'},
    ]

    return (
        <>
            <h1>Reglas de firewall</h1>
            <Table data={defaultValue} columns={columns} url={url}/>
        </>
    );
}

const BlackList = () => {
    const url = 'http://tfg_server.localhost/api/firewall/blacklist';
    const defaultValue = [{
        "address": "192.168.1.0",
        "creation-time": "2024-05-17 09:54:28",
        "list": "blacklist"
    }]

    const columns = [
        {header: 'Nombre', accesor: 'list'},
        {header: 'Direcciones', accesor: 'address'},
        {header: 'Creado', accesor: 'creation-time'},
    ]

    return (
        <>
            <h1>Blacklist</h1>
            <ListComponent data={defaultValue} columns={columns} url={url} />
        </>
    );
}

function Firewall() {
    return (
        <Stack direction={"vertical"} gap={2}>
            <Container className={"p-2 mx-auto"} maxWidth={"lg"}>
                <BlackList/>
            </Container>
            <Container className={"p-2 mx-auto"} maxWidth={"lg"}>
                <FirewallTable/>
            </Container>
        </Stack>
    );
}

export default Firewall;