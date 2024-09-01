from datetime import datetime

from app.backend.database.seeders.fast_seeder import FastSeeder
from app.backend.src.alerts.infrastructure.repository.alert_repository import AlertRepository

data = "2024-08-13 14:48:01,1:2100498:7,2,TCP,18.154.22.65,80,192.168.1.22,48478, GPL ATTACK_RESPONSE id check returned root,Potentially Bad Traffic,True"


def alert_str_to_dict(csv_line: str):
    csv_order = "fecha,identificador,prioridad,protocolo,ip_origen,puerto_origen,ip_destino,puerto_destino,alerta,clasificacion,reciente"

    alert_dict = dict(zip(csv_order.split(","), csv_line.split(",")))

    # parse dict value types
    aux = alert_dict["reciente"]
    alert_dict["reciente"] = True if aux == "True" else False
    alert_dict["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # if any column does not have value, return None
    # for csv_column in csv_order.split(","):
    #     if not alert_dict.get(csv_column, None):
    #         return None

    return dict(alert_dict)


def test_alert_str_to_dict_method():
    alert_dict = alert_str_to_dict(data)
    assert isinstance(alert_dict, dict)
    assert isinstance(alert_dict["reciente"], bool)


def prepare_items(generate_database, csv_str_list: list[str] = None):
    generate_database['db'].create_database()

    seeder = FastSeeder(generate_database['db'])
    items_created = []

    if not csv_str_list:
        csv_str_list = [data]

    alert_dict_list = [alert_str_to_dict(csv_str) for csv_str in csv_str_list]
    for alert_data in alert_dict_list:
        item = seeder.create_alert(alert_data)
        items_created.append(item)
    return items_created


def test_seeder_store_alert(generate_database):
    """test if alert seeder class store an alert given by string in csv format"""
    alert_id = prepare_items(generate_database=generate_database)

    assert alert_id is not None
    assert isinstance(alert_id[0], int)
    print(alert_id)


def test_get_alert_by_id(generate_database):
    alert_id = prepare_items(generate_database=generate_database)[0]
    repository = AlertRepository(session_factory=generate_database['session'])

    expected_data = repository.get_alert_by_id(alert_id=alert_id)
    print(expected_data)
    assert expected_data.get("ip_destino", None) == "192.168.1.22"


def test_update_old(generate_database):
    alert_id = prepare_items(generate_database=generate_database)[0]
    repository = AlertRepository(session_factory=generate_database['session'])

    repository.update_old()
    expected_data = repository.get_alert_by_id(alert_id)

    assert not expected_data.get("reciente", True)


def test_get_priority_alerts(generate_database):
    repository = AlertRepository(session_factory=generate_database['session'])
    priority_alerts = repository.get_priority_alerts()
    priority_blacklist = set(repository.get_public_ip(alert.ip_origen, alert.ip_destino) for alert in priority_alerts)
    print(priority_blacklist)
    assert priority_blacklist is not None


def test_get_message_alerts(generate_database):
    repository = AlertRepository(session_factory=generate_database['session'])
    message_alerts = repository.get_message_alerts()
    messages_blacklist = set(repository.get_public_ip(alert.ip_origen, alert.ip_destino) for alert in message_alerts)
    print(messages_blacklist)
    assert messages_blacklist is not None


def test_drop_dangerous_alerts(generate_database):
    repository = AlertRepository(session_factory=generate_database['session'])
    blacklist = repository.drop_dangerous_alerts()
    print(blacklist)
    assert blacklist is not None
