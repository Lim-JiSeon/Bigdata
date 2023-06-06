import styled from "styled-components";

const Style = {
  Wrapper: styled.div`
    flex: 1;
  `,
};

function RecipeListCtn() {
  return (
    <>
      <Style.Wrapper>
        레시피 목록 페이지
      </Style.Wrapper>
    </>
  );
}
  
export default RecipeListCtn;