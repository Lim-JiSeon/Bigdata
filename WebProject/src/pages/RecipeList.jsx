import Footer from "../containers/Footer";
import Header from "../containers/Header";
import styled from "styled-components";
import RecipeListCtn from "../containers/RecipeListCtn";

function RecipeList() {
    
  const Style = {
    Wrapper: styled.div`
      display: flex;
      flex-direction: column;
      height: 100%;
    `,
  }  

  return (
    <Style.Wrapper>
      <Header></Header>
      <RecipeListCtn></RecipeListCtn>
      <Footer></Footer>
    </Style.Wrapper>
  );
}
  
export default RecipeList;