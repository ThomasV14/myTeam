import React, { Component } from "react";

class LastGame extends Component {
  assignResult(result) {
    if (result === "W") {
      return (
        <p>
          {" "}
          Result: <span className="winStyle"> Win </span>{" "}
        </p>
      );
    } else {
      return (
        <p>
          {" "}
          Result: <span className="lossStyle"> Loss </span>{" "}
        </p>
      );
    }
  }
  assignLocation(location, team, opposingTeam) {
    if (location === "Home") {
      return <p> Home Game</p>;
    } else {
      return <p> Away Game</p>;
    }
  }

  render() {
    const { gameToShow } = this.props;
    const result = gameToShow.win ? "W" : "L";
    const location = gameToShow.atHome ? "Home" : "Away";
    let location_element = this.assignLocation(
      location,
      gameToShow.team,
      gameToShow.opposingTeam
    );
    let result_element = this.assignResult(result);
    return (
      <div>
        <div className="container">
          <div className="card card-body bg-light mb-3">
            <div className="row">
              <div className="col-lg-4 col-md-4 col-8">
                <span className="mx-auto">
                  {" "}
                  <b>Last Game</b>
                </span>
                {result_element}
              </div>
              <div className="col-lg-4 col-md-4 col-8">
                <h3>{gameToShow.opposingTeam} </h3>
                <span>{location_element}</span>
              </div>
              <div className="col-lg-4 col-md-4 col-8">
                <span className="mx-auto">
                  {" "}
                  <b>Score</b>
                </span>
                <p>
                  {String(gameToShow.score).substring(
                    0,
                    String(gameToShow.score).length - 1
                  )}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default LastGame;
