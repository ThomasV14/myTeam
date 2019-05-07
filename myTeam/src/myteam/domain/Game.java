package com.tdev.myteam.domain;

import javax.persistence.*;

@Entity
@Table(name = "LastGames")
public class Game {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "GameID")
    private Integer id;

    @Column(name = "Team")
    private String team;

    @Column(name = "OpposingTeam")
    private String opposingTeam;

    @Column(name = "WIN")
    private Boolean win;

    @Column(name = "AT_HOME")
    private Boolean atHome;

    @Column(name = "Score")
    private String score;

    public Game(){

    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getTeam() {
        return team;
    }

    public void setTeam(String team) {
        this.team = team;
    }

    public String getOpposingTeam() {
        return opposingTeam;
    }

    public void setOpposingTeam(String opposingTeam) {
        this.opposingTeam = opposingTeam;
    }

    public Boolean getWin() {
        return win;
    }

    public void setWin(Boolean win) {
        this.win = win;
    }

    public Boolean getAtHome() {
        return atHome;
    }

    public void setAtHome(Boolean atHome) {
        this.atHome = atHome;
    }

    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }
}
