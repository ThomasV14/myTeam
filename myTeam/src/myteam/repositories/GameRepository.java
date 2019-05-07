package com.tdev.myteam.repositories;

import com.tdev.myteam.domain.Game;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface GameRepository extends CrudRepository<Game, Integer> {
    Game findByTeam(String team);
}
