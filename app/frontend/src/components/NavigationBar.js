import React from 'react';
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Container from 'react-bootstrap/Container'
import {LinkContainer} from 'react-router-bootstrap'

const NavigationBar = () => {
    return (
        <Navbar className={"bg-body-secondary bs-popover-auto"} expand="lg" data-bs-theme={"dark"}>
            <Container>
                <LinkContainer to="/"><Navbar.Brand>IPS</Navbar.Brand></LinkContainer>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <LinkContainer to="/"><Nav.Link href="/">Inicio</Nav.Link></LinkContainer>
                        <LinkContainer to="/alerts"><Nav.Link href="/alerts">Alertas</Nav.Link></LinkContainer>
                        <LinkContainer to="/rules"><Nav.Link href="/rules">Reglas</Nav.Link></LinkContainer>
                        <LinkContainer to="/firewall"><Nav.Link href="/firewall">Firewall</Nav.Link></LinkContainer>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default NavigationBar;
