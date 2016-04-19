(function() {
	'use strict';

	angular.module('myApp', ['ngMaterial', 'ngRoute', 'ngResource'])
	.config(config)
	.factory('Event', Event)
	.factory('Travel', Travel)
	.directive('home', home)
	.directive('about', about)
	.directive('contact', contact)
	.directive('eventsList', eventsList)
	.directive('eventDetail', eventDetail)

	function config($routeProvider) {
		$routeProvider
			.when('/', {
				template: '<home></home>',
			})
			.when('/about', {
				template: '<about></about>',
			})
			.when('/contact', {
				template: '<contact></contact>',
			})
			.when('/events', {
				template: '<events-list></events-list>',
			})
			.when('/events/:id', {
				template: '<event-detail></event-detail>',
			})
			.otherwise({ redirectTo: '/' })
	}

	function Event($resource) {
		return $resource('/api/events/:id')
	}

	function Travel($resource) {
		return $resource('/api/travels/:id')
	}

	function home() {
		return {
			scope: {},
			controller: function() {
				this.title = "Home"
				document.title = this.title
			},
			controllerAs: 'vm',
			template: [
				'<h1>{{ vm.title }}</h1>'
			].join('')
		}
	}

	function about() {
		return {
			scope: {},
			controller: function() {
				this.title = "about"
				document.title = this.title
			},
			controllerAs: 'vm',
			template: [
				'<h1>{{ vm.title }}</h1>'
			].join('')
		}
	}

	function contact() {
		return {
			scope: {},
			controller: function() {
				this.title = "Contact"
				document.title = this.title
			},
			controllerAs: 'vm',
			template: [
				'<h1>{{ vm.title }}</h1>'
			].join('')
		}
	}

	function eventsList(Event) {
		return {
			scope: {},
			controller: function() {
				this.title = "Events"
				document.title = this.title
				this.events = Event.query()
			},
			controllerAs: 'vm',
			template: [
			'<div layout="row" layout-wrap>',
				'<md-card flex="30" ng-repeat="event in vm.events">',
			        '<md-card-header>',
			          '<md-card-avatar>',
			            '<img src="img/logo.svg"/>',
			          '</md-card-avatar>',
			          '<md-card-header-text>',
			            '<span class="md-title">Angular</span>',
			            '<span class="md-subhead">Material</span>',
			          '</md-card-header-text>',
			        '</md-card-header>',
			        '<img ng-src="{{ event.photo }}" class="md-card-image" alt="Washed Out">',
			        '<md-card-title>',
			          '<md-card-title-text>',
			            '<span class="md-headline">{{ event.name }}</span>',
			          '</md-card-title-text>',
			        '</md-card-title>',
			        '<md-card-content>',
			          '<p>',
			            "The titles of Washed Out's breakthrough song and the first single from Paracosm share the",
			            "two most important words in Ernest Greene's musical language: feel it. It's a simple request, as well...",
			          '</p>',
			        '</md-card-content>',
			    '</md-card>',
			'</div>',
			].join('')
		}
	};

	function eventDetail() {
		return {
			scope: {},
			controller: function($routeParams, Event) {
				var vm = this;
				var id = $routeParams.id;

				Event.get({ id: id }, function(data) {
					vm.event = data;
					document.title = data.name
				});
			},
			controllerAs: 'vm',
			template: [
				'<h1>{{ vm.event.name }}</h1>'
			].join('')
		}
	};

})();