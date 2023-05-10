import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUserChef } from "@fortawesome/free-regular-svg-icons";

function Footer() {
    return (
      <>
        <div><FontAwesomeIcon icon={faUserChef} /></div>
        <div>Copyright 2023 요리조리 All rights reserved</div>
      </>
    );
  }
  
  export default Footer;