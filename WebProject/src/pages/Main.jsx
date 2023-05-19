import Footer from "../containers/Footer";
import Header from "../containers/Header";
import styled from "styled-components";
import MainCtn from "../containers/MainCtn";

function Main() {
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
      <MainCtn></MainCtn>
      <Footer></Footer>
    </Style.Wrapper>
  );
}

export default Main;