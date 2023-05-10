import styled from "styled-components";

function RecipeListCtn() {
    
  const Style = {
    Wrapper: styled.div`
      flex: 1;
    `,
  }  

  return (
    <>
      <Style.Wrapper>
        레시피 목록 페이지
      </Style.Wrapper>
    </>
  );
}
  
export default RecipeListCtn;