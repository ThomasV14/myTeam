package com.tdev.myteam.services;

import com.tdev.myteam.domain.Game;
import com.tdev.myteam.repositories.GameRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class GameService {

    @Autowired
    private GameRepository gameRepository;

    public Game findLastGame(String team){
        return gameRepository.findByTeam(team);
    }


}
