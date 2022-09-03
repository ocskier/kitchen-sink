import { useCallback, useEffect, useState } from "react";
import { useMutation, useLazyQuery } from "@apollo/client";

import logo from "./logo.svg";
import "./App.css";
import { CONNECT, GET_TIME } from "./services/api";

function App() {
  const [connected, setConnected] = useState<boolean>(false);

  const [connect, { loading: loadingConnect, error: connectError }] =
    useMutation(CONNECT);
  const [getTime, { loading: loadingTime, error: timeError, data }] =
    useLazyQuery(GET_TIME);

  const connectToServer = useCallback(async () => {
    try {
      const { data } = await connect({
        variables: { payload: window.location.href },
      });
      if (data?.connect?.msg) setConnected(true);
    } catch (err) {
      console.log(err);
    }
  }, [connect]);

  const getTimeFromServer = useCallback(async () => {
    try {
      await getTime({ pollInterval: 1000 });
    } catch (err) {
      console.log(err);
    }
  }, [getTime]);

  useEffect(() => {
    connectToServer();
  }, [connectToServer]);

  useEffect(() => {
    getTimeFromServer();
  }, [getTimeFromServer]);

  if (connectError || timeError) return <p>Error :(</p>;
  return (
    <div className="App">
      <header className="App-header">
        <div style={{ height: "250px" }}>
          {loadingConnect && <p>Connecting to server...</p>}
          {loadingTime && <p>Loading...</p>}
          {connected && data?.getTime?.time && (
            <>
              <h2 style={{ margin: "3rem 0" }}>Server time:</h2>
              <p>{new Date(data?.getTime?.time * 1000).toUTCString()}</p>
            </>
          )}
        </div>
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

