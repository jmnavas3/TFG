import logo from './logo.svg';
import './App.css';
import React from 'react';
import {Box, Container, Typography} from "@mui/material";

// import FirewallPage from './components/FirewallPage';

function App() {
    return (
        <Container maxWidth="lg">
            <Box sx={{my: 4}}>
                <Typography variant="h4" component={"h1"} sx={{mb: 2}}>
                    <div className="App">
                        <header className="App-header">
                            <img src={logo} className="App-logo" alt="logo"/>
                            <p>
                                Edit <code>src/App.js</code> and save to reload.
                            </p>
                            <a
                                className="App-link"
                                href="https://reactjs.org"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                Learn React
                            </a>
                        </header>
                    </div>
                </Typography>
            </Box>
        </Container>
    );
}

export default App;
