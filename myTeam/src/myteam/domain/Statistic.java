package com.tdev.myteam.domain;

import javax.persistence.*;

@Entity
@Table(name = "PlayerSTATs")
public class Statistic {

    @Id
    @Column(name = "PlayerID")
    private Integer id;

    @Column(name = "PPG")
    private Float pointsPerGame;

    @Column(name = "APG")
    private Float assistsPerGame;

    @Column(name = "RPG")
    private Float reboundsPerGame;

    @Column(name = "SPG")
    private Float stealsPerGame;

    @Column(name = "BPG")
    private Float blocksPerGame;

    @Column(name = "TOVPG")
    private Float tosPerGame;

    @Column(name = "FT_PERC")
    private Float freeThrowPerc;

    @Column(name = "FG_PERC")
    private Float fieldGoalPerc;

    public Statistic(){

    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Float getPointsPerGame() {
        return pointsPerGame;
    }

    public void setPointsPerGame(Float pointsPerGame) {
        this.pointsPerGame = pointsPerGame;
    }

    public Float getAssistsPerGame() {
        return assistsPerGame;
    }

    public void setAssistsPerGame(Float assistsPerGame) {
        this.assistsPerGame = assistsPerGame;
    }

    public Float getReboundsPerGame() {
        return reboundsPerGame;
    }

    public void setReboundsPerGame(Float reboundsPerGame) {
        this.reboundsPerGame = reboundsPerGame;
    }

    public Float getStealsPerGame() {
        return stealsPerGame;
    }

    public void setStealsPerGame(Float stealsPerGame) {
        this.stealsPerGame = stealsPerGame;
    }

    public Float getBlocksPerGame() {
        return blocksPerGame;
    }

    public void setBlocksPerGame(Float blocksPerGame) {
        this.blocksPerGame = blocksPerGame;
    }

    public Float getTosPerGame() {
        return tosPerGame;
    }

    public void setTosPerGame(Float tosPerGame) {
        this.tosPerGame = tosPerGame;
    }

    public Float getFreeThrowPerc() {
        return freeThrowPerc;
    }

    public void setFreeThrowPerc(Float freeThrowPerc) {
        this.freeThrowPerc = freeThrowPerc;
    }

    public Float getFieldGoalPerc() {
        return fieldGoalPerc;
    }

    public void setFieldGoalPerc(Float fieldGoalPerc) {
        this.fieldGoalPerc = fieldGoalPerc;
    }
}
