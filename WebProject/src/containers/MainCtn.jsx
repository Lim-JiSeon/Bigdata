import { Link } from "react-router-dom";
import styled, {keyframes} from "styled-components";
import img1 from "../img/img1.jpg";
import img2 from "../img/img2.jpg";
import img3 from "../img/img3.jpg";


function MainCtn() { 
  const rotate = keyframes`
  from {
      transform:rotate(0deg);
  }
  to{
      transform:rotate(360deg);
  }`;

  const Style = {
    Wrapper: styled.div`
      flex: 1;
    `,
    Intro: styled.div`
      display: flex;
      flex-direction: column;
      align-items: center;
      font-family: 'Jua', sans-serif;
    `,
    Detail: styled.div`
        text-align: center;
        padding: 1vh 0;
    `,
    Title: styled.div`
      font-size: 42px;
      color: #3B7400;
      display: flex;
    `,
    Main: styled.div`
      font-size: 64px;
      color: #B6E388;
      animation: ${rotate} 2s;
    `,
    Content: styled.div`
      font-size: 24px;
      padding: 2vh 0;
    `,
    ImgList: styled.div`
      display: flex;
      justify-content: center;
      align-items: center;
      padding-top: 2vh;
    `,
    ImgElement: styled.img`
      width: 30vw;
      height: 30vh;
      border: 2px solid #C7C7C7;
      border-radius: 20px;
    `,
    BtnWrap: styled.div`
      padding: 3vh 0;
    `,
    StartBtn: styled.button`
      width: 20vw;
      height: auto;
      padding: 1vh 0;
      border-radius: 10px;
      border: 2px solid #3B7400;;
      background-color: #E1FFB1;
      font-size: 24px;
      font-weight: bold;
    `
  }  

  const ImgArray = [
    <Style.ImgElement src={img1}></Style.ImgElement>,
    <Style.ImgElement src={img2}></Style.ImgElement>,
    <Style.ImgElement src={img3}></Style.ImgElement>
  ];

  return (
    <>
      <Style.Wrapper>
        <Style.Intro>
            <Style.Detail>
                <Style.Title>
                  <Style.Main>자</Style.Main>취생도&nbsp;&nbsp;
                  <Style.Main>만</Style.Main>들수있는&nbsp;&nbsp;
                  <Style.Main>추</Style.Main>천 레시피
                </Style.Title>
                <Style.Content>
                    "냉장고 속 남아있는 재료만 알려주세요!<br/>
                    자취생도 만들 수 있는 추천 레시피를 알려드릴게요."
                </Style.Content>
            </Style.Detail>
            <Style.ImgList>
              {ImgArray}
            </Style.ImgList>
            <Link to="../pages/Input"><Style.BtnWrap>
              <Style.StartBtn onClick={test}>시작하기</Style.StartBtn>
            </Style.BtnWrap></Link>
        </Style.Intro>
      </Style.Wrapper>
    </>
  );
}
  
export default MainCtn;