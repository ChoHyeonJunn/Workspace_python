package com.mvc.mongo.model.dao;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Repository;

import com.mvc.mongo.dto.Score;

@Repository
public class ScoreMongoDao {

	@Autowired
	private MongoTemplate mongoTemplate;

	public List<Score> findAll() {
		return mongoTemplate.findAll(Score.class, "score");
	}
}
