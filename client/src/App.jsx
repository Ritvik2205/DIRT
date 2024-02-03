import { useState } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";

const urlImg = "https://via.placeholder.com/500"; // This should be changed to the generated background image
const outputQuestion =
  "This is a placeholder question, what happens oo long to fit?";

function ImageURL() {
  return urlImg;
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

  // State to hold the user's selected language
  const [selectedLanguage, setSelectedLanguage] = useState('');


  
  return (

    <div class="float-container">
      <div class="float-child">
        <div
          id="imageDisplay"
          style={{
            backgroundImage: "url(" + ImageURL() + ")",
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
  );
}

export default App;
