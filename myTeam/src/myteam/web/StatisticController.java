package com.tdev.myteam.web;

import com.tdev.myteam.domain.Statistic;
import com.tdev.myteam.services.StatisticService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/statistics")
public class StatisticController {
    @Autowired
    private StatisticService statisticService;

    @GetMapping("/{playerId}")
    public ResponseEntity<?> getPlayerStatistics(@PathVariable String playerId){
        Statistic statistic = statisticService.findStatistic(Integer.parseInt(playerId));
        return new ResponseEntity<Statistic>(statistic, HttpStatus.OK);
    }

}
