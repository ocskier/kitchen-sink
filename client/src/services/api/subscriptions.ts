import { gql } from "@apollo/client";

export const USER_CONNECTED = gql`
  subscription {
    userConnected {
      time
      success
      errors
    }
  }
`;
