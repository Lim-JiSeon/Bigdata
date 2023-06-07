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
    width: 80vw;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    flex-wrap: wrap;
  `,
  Btn: styled.button`
    width: 20vw;
    height: 30vh;
    border: none;
    background-color: transparent;
    &:hover {
      color: #B6E388;
    }
  `,
  Img: styled.img`
    width: 15vw;
    height: 26vh;
    text-align: center;
    border-radius: 20px;
    &:hover {
      opacity: 0.5;
    }
  `,
  Txt: styled.div`
    font-size: 22px;
    font-family: 'Jua', sans-serif;
  `,
};

function RecipeListCtn() {
  const location = useLocation();
  const [viewList, setViewList] = useState([]);
  const [search, setSearch] = useState("");

  const dish = JSON.parse(JSON.stringify(dishData));
  const ingredient = JSON.parse(JSON.stringify(ingredientData));
  const recipe = JSON.parse(JSON.stringify(recipeData));
  
  let target = location.state.name;
  const select = location.state.select;
//<Style.Img src={recipe[key]["M_PHO"]}></Style.Img>
  const getName = () => {
    let lst = dish[target];
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
        name: recipe[key]["DISH"],
        value: newData
      };
      viewList.push(element);
    }
    setViewList(viewList);
    console.log(viewList);
    setViewList([]);

  };

  useEffect(() => {
    getName();
  }, []);

  return (
    <>
      <Style.Wrapper>
        <Style.ContentWrap>
          <Style.InputWrap>
            <Style.Input
              type="text"
              onChange={(e) => {setSearch(e.target.value)}}
            ></Style.Input>
            <Style.Link to="../pages/Recipe">
              <Style.SearchBtn><FontAwesomeIcon icon={faMagnifyingGlass} size="2x" color="#B6E388"/></Style.SearchBtn>
            </Style.Link>
          </Style.InputWrap>

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