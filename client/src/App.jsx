import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

const imageSizeFactor = 0.5;

function Image() {
  return (
    <img
      src={reactLogo} // This should be changed to the generated background image
      className="logo"
      alt="React logo"
      width={screen.availWidth * imageSizeFactor}
      height={screen.availHeight * imageSizeFactor}
    />
  );
}

function ImageURL() {
  const urlImg = "https://via.placeholder.com/500"; // This should be changed to the generated background image
  return urlImg;
}

const outputQuestion =
  "This is a placeholder question, what happens if this issssssss ssssss sssssssss ssssssss sssssssss ssss too long to fit?";

function Question() {
  return (
    <div>
      <p class="textBox"> {outputQuestion}</p>
    </div>
  );
}

function App() {
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
          <input class="textBox" id="userInput" type="text"></input>
          <button
            onClick={() => {
              const userInput = document.getElementById("userInput").value;
              alert(`You entered: ${userInput}`);
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
