import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { setTeam } from "../actions/gameActions";

class SelectTeam extends Component {
  constructor() {
    super();
    this.state = {
      team: ""
    };
    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onSubmit(e) {
    e.preventDefault();
    this.props.setTeam(this.state.team);
    this.props.history.push("/home");
  }

  onChange(e) {
    this.setState({
      [e.target.name]: e.target.value
    });
  }
  render() {
    return (
      <div className="select_team">
        <div className="container">
          <div className="row">
            <div className="col-md-8 m-auto">
              <h1 className="display-4 text-center">Select A Team</h1>
              <p className="lead text-center">
                Select the team for your dashboard
              </p>
              <form onSubmit={this.onSubmit}>
                <div className="form-group">
                  <input
                    type="text"
                    className="form-control form-control-lg"
                    placeholder="Team Acronym"
                    name="team"
                    value={this.state.team}
                    onChange={this.onChange}
                  />
                </div>
                <input type="submit" className="btn btn-info btn-block mt-4" />
              </form>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

SelectTeam.propTypes = {
  setTeam: PropTypes.func.isRequired
};

export default connect(
  null,
  { setTeam }
)(SelectTeam);
