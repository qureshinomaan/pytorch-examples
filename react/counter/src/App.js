import React from 'react';
import logo from './logo.svg';
import './App.css';
import navbar from './components/navbar';
import Counters from './components/counters'
import Counter from './components/counter';

function App() {
  return (
    <React.Fragment> 
      <navbar /> 
      <main className="container">
        <Counters />
      </main>
    </React.Fragment>
    );
  
}

export default App;
