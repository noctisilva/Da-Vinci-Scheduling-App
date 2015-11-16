angular.module('starter.controllers', [])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  // Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };
})

.controller('LoginCtrl', function($scope) {

})

.controller('ScheduleCtrl', function($scope, $http) {
  $scope.date = moment("2015-10-28T13:00:00+00:00").format("h:mm a");
  var events = [
    {
      "exhibit":
        {
            "id": "5664248772427776",
            "picture": "http://www.davincisciencecenter.org/wp-content/uploads/2015/09/RFAthumb3-280x164.jpg",
            "description": "Feature Exhibition Showing Now through Jan. 18, 2016 Rainforest Adventure is a life-sized maze that encourages kids to leap, jump, hang, climb, and explore a virtual rainforest through more...",
            "name": "Rainforest Adventure",
            "location": "5682617542246400"
        },
      "start_time": "2015-10-28T13:00:00",
      "id": "5692462144159744",
      "end_time": "2015-10-28T14:00:00",
      "schedule": "5631986051842048"
    },
    {
      "exhibit":
        {
          "id": "6202395558150144",
          "picture": "http://www.davincisciencecenter.org/wp-content/uploads/2014/12/Animation-Station-SM-280x164.jpg",
          "description": "The Animation Station exhibit gives visitors opportunities to create their own stop-motion animations by moving objects on a stage and taking a series of still frame images. A computer...",
          "name": "Animation Station",
          "location": "5682617542246400"
        },
      "start_time": "2015-10-28T14:00:00",
      "id": "5672749318012928",
      "end_time": "2015-10-28T15:00:00",
      "schedule": "5631986051842048"
    },
    {
      "exhibit":
        {
          "id": "5137355874762752",
          "picture": "http://www.davincisciencecenter.org/wp-content/uploads/2015/02/Hurricane-Simulator-SM1-280x164.jpg",
          "description": "Grab a bite to eat at Leo's Landing!",
          "name": "Lunch",
          "location": "5682617542246400"
        },
      "start_time": "2015-10-28T15:00:00",
      "id": "5109799364591616",
      "end_time": "2015-10-28T16:00:00",
      "schedule": "5631986051842048"
    },
    {
      "exhibit":
        {
          "id": "5710239819104256",
          "picture": "http://www.davincisciencecenter.org/wp-content/uploads/2015/03/Quakes-and-Shakes-Seismo-280x164.jpg",
          "description": "The Da Vinci Science Center’s Quakes and Shakes Seismometer measures strong seismic activity around the world and broadcasts live to its exhibit floor and website. How it Works A...",
          "name": "Quakes and Shakes Seismometer",
          "location": "5682617542246400"
        },
      "start_time": "2015-10-28T16:00:00",
      "id": "5769015641243648",
      "end_time": "2015-10-28T17:00:00",
      "schedule": "5631986051842048"
    }
  ];

  var eventsOut = [];
  for (var i = 0; i < events.length; i++) {
    var e = {};
    e.start_time = moment(events[i].start_time).format("h:mm a");
    e.end_time   = moment(events[i].end_time).format("h:mm a");
    e.name       = events[i].exhibit.name;
    eventsOut.push(e);
  };
  $scope.events = eventsOut;

  $http
    .get(
      'https://stone-goal-858.appspot.com/exhibits',
      {
        headers: { 'password': "SECRET" }
      }
    )
    .then(
      function(response) {
        $scope.exhibits = response.data;
      },
      function(response) {
        $scope.exhibits = [];
      }
    );


  $http
    .get(
      'https://stone-goal-858.appspot.com/schedules/5631986051842048/notifications',
      {
        headers: { 'password': "SECRET" }
      }
    )
    .then(
      function(response) {
        var notifications = response.data;
        for (var i = 0; i < notifications.length; i++) {
          notifications[i].parsedTime = moment(notifications[i].timestamp).format("h:mm a");
        }
        $scope.notifications = notifications;
      },
      function(response) {
        $scope.notifications = [];
      }
    );
})

.controller('PlaylistsCtrl', function($scope) {
  $scope.playlists = [
    { title: 'Reggae', id: 1 },
    { title: 'Chill', id: 2 },
    { title: 'Dubstep', id: 3 },
    { title: 'Indie', id: 4 },
    { title: 'Rap', id: 5 },
    { title: 'Cowbell', id: 6 }
  ];
})

.controller('PlaylistCtrl', function($scope, $stateParams) {
});
