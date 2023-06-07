import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { faXmark } from "@fortawesome/free-solid-svg-icons";
import { Link, useLocation } from "react-router-dom";
import styled from "styled-components";
import { useState } from "react";
import img4 from "../img/img4.png";
import img5 from "../img/img5.png";

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
    padding: 0 1vw;
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
    width: 15vw;
    padding: 5vh 5vh;
  `,
  Img2: styled.img`
    width: 15vw;
    padding: 3vh 3vh;
  `,
  Link: styled(Link)`
    text-decoration: none;
  `,
  TagWrap: styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2vh 0 1vh 0;
  `,
  Tags: styled.div`
    width: 50vw;
    display: flex;
    align-items: center;
    justify-content: left;
    flex-wrap: wrap;
  `,
  Tag: styled.div`
    display: flex;
    align-items: center;
    background: #B6E388;
    border-radius: 10px;
    padding: 0.5vh 1vw 0.5vh 0.5vw;
    margin: 1vh 0.5vw;
  `,
  Txt: styled.div`
    color: #FFFFFF;
    font-size: 16px;
    padding-left: 5px;
  `,
  DelBtn: styled.button`
    background-color: transparent;
    border: none;
  `,
  SubmitBtn: styled.button`
    width: 15vw;
    height: auto;
    padding: 1vh 0;
    border-radius: 10px;
    border: 2px solid #3B7400;;
    background-color: #E1FFB1;
    font-size: 24px;
    font-family: 'Jua', sans-serif;
    margin-bottom: 3vh;
  `,
};

function InputCtn() {
  const location = useLocation();
  const select = location.state.select;
  const [dish, setDish] = useState("");
  const [tagTxt, setTagTxt] = useState("");
  const [tagLst, setTagLst] = useState([]);
  const [tagBlocks, setTagBlocks] = useState([]);

  const createTag = () => {
    tagLst.push(tagTxt);
    setTagLst(tagLst);
    let newTag = (
      <Style.Tag key={tagBlocks.length}>
        <Style.DelBtn onClick={() => deleteTag(tagTxt)}><FontAwesomeIcon icon={faXmark} color="#FFFFFF" /></Style.DelBtn>
        <Style.Txt># {tagTxt}</Style.Txt>
      </Style.Tag>
    );
    let element = {
      id: tagTxt, 
      value: newTag
    };
    tagBlocks.push(element);
    setTagBlocks(tagBlocks);
    setTagTxt("");
  };

  const deleteTag = (id) => {
    setTagBlocks(oldValues => {
      return oldValues.filter(tagBlock => tagBlock.id != id)
    })
    setTagLst([tagLst.filter(tag => tag != id)]);
  };

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
            <Style.Link to="../pages/RecipeList" state={{name: dish, select: true}}>
              <Style.SearchBtn><FontAwesomeIcon icon={faMagnifyingGlass} size="3x" color="#B6E388"/></Style.SearchBtn>
            </Style.Link>
          </Style.InputWrap>
          <Style.Img1 src={img4}></Style.Img1>
        </Style.Detail>
        : 
        <Style.Detail>
        <Style.TitleWrap>원하는 레시피 식재료를 입력해주세요</Style.TitleWrap>
        <Style.InputWrap>
          <Style.Input
            type="text"
            name="tagLst"
            onChange={(e) => setTagTxt(e.target.value)}
          ></Style.Input>
          <Style.SearchBtn
            onClick={createTag}
          ><FontAwesomeIcon icon={faMagnifyingGlass} size="3x" color="#B6E388"/></Style.SearchBtn>
        </Style.InputWrap>
        <Style.TagWrap>
          <Style.Tags>
            {tagBlocks.map(tagBlock => {
              return (
                <>{tagBlock.value}</>
              )
            })}
          </Style.Tags>
        </Style.TagWrap>
        <Style.Img2 src={img5}></Style.Img2>
        <Style.Link to="../pages/RecipeList" state={{name: tagLst, select: false}}><Style.SubmitBtn>레시피 찾기</Style.SubmitBtn></Style.Link>
      </Style.Detail>}
      </Style.Wrapper>
    </>
  );
}
  
export default InputCtn;