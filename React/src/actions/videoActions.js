import axios from "axios";
import { GET_VIDEOS } from "./types";

export const getVideo = team => async dispatch => {
  const res = await axios.get("/api/video/".concat(team));
  dispatch({
    type: GET_VIDEOS,
    payload: res.data
  });
};
