import { gql } from "@apollo/client";

export const CONNECT = gql`
  mutation ($payload: String) {
    connect(payload: $payload) {
      msg
      success
      errors
    }
  }
`;
