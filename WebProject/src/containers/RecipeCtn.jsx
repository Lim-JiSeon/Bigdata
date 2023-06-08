import { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSpoon } from "@fortawesome/free-solid-svg-icons";
import { faUtensils } from "@fortawesome/free-solid-svg-icons";
import recipeData from "../data/Recipe.json";

const Style = {
  Wrapper: styled.div`
    flex: 1;
    font-family: 'Jua', sans-serif;
  `,
  IntroWrap: styled.div`
    display: flex;
    align-items: center;
    justify-content: space-evenly;
  `,
  MainImg: styled.img`
    width: 25vw;
    border-radius: 20px;
  `,
  Intro: styled.div`
    display: flex;
    flex-direction: column;
    align-items: start;
  `,
  TitleWrap: styled.div`
    display: flex;
    align-items: center;
    justify-content: start;
  `,
  Title: styled.div`
    font-size: 20px;
    padding-left: 10px;
  `,
  DetailWrap: styled.div`
    border: 2px solid #C7F2A4;
    border-radius: 20px;
  `,
  SubWrap: styled.div`
    display: flex;
    justify-content: space-evenly
    align-items: center;
  `,
  SubTitle: styled.div`
    font-size: 16px;
    color: #808080;
  `,
  SubContent: styled.div`
    font-size: 18px;
  `,
  AddBtn: styled.button`
    border: none;
    font-size: 18px;
    color: #808080;
  `,
  ListWrap: styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
  `,
  Lists: styled.div`
    width: 70vw;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
  `,
  RecipeWrap: styled.div`
  `,
  RecipeImg: styled.img`
  `,
  RecipeContentWrap: styled.div`
  `,
  OrderNum: styled.div`
  `,
  Content: styled.div`
  `,
}; 

function RecipeCtn() { 
  const location = useLocation();
  const [recipeList, setRecipeList] = useState([]);

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
  }

  useEffect(() => {
    getData();
  }, []);

  return (
    <>
      <Style.Wrapper>
        <Style.IntroWrap>
          <Style.MainImg src={recipe[target]["M_PHO"]}></Style.MainImg>
          
          <Style.Intro>
            <Style.TitleWrap>
              <FontAwesomeIcon icon={faSpoon} color="#C7F2A4"/>
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
                <Style.AddBtn>더보기</Style.AddBtn>
              </Style.SubWrap>
            </Style.DetailWrap>
          </Style.Intro>

        </Style.IntroWrap>

        <Style.TitleWrap>
        <FontAwesomeIcon icon={faUtensils} color="#C7F2A4" />
          <Style.Title>레시피</Style.Title>
        </Style.TitleWrap>

        <Style.ListWrap>
          <Style.Lists>
            {recipeList.map(lst => {
              return (
                <>{lst.value}</>
              )
            })}
          </Style.Lists>
        </Style.ListWrap>

      </Style.Wrapper>
    </>
  );
}
  
export default RecipeCtn;