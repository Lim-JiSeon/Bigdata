import styled from "styled-components";
import logoImg from "../img/Logo.png";
import { Link } from "react-router-dom";

function Header() {
  const Style = {
    Header: styled.div`
        width: 100%;
        height: 10vh;
        display:flex;
        align-items: center;
        justify-content: center;
        padding: 2vh 0;
    `,
    Logo: styled.img`
        width: 100px;
        height: 100px;
    `,
  }  
  
  return (
    <>
      <Style.Header>
        <Link to="/"><Style.Logo src={ logoImg }></Style.Logo></Link>
      </Style.Header>
      
    </>
  );
}
  
export default Header;