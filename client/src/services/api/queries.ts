import { gql } from "@apollo/client";

export const GET_TIME = gql`
  query {
    getTime {
      time
      success
      errors
    }
  }
`;
