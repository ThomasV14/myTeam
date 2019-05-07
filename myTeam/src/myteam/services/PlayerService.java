package com.tdev.myteam.services;

import com.tdev.myteam.domain.Player;
import com.tdev.myteam.repositories.PlayerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


import java.util.List;
@Service
public class PlayerService {
    @Autowired
    private PlayerRepository playerRepository;

    public List<Player> findPlayersForTeam(String team){
        return playerRepository.findByTeam(team);
    }
}

