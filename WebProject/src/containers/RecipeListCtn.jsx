import { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import dishData from "../data/DISH.json";
import ingredientData from "../data/Ingredient.json";
import recipeData from "../data/Recipe.json";
import img4 from "../img/img4.png";

const Style = {
  Wrapper: styled.div`
    flex: 1;
    font-family: 'Jua', sans-serif;
  `,
  ContentWrap: styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  `,
  InputWrap: styled.div`
    width: 30vw;
    height: 5vh;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #B6E388;
    border-radius: 20px;
    padding: 0 1vw;
    margin-top: 5vh;
  `,
  Input: styled.input`
    width: 25vw;
    height: 4vh;
    text-align: center;
    font-size: 24px;
    border: none;
    border-radius: 20px;
    outline: none;
  `,
  SearchBtn: styled.button`
    width: 2vw;
    height: 7vh;
    border: none;
    border-radius: 20px;
    background: transparent;
  `,
  Link: styled(Link)`
    text-decoration: none;
  `,
  ListWrap: styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2vh 0 1vh 0;
  `,
  Lists: styled.div`
    width: 70vw;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    flex-wrap: wrap;
  `,
  Btn: styled.button`
    width: 15vw;
    height: 30vh;
    border: none;
    background-color: transparent;
    &:hover {
      color: #B6E388;
    }
  `,
  Img: styled.img`
    width: 13vw;
    height: 22vh;
    text-align: center;
    border-radius: 20px;
    &:hover {
      opacity: 0.5;
    }
  `,
  Txt: styled.div`
    font-size: 18px;
    font-family: 'Jua', sans-serif;
  `,
  TitleWrap: styled.div`
    height: 61vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 6vh 0;
  `,
  Title: styled.div`
    font-size: 36px;
  `,
  AddImg: styled.img`
    width: 20vw;
  `,
};

function RecipeListCtn() {
  const location = useLocation();
  const [viewList, setViewList] = useState([]);
  const [search, setSearch] = useState(""); 

  const dish = JSON.parse(JSON.stringify(dishData));
  const ingredient = JSON.parse(JSON.stringify(ingredientData));
  const recipe = JSON.parse(JSON.stringify(recipeData));
  
  const target = location.state.name;
  const select = location.state.select;

  const getName = () => {
    let lst = dish[target];
    if(lst) {
      for (let i=0; i<lst.length; i++) {
        let key = lst[i];
        let newData = (
          <Style.Btn>
            <Style.Img src={recipe[key]["M_PHO"]}></Style.Img>
            <Style.Txt>{recipe[key]["DISH"]}</Style.Txt>
          </Style.Btn>
        );
        let element = {
          id: key, 
          dishName: recipe[key]["DISH"],
          value: newData
        };
        viewList.push(element);
      }
    } else {
      let newData = (
        <Style.TitleWrap>
          <Style.Title>현재 레시피가 존재하지 않습니다.</Style.Title>
          <Style.AddImg src={img4}></Style.AddImg>
        </Style.TitleWrap>
      );
      let element = {
        id: "404", 
        dishName: "레시피없음",
        value: newData
      };
      viewList.push(element);
    }
    setViewList(viewList);
    setSearch(" ");
  };

  const getIngredients = () => {
    let lst = [];
    for (let i=0; i<target.length; i++) {
      let temp = ingredient[target[i]];
      if (temp) {
        lst.push(...temp);
      }
    }

    if(lst.length != 0) {
      for (let i=0; i<lst.length; i++) {
        let key = lst[i];
        let newData = (
          <Style.Btn>
            <Style.Img src={recipe[key]["M_PHO"]}></Style.Img>
            <Style.Txt>{recipe[key]["DISH"]}</Style.Txt>
          </Style.Btn>
        );
        let element = {
          id: key, 
          dishName: recipe[key]["DISH"],
          value: newData
        };
        viewList.push(element);
      }
    } else {
      let newData = (
        <Style.TitleWrap>
          <Style.Title>현재 레시피가 존재하지 않습니다.</Style.Title>
          <Style.AddImg src={img4}></Style.AddImg>
        </Style.TitleWrap>
      );
      let element = {
        id: "404", 
        dishName: "레시피없음",
        value: newData
      };
      viewList.push(element);
    }
    setViewList(viewList);
    setSearch(" ");
  };

  const searchRecipe = (input) => {
    setViewList(oldValues => {
      return oldValues.filter(view => view.dishName == input)
    })
    console.log(viewList);
    if (viewList.length == 0) {
      let newData = (
        <Style.TitleWrap>
          <Style.Title>현재 레시피가 존재하지 않습니다.</Style.Title>
          <Style.AddImg src={img4}></Style.AddImg>
        </Style.TitleWrap>
      );
      let element = {
        id: "404", 
        dishName: "레시피없음",
        value: newData
      };
      viewList.push(element);
      setViewList(viewList);
      setSearch(" ");
    }
    setSearch(" ");
  };

  useEffect(() => {
    if(select) {
      getName();
    } else {
      getIngredients();
    }
  }, []);

  return (
    <>
      <Style.Wrapper>
        <Style.ContentWrap>
          {viewList.length != 1 && <Style.InputWrap>
            <Style.Input
              type="text"
              onChange={(e) => {setSearch(e.target.value)}}
            ></Style.Input>
            <Style.SearchBtn
              onClick={() => {searchRecipe(search)}}
            ><FontAwesomeIcon icon={faMagnifyingGlass} size="2x" color="#B6E388"/></Style.SearchBtn>
          </Style.InputWrap>}

          <Style.ListWrap>
            <Style.Lists>
              {viewList.map(view => {
                return (
                  <>{view.value}</>
                )
              })}
            </Style.Lists>
          </Style.ListWrap>

        </Style.ContentWrap>
      </Style.Wrapper>
    </>
  );
}
  
export default RecipeListCtn;