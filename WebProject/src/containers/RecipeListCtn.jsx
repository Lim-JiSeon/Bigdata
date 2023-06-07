import { useLocation } from "react-router-dom";
import styled from "styled-components";
import dishData from "../data/DISH.json";

const Style = {
  Wrapper: styled.div`
    flex: 1;
  `,
};

function RecipeListCtn() {
  const location = useLocation();
  const dishName = JSON.parse(JSON.stringify(dishData));

  console.log(dishName[location.state.dish]);
  console.log(dishName["\ubcf6\uc74c"]);

  return (
    <>
      <Style.Wrapper>
        레시피 목록 페이지
      </Style.Wrapper>
    </>
  );
}
  
export default RecipeListCtn;