import { useCallback, useEffect, useState } from "react";
import axios from "axios";

import logo from "./logo.svg";
import "./App.css";

function App() {
  const [time, setTime] = useState<number | null>(null);

  const getTime = useCallback(async () => {
    try {
      const { data, status } = await axios.get("/current-time");
      if (status === 200) setTime(Math.round(data.time) * 1000);
    } catch (err) {
      console.log(err);
    }
  }, []);

  useEffect(() => {
    // const timeInterval = setInterval(() => getTime(), 1000);
    // return () => clearInterval(timeInterval);
  }, [getTime]);

  return (
    <div className="App">
      <header className="App-header">
        {time && (
          <>
            <h2 style={{ margin: "3rem 0" }}>Server time:</h2>
            <p>{new Date(time).toUTCString()}</p>
          </>
        )}
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

