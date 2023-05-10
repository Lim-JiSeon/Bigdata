import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faKitchenSet } from "@fortawesome/free-solid-svg-icons";
import styled from "styled-components";

function Footer() {
  const Style = {
    Footer: styled.div`
      width: 100%;
      height: 10vh;
      line-height: 3vh;
      display:flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: #B6E388;
      text-align: center;
      color: white;
      font-family: 'Jua', sans-serif;
    `,
  }  
  
  return (
    <>
      <Style.Footer>
        <div><FontAwesomeIcon icon={faKitchenSet} size="2x"/></div>
        <div>Copyright 2023 요리조리 All rights reserved</div>
      </Style.Footer>
      
    </>
  );
}
  
export default Footer;