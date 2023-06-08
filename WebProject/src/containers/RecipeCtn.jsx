import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import styled from "styled-components";
import PopupContent from './PopupContent';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSpoon } from "@fortawesome/free-solid-svg-icons";
import { faUtensils } from "@fortawesome/free-solid-svg-icons";
import recipeData from "../data/Recipe.json";

const Style = {
  Wrapper: styled.div`
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: 'Jua', sans-serif;
  `,
  IntroWrap: styled.div`
    width: 60vw;
    display: flex;
    align-items: end;
    justify-content: space-between;
    padding-top: 5vh;
  `,
  MainImg: styled.img`
    width: 25vw;
    height: 35vh;
    border-radius: 20px;
  `,
  Intro: styled.div`
    width: 25vw;
    display: flex;
    flex-direction: column;
    align-items: start;
  `,
  TitleWrap: styled.div`
    display: flex;
    align-items: center;
    justify-content: start;
    padding-bottom: 2vh;
  `,
  Title: styled.div`
    font-size: 30px;
    padding-left: 10px;
  `,
  DetailWrap: styled.div`
    width: 20vw;
    border: 2px solid #C7F2A4;
    border-radius: 20px;
    padding: 2vh 2vw;
  `,
  SubWrap: styled.div`
    display: flex;
    justify-content: start;
    align-items: center;
    padding-bottom: 2vh;
  `,
  SubTitle: styled.div`
    font-size: 24px;
    color: #808080;
  `,
  SubContent: styled.div`
    padding-left: 3vw;
    font-size: 26px;
  `,
  AddBtn: styled.button`
    border: none;
    font-size: 20px;
    background-color: #E1FFB1;
    border-radius: 10px;
    margin-left: 3vw;
    font-family: 'Jua', sans-serif;
    padding: 1vh 1vw;
    &:hover {
      background-color: #C7F2A4;
    }
  `,
  RecipeListWrap: styled.div`
    width: 60vw;
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: center;
    padding-top: 10vh;
  `,
  ListWrap: styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
  `,
  RecipeWrap: styled.div`
    display: flex;
    justify-content: space-evenly;
    align-items: start;
    padding-bottom: 10vh;
  `,
  RecipeImg: styled.img`
    width: 20vw;
    height: 25vh;
    border-radius: 20px;
    margin-right: 3vw;
  `,
  RecipeContentWrap: styled.div`
    display: flex;
    flex-direction: column;
    align-items: start;
  `,
  OrderNum: styled.div`
    width: 5vw;
    font-size: 24px;
    border-radius: 10px 10px 0 0;
    text-align: center;
    background-color: #C7F2A4;
    padding: 0.5vh 0;
    color: #FFFFFF;
  `,
  Content: styled.div`
    width: 35vw;
    height: 15vh;
    font-size: 18px;
    border: 3px solid #C7F2A4;
    border-radius: 0 20px 20px 20px;
    padding: 1vh 1vw;
  `,
}; 

function RecipeCtn() { 
  const location = useLocation();
  const [recipeList, setRecipeList] = useState([]);
  const [isOpenPopup, setIsOpenPopup] = useState(false);
  const [test, setTest] = useState("");

  const recipe = JSON.parse(JSON.stringify(recipeData));
  const target = location.state.code;
  
  const getData = () => {
    for (let key in recipe[target]["RECP"]) {
      let newLst = (
        <Style.RecipeWrap>
          <Style.RecipeImg src={recipe[target]["R_PHO"][key]}></Style.RecipeImg>
          <Style.RecipeContentWrap>
            <Style.OrderNum>{key}</Style.OrderNum>
            <Style.Content>{recipe[target]["RECP"][key]}</Style.Content>
          </Style.RecipeContentWrap>
        </Style.RecipeWrap>
      );
      let element = {
        id: target,
        value: newLst
      };
      recipeList.push(element);
    }
    setRecipeList(recipeList);
    setTest("완료");
  };

  const openPopup = () => {
    setIsOpenPopup(true);
  };

  const closePopup = () => {
      setIsOpenPopup(false);
  };

  useEffect(() => {
    getData();
    console.log(recipe[target])
  }, []);

  return (
    <>
      <Style.Wrapper>
        <Style.IntroWrap>
          <Style.MainImg src={recipe[target]["M_PHO"]}></Style.MainImg>
          
          <Style.Intro>
            <Style.TitleWrap>
              <FontAwesomeIcon icon={faSpoon} color="#C7F2A4" size="2x"/>
              <Style.Title>{recipe[target]["DISH"]}</Style.Title>
            </Style.TitleWrap>
            
            <Style.DetailWrap>
              <Style.SubWrap>
                <Style.SubTitle>요리 난이도</Style.SubTitle>
                <Style.SubContent>{recipe[target]["DIFF"]}</Style.SubContent>
              </Style.SubWrap>
              <Style.SubWrap>
                <Style.SubTitle>요리 시간</Style.SubTitle>
                <Style.SubContent>{recipe[target]["TIME"]}</Style.SubContent>
              </Style.SubWrap>
              <Style.SubWrap>
                <Style.SubTitle>요리 양(인분)</Style.SubTitle>
                <Style.SubContent>{recipe[target]["QUAN"]}</Style.SubContent>
              </Style.SubWrap>
              <Style.SubWrap>
                <Style.SubTitle>요리 식재료</Style.SubTitle>
                <Style.AddBtn
                  type='button'
                  id='popupDom'
                  onClick={openPopup}
                >재료보기</Style.AddBtn>
              </Style.SubWrap>
              {isOpenPopup && <PopupContent code={target} close={closePopup}></PopupContent>}
            </Style.DetailWrap>
          </Style.Intro>

        </Style.IntroWrap>

        <Style.RecipeListWrap>
          <Style.TitleWrap>
            <FontAwesomeIcon icon={faUtensils} color="#C7F2A4" size="2x"/>
            <Style.Title>레시피</Style.Title>
          </Style.TitleWrap>

          <Style.ListWrap>
            {recipeList.map(lst => {
              return (
                <>{lst.value}</>
              )
            })}
          </Style.ListWrap>
        </Style.RecipeListWrap>
      </Style.Wrapper>
    </>
  );
}
  
export default RecipeCtn;