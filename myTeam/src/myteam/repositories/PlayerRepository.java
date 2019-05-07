package com.tdev.myteam.repositories;

import com.tdev.myteam.domain.Player;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface PlayerRepository extends CrudRepository<Player,Integer> {
    List<Player> findByTeam(String team);
}
