package com.tdev.myteam.repositories;

import com.tdev.myteam.domain.Statistic;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface StatisticRepository extends CrudRepository<Statistic, Integer> {
    Statistic findById(int id);
}
