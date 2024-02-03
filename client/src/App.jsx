import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function Image() {
  return (
    <a href="https://vitejs.dev" target="_blank">
      <img src={viteLogo} className="logo" alt="Vite logo" />
    </a>
  );
}

function App() {
  return (
    <>
      <Image />
      <div>
        <h1>Below is some text input:</h1>
        <input id="userInput" type="text"></input>
      </div>
      <div>
        <button
          onClick={() => {
            const userInput = document.getElementById("userInput").value;
            alert(`You entered: ${userInput}`);
          }}
        >
          Submit answer
        </button>
      </div>
    </>
  );
}

export default App;
