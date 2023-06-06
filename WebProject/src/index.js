import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import reportWebVitals from './reportWebVitals';
import Input from './pages/Input';
import Select from './pages/Select';
import Main from './pages/Main';
import RecipeList from './pages/RecipeList';
import Recipe from './pages/Recipe';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={ <Main />} />
        <Route path='/pages/Select' element={ <Select />} />
        <Route path='/pages/Input' element={ <Input />} />
        <Route path='/pages/RecipeList' element={ <RecipeList />} />
        <Route path='/pages/Recipe' element={ <Recipe />} />
      </Routes>
    </BrowserRouter>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
