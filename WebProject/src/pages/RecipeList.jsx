import Footer from "../containers/Footer";
import styled from "styled-components";
import RecipeListCtn from "../containers/RecipeListCtn";

function RecipeList() {
    
  const Style = {
    Wrapper: styled.div`
      display: flex;
      flex-direction: column;
      height: 100vh;
    `,
  }  

  return (
    <Style.Wrapper>
      <RecipeListCtn></RecipeListCtn>
      <Footer></Footer>
    </Style.Wrapper>
  );
}
  
export default RecipeList;