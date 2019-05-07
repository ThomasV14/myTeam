import React, { Component } from "react";
import YouTube from "react-youtube";

export default class Video extends Component {
  _onReady(event) {
    event.target.pauseVideo();
  }

  render() {
    const { videoToShow, number } = this.props;
    const opts = {
      height: "250",
      width: "300",
      playerVars: {
        autoplay: 0
      }
    };
    return (
      <div className="video">
        <div className="container">
          <div className="card card-body bg-light mb-3">
            <div className="row">
              <div className="videoRow">
                <h3>{number + 1}</h3>
                <YouTube
                  videoId={videoToShow.url}
                  opts={opts}
                  onReady={this._onReady}
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
