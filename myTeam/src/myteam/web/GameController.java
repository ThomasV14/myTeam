package com.tdev.myteam.web;

import com.tdev.myteam.domain.Game;
import com.tdev.myteam.services.GameService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/game")
public class GameController {
    @Autowired
    private GameService gameService;

    @CrossOrigin
    @GetMapping("/last/{team}")
    public ResponseEntity<?> getLastGame(@PathVariable String team){
        Game game = gameService.findLastGame(team);
        return new ResponseEntity<Game>(game, HttpStatus.OK);
    }
}
