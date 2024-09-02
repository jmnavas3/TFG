import '../App.css';
import Table from '../components/Table'
import Container from "react-bootstrap/Container";

const AlertsTable = () => {
  const url = 'http://tfg_server.localhost/api/alerts/list';
  const defaultValue = [{
      "alerta": " ET INFO curl User-Agent Outbound",
      "clasificacion": "Attempted Information Leak",
      "fecha": "Tue, 13 Aug 2024 09:55:01 GMT",
      "identificador": "1:2013028:7",
      "ip_destino": "18.154.22.65",
      "ip_origen": "192.168.1.22",
      "prioridad": 2,
      "protocolo": "TCP",
      "puerto_destino": 80,
      "puerto_origen": 37484,
      "reciente": "nuevo"
  }]

  const columns = [
    { header: 'Alerta', accesor: 'alerta' },
    { header: 'Clasificación', accesor: 'clasificacion' },
    { header: 'Fecha', accesor: 'fecha' },
    { header: 'Identificador', accesor: 'identificador' },
    { header: 'IP Origen', accesor: 'ip_origen' },
    { header: 'IP Destino', accesor: 'ip_destino' },
    { header: 'Protocolo', accesor: 'protocolo' },
    { header: 'Puerto Origen', accesor: 'puerto_origen' },
    { header: 'Puerto Destino', accesor: 'puerto_destino' },
    { header: 'Prioridad', accesor: 'prioridad' },
    { header: 'Reciente', accesor: 'reciente' }
  ]

  return (
    <Container maxWidth={"lg"}>
      <h1 className={"h1 top-50"}>Alertas Obtenidas</h1>
      <Table data={defaultValue} columns={columns} url={url} />
    </Container>
  );
}

function Alerts() {
  return (
      <Container maxWidth={"lg"}>
        <AlertsTable />
      </Container>
  );
}

export default Alerts;