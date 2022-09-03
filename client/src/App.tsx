import { useEffect, useState } from "react";
import { useMutation, useLazyQuery } from "@apollo/client";

import logo from "./logo.svg";
import "./App.css";
import { CONNECT, GET_TIME } from "./services/api";

function App() {
  const [connected, setConnected] = useState(false);
  const [connect] = useMutation(CONNECT);
  const [getTime, { loading, error, data }] = useLazyQuery(GET_TIME);

  useEffect(() => {}, []);

  useEffect(() => {
    let timeInterval: NodeJS.Timer | undefined = undefined;
    console.log(connected);
    if (connected) {
      timeInterval = setInterval(() => getTime(), 1000);
    }
    return () => clearInterval(timeInterval);
  }, [connected, getTime]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;
  return (
    <div className="App">
      <header className="App-header">
        {data?.getTime?.time && (
          <>
            <h2 style={{ margin: "3rem 0" }}>Server time:</h2>
            <p>{new Date(data.getTime.time * 1000).toUTCString()}</p>
          </>
        )}
        <a
          href="http://localhost:5001/graphql"
          style={{ color: "white" }}
          target="_blank"
          rel="noreferrer"
        >
          GraphQL playground
        </a>
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

