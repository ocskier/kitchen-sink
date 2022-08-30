import { useCallback, useEffect, useState } from "react";
import { useQuery } from "@apollo/client";

import logo from "./logo.svg";
import "./App.css";
import { GET_TIME } from "./services/api";

function App() {
  const [time, setTime] = useState<number | null>(null);
  const { loading, error, data, refetch } = useQuery(GET_TIME);

  useEffect(() => {
    const timeInterval = setInterval(() => refetch(), 1000);
    return () => clearInterval(timeInterval);
  }, [refetch]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;
  return (
    <div className="App">
      <header className="App-header">
        {data.time && (
          <>
            <h2 style={{ margin: "3rem 0" }}>Server time:</h2>
            <p>{new Date(data.time).toUTCString()}</p>
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

