import React, { useState } from "react";
import { Alert } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

function ErrorAlert() {
    const [show, setShow] = useState(true);

    return (
        <div>
            {show && (
                <Alert
                    variant="danger"
                    onError={() => setShow(true)}
                    onClose={() => setShow(false)}
                    dismissible>

                    <Alert.Heading>Error</Alert.Heading>
                    <p>Error</p>
                </Alert>
            )}
        </div>
    );
}

export default ErrorAlert;