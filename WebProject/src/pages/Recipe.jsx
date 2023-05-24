import Footer from "../containers/Footer";
import Header from "../containers/Header";
import styled from "styled-components";
import RecipeCtn from "../containers/RecipeCtn";

function Recipe() {
  const Style = {
    Wrapper: styled.div`
      display: flex;
      flex-direction: column;
      height: 100vh;
    `,
  }  

  return (
    <Style.Wrapper>
      <Header></Header>
      <RecipeCtn></RecipeCtn>
      <Footer></Footer>
    </Style.Wrapper>
  );
}

export default Recipe;