package com.tdev.myteam.web;

import com.tdev.myteam.domain.Player;
import com.tdev.myteam.services.PlayerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/players")
public class PlayerController {
    @Autowired
    private PlayerService playerService;

    @GetMapping("/{team}")
    public ResponseEntity<?> getPlayersForTeam(@PathVariable String team){
        List<Player> players = playerService.findPlayersForTeam(team);
        return new ResponseEntity<List<Player>>(players, HttpStatus.OK);
    }

}
