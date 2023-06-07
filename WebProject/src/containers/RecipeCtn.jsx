import styled from "styled-components";

const Style = {
  Wrapper: styled.div`
    flex: 1;
  `,
}; 

function RecipeCtn() { 
  return (
    <>
      <Style.Wrapper>
        레시피페이지 컴포넌트
      </Style.Wrapper>
    </>
  );
}
  
export default RecipeCtn;