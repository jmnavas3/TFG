import React from 'react';
import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {
  return (
    <div className="container">
      <div className="row justify-content-center my-5">
        <div className="col-12 text-center">
          <h1 className="mb-4">Sistema de Prevención de Intrusiones</h1>
          <img src={logo} className="img-fluid" alt="logo" style={{ width: '150px' }} />
        </div>
      </div>
    </div>
  );
};

export default App;
