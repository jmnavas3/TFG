import React, {useEffect, useState} from 'react';
import axios from "axios";
import {Button} from "react-bootstrap";

export default Table;

function Table({data, columns, url, handleAction}) {
    const elementosPorPagina = 10;
    const [order, setOrder] = useState({"per_page": elementosPorPagina});
    const [values, setValues] = useState(data);
    const [paginaActual, setPaginaActual] = useState(1);
    const [totalElementos, setTotalElementos] = useState(1);

    const controlColumnOrder = (columnName) => {
        let newOrder;

        if (order["field"] !== columnName || !order["sort_type"]) {
            newOrder = 'desc';
        } else if (order["sort_type"] === 'desc') {
            newOrder = 'asc';
        } else if (order["sort_type"] === 'asc') {
            newOrder = null;
        }

        setOrder((prevOrder) => ({
            ...prevOrder,
            "field": columnName,
            "sort_type": newOrder,
            "per_page": elementosPorPagina,
        }));
    };

    const manejarPaginaSiguiente = () => {
        if (paginaActual * elementosPorPagina < totalElementos) {
            setPaginaActual(paginaActual + 1);
        }
    };

    const manejarPaginaAnterior = () => {
        if (paginaActual > 1) {
            setPaginaActual(paginaActual - 1);
        }
    };

    useEffect(() => {
        const getValues = async () => {
            try {
                const response = await axios.post(url, {...order, "page": paginaActual - 1});
                setValues(response.data["data"]);
                setTotalElementos(response.data["total"]);
            } catch (error) {
                console.log(error.message);
            }
        };

        getValues()
    }, [url, order, paginaActual]);

    return (
        <>
            <div className={"table-responsive"}>
                <table className={"table table-striped table-hover"}>
                    <thead>
                    <tr>
                        {columns.map((col) => (
                            <th
                                key={col.header}
                                onClick={() => controlColumnOrder(col.accesor)}
                                style={{cursor: 'pointer'}}
                            >
                                {col.header} {order["field"] === col.accesor && (order["sort_type"] === 'asc' ? ' (asc)' : ' (desc)')}
                            </th>
                        ))}
                    </tr>
                    </thead>
                    <tbody>
                    {values.map((row, index) => (
                        <tr key={index}>
                            {columns.map((col, colIndex) => (
                                !col?.action
                                    ? <td key={colIndex}>{row[col.accesor] ? row[col.accesor] : "-"}</td>
                                    : <td>
                                        <button className={"btn btn-light btn-sm"}
                                                onClick={() => handleAction(row["id"], row[col.accesor])}>
                                            {row[col.accesor] ? row[col.accesor] : "-"}
                                        </button>
                                    </td>
                            ))}
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
            <div>
                <div style={{marginTop: '10px'}}>
                    <Button variant="primary" size="sm" onClick={manejarPaginaAnterior} disabled={paginaActual === 1}>
                        Anterior
                    </Button>
                    <span style={{margin: '0 10px'}}>
                        Página {paginaActual} de {Math.ceil(totalElementos / elementosPorPagina)}
                    </span>
                    <Button variant="primary" size="sm"
                            onClick={manejarPaginaSiguiente}
                            disabled={paginaActual * elementosPorPagina >= totalElementos}
                    >
                        Siguiente
                    </Button>
                </div>
            </div>
        </>
    );
}
