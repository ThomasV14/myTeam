import { GET_GAME } from "../actions/types";

const initialState = {
  games: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_GAME:
      return { ...state, games: action.payload };
    default:
      return state;
  }
}
