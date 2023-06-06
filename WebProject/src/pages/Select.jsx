import Footer from "../containers/Footer";
import Header from "../containers/Header";
import styled from "styled-components";
import SelectCtn from "../containers/SelectCtn";

function Select() {
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
      <SelectCtn></SelectCtn>
      <Footer></Footer>
    </Style.Wrapper>
  );
}

export default Select;