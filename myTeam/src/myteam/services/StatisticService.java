package com.tdev.myteam.services;

import com.tdev.myteam.domain.Statistic;
import com.tdev.myteam.repositories.StatisticRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class StatisticService {
    @Autowired
    private StatisticRepository statisticRepository;

    public Statistic findStatistic(int id){
        return statisticRepository.findById(id);
    }
}
