import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function Formulario(controlId, placeHolder, formLabel) {
  return (
    <Form>
      <Form.Group className="mb-3" controlId={controlId}>
        <Form.Label>{formLabel}</Form.Label>
        <Form.Control type="text" placeholder={placeHolder} />
      </Form.Group>

      <Button variant="primary" type="submit">
        Confirmar
      </Button>
    </Form>
  );
}

export default Formulario;