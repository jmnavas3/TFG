import React, {useState} from 'react';
import Form from 'react-bootstrap/Form';
import Button from "react-bootstrap/Button";
import axios from 'axios';
import {API_URL} from "../config/config";

function FileUpload() {
    const [file, setFile] = useState(null);
    const [uploadStatus, setUploadStatus] = useState('');

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!file) {
            setUploadStatus('Por favor, selecciona un archivo.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post(`${API_URL}/api/rules/add_file`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            if (response.status === 201) {
                setUploadStatus('Archivo subido exitosamente.');
            } else {
                setUploadStatus('Error al subir el archivo.');
            }
        } catch (error) {
            console.error('Error al enviar el archivo:', error);
            setUploadStatus('Error al enviar el archivo.');
        }
    };

    return (
        <Form onSubmit={handleSubmit}>
            <Form.Group controlId="formFile" className="mb-3">
                <Form.Control type="file" onChange={handleFileChange}/>
                <Button className={"btn-outline-primary d-inline"} variant={"primary"} type="submit">Guardar</Button>
            </Form.Group>
            <p>{uploadStatus}</p>
        </Form>
    );
}

export default FileUpload;
