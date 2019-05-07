import { combineReducers } from "redux";
import gameReducer from "./gameReducer";
import videoReducer from "./videoReducer";
import securityReducer from "./securityReducer";
import teamReducer from "./teamReducer";

export default combineReducers({
  game: gameReducer,
  video: videoReducer,
  security: securityReducer,
  team: teamReducer
});
