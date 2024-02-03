import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";
import Image from "./Image";

const urlImg = "https://via.placeholder.com/500"; // This should be changed to the generated background image
const outputQuestion =
  "¿Cómo te llamas? (What is your name?)";

function ImageURL(prompt, cb) {
  Image(prompt, cb);
  // console.log(url);
  // return url;
}

function Question() {
  return (
    <div>
      <p class="textBox"> {outputQuestion}</p>
    </div>
  );
}

function SendAnswer() {
  const userInput = document.getElementById("userInput").value;
  alert(`You entered: ${userInput}`);
}

function App() {
  // Change the background colout of the page
  document.body.style.backgroundColor = "white";
  // State to hold the user's selected language
  const [selectedLanguage, setSelectedLanguage] = useState("");
  const [urlResponse, setUrlResponse] = useState("");

  useEffect(() => {
    ImageURL("An image of a water fountain", maybeSetUrl)
  }, [])


  function maybeSetUrl(newUrl){
    newUrl && setUrlResponse(newUrl)
  }

  

  return (
    <>
    <div class="float-container">
      <div class="float-child">
        <div
          id="imageDisplay"
          style={{
            backgroundImage:
              "url(" + urlResponse + ")",
            backgroundSize: "cover",
          }}
        ></div>
      </div>
      <div class="float-child">
        <div id="answerPanel">
          <br />
          <Question />
          <h3> Your anwer: </h3>
          <input id="userInput" type="textArea"></input>
          <button
            onClick={() => {
              SendAnswer();
            }}
          >
            Submit answer
          </button>
        </div>
        <div />
      </div>{" "}
    </div>
    </>
  );
}

export default App;
