package com.tdev.myteam.web;

import com.tdev.myteam.domain.Video;
import com.tdev.myteam.services.VideoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/video")
public class VideoController {
    @Autowired
    VideoService videoService;

    @CrossOrigin
    @GetMapping("/{team}")
    public ResponseEntity<?> getVideosForTeam(@PathVariable String team){
        List<Video> videos = videoService.findVideosForGame(team);
        return new ResponseEntity<List<Video>>(videos, HttpStatus.OK);
    }
}
