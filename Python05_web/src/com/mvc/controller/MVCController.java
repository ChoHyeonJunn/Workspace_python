package com.mvc.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class MVCController
 */
@WebServlet("/MVCController")
public class MVCController extends HttpServlet {
	private static final long serialVersionUID = 1L;

	private HttpServletRequest request;
	private HttpServletResponse response;
	private String view;
	private PrintWriter out;

	public MVCController() {
		// TODO Auto-generated constructor stub
	}

	protected void processRequest(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		this.request = request;
		this.response = response;

		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");

		out = response.getWriter();

		String command = request.getParameter("command");

		switch (command) {
		case "naver":
			doNaver();
			break;
		}

		RequestDispatcher dispatcher = request.getRequestDispatcher(view);
		dispatcher.forward(request, response);
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	private void doNaver() {
		
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		processRequest(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		processRequest(request, response);
	}

}
