import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Input from './pages/Input';
import Select from './pages/Select';
import Main from './pages/Main';
import RecipeList from './pages/RecipeList';
import Recipe from './pages/Recipe';

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={ <Main />} />
          <Route path='/pages/Select' element={ <Select />} />
          <Route path='/pages/Input' element={ <Input />} />
          <Route path='/pages/RecipeList' element={ <RecipeList />} />
          <Route path='/pages/Recipe' element={ <Recipe />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
