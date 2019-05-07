import axios from "axios";
import { GET_GAME } from "./types";
import { SET_TEAM } from "./types";

export const getGame = team => async dispatch => {
  const res = await axios.get("/api/game/last/".concat(team));
  dispatch({
    type: GET_GAME,
    payload: res.data
  });
};

export const setTeam = team => dispatch => {
  localStorage.setItem("team", team);
  dispatch({
    type: SET_TEAM,
    payload: team
  });
};
