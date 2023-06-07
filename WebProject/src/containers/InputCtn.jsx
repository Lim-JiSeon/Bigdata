import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { Link, useLocation } from "react-router-dom";
import styled from "styled-components";
import { useState } from "react";

const Style = {
  Wrapper: styled.div`
    flex: 1;
    font-family: 'Jua', sans-serif;
  `,
  Detail: styled.div`
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
  `,
  TitleWrap: styled.div`
    font-size: 32px;
    padding: 7vh 0 5vh 0;
  `,
  InputWrap: styled.div`
    width: 50vw;
    height: 8vh;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #B6E388;
    border-radius: 20px;
  `,
  Input: styled.input`
    width: 45vw;
    height: 7vh;
    text-align: center;
    font-size: 24px;
    border: none;
    border-radius: 20px;
    outline: none;
  `,
  SearchBtn: styled.button`
    width: 4vw;
    height: 7vh;
    border: none;
    border-radius: 20px;
    background: transparent;
  `,
  Img1: styled.img`
    width: 25vw;
    padding: 5vh 5vh;
  `,
  Img2: styled.img`
    width: 15vw;
    padding: 5vh 3vh;
  `,
  Link: styled(Link)`
    text-decoration: none;
  `
};

function InputCtn() {
  const location = useLocation();
  const select = location.state.select;
  const [dish, setDish] = useState("");

  return (
    <>
      <Style.Wrapper>
        {select? 
        <Style.Detail>
          <Style.TitleWrap>원하는 레시피 요리명을 입력해주세요</Style.TitleWrap>
          <Style.InputWrap>
            <Style.Input
              type="text"
              onChange={(e) => {setDish(e.target.value)}}
            ></Style.Input>
            <Style.Link to="../pages/RecipeList" state={{name: dish}}>
              <Style.SearchBtn><FontAwesomeIcon icon={faMagnifyingGlass} size="3x" color="#B6E388"/></Style.SearchBtn>
            </Style.Link>
          </Style.InputWrap>
          <Style.Img1 src="https://o.remove.bg/downloads/8fe3c827-8b39-4150-9ad6-5b6d6b8e6977/image-removebg-preview.png"></Style.Img1>
        </Style.Detail>: 
        <Style.Detail>
        <Style.TitleWrap>원하는 레시피 식재료를 입력해주세요</Style.TitleWrap>
        <Style.InputWrap>
          <Style.Input
            type="text"
            onChange={(e) => {setDish(e.target.value)}}
          ></Style.Input>
          <Style.Link to="../pages/RecipeList" state={{name: dish}}>
            <Style.SearchBtn><FontAwesomeIcon icon={faMagnifyingGlass} size="3x" color="#B6E388"/></Style.SearchBtn>
          </Style.Link>
        </Style.InputWrap>
        <Style.Img2 src="https://o.remove.bg/downloads/b7ec8e7b-101f-49bb-8096-979fec9f936d/image-removebg-preview.png"></Style.Img2>
      </Style.Detail>}
      </Style.Wrapper>
    </>
  );
}
  
export default InputCtn;