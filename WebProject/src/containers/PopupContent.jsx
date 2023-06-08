import styled from "styled-components";
import { faXmark } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import recipeData from "../data/Recipe.json";

const Style = {
    FullLayer: styled.div`
        position: fixed;
        top: 50%;
        left: 50%;
        z-index: 300;
        transform: translate(-50%, -50%);
    `,
    CommonAlert: styled.div`
        text-align: left;
        background-color: #FFFFFF;
        border: 2px solid #C7F2A4;
        border-radius: 10px;
        padding: 40px;
        margin: auto;
        box-sizing: border-box;
        font-size: 16px;
    `,
    ContentWrap: styled.div`
        width: 100%;
        align-text: left;
        display: flex;
        flex-direction: row;
    `,
}; 

const PopupContent = (props) => { 
  const { code, close } = props;
  const recipe = JSON.parse(JSON.stringify(recipeData));

  return (
    <>
      <Style.FullLayer>
        <Style.CommonAlert>
          <Style.ContentWrap>
            <a onClick={close}>
              <FontAwesomeIcon icon={faXmark} color="#C7F2A4" size="2x" />
            </a>
          </Style.ContentWrap>
          

          
        </Style.CommonAlert>
      </Style.FullLayer>
    </>
  );
}
  
export default PopupContent;