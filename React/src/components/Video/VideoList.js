import React, { Component } from "react";
import Video from "./Video";
import PropTypes from "prop-types";
import { connect } from "react-redux";

import { getVideo } from "../../actions/videoActions";

const rowStyle = {
  marginLeft: "0",
  marginRight: "0"
};

class VideoList extends Component {
  componentDidMount() {
    this.props.getVideo(this.props.team.team);
  }

  render() {
    const { videos } = this.props.video;
    return (
      <div className="video_list">
        <div className="container">
          <div className="card card-body bg-light mb-3">
            <div className="row" style={rowStyle}>
              {videos.map((video, index) => (
                <Video key={video.id} number={index} videoToShow={video} />
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }
}

VideoList.propTypes = {
  video: PropTypes.object.isRequired,
  team: PropTypes.object.isRequired,
  getVideo: PropTypes.func.isRequired
};

const mapStateToProps = state => ({
  video: state.video,
  team: state.team
});

export default connect(
  mapStateToProps,
  { getVideo }
)(VideoList);
