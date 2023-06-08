import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faXmark } from "@fortawesome/free-solid-svg-icons";
import { faPizzaSlice } from "@fortawesome/free-solid-svg-icons";
import { faBlender } from "@fortawesome/free-solid-svg-icons";
import recipeData from "../data/Recipe.json";
import { useEffect, useState } from "react";

const Style = {
    FullLayer: styled.div`
        position: fixed;
        top: 50%;
        left: 50%;
        z-index: 300;
        transform: translate(-50%, -50%);
    `,
    CommonAlert: styled.div`
        width: 40vw;
        height: 100%;
        text-align: left;
        background-color: #FFFFFF;
        border: 2px solid #C7F2A4;
        border-radius: 10px;
        padding: 40px;
        margin: auto;
        box-sizing: border-box;
        font-size: 24px;
    `,
    Contents: styled.div`
        display: flex;
        flex-direction: column;
        align-items: start;
        justify-content: center;
        padding: 2vh 4vw;
    `,
    ContentWrap: styled.div`
        display: flex;
        flex-direction: column;
        align-items: start;
        justify-content: center;
        padding-bottom: 5vh;
    `,
    TitleWrap: styled.div`
        display: flex;
        align-items: center;
        justify-content: start;
        padding-bottom: 3vh;
    `,
    Title: styled.div`
        font-size: 30px;
        padding-left: 1vw;
    `,
    List: styled.div`
        display: flex;
        flex-direction: column;
        align-items: center;
    `,
    Row: styled.div`
        width: 25vw;
        display: flex;
        justify-content: space-between;
        align-items: center;
    `,
    Name: styled.div`
        font-size: 24px;
    `,
    Qun: styled.div`
        font-size: 24px;
    `,
}; 

const PopupContent = (props) => { 
  const { code, close } = props;
  const [ingredients, setIngredients] = useState([]);
  const [seasoning, setSeasoning] = useState([]);
  const [test, setTest] = useState("");
  const recipe = JSON.parse(JSON.stringify(recipeData));

  const getIngr = () => {
    for (let i=0; i<recipe[code]["INGR"].length; i++) {
      let newLst = (
        <Style.Row key={recipe[code]["INGR"][i][1]}>
            <Style.Name>{recipe[code]["INGR"][i][1]}</Style.Name>
            <Style.Qun>{recipe[code]["INGR"][i][2]}</Style.Qun>
        </Style.Row>
      );
      let element = {
        id: recipe[code]["INGR"][i][1],
        value: newLst
      };
      ingredients.push(element);
    }
    setIngredients(ingredients);
    setTest("완료");
  };

  const getSsn = () => {
    for (let i=0; i<recipe[code]["COND"].length; i++) {
      let newLst = (
        <Style.Row key={recipe[code]["COND"][i][1]}>
            <Style.Name>{recipe[code]["COND"][i][1]}</Style.Name>
            <Style.Qun>{recipe[code]["COND"][i][2]}</Style.Qun>
        </Style.Row>
      );
      let element = {
        id: recipe[code]["COND"][i][1],
        value: newLst
      };
      seasoning.push(element);
    }
    setSeasoning(seasoning);
    setTest("완료");
  };

  useEffect(() => {
    getIngr();
    getSsn();
  }, []);

  return (
    <>
      <Style.FullLayer>
        <Style.CommonAlert>
            <a onClick={close}>
              <FontAwesomeIcon icon={faXmark} color="#C7F2A4" size="2x" />
            </a>
            <Style.Contents>
                <Style.ContentWrap>
                    <Style.TitleWrap>
                        <FontAwesomeIcon icon={faPizzaSlice} color="#C7F2A4" size="2x" />
                        <Style.Title>재료</Style.Title>
                    </Style.TitleWrap>

                    <Style.List>
                        {ingredients.map(lst => {
                            return (
                                <>{lst.value}</>
                            )
                        })}
                    </Style.List>
                </Style.ContentWrap>

                <Style.ContentWrap>
                    <Style.TitleWrap>
                        <FontAwesomeIcon icon={faBlender} color="#C7F2A4" size="2x" />
                        <Style.Title>양념</Style.Title>
                    </Style.TitleWrap>
                    
                    <Style.List>
                        {seasoning.map(lst => {
                            return (
                                <>{lst.value}</>
                            )
                        })}
                    </Style.List>
                </Style.ContentWrap>
            </Style.Contents>
        </Style.CommonAlert>
      </Style.FullLayer>
    </>
  );
}
  
export default PopupContent;