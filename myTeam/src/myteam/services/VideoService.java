package com.tdev.myteam.services;

import com.tdev.myteam.domain.Video;
import com.tdev.myteam.repositories.VideoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class VideoService {
    @Autowired
    private VideoRepository videoRepository;

    public List<Video> findVideosForGame(String team){
        return videoRepository.findByTeam(team);
    }
}
