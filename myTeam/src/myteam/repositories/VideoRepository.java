package com.tdev.myteam.repositories;

import com.tdev.myteam.domain.Video;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface VideoRepository extends CrudRepository<Video, Integer> {
    List<Video> findByTeam(String team);
}
