import React, { Component } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import { connect } from "react-redux";

class Landing extends Component {
  componentDidMount() {
    if (this.props.security.validToken) {
      this.props.history.push("/home");
    }
  }

  render() {
    return (
      <div className="landing">
        <div className="light-overlay landing-inner text-dark">
          <div className="container">
            <div className="row">
              <div className="col-md-12 text-center">
                <h1 className="display-3 mb-4">myTeam</h1>
                <p className="lead">
                  Create an account or login to view your team dashboard
                </p>
                <hr />
                <Link className="btn btn-lg btn-primary mr-2" to="/register">
                  {" "}
                  Sign Up{" "}
                </Link>
                <Link className="btn btn-lg btn-secondary mr-2" to="/login">
                  {" "}
                  Login{" "}
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

Landing.propTypes = {
  security: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  security: state.security
});

export default connect(mapStateToProps)(Landing);
