import ListGroup from 'react-bootstrap/ListGroup';
import React, {useEffect, useState} from "react";
import axios from "axios";

function ListComponent({data, columns, url}) {
    const [values, setValues] = useState(data);

    useEffect(() => {
        const getValues = async () => {
            try {
                const response = await axios.post(url, {});
                setValues(response.data);
            } catch (error) {
                console.log(error.message);
            }
        };

        getValues()
    }, [url]);

    return (
        <ListGroup className={"list-group-flush"}>
            {values.map((row) => (
                <>
                {columns.map((col, colIndex) => (
                    <ListGroup.Item className={"list-group-item-action list-group-item-dark"} key={colIndex}>{row[col.accesor] ? row[col.accesor] : "-"}</ListGroup.Item>
                    ))}
                </>
            ))}
        </ListGroup>
    );
}

export default ListComponent;