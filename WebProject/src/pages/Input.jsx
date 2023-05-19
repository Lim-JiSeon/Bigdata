import Footer from "../containers/Footer";
import Header from "../containers/Header";
import styled from "styled-components";
import InputCtn from "../containers/InputCtn";

function Input() {
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
      <InputCtn></InputCtn>
      <Footer></Footer>
    </Style.Wrapper>
  );
}

export default Input;