import { SET_TEAM } from "../actions/types";

const initialState = {
  team: {}
};

export default function(state = initialState, action) {
  switch (action.type) {
    case SET_TEAM:
      return {
        ...state,
        team: action.payload
      };
    default:
      return state;
  }
}
