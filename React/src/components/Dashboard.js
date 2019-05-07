import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";

import { getGame } from "../actions/gameActions";

import LastGame from "./Game/LastGame";
import VideoList from "./Video/VideoList";

class Dashboard extends Component {
  componentDidMount() {
    this.props.getGame(this.props.team.team);
  }

  render() {
    const { games } = this.props.game;
    return (
      <div className="lastgame">
        <div className="container">
          <div className="row">
            <div className="col-md-12">
              <h1 className="display-4 text-center">Home</h1>
              <hr />
              <LastGame gameToShow={games} />
              <hr />
              <h4 className="display-10 text-center">Videos </h4>
              <VideoList />
            </div>
          </div>
        </div>
      </div>
    );
  }
}
Dashboard.propTypes = {
  game: PropTypes.object.isRequired,
  team: PropTypes.object.isRequired,
  getGame: PropTypes.func.isRequired
};

const mapStateToProps = state => ({
  game: state.game,
  team: state.team
});

export default connect(
  mapStateToProps,
  { getGame }
)(Dashboard);
