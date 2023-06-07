import { Link } from "react-router-dom";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCarrot } from "@fortawesome/free-solid-svg-icons";
import { faBurger } from "@fortawesome/free-solid-svg-icons";

const Style = {
    Wrapper: styled.div`
      flex: 1;
    `,
    Wrap: styled.div`
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: space-evenly;
    `,
    BtnWrap: styled.div`
        width: 25vw;
        height: 40vh;
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
        border: 4px solid #B6E388;
        border-radius: 20px;
        background: #E1FFB1;
    `,
    DishBtn: styled.button`
        width: 25vw;
        font-size: 45px;
        font-family: 'Jua', sans-serif;
        border: none;
        background: transparent;
        color: #325211;
    `,
    Link: styled(Link)`
        text-decoration: none;
    `,
}; 

function SelectCtn() {
  return (
    <>
      <Style.Wrapper>
        <Style.Wrap>
            <Style.Link to="../pages/Input" state={{select: true}}>
                <Style.BtnWrap>
                    <FontAwesomeIcon icon={faBurger} size="5x" color="#7AB241"/>
                    <Style.DishBtn>요리명으로<br/> 레시피 찾기</Style.DishBtn>
                </Style.BtnWrap>
            </Style.Link>
            <Style.Link to="../pages/Input" state={{select: false}}>
                <Style.BtnWrap>
                    <FontAwesomeIcon icon={faCarrot} size="5x" color="#7AB241"/>
                    <Style.DishBtn>식재료로<br/> 레시피 찾기</Style.DishBtn>
                </Style.BtnWrap>
            </Style.Link>
        </Style.Wrap>
      </Style.Wrapper>
    </>
  );
}
  
export default SelectCtn;