import styled from "styled-components";

const Style = {
  Wrapper: styled.div`
    flex: 1;
  `,
};

function InputCtn() {
  return (
    <>
      <Style.Wrapper>
        입력페이지 컴포넌트
      </Style.Wrapper>
    </>
  );
}
  
export default InputCtn;